from hi.python.learn import hello, Class_

hello()

x = Class_()

print(x.data)



print('%03d' %int('23'))
a = '97.xlsx 98.docx 99.docx 100.xlsx 101.docx 102.docx'
files = a.split()




print([(lambda x: '%03d' %int(x[0]))(x:=i.split('.')) + '.'+ x[1] for i in files])



print([(lambda x: '%03d' %int(x[0]))(i.split('.')) + '.'+ i.split('.')[1] for i in files])