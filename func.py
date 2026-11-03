# write a func tocalculate the unique elements in voth the list.

# a1 = [1,2,3,4]
# a2 = [2,3,5,6]
# def unique(a1,a2):
#     a1 = set(a1)
#     a2 = set(a2)
#     result = (a1|a2) - (a1&a2) # result = a1^a2
#     return result
# print(unique(a1,a2))

# write a python func to print the count of unique words in the given sentence.

s = "The cat and the hat"
def unique(s):
    s = s.lower().split()
    # conv_s = set(s)
    result = len(set(s))
    return result
print(unique(s))