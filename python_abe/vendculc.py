drinks = {"お茶": 110, "コーヒー": 100, "ソーダ": 160, "コーンポタージュ": 130}
for k,v in drinks.items():
    print(f'{k}: {v}円')
money = int(input('投入金額を入力してください'))
# 最小の値
flg = True
while True:
    if money >= 10001:
        money = int(input(('10000円を超える金額は入力できません　再度投入金額を入力してください')))
    elif money < min(drinks.values()):
        money = int(input((f'{money}円では購入できません　再度投入金額を入力してください')))
    elif str(money)[-1] != 0:
        money = int(input((f'1円玉と5円玉では購入できません　再度投入金額を入力してください')))
    elif money >= min(drinks.values()):
        res = input('何を購入しますか (商品名/cancel)')
        if res != "cancel":
            print(f'残金: {money}円')
            r = input('続けて購入しますか(Y/N)')
            if r == 'Y':
                next
            elif r == 'N':
 