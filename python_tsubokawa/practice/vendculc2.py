import math


vend_item = {
    "お茶" : 110,
    "コーヒー" : 100,
    "ソーダ" : 160,
    "コーンポタージュ" : 130
}

money_array = {
            5000 : 0, 
            2000 :0,
            1000 : 0,
            500 : 0,
            100 : 0,
            50 : 0,
            10: 0
}

flg = True
# flg2 = True
min_price = 10000

for price in vend_item:
    # print(vend_item[price])
    if vend_item[price] < min_price:
        min_price = vend_item[price]


def out_change(input_money):
    global money_array
    for money in money_array.keys():
        # print(input_money/money)
        money_array[money] = math.floor(input_money / money)
        # global input_money
        input_money -= money_array[money] * money 
        if money_array[money] > 0:
            print(f'{money}円玉:{money_array[money]}枚')

def buyItem(buy_item):
    global input_money
    buy_item_price = vend_item[buy_item]
    # 投入金額が買いたい値段よりも高いか判定
    if input_money >= buy_item_price:
        input_money -= buy_item_price
        print(f'残金:{input_money}円')
    else:
        print('金額が足りません')


while flg:

    for item_name in vend_item.keys():
        print(f'{item_name}:{vend_item[item_name]}円')
    input_money = int(input("投入金額を入力してください"))


    if input_money > 10000:
        print('10000円を超える金額は投入できません。再度投入金額を入力してください')
        continue
    elif min_price > input_money:
        print(f'{input_money}円では購入できる商品がありません。再度投入金額を入力してください')
        continue
    elif str(input_money)[-1] != '0':
        print('１円玉、５円玉は使用できません。再度投入金額を入力してください')
        continue
    else:
        while True:
            buy_item = input('何を購入しますか（商品名/cancel）')
            if buy_item == 'cancel':
                out_change(input_money)
                # flg= Falseにすることで一番外のwhileを抜ける
                flg = False
                break
            
            #入力した文字が商品内にあるのかの判定
            is_item = False
            for item_name in vend_item.keys():
                if buy_item == item_name:
                    is_item = True


            #購入する商品を選択
            if is_item:
                # buyItem(buy_item)

                buy_item_price = vend_item[buy_item]
        # 投入金額が買いたい値段よりも高いか判定
                if input_money >= buy_item_price:
                    #購入した分だけ金額を引く
                    input_money -= buy_item_price
                    print(f'残金:{input_money}円')
                    if input_money != 0 and min_price <= input_money:
                        is_continue = input('続けて購入しますか(Y/N)')
                        if is_continue == 'Y':
                            continue
                        else:
                            out_change(input_money)
                            flg = False
                            break
                    else:
                        print('残金が足りません。お釣りを出します')
                        out_change(input_money)
                        flg = False
                        break
                else:
                    #商品の金額よりも投入金額が小さい場合
                    print('金額が足りません')
                    print('商品を選択しなおしてください')
                    continue
            
            else:
                print('存在しない商品です')
                print('入力しなおしてください')
                continue


            # #以下コピペ
            # #所持金が最安価格よりも高い場合
            # while input_money != 0 and min_price <= input_money:
            #         is_continue = input('続けて購入しますか(Y/N)')
            #         if is_continue == 'Y':
            #             buyItem()

            #         # 続けて購入しない、または、投入金額が少ない場合のお釣りを出す処理
            #         else:
            #             print('残金が足りないよ')
            #             # お釣りを出す処理
            #             out_change(input_money)

            #             flg = False
            #             break
            



    