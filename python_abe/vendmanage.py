from database import session
from tables import MstMerchandise
from tables import TblStock
drinks = {}
samples =session.query(MstMerchandise).all()

def renew_drinks():
    for s in samples:
        res = session.query(TblStock).filter(TblStock.id == s.id)
        for r in res:
            if r.stock != 0:
                drinks[s.name] = s.price
renew_drinks()
for k,v in drinks.items():
    print(f'{k}: {v}円')

def decrease_stock(item_name):
  item = session.query(MstMerchandise).filter(MstMerchandise.name == item_name).first()
  res = session.query(TblStock).filter(TblStock.id == item.id).first()
  res.stock = res.stock + 1
  session.commit()

money = int(input('投入金額を入力してください'))
changes = [5000,2000,1000,500,100,50,10]

def func_change(money):
    result = {}
    for ch in changes:
        if money >= ch:
            while True:
                tmp = money - ch
                if tmp < 0:
                    break
                else:
                    money = tmp
                    if ch in result:
                        result[ch]= result[ch]+1
                    else:
                        result[ch] = 1
    print('おつり')
    for k,v in result.items():
        if k == 5000 or k == 2000 or k == 1000:
            print(f'{k}円札: {v}枚')
        else:
            print(f'{k}円玉: {v}枚')

def func_print_items():
    for k,v in drinks.items():
        print(f'{k}: {v}円')

def func_buy_items(item):
    if item in drinks:
        return drinks[item]
    else:
        print('存在する飲み物を入力してください')

# 最小の値
flg = True
while True:
    if money >= 10001:
        money = int(input(('10000円を超える金額は入力できません　再度投入金額を入力してください')))
    elif money < min(drinks.values()):
        money = int(input((f'{money}円では購入できません　再度投入金額を入力してください')))
    elif str(money)[-1] != "0":
        money = int(input((f'1円玉と5円玉では購入できません　再度投入金額を入力してください')))
    elif money >= min(drinks.values()):
        res = input('何を購入しますか (商品名/cancel)')
        if res != "cancel":
            money = money - func_buy_items(res)
            decrease_stock(res)
            while True:
                renew_drinks()
                decrease_stock(res)
                print(f'残金: {money}円')
                if money < min(drinks.values()):
                    func_change(money)
                    exit()
                r = input('続けて購入しますか(Y/N)')
                if r == 'Y':
                    # 買う処理
                    func_print_items()
                    res = input('何を購入しますか (商品名/cancel)')
                    if res == "cancel":
                        func_change(money)
                        exit()
                    money = money - func_buy_items(res)
                elif r == 'N':
                    func_change(money)
                    exit()
        else:
            func_change(money)
            exit()
    else:
        func_change(money)
        exit()
 