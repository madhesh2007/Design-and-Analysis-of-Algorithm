def linear_search(a, n):
    for i in range(len(a)):
        if a[i] == n:
            return i
    return -1

a = [1,2,3,4,5,6,7,8,9,10]
n = int(input("Enter the number: "))

result = linear_search(a, n)

if result != -1:
    print("Found at index:", result)
else:
    print("Not found")