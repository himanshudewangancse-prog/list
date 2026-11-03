# a = [3,-1,4,-5,9]
# p=[]
# n=[]
# def posneg():
#     for i in a:
#         if i >= 0:
#             p.append(i)
#         else:
#             n.append(i)
#     print(p)
#     print(n)

# posneg()


# l = [10,20,30,40]
# def avg():
#     sum = 0
#     for i in l:
#         sum = sum + i
#     avg = sum/(len(l))
#     print(f"Mean : {avg}")
# avg()


# l = [4,8,2,9,1]
# def largest():
#     larg = 0
#     index = 0
#     for i in range(len(l)):
#         if l[i] > larg:
#             larg = l[i]
#             index = i
#     print(f"large value {larg} at index {index}")
# largest()



# l = [4,2,9,1,8]
# large = l[0]
# sec_large = l[0]
# for i in l:
#     if i > large:
#         sec_large = large
#         large = i
#     elif i > sec_large:
#         sec_large = i 
# print(sec_large)



# l = [10,30,40,60,50]
# l = [10,20,30,40,50]

# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("not sorted")
#         break
# else:
#     print("sorted")
