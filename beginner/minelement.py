number=[]
n=int(input("Enter no.of elements:"))

for i in range(n):
    item=input()
    number.append(item)
print(number)
print("min element:",min(number))
