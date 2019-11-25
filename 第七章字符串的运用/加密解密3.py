# 检查并判断密码字符串的强度
import string


def cheak(pwd):
    # 密码必须至少包含6个字符
    if not isinstance(pwd, str) or len(pwd) < 6:
        return 'not suitable for password'
    d = {1: 'weak', 2: 'below middle', 3: 'above middle', 4: 'strong'}
    r = [False] * 4

    for ch in pwd:
        if not r[0] and ch in string.digits:
            r[0] = True
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = True
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = True
        elif not r[3] and ch in ',.!;?<>':
            r[3] = True

    return d.get(r.count(True), 'error')


print(cheak('a2Dd,6'))
