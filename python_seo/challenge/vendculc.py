def change(money):
    print("おつり")
    otsuri = money
    otsuri_5000 = otsuri // 5000
    otsuri = otsuri % 5000
    otsuri_2000 = otsuri // 2000
    otsuri = otsuri % 2000
    otsuri_1000 = otsuri // 1000                    
    otsuri = otsuri % 1000
    otsuri_500 = otsuri // 500
    otsuri = otsuri % 500
    otsuri_100 = otsuri // 100
    otsuri = otsuri % 100
    otsuri_50 = otsuri // 50                        
    otsuri = otsuri % 50
    otsuri_10 = otsuri // 10
                    
    if otsuri_5000 != 0:
        print("5000円:{otsuri}枚".format(otsuri=otsuri_5000))
    if otsuri_2000 != 0:                           
        print("2000円:{otsuri}枚".format(otsuri=otsuri_2000))
    if otsuri_1000 != 0:
        print("1000円:{otsuri}枚".format(otsuri=otsuri_1000))
    if otsuri_500 != 0:
        print("500円:{otsuri}枚".format(otsuri=otsuri_500))
    if otsuri_100 != 0:
        print("100円:{otsuri}枚".format(otsuri=otsuri_100))           
    if otsuri_50 != 0:
        print("50円:{otsuri}枚".format(otsuri=otsuri_50))
    if otsuri_10 != 0:
        print("10円:{otsuri}枚".format(otsuri=otsuri_10)) 





vend = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}


money = int(input("投入金額を入力してください"))

while True:
    if money > 10000:
        money = int(
            input("10,000を超える金額は投入できません。再度投入金額を入力してください")
            )

    elif money < min(vend.values()):
        money = int(
            input("{money}円では購入できる商品がありません。再度投入金額を入力してください".format(money=money))
            )

    elif not(str(abs(money))[-1] == "0"):
        money = int(
            input("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        )

    else:

        if money >= min(vend.values()):
            print("お茶:110円")
            print("コーヒー:100円")
            print("ソーダ:160円")
            print("コーンポタージュ:130円")
            buy = input("何を購入しますか(商品名/cancel)")

            if buy == "cancel":
                otsuri = money
                print("お釣りを返却します:", money)

            else:
                money = money - vend[buy]

                if money >= min(vend.values()):
                    print("残金:{money}".format(money=money))
                    c_buy = input("続けて購入しますか（Y/N）")

                    if c_buy == "Y":
                        continue
                    else:
                        change(money)
                        break


                elif money > 0 and money < min(vend.values()):
                    change(money)
            

                elif money == 0:
                    break

        break
