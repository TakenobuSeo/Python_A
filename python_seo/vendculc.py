vend = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

money = int(input("投入金額を入力してください"))

if money > min(vend.values()):
    buy = input("何を購入しますか(商品名/cancel)")

    if buy == "cancel":
        otsuri = money
        print("お釣りを返却します:", money)