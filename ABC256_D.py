import io
import sys
from threading import activeCount

_INPUT = """\
6
3
10 20
20 30
40 50
3
10 40
30 60
20 50
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import accumulate
  N=int(input())
  ans=[0]*(2*10**5+1)
  for i in range(N):
    L,R=map(int,input().split())
    ans[L]+=1
    ans[R]-=1
  ans=list(accumulate(ans))
  ans2=[]
  flg=0
  for i in range(2*(10**5)+1):
    if flg==0:
      if ans[i]>0: L=i; flg=1
    else:
      if ans[i]==0: R=i; ans2.append((L,R)); flg=0
  if flg==1:
    ans.append((L,2*(10**5)+1))
  for i in range(len(ans2)): print(*ans2[i])