def merge(a1, a2):
    array = []
    i = 0
    j = 0
    inversions = 0
    
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            array.append(a1[i])
            i += 1
        else:
            array.append(a2[j])
            j += 1
            inversions += len(a1) - i  # Count inversions
            
    array += a1[i:]
    array += a2[j:]
    return array, inversions
    
def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr)//2
    
    left, left_inversions = mergeSort(arr[:mid])
    right, right_inversions = mergeSort(arr[mid:])
    
    merged, merge_inversions = merge(left, right)
    
    total_inversions = left_inversions + right_inversions + merge_inversions
    return merged, total_inversions

N = int(input())
arr = list(map(int, input().split()))
sorted_array, inversion_count = mergeSort(arr)
print(inversion_count)
print(*sorted_array)