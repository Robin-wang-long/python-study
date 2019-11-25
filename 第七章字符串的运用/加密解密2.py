from random import choice, randint
import string
import codecs

StringBase = '\u7684\u4e00\u4e86\u662f\u6211\u4e0d\5728\u4eba'


def getEamil():
    suffix = ['.comm', '.org', '.net', '.cn']
    characters = string.ascii_letters + string.digits + '_'
    username = ''.join((choice(characters) for i in range(randint(6, 12))))
    domain = ''.join((choice(characters) for i in range(randint(3, 6))))
    return username + '@' + domain + choice(suffix)


def getTelNo():
    return ''.join((str(randint(0, 9)) for i in range(11)))


def getNameOrAddress(flag):
    ''' flag=1表示返回随机姓名，flag=0表示返回随机地址'''
    if flag == 1:
        rangestart, rangeend = 2, 5
    elif flag == 0:
        rangestart, rangeend = 10, 30
    result = ''.join((choice(StringBase) for i in range(randint(rangestart, rangeend))))
    return result


def getSex():
    return choice(('男', '女'))


def getAge():
    return str(randint(18, 100))


def main(filenname):
    with codecs.open(filename, 'w', 'utf-8')as fp:
        fp.write('Name,Sex,Age,TelNO,Address,Eamil\n')
        # 随机生成200个人的信息
        for i in range(200):
            name = getNameOrAddress(1)
            sex = getSex()
            age = getAge()
            tel = getTelNo()
            address = getNameOrAddress(0)
            eamil = getEamil()
            line = ','.join([name, sex, age, tel, address, eamil]) + '\n'
            fp.write(line)


def output(filenname):
    with codecs.open(filename, 'r', 'utf-8')as fp:
        for line in fp:
            line = line.split(',')
            for i in line:
                print(i, end=',')
            print()


if __name__ == '__main__':
    filename = 'information.txt'
    main(filename)
    output(filename)
