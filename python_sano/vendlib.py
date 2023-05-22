def print_items(items: dict) -> None:
    '''商品名と価格の一覧を出力する'''
    for key in  items.keys():
        print(f"{key}:{items[key]}円")

def print_changes(money: int) -> None:
    '''おつりを出力する'''
    def get_change_unit_name(num: int) -> bool:
        '''単位が札か玉かを返す'''
        if num >= 1000:
            return "札"
        else:
            return "玉"
    
    # おつりの内容を出力
    print("おつり")
    CHANGE_UNITS = [5000, 2000, 1000, 500, 100, 50, 10]
    for change in CHANGE_UNITS:
        refund_num = money // change
        if refund_num > 0:
            print(f"{change}円{get_change_unit_name(change)}:{refund_num}枚")
            money %= change
