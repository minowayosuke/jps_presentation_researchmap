# jps_presentation_reserachmap
日本物理学会の発表業績（ただし2018年秋季大会以降）を、発表者の名前を元にスクレイピングで抽出します。さらにその抽出結果をresearchmapにインポート可能なjsonlファイルとして出力するpythonプログラムです。
日本物理学会のプログラムページの検索機能を利用します。

# 注意事項
- 招待講演の有無は判定されません（招待講演では無いと判定される）
- 英語対応していません
- 国際共著かどうかは判定しません
- 講演番号を元にポスター発表かどうかを判別しているため、講演番号によってはポスター発表と口頭発表の別が間違っているかもしれません。
- ```jps_meetiings_to_researchmap_2018_2022.py```を使用した場合、学会名と会期情報は```学会情報_物性.csv```と```学会情報_素核.csv```から抽出します。結果に問題がある場合は各csvファイルを事前に修正の上、再実行してください。
- 2023年以降も使えるかどうかは定かではありません

# 必要なもの
- google chrome
- python 実行環境

# 必要なpythonのライブラリ
- numpy
- selenium
- selenium
- webdriver_manager
公式ページを参考にしてインストールしてください。おそらく
pipでインストールできるはず。

# その他の準備
- 自分のresearchmap会員ID

# 使用方法
次項で説明する方法で生成されるjsonlファイルをresearchmapにインポートしてください。

## 2018年秋季大会から2022年秋季大会までまとめて抽出したい場合
- ```jps_meetiings_to_researchmap_2018_2022.py```
- ```学会情報_物性.csv```
- ```学会情報_素核.csv```
のすべてのファイルを同じ場所に置きます。
```
meetings, fromdates, todates = np.genfromtxt('学会情報_素核.csv',delimiter=",",dtype='str',encoding='utf-8-sig',unpack =True)
```
のファイル名を、自分の分野に応じて```'学会情報_素核.csv'```あるいは```'学会情報_物性.csv'```に変更します。
```
authors = "山田太郎" #検索用の著者名
```
に、検索用に使う名前（例えば自分の姓名など）を入れます。
```
user_id = "B000000000" #researchmap会員ID
```
に自分のresearchmap会員IDを記入してください（researchmapの各自のホームページに記載があるはず）。

```jps_meetiings_to_researchmap_2018_2022.py```
を実行すると、google chromeが複数回立ち上がり、各学会の情報がスクレイピングされます。最終的に出力された```jps_presentations.jsonl```をresearchmapの講演・口頭発表等からインポートしてください。
