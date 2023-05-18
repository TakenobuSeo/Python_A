per_ct = 0.2
user = input("何カラットですか？")
ct = float(user)
g = ct*per_ct
desc = "{0}カラット = {1}グラム".format(ct, g)
print(desc)