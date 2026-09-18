n = int(input())

if n%2 == 0:
    n = n//2
if n%2 != 0:
    n = (n+1)//2

print(n)