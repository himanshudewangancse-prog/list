a = [3,-1,4,-5,9]
positive = []
negative = []

for i in a :
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)
print(f"{positive} {negative}")


a = [3,-1,4,-5,9]

sum = 0 
for i in a :
    sum += i
avg = sum/len(a)
print(avg)

a = [3,-1,4,-5,9]
large = a[0]
index = 1
for i in range(len(a)):
    a[i] < large
    large = a[i]
    index = i
print(f"{large} {index}")


a = [3,-1,4,-5,9]
large = a[0]
sec_large = a[0]

for i in a:
    if i > large:
        sec_large = large
        large = i
    elif i > sec_large:
        sec_large = i
print(f"{large} {sec_large}")

a = [3,-1,4,-5,9]
a = [1,2,3,4,5,6,7,8,9]

for i in range(len(a)-1):
    if a[i] > a[i+1]:
        print("not sorted")
        break
else:
    print("sorted")