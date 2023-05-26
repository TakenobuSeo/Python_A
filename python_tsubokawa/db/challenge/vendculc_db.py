import math
import funcs_vend as funcs

vend_item = {
    "お茶" : 110,
    "コーヒー" : 100,
    "ソーダ" : 160,
    "コーンポタージュ" : 130
}

money_array = {
            10000 : 0,
            5000 : 0, 
            2000 :0,
            1000 : 0,
            500 : 0,
            100 : 0,
            50 : 0,
            10: 0
}

#お金の在庫を格納する辞書データ
money_stock = {}

# 足りないお金を入れる変数
not_enough_money = None

flg = True
# flg2 = True
min_price = 10000

for price in vend_item:
    # print(vend_item[price])
    if vend_item[price] < min_price:
        min_price = vend_item[price]



#在庫があるものを表示する関数
show_stock = funcs.show_stock
update_stock = funcs.update_stock
show_money = funcs.show_money
update_money = funcs.update_money
insert_msg = funcs.insert_message



def add_money(input_money):
    '''お金の在庫を足す処理'''
    global money_array
    for money in money_array.keys():
        money_array[money] = math.floor(input_money / money)
        # 出した分を引く
        input_money -= money_array[money] * money

        in_money_num = money_array[money] * 1

        #在庫からお金を減らす処理
            #減らすので枚数 * -1
        update_money(money, in_money_num)


def out_change(input_money):
    '''
    お釣りを出す処理
    '''
    global money_array
    for money in money_array.keys():
        #お釣りが出せるか
        #money_array[money]には引く枚数が入る
        money_array[money] = math.floor(input_money / money)
        # 出した分を引く
        input_money -= money_array[money] * money

        out_money_num = money_array[money] * -1

        #在庫からお金を減らす処理
            #減らすので枚数 * -1
        update_money(money, out_money_num)

        if money_array[money] > 0:
            if money <= 500:
                print(f'{money}円玉:{money_array[money]}枚')
            else:
                print(f'{money}札:{money_array[money]}枚')

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

    # for item_name in vend_item.keys():
    #     print(f'{item_name}:{vend_item[item_name]}円')
    
    #在庫がある商品を表示する
    show_stock()
    
    input_money = int(input("投入金額を入力してください"))

    #在庫用
    init_input_money = input_money


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

                    #買った商品の在庫を減らす処理
                    update_stock(buy_item)




                    if input_money != 0 and min_price <= input_money:
                        is_continue = input('続けて購入しますか(Y/N)')
                        if is_continue == 'Y':
                            continue
                        else:
                            out_change(input_money)
                            add_money(init_input_money)

                            # 足りないお金の種類を格納
                            not_enough_money = show_money(money_stock)
                            for key in not_enough_money.keys():
                                # 足りないお金についてメッセージを送信処理
                                insert_msg(key, not_enough_money[key])

                            flg = False
                            break
                    else:
                        print('残金が足りません。お釣りを出します')
                        out_change(input_money)
                        flg = False
                        add_money(init_input_money)
                        # 足りないお金を格納
                        not_enough_money = show_money(money_stock)
                        for key in not_enough_money.keys():
                            # 足りないお金についてメッセージを送信
                            insert_msg(key, not_enough_money[key])
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


            



    