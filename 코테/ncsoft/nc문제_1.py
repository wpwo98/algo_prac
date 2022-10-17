answer = ''
source = 'execute'
dest = ''
if len(source) == 0:
    print(dest)
#sorted(source)
s = ''.join(dict.fromkeys(source))
s1 = sorted(s)
for i in range(len(s1)):
    dest += s1[i]
for j in range(len(s1)):
    c = source.count(s1[j]) - 1
    dest += s1[j] * c
print(dest)