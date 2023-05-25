import vendlibdb

ITEMS_AVAILABLE = vendlibdb.renew_available_items()

# 投入金額のループ
while True:
    money = input("投入金額を入力してください")
    try:
        money = int(money)

        # 投入金額チェック
        if money > 10000:
            print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
            continue

        if money < vendlibdb.get_lowest_price():
            print(f"{money}円では購入できる商品がありません。再度投入金額を入力してください")
            continue

        if money % 10 != 0:
            print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
            continue
        
        break

    except:
        print("投入金額は整数で入力してください")
    

vendlibdb.store_change(money)

# 商品購入のループ
while True:
    purchase_item = input("何を購入しますか（商品名/cancel）")

    # cancel入力の場合、お釣りを出して終了
    if purchase_item =="cancel":
        break

    # 商品購入チェック、最初に戻る
    if purchase_item not in ITEMS_AVAILABLE.keys():
        print("その商品名の商品は販売していません")
        continue
    
    if money < ITEMS_AVAILABLE[purchase_item]:
        print("その商品を購入するには金額が足りません")
        continue

    # 指定商品を購入できる場合
    money -= ITEMS_AVAILABLE[purchase_item]
    vendlibdb.buy_item(purchase_item)
    
    # もう購入できる商品がない場合、お釣りを出力して終了
    if money < vendlibdb.get_lowest_price():
        break

    print(f"残金：{money}円")
    
    # YかNを入力するまで訊く
    is_continue = input("続けて購入しますか（Y/N）")
    while is_continue not in ['Y', 'N']:
        print("Y か N を入力してください")
        is_continue = input("続けて購入しますか（Y/N）")

    # 商品購入に戻る
    if is_continue == 'Y':
        ITEMS_AVAILABLE = vendlibdb.renew_available_items()
        continue
    # お釣りを出力して終了
    elif is_continue == 'N':
        break


# 終了処理
# 残金があればお釣りを出力
if money != 0:
    vendlibdb.pay_out_change(money)