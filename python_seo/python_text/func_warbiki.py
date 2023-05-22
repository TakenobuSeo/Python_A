def waribiki(name, time, num, price):

    if time == 14 and num >= 3:
        price = price * 0.9
        print("{name}さんは{price}を支払う".format(name=name, price=price))

    elif time == 15 and num >= 5:
        price = price * 0.8
        print("{name}さんは{price}を支払う".format(name=name, price=price))
    
    else:
        print("割引なし")

waribiki("A", 15, 3, 1200)
