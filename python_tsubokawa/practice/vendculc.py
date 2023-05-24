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

# 
def buyItems():
    buy_item = input('何を購入しますか（商品名/cancel）')
    global input_money
    if buy_item == 'cancel':
        out_change(input_money)
        flg = False
    else:
        buy_item_price = vend_item[buy_item]
        # 投入金額が買いたい値段よりも高いか判定
        if input_money >= buy_item_price:
            input_money -= buy_item_price
            print(f'残金:{input_money}円')
        else:
            print('金額が足りません')

def out_change(input_money):
    global money_array
    for money in money_array.keys():
        # print(input_money/money)
        money_array[money] = math.floor(input_money / money)
        # global input_money
        input_money -= money_array[money] * money 
        if money_array[money] > 0:
            print(f'{money}円玉:{money_array[money]}枚')



# def checkMinPrice():
#     for price in vend_item:
#     # print(vend_item[price])
#     if vend_item[price] < min_price:
#         min_price = vend_item[price]



flg = True

while flg:
    for item_name in vend_item.keys():
        print(f'{item_name}:{vend_item[item_name]}円')
    input_text = input("投入金額を入力してください")
    min_price = 10000
    # if input_text == 'cancel':
    #     print('おつり')
    #     flg = False
        #投入された金額をそのまま返す
        #おつりを返却する関数
        
    if int(input_text) >= 10001:
        print('10,000円を超える金額は投入できません。再度投入金額を入力してください')
        continue
        # flg = False

    else:
        input_money = int(input_text)
        # print(input_money)

        # 自動販売機の最安価格を求める処理
        for price in vend_item:
            # print(vend_item[price])
            if vend_item[price] < min_price:
                min_price = vend_item[price]
        # print(min_price)


        # 最安価格よりも投入金額が大きい場合
        if min_price <= input_money: 
            
            # 1円玉か５円玉を投入していないか判定
            if input_text[-1] != '0':
                print('１円玉、５円玉は使用できません。再度投入金額を入力してください')
            else:
                buyItems()


                # 残金が０円か判定し、０円でない限り繰り返す
                while input_money != 0 and min_price <= input_money:
                    is_continue = input('続けて購入しますか(Y/N)')
                    if is_continue == 'Y':
                        buyItems()

                    # 続けて購入しない、または、投入金額が少ない場合のお釣りを出す処理
                    else:
                        print('残金が足りないよ')
                        # お釣りを出す処理
                        out_change(input_money)

                        flg = False
                        break

            

                #残金が足りないので終了
                # else:
                #     break

            # flg = False

        else:
            print(f'{input_money}円では購入できる商品がありません。再度投入金額を入力してください')
            continue


