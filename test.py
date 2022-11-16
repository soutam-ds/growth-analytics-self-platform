from collections import OrderedDict
A,B,C = 'XXY','X', 'XXY'

dict = OrderedDict()
lst = []
lst_a = []
lst_b = []
flag1 = 0
flag2 = 0
for a in A:
    if a not in lst_a:
        lst_a.append(a)
    else:
        pass

for b in B:
    if b not in lst_b:
        lst_b .append(b)
    else:
        pass

for i in range(0,len(C)):
    if C[i] not in lst:
        lst.append(C[i])
        if i< len(A):
            if C[i] == lst_a[i]:
                flag1 += 0
            else:
                flag1 += 1
        else:
            pass
        if i< len(B):
            if C[i] == lst_b[i]:
                flag2 += 0
            else:
                flag2 += 1
    else:
        pass

if flag1 == 0 and flag2 == 0:
    print('True')
else:
    print('False')