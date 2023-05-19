per_ct = 0.2

user = input("何カラットですか？")
ct = float(user)

g = ct * per_ct

desc = f"{ct}カラット = {g}グラム"
print(desc)