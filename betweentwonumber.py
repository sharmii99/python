def isPrime(n):
  if(n==1 or n==0):
    return False
  for i in range(2,n):
    if(n%i==0):
      return False
  return True
n=int(input("enter lower range="))
N=int(input("enter the upper range ="))
for i in range(n,N+1):
  if(isPrime(i)):
    print(i,end=" ")
