a = '''the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.'''
count = 0
for i in range(len(a)-2):
    if a[i:i+3]=='the' and not a[i+3].isalpha():
        count += 1











import re

findlist = re.findall('the[^\w]', a)

print(findlist)
print(count)