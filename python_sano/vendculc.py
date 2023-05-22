
item_prices = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

# 商品の一覧を出力
for key in  item_prices.keys():
    print(f"{key}:{item_prices[key]}円")

# 投入金額のループ
while True:
    money = input("投入金額を入力してください")
    try:
        money = int(money)

        # 投入金額チェック
        if money > 10000:
            print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
            continue

        if money < min(item_prices.values()):
            print(f"{money}円では購入できる商品がありません。再度投入金額を入力してください")
            continue

        if money % 10 != 0:
            print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
            continue
        
        break

    except:
        print("投入金額は整数で入力してください")
    

# 商品購入のループ
while True:
    purchase_item = input("何を購入しますか（商品名/cancel）")

    if  purchase_item =="cancel":
        break

    # 商品購入チェック、最初に戻る
    if purchase_item not in item_prices.keys():
        print("その商品名の商品は販売していません")
        continue
    
    if money < item_prices[purchase_item]:
        print("その商品を購入するには金額が足りません")
        continue

    # 購入できる場合
    money -= item_prices[purchase_item]
    
    # もう購入できる商品がない場合お釣りを出力して終了
    if money < min(item_prices.values()):
        break

    # YかNを入力するまで訊く
    is_continue = input("続けて購入しますか（Y/N）")
    while is_continue not in ['Y', 'N']:
        print("Y か N を入力してください")
        is_continue = input("続けて購入しますか（Y/N）")

    # 商品購入に戻る
    if is_continue == 'Y':
        continue
    # お釣りを出力して終了
    elif is_continue == 'N':
        break


# 終了処理
# 残金があるならお釣りを出力する
if money != 0:
    change_units = [5000, 2000, 1000, 500, 100, 50, 10]
    
    # 単位が札か玉かを返す
    def get_change_unit_name(num: int) -> bool:
        if num > 1000:
            return "札"
        else:
            return "玉"
    
    # おつりの内容を出力する
    print("おつり")
    for change in change_units:
        refund_num = money // change
        if refund_num > 0:
            print(f"{change}円{get_change_unit_name(change)}:{refund_num}枚")
            money %= change
