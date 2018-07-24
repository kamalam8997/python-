num=int(input(""))
count=0
for a in range(1,11):
    if a==num:
        count=1
if(count==1):
    print("yes")
else:
    print("no")
