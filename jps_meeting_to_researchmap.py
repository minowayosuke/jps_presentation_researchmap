#特定の物理学会（ただし2018年秋季大会以降）の発表について、プログラムの検索を利用してjsonl化する

import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import copy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


authors = "山田太郎" #検索用の著者名
user_id = "B000000000" #researchmap会員ID



myjsonl = []

mytemplate = {
  "insert": {
    "type": "presentations",
    "id": None,
    "user_id": None
  },
  "similar_merge": {
    "display": "disclosed",
    "major_achievement": False,
    "presentation_title": {
      "ja": "仮タイトル"
    },
    "presenters": {
      "ja": [
        {
          "name": "山田太郎"
        },
        {
          "name": "山田花子"
        },
        {
          "name": "山田二郎"
        }
      ]
    },
    "event": {
      "ja": "日本物理学会 2022年秋季大会"
    },
    "publication_date": "2022-09-14",
    "from_event_date": "2022-09-12",
    "to_event_date": "2022-09-15",
    "invited": False,
    "presentation_type": "oral_presentation"
  }
}


jps_url = "https://onsite.gakkai-web.net/jps/jps_search/2022au/data2/search/index.html"#検索画面url
fromdate = "2022-09-12"#学会開始日
todate = "2022-09-15"#学会終了日


mytemplate["insert"]["user_id"]=user_id
mytemplate["similar_merge"]["from_event_date"]=fromdate
mytemplate["similar_merge"]["to_event_date"]=todate

# Use the `install()` method to set `executabe_path` in a new `Service` instance:
service = Service(executable_path=ChromeDriverManager().install())

# Pass in the `Service` instance with the `service` keyword: 
driver = webdriver.Chrome(service=service)
driver.get(jps_url)

element = driver.find_element(By.XPATH, '//*[@id="main_form"]/div[1]/table/tbody/tr[4]/td/input[2]')
element.send_keys(authors)

#検索結果がない場合の例外処理
try:
    element.send_keys(Keys.ENTER)
    element_table = driver.find_elements(By.XPATH, '//*[@id="result_data_table"]')
    #wait = WebDriverWait(driver, 30)
    #wait.until(EC.alert_is_present())
    #alert = driver.switch_to.alert
    #alert.accept()
    #print("Alert accepted 0")
except Exception:
    pass
else:   

    rows = element_table[0].find_elements(By.TAG_NAME, "tr")

    #著者名の上付き文字を消す
    for row in rows[1:]:#表の一行目は飛ばす
        cells = row.find_elements(By.TAG_NAME,'td') 
        sup_removes = cells[3].find_elements(By.TAG_NAME,'sup') 
        for sup_remove in sup_removes:
            driver.execute_script('arguments[0].remove()', sup_remove)

    #jsonl用データ準備
    for row in rows[1:]:
        cells = row.find_elements(By.TAG_NAME,'td')
        presentation_style="oral_presentation"
        if re.sub('^[0-9]*','',cells[0].text)[0]=="P":
            presentation_style="poster_presentation"
        mytemplate["similar_merge"]["presentation_type"]=presentation_style
        mytemplate["similar_merge"]["presentation_title"]["ja"]=cells[2].text
        names = cells[3].text
        mytemplate["similar_merge"]["presenters"]["ja"] = [{'name': x.strip()} for x in names.split(',')]
        mytemplate["similar_merge"]["event"]["ja"] = driver.title
        presentation_id = cells[0].text
        mytemplate["similar_merge"]["publication_date"]=todate[:-2]+(re.findall(r"\d+", presentation_id)[0]).zfill(2)
        myjsonl.append(copy.deepcopy(mytemplate))
    
driver.close()


with open('jps_presentations.jsonl', mode='w', encoding='utf-8') as fout:
    for obj in myjsonl:
        json.dump(obj, fout, ensure_ascii=False)
        fout.write('\n')
        
        