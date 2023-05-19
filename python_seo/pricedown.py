import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く

if hm_class == "果物類":
    for fruit in fruits:
        hinmoku[fruit] = hinmoku.get(fruit) - price_down
        if hinmoku[fruit] <= 0:
            hinmoku[fruit] = 1
elif hm_class == "酒類":
    for each_alcohol in alcohol:
        hinmoku[each_alcohol] = hinmoku.get(each_alcohol) - price_down
        if hinmoku[each_alcohol] <= 0:
            hinmoku[each_alcohol] = 1
elif hm_class == "麺類":
    for noodle in noodles:
        hinmoku[noodle] = hinmoku.get(noodle) - price_down
        if hinmoku[noodle] <= 0:
            hinmoku[noodle] = 1


print(hinmoku, end="")
