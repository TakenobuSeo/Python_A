import os 
import qrcode




#QRコードを生成
img = qrcode.make("http://www.tamagoken.com/blog/3508/")

path = os.path.join("..","..","..","..","local","day4","img","tamagoken.jpg")
print(path)
#画像ファイルを保存
img.save(path)


