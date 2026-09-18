A, B = map(int, input().split())

if A > B:
    num = A - B
elif B > A:
    num = B -A
else:
    num = 0

print(num)
