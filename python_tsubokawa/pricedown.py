#辞書作成
fruits_dic = {'リンゴ': 80, 'みかん':198, 'バナナ':150}
alchol_dic = {'ビール': 360, '日本酒':580}
noodle_dic = {'ラーメン': 380,'うどん': 128,'パスタ': 258}


#カテゴリーごとの辞書を作成
category_dic = {'果物類' :fruits_dic, '酒類' : alchol_dic, '麺類' :noodle_dic}


#デバッグ用
# category = '麺類'
# price_down = 100

import sys
args = sys.argv
category = args[1]
price_down = int(args[2])

output = {}

#値下げ処理
#指定されたカテゴリーの関する辞書内の全ての商品に対して処理を行う
for item in category_dic[category]:
    # category_dic[category][item]でitemの価格を取得
    item_price = category_dic[category][item]
    item_price -= price_down
    if item_price<=0:
        item_price = 1
    #それぞれの辞書内の価格を上書き
    category_dic[category][item] = item_price



#表を出力
for category in category_dic:
    for item in category_dic[category]:
        output[item] = category_dic[category][item]

# 表を出力
print(output, end="")