set1 = {1,3,5,7,9,4}
set2 = {2,5,4,10,8,9}
print("Set1: ", set1)
print("Set2: ", set2)

print("\nUnion:")
print(set1 | set2)

print("\nIntersection:")
print(set1 & set2)

print("\nDifference (A-B):")
print(set1 - set2)

nums = {1,4,3,7,10,6}

print("\nAdd element:")
nums.add(2)
print(nums)

print("\nRemove element:")
nums.remove(4)
print(nums)

print("\nRemove random element:")
nums.pop()
print(nums)