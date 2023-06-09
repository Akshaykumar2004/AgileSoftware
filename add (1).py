#ADDITION
def add(a,b):
  res=a+b
  return res

print(f"The sum is {add(2,3)}")

#ADD EVEN NUMBERS
def add_even(a,b):
  s=0
  if a%2==0 and b%2==0:
    s=a+b
    return s
  else:
    print("The numbers are not even")

print(add_even(2,4))

#ADD ODD NUMBERS
def add_odd(a,b):
  s=0
  s=a+b
  if a%2==1 and b%2==1:
    s=a+b
    return s
  else:
    print("The numbers are not odd")

print(add_odd(3,5))

#SUM OF N NUMBERS

def sum_n(n):
  s=0
  for i in range(1,n+1):
    s=s+i
  return s
print(sum_n(10))