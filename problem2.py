# Project Euler problem no. 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

x = 1
result = 0
while fib(x) <= 4000000:
    if fib(x)%2 == 0:
        result += fib(x)
    x += 1

print(result)