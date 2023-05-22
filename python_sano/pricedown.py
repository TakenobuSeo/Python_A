import sys

# args[1]：値下げする分類（果物類、酒類、麺類）
# args[2]：値下げ額
args = sys.argv
price_down_category = args[1]
down_price = int(args[2])

# 初期価格
prices = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#果実類、酒類、麺類に分かれる
category_to_food = {}
category_to_food["果物類"] = ("リンゴ", "みかん", "バナナ") 
category_to_food["酒類"] = ("ビール", "日本酒") 
category_to_food["麺類"] = ("ラーメン", "うどん", "パスタ") 

# 値下げする
for food in category_to_food[price_down_category]:
    # 1円未満にならないよう値下げする
    prices[food] = max(prices[food] - down_price, 1)

print(prices, end="")
