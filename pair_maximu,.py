
def solve(A, left, right):
    
    if right - left < 1:
        return float('-inf')
    if right - left == 1:
        return A[left] + A[right] ** 2
    
    
    mid = (left + right) // 2
    
    
    max_left = solve(A, left, mid)
    max_right = solve(A, mid + 1, right)
    
 
    max_A_left = max(A[left:mid + 1])
    max_cross = max(max_A_left + A[j] ** 2 for j in range(mid + 1, right + 1))
    
 
    return max(max_left, max_right, max_cross)
 
N = int(input(""))
A = list(map(int, input("").split()))
 
 
result = solve(A, 0, N - 1)
print("", result)