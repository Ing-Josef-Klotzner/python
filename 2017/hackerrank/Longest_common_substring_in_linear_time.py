G=range;w=raw_input;z=L,m,h=[0]*3
s=w();t=len(s);s+='!%s#'%w();u=len(s);I=z*u
def f(s,n):
 def r(o):
    b=[[]for _ in s];c=[]
    for x in B[:N]:b[s[x+o]]+=x,
    map(c.extend,b);B[:N]=c
 M=N=n--~n/3;t=n%3%2;B=G(n+t);del B[::3];r(2);u=m=p=r(1)>r(0);N-=n/3
 for x in B*1:v=s[x:x+3];m+=u<v;u=v;B[x/3+x%3/2*N]=m
 A=1/M*z or f(B+z,M)+z;B=[x*3for x in A if x<N];J=I[r(0):n];C=G(n)
 for k in C:b=A[t]/N;a=i,j=A[t]%N*3-~b,B[p];q=p<N<(s[i:i-~b],J[i/3+b+N-b*N])>(s[j+t/M:j-~b],J[j/3+b*N]);C[k]=x=a[q];I[x]=k;p+=q;t+=1-q
 return C
S=f(map(ord,s)+z*40,u)
for i in G(u):
 h-=h>0;j=S[I[i]-1]
 while s[i+h]==s[j+h]:h+=1
 if(i<t)==(t<j)<=h>m:m=h;L=min(i,j)
print-~L,L+m
