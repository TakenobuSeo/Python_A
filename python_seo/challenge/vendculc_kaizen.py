# おつりを計算する関数
def change_money(money):
    money_type = [5000, 2000, 1000, 500, 100, 50, 10]  # お金の種類のリスト

    change = money  # 残金をおつりに代入

    print("おつり")
    for i in money_type:
        if change // i != 0:  # おつりが出てこないお金の種類は表示しない
            print("{0}円:{1}枚".format(i, change // i))
            change = change % i  # 表示していない部分のおつりを再度changeに代入しおつりの枚数を計算






vend = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}  # 商品名と値段


money = int(input("投入金額を入力してください"))  # 投入金額の入力

while True:
    if money > 10000:  # 10,000円超で再度入力を要求
        money = int(
            input("10,000を超える金額は投入できません。再度投入金額を入力してください")
            )

    elif money < min(vend.values()):  # 最安値の商品以下の投入金額で再度入力を要求
        money = int(
            input("{money}円では購入できる商品がありません。再度投入金額を入力してください".format(money=money))
            )

    elif not(str(abs(money))[-1] == "0"):  # 1の位(1円玉、5円玉の投入)に数値が存在すると再度入力を要求
        money = int(
            input("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        )

    else:

        if money >= min(vend.values()):  # 最安値の商品よりも投入金額が高いと商品選択
            print("お茶:110円")
            print("コーヒー:100円")
            print("ソーダ:160円")
            print("コーンポタージュ:130円")
            buy = input("何を購入しますか(商品名/cancel)")

            if buy == "cancel":  # 商品購入前にキャンセル入力でおつりを全額返金
                change = money
                print("お釣りを返却します:", money)

            else:
                money = money - vend[buy]  # 投入金額(or残額)から商品の値段を引く

                if money >= min(vend.values()):  # 最安値の商品よりも残額が高い残金表示と購入意思確認
                    print("残金:{money}".format(money=money))
                    c_buy = input("続けて購入しますか（Y/N）")

                    if c_buy == "Y":  # Yを選択で、whileの中身を再度実行する
                        continue
                    else:
                        change_money(money)  # Nを選択で、おつり(change_money関数)を実行
                        break


                elif money > 0 and money < min(vend.values()):  # 残額が0超、商品の最安値未満でおつり関数を実行
                    change_money(money)
            

                elif money == 0:  # 残額が0でwhileを終了
                    break

        break
