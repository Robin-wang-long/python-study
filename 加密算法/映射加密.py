def robin(s):

    a = "awexrcghjK"
    x = "!@#$%^&*()"
    table = ''.maketrans(a, x)
    return s.translate(table)
s = input("请输入你的原密码：")
print(robin(s))