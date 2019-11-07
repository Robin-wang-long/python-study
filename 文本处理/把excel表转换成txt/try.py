import xlrd
def main(name):
    date = xlrd.open_workbook(name)
    st = date.sheets()[0]
    row = st.nrows
    t = open('test1.txt','w')
    for i in range(row):
        t.write(str(st.row_values(i))+'\n')
    t.close()
main('test1.xlsx')