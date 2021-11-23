s2 = input('Введите вашу фразу:')
s1 = s2

d2 = {}
for l1, l2 in zip(s1, s2):
    d2[l1] = l2
b = "abcdefghijklmnopqrstuvwxyz"
c = range(1,27)
di = dict(zip(b, c))
d3 = d2.copy()







d2.update(di)
#print(d2)

for key in d2.keys():
    if d2[key] == d3[key]:
        print(d2.values())