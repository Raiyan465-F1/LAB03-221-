lenght = int(input())
arr = list(map(int, input().split()))
result = []

def makeTree(arr, i, n):
    if i>n:
        return
    mid = (n+i)//2
    print(arr[mid], end=" ")
    makeTree(arr, i, mid-1)
    makeTree(arr, mid+1, n)
    
    
makeTree(arr, 0, lenght-1)
print()