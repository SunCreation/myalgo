import re
s = 'A man, a plan, a can}al: _Panama'
s = re.sub('[^{A-Za-z0-9}]','',s).lower()

print(s)
print(ord('_'), ord('A'),ord('z'))