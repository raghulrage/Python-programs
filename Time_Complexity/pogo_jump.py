'''
Pogo Jump 2
Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.
Return True or False
'''
def canJump(nums):
  x = 1
  for y in nums[::-1]:
      x = max(x-1,y)
      if x == 0:
        return False
  return True
n = int(input())
if n==1 or n==0:
  print('True')
  exit()
m = list(map(int,input().split()))
print(canJump(m))
