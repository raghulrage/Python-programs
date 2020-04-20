'''Write a Program to extract the user id, domain name and suffix from the following email addresses.'''

for i in input().split():
    if '@' in i:
        for j in i:
            print(j in j.isalnum() else ' ',end='')
        print()
