import io
import sys

_INPUT = """\
6
3 2
299792458 3141
"""
sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def multi(a,b,mod):
    m=0
    while m**2<len(a): m+=1
    return [sum([a[i//m*m+j]*b[j*m+i%m]%mod for j in range(m)])%mod for i in range(m**2)]
  def pow_mat(a,n,mod):
    m=0
    while m**2<len(a): m+=1
    res=[1 if i%(m+1)==0 else 0 for i in range(m**2)]
    tmp=[a]
    for i in range(59):
      tmp.append(multi(tmp[-1],tmp[-1],mod))
    for i in range(60):
      if (n>>i)&1==1: res=multi(res,tmp[i],mod)
    return res
  mod=998244353
  N,D=map(int,input().split())
  F=[1]
  for i in range(D+1):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(D+1):
    I.append(I[-1]*(D+1-i)%mod)
  I=I[::-1]
  ans=0
  for i in range(D+2):
    a=[]
    if i<D:
      a.append(F[D-1]*I[i]*I[D-1-i]%mod)
    else:
      a.append(0)
    if i>0 and i<=D:
      a.append(F[D-1]*I[i-1]*I[D-i]%mod)
      a.append(F[D-1]*I[i-1]*I[D-i]%mod)
    else:
      a.append(0)
      a.append(0)
    if i>1:
      a.append(F[D-1]*I[i-2]*I[D+1-i]%mod)
    else:
      a.append(0)
    b=pow_mat(a,N-1,mod)
    ans+=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]
    ans%=mod
  print(ans)