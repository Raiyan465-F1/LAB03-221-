
test_case = int(input())

for i in range(test_case):
    a, n, m = map(int, input().split())
    def exp(a, b, m):
        res = 1
        while b > 0:
            if b % 2: res = (res*a) % m
            a = (a**2) % m
            b //= 2
        return res


    def solve(a, n, m):
        if n == 1: return a % m

        half = n//2
        res_half = solve(a, half, m)
        maxi = exp(a, half, m)

        if n % 2: return (res_half + maxi*res_half + exp(a, n, m)) % m
        else: return (res_half + maxi*res_half) % m

    print(solve(a, n, m))