input_ = '51900;83000;158000;367500;250000;59200;128500;1304000'

inputlist = sorted(map(int,input_.split(';')),reverse=True)

def comma(s):
    return "%9s" %format(s, ',')

for i in list(map(comma, inputlist)):
    print(i)