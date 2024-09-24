# jps_presentation_researchmap
日本物理学会の発表業績（ただし2018年秋季大会以降）を、発表者の名前を元にスクレイピングで抽出します。さらにその抽出結果をresearchmapにインポート可能なjsonlファイルとして出力するpythonプログラムです。
日本物理学会のプログラムページの検索機能を利用します。2018年より前と後で、検索ページのフォーマットが異なるため、2018年以前には対応していません。

Google Colaboratoryで楽にやりたい人向けの説明を用意しました（一番上に追加）。

# 注意事項
- 招待講演の有無は判定されません（招待講演では無いと判定される）
- 英語対応していません
- 国際共著かどうかは判定しません
- 講演番号の最初のアルファベットを元にポスター発表かどうかを判別しているため、講演番号の付け方の慣習の違いによってポスター発表と口頭発表の別が間違っているかもしれません。

以上の点が、もし問題になる場合はresearchmapにインポート後に手動で修正すれば対応するのが一番楽だと思います。
また
- ```jps_meetiings_to_researchmap_2018_2022.py```を使用した場合、学会名と会期情報は```学会情報_物性.csv```と```学会情報_素核.csv```から抽出します。結果に問題がある場合は各csvファイルを事前に修正の上、再実行してください。
- 2025年以降も使えるかどうかは定かではありません
- 対象のサイトに負荷を与えないよう責任を持って実行してください
- その他、このプログラムの利用により直接的または間接的に生じたいかなる損害に関しても、その責任を負いません

# とにかく楽したい人向けの手順
## researchmap会員IDを調べる
researchmapにログインして、「設定」画面に入ると調べることができます。

<br>

|![researchmap設定](https://github.com/minowayosuke/jps_presentation_researchmap/blob/images/researchmap.png)|
|---|

## google colabでスクレイピング
物性の場合
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minowayosuke/jps_presentation_researchmap/blob/main/%E6%97%A5%E6%9C%AC%E7%89%A9%E7%90%86%E5%AD%A6%E4%BC%9A%E6%A5%AD%E7%B8%BE%E5%8F%96%E3%82%8A%E8%BE%BC%E3%81%BF_%E7%89%A9%E6%80%A7_%E5%85%B1%E6%9C%89%E7%94%A8.ipynb)
を
素核宇の場合
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minowayosuke/jps_presentation_researchmap/blob/main/日本物理学会業績取り込み_素核_共有用.ipynb)
を開く。

## 必要な情報を入力
authorsとuser_idの中身を、自分の名前と自分のresearchmap会員IDに置き換えます。

## すべてのセルを実行
ランタイムメニューからすべてのセルを実行してください。googleへのログインを求められるかもしれません。


<br>


|![すべてのセルを実行](https://github.com/minowayosuke/jps_presentation_researchmap/blob/images/runall.png)|
|---|

## 待つ
インストール作業やスクレイピング作業には数分かかると思います。気長に待っていると、そのうち"jps_presentations.jsonl"というファイルがダウンロードされるはずです。

## Researchmapにインポート
researchmapにログインして、インポート（先程使った「設定」ボタンのとなり）画面に行きます。
さらに、この画面で「インポート」のボタンを押します。

|![インポート](https://github.com/minowayosuke/jps_presentation_researchmap/blob/images/import.png)|
|---|

インポートファイルとして、さきほどダウンロードした"jps_presentations.jsonl"を選択し、「整合性をチェック」ボタンを押します。

"処理待ち"の状態になるので、適当に待ってから「更新」ボタンを押します。
"チェック完了"状態になったら、「チェック結果確認」をクリック。内容に間違いがないかをチェックし、一番下の「インポート」をクリックします。
何か間違いがあれば、researchmap上で修正しましょう。

# 自分のローカル環境でやりたい人向けの説明

## 必要なもの
- google chrome
- python 実行環境

## 必要なpythonのライブラリ
- numpy
- selenium
- webdriver_manager

それぞれ公式ページを参考にしてインストールしてください。おそらく、全て
pipでインストールできるはず。

## その他の準備
- 自分のresearchmap会員ID

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

## 特定の物理学会（ただし2018年秋季大会以降）について、発表業績を抽出したい場合
```jps_meeting_to_researchmap.py```を使用します。
```
authors = "山田太郎" #検索用の著者名
```
に、検索用に使う名前（例えば自分の姓名など）を入れます。
```
user_id = "B000000000" #researchmap会員ID
```
に自分のresearchmap会員IDを記入してください（researchmapの各自のホームページに記載があるはず）。
```
jps_url = "https://onsite.gakkai-web.net/jps/jps_search/2022au/data2/search/index.html"#検索画面url
```
に適切なurlを入れてください。
学会プログラムトップページではなく、そこから辿れる検索ページのurlを入れる必要があります。
```
fromdate = "2022-09-12"#学会開始日
todate = "2022-09-15"#学会終了日
```
に適切な会期情報を入れてください。
```jps_meeting_to_researchmap.py```
を実行すると、google chromeが一回立ち上がり、各学会の情報がスクレイピングされます。最終的に出力された```jps_presentations.jsonl```をresearchmapの講演・口頭発表等からインポートしてください。

