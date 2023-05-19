import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]  #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ") #果物類をタプルで定義
alcohol = ("ビール", "日本酒") #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ") #麺類をタプルで定義

#ここ以降にプログラムを書く

#種別を判定
foodType = None
if hm_class == "果物類":
     foodType = fruits
elif hm_class == "酒類":
     foodType = alcohol
elif hm_class == "麺類":
    foodType = noodles

for type in foodType:
     hinmoku[type] = hinmoku[type] - price_down
     
     # 値下げ額が1円未満の場合、1円にする
     if hinmoku[type] < 1:
        hinmoku[type] = 1

print(hinmoku, end="")
     