vend_item = {
    "お茶" : 110,
    "コーヒー" : 100,
    "ソーダ" : 160,
    "コーンポタージュ" : 130
}


input = input("投入金額を入力してください")
if input == 'cancel':
    print('おつり')
    #投入された金額をそのまま返す
    #おつりを返却する関数

else:
    input_money = int(input)
