import string

def kaisa(s,k=3):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    before = string.ascii_letters
    after = lower[k:]+lower[:k]+upper[k:]+upper[:k]
    table = ''.maketrans(before,after)
    return s.translate(table)

s = input("输入你的原密码：")
s = kaisa(s)
print(s)