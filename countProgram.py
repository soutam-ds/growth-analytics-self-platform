import re
st  = '1abc'
sm = []
temp = re.findall(r'\d+', st)
sm = list(map(int,temp))
total = 0
for i in sm:
    total += i

print(total)


