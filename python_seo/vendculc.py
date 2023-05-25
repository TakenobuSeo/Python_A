vend = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

name = ["お茶", "コーヒー", "ソーダ", "コーンポタージュ"]

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
                        print("お釣りを返却します:", money)
                        break


                elif money > 0 and money < min(vend.values()):
                    print("お釣りを返却します:", money)

                elif money == 0:
                    break

        break

