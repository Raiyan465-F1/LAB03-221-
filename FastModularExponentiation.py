
def FastModularExponentiation(base, power, mod=107):
    if power == 0:
        return 1
    if power % 2 == 0:
        return FastModularExponentiation(base, power // 2, mod) ** 2 % mod
    else:
        return base * FastModularExponentiation(base, power - 1, mod) % mod
    
base, power = map(int, input().split())

print(FastModularExponentiation(base, power))