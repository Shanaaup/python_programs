"""
Given an array representing the heights of towers, the task is to find, for each tower, the index of the nearest tower that is shorter than it.
The search for a shorter tower can be performed by looking to the left and right sides of each tower.

The following rules apply:

If there are two or more smaller towers at the same distance from the current tower, choose the tower with the smallest height.
If two towers have the same height, choose the one with the smaller index.
Example 1:

Input : Array: [1, 3, 2]
Output : Indexes: [-1, 0, 0]
Explanation:
For the tower at index 0, there is no tower shorter than it, so the output is -1.

For the tower at index 1 (height 3), there are two towers (heights 1 and 2) at the same distance. Following the rules, we choose the tower with the smallest height, which is at index 0.
For the tower at index 2 (height 2), the only tower shorter than it is at index 0.
Therefore, the final output is the array of indexes: [-1, 0, 0].
"""
def tow(i,l):
  w=list(set(l))
  j=sorted(w)
  for k in range(len(j)):
    if i==j[k]:
      if k==0:
        return -1
      else:
        m=j[0]
        return l.index(m)

l=list(map(int,input().split()))
h=[]
for i in l:
  k=tow(i,l)
  h.append(k)
print(h)