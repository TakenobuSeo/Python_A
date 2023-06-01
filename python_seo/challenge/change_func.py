# お釣りを計算する関数

def change_money(money):
    money_type = [5000, 2000, 1000, 500, 100, 50, 10]  # お金の種類のリスト

    change = money  # 残金をおつりに代入

    print("おつり")
    for i in money_type:
        if change // i != 0:  # おつりが出てこないお金の種類は表示しない
            print("{0}円:{1}枚".format(i, change // i))
            change = change % i  # 表示していない部分のおつりを再度changeに代入しおつりの枚数を計算


