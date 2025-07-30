def gcd(a, b):
    if b == 0:
        return a 
    return gcd(b, a % b)

def factorize(n: int) -> list[tuple[int,int]]:
    factors = []
    p = 2
    while p * p <= n:
        cnt = 0
        while n % p == 0:
            cnt += 1
            n //= p
        if cnt > 0:
            factors.append((p, cnt))
        p += 1
    if n > 1:
        factors.append((n, 1)) 
    return factors 

cache_phi = dict()

def phi(n: int) -> int:
    if n in cache_phi:
        return cache_phi[n]
    factors = factorize(n)
    result = n
    for prime, exponent in factors:
        result *= (prime - 1)
        result //= prime 
    cache_phi[n] = result 
    return result     
            

class ModInt:
    def __init__(self, value: int, modulo: int):
        self.M = modulo 
        self.x = value % modulo 
        
    def __add__(self, other: 'ModInt') -> 'ModInt':
        # we can only add numbers if they have the same modulo 
        assert self.M == other.M, 'You cannot operate on numbers with different modulo'
        return ModInt(self.x + other.x, self.M)
    
    def __sub__(self, other: 'ModInt') -> 'ModInt':
        assert self.M == other.M, 'You cannot operate on numbers with different modulo'
        return ModInt(self.x - other.x + self.M, self.M)
    
    def __mul__(self, other: 'ModInt') -> 'ModInt':
        assert self.M == other.M, 'You cannot operate on numbers with different modulo'
        return ModInt(self.x * other.x, self.M)
    
    def __pow__(self, exponent: int):
        if exponent == 0:
            return ModInt(1, self.M)
        if exponent % 2 == 1:
            return (self ** (exponent - 1)) * self 
        p = self ** (exponent // 2)
        return p * p 
            
    def _inverse(self):
        assert gcd(self.x, self.M) == 1, 'You cannot invert numbers that are not coprime with the modulo'
        return self ** (phi(self.M) - 1)
    
    def __truediv__(self, other: 'ModInt') -> 'ModInt':
        assert self.M == other.M, 'You cannot operate on numbers with different modulo'
        # find the inverse of other.x 
        return self * other._inverse()
        

def main():
    x = ModInt(value = 3, modulo = 4)
    y = ModInt(value = 7, modulo = 4)
    

    a = x + w
    s = x - w
    m = x * w
    z = x / w
    
    # # print(a.x)
    # assert a.x == 2
    # assert s.x == 0
    # assert m.x == 1
    # assert z.x == 1 
    # 3 * 7^(-1) == (3 * 3) == 9 == 1 % 4 
    

if __name__ == '__main__':
    main()