def binary_search(arr, target):
    low=0
    high=len(arr) - 1
    while low <= high:
        mid=(low + high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1  
sorted_numbers=list(map(int, input("Enter elements: ").split()))
target_value=int(input("Enter the number :"))
result = binary_search(sorted_numbers,target_value)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")