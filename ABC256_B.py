import io
import sys

_INPUT = """\
6
4
1 1 3 2
3
1 1 1
10
2 2 4 1 1 1 4 2 2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import accumulate
  N=int(input())
  A=list(map(int,input().split()))
  A=list(accumulate(A[::-1]))
  print(len([i for i in range(N) if A[i]>=4]))