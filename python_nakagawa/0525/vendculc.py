text = 'お茶：110円\nコーヒー：100円\nソーダ：160円\nコーンポタージュ：130円\n投入金額を入力してください'
inputAmount:int = int(input(text))
print(inputAmount)

items = {
    "お茶":110,
    "コーヒー": 100, 
    "ソーダ": 160, 
    "コーンポタージュ": 130
    }

while inputAmount:
    #1の位が0以外の場合
    ones = str(abs(inputAmount))[-1]
    if ones != 0:
        inputAmount = input('1円玉、5円玉は使用できません。再度投入金額を入力してください')

    #一番安い商品よりも高い金額が入力されていれば何を購入するかを問う
    if 110 < int(inputAmount) <= 10000:
        seleceted = input('何を購入しますか（商品名/cancel）')
        #cancelと入力された場合はおつり
        if seleceted == 'cancel':
            print(f'おつり{inputAmount}')#
        #商品入力されたら
        #残金計算
        print(seleceted)
        #
        break
    
    #入力金額が10,000円を超えたら再質問
    elif int(inputAmount) > 10000:
        inputAmount = input('10,000円を超える金額は投入できません。再度投入金額を入力してください')
        continue
    
    #何も買えない
    elif int(inputAmount) < 100:
        inputAmount = input(f'{inputAmount}円では購入できる商品がありません。再度投入金額を入力してください')
        continue
    
    else:
        break
# def calcVend():
#   if int(inputAmount) < 100: 
#      return
#   item = input('何を購入しますか（商品名/cancel）')
#   if item == 'cancel':
#       text = 'おつり \n aa'
#   else 
  #itemsとこうにゅうしたいものを比較
