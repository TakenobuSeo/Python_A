import math

# 商品名と価格を格納したデータ
vend_item = {
    "お茶" : 110,
    "コーヒー" : 100,
    "ソーダ" : 160,
    "コーンポタージュ" : 130
}


# 貨幣の種類を格納した配列
money_types = [5000,2000,1000,500,100,50,10]

# True : 購買処理をループ
flg = True



#----販売商品の最安価格をmin_priceに格納-----------------------

# 最安価格を10000円に仮置き
min_price = 10000


for price in vend_item:
    if vend_item[price] < min_price:
        min_price = vend_item[price]
# ---------------------------------------------------



def out_change(out_money):
    '''
    お釣りを排出する関数
    '''
    for money in money_types:
        #　数の大きい貨幣からお釣りにできるか判定する
        change_num = math.floor(out_money / money)
        out_money -= change_num * money 

        #お釣りとして出す枚数がある場合にprint
        if change_num > 0:
            print(f'{money}円玉:{change_num}枚')


# True : 購買処理をループ
# False : 購買処理を終了
while flg:

#------商品を一覧表示する処理

    for item_name in vend_item.keys():
        print(f'{item_name}:{vend_item[item_name]}円')

#----------------------------------商品を一覧表示する処理



# 投入金額を入力値より取得 
    input_money = int(input("投入金額を入力してください"))


#-------10000円を超える際の処理
    


    if input_money > 10000:
        print('10000円を超える金額は投入できません。再度投入金額を入力してください')
        continue

#--------------------------------10000円を超える際の処理



#----商品の最安価格よりも投入金額が低い際の処理-------------------------
    
    elif min_price > input_money:
        print(f'{input_money}円では購入できる商品がありません。再度投入金額を入力してください')
        continue

    #-------------------------------------商品の最安価格よりも投入金額が低い際の処理----------

#----1円玉や5円玉が投入された際の処理----------------------------------------------
   
    elif str(input_money)[-1] != '0':
        print('１円玉、５円玉は使用できません。再度投入金額を入力してください')
        continue

#------------------------------------------------1円玉や5円玉が投入された際の処理-------------

#---購入処理------------------------------------------------

    else:
        # True : 商品を選択・購入をループ
        while True:
            buy_item = input('何を購入しますか（商品名/cancel）')

            # cancel入力時に購買終了
            if buy_item == 'cancel':
                out_change(input_money)
            # flg : Falseで購買処理を終了
                flg = False
                break
            
            #----入力した文字が商品内にあるか判定する処理------------------
            is_item = False
            for item_name in vend_item.keys():
                if buy_item == item_name:
                    is_item = True
            #-------------------------------入力した文字が商品内にあるか判定する処理----

            # 商品が存在するか判定
            if is_item:
                buy_item_price = vend_item[buy_item]
                # 投入金額が買いたい値段よりも高いか判定
                if input_money >= buy_item_price:
                    #購入した分だけ金額を引く
                    input_money -= buy_item_price
                    print(f'残金:{input_money}円')
                    # 残金が最安価格よりも高いか
                    if min_price <= input_money:
                        # is_continue : Yで購入継続
                        # is_continue : Nで購入終了
                        is_continue = input('続けて購入しますか(Y/N)')
                        if is_continue == 'Y':
                            continue
                        else:
                            out_change(input_money)
                            flg = False
                            break
                    else:
                    # 残金が最安価格よりも低い場合、購買処理を終了
                        print('残金が足りません。お釣りを出します')
                        out_change(input_money)
                        flg = False
                        break
                else:
                    #買いたい商品の金額よりも投入金額が小さい場合
                    print('金額が足りません')
                    print('商品を選択しなおしてください')
                    continue
            
            else:
            # 存在しない商品名を入力した場合
                print('存在しない商品です')
                print('入力しなおしてください')
                continue

# ----------------------------------------------------購入処理--------------------------





    