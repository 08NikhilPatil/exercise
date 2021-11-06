'''P=[1,2,3,5,6]
Q=[1,2,3,4]
def equality(P,Q):
  if len(P) != len(Q):
    return False
  for ele in P:
    if ele not in Q:
      return False
  return True
  #if len(P) != len(Q):
    #return False
  size =len(P)
  for i in range(size):
    if P[i] !=Q[i]:
      return False
  return True

#return P==Q



print(equality(P,Q))'''


def bin_to_dec(bin):
    if len(bin) == 1:
        return int(bin)
    init = bin[:-1]
    last = bin[-1]
    return bin_to_dec(init) * 2 + int(last)

print(bin_to_dec('1010'))

#number of digits in a number
def f(n):
  if n<10:
    return 1
  return 1+f(n//10)

#sum of digits of a number
def g(n):
  if n<10:
    return n
  return n%10 + g(n//10)

#factorial of a number
def h(n):
  if n<=1:
    return n
  return n*h(n-1)
print(h(1))

#binary search
def search(L,k):
  if len(L)==0:
    return False
  if len(L)==1:
    if L[0]==k:
      return True
    return False
  
  if len(L)>0:
    mid = len(L)//2
    mid_ele=L[mid]
    if mid_ele==k:
      return True
    if k>mid_ele:
      return search(L[mid+1:],k)
    if k<mid_ele:
      return search(L[:mid],k)

print(search([1,4,6,8,10],9))