# Probably using Two Pointers Technique

# Currency called stars
# Need to find 50 stars by December 25th

# Read in all lines of file to list of lines
numlist = [line.rstrip() for line in open('input')]
numlist = list(map(int, numlist))
numlist.sort()

# Debug to print list
# for x in range(len(numlist)):
#   print(numlist[x])

wantSum = 2020
ptr1 = 0
ptr2 = len(numlist) - 1

while (ptr1 < ptr2):
  if(numlist[ptr1] + numlist[ptr2] == wantSum):
    print(f'{numlist[ptr1]} & {numlist[ptr2]}')
    answer = numlist[ptr1] * numlist[ptr2]
    print(answer)
    exit()
  elif (numlist[ptr1] + numlist[ptr2] < wantSum): ptr1+=1
  else: ptr2-=1
print(f'No pair of numbers = {wantSum}')

# Solution found in O(n)