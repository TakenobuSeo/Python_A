import sys
import os

def main(args):
    '''
    メイン関数
    '''
    sheep_num = int(args[1])
    output_path = os.path.join("..", "files", "sheep.txt")

    # ２回目以降の処理
    if os.path.exists(output_path):
        with open(output_path, mode="r+") as f:
            past_str = f.read()
            f.write("\n")
            print_sheeps(f, past_str.count("回目処理後")+1, sheep_num)

    # 初回の処理   
    else:
        with open(output_path, mode="x") as f:
            print_sheeps(f, 1, sheep_num)


def print_sheeps(f, loop_count: int, sheep_num: int):
    '''
    「ひつじがi匹」をsheep_num回出力する
    '''
    f.write(f"<{loop_count}回目処理後>\n")
    for i in range(1, sheep_num+1):
            f.write(f"ひつじが{i}匹\n")


if __name__ == "__main__":
     main(sys.argv)