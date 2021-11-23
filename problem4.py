a = list(map(int,input().split()))
count = {}
for i in range(1,10):
    c=0
    for j in a:
        if j%i==0:
            c+=1
        count[i]=c
print(count)