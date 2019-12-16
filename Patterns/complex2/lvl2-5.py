n = int(input())
alpha=[chr(97+i) for i in range(n)]
l = []
for i in range(n):
    s = "-".join(alpha[i:n])
    l.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(l[:0:-1]+l))
