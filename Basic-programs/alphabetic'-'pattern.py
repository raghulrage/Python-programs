import string
n = int(input())
alpha=string.ascii_lowercase
l = []
for i in range(n):
    s = "-".join(alpha[i:n])
    l.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(l[:0:-1]+l))
'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
