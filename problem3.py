a = int(input())
if a%2==0:
    a= a-1
for i in range(0, a):
    print(i + (i + 1), end=" ")
    i += 1