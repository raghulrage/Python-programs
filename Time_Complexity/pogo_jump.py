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
m = list(map(int,input().split()))
print(canJump(m))
