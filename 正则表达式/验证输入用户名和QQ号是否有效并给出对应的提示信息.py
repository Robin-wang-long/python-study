import re

def main():
    uername = input("请输入你的名字：")
    qq = input("请输入你的qq号：")
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',uername)
    if not m1:
        print("请输入有效的用户名")
    m2 = re.match(r'^[0-9]/d{4,12}$',qq)
    if not m1:
        print("请输入有效的QQ号")

    if m1 and m2:
        print("你输入的数据是有效的")


if __name__ == '__main__':
    main()