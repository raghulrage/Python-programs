'''
You will be provided with N lines of what are possibly IP addresses. You need to detect if the text contained in each of the lines represents an

(a)IPv4 address

(b)IPv6 address or

(c)None of these.



The typical format of an IPv4 address is A.B.C.D where A, B, C and D are Integers lying between 0 and 255 (both inclusive).

The 128 bits of an IPv6 address are represented in 8 groups of 16 bits each. Each group is written as 4 hexadecimal digits and the groups are separated by colons (:).

The address 2001:0db8:0000:0000:0000:ff00:0042:8329 is an example of IPV6 representation. 
'''

for i in range(int(input())):
    n = input()
    if '.' in n:
        print('IPv4')
    if ':' in n:
        print('IPv6')
