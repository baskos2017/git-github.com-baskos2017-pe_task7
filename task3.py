def gen_primes(n, i = 2, prim = []):
    
    while n:
        if all(i%d for d in prim):
            n -= 1
            prim.append(i)
            yield i
        i += 1 + i%2
 
for i in gen_primes(10):
    print(i)