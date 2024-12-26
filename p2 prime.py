def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_till_n(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

print(f"Prime numbers till {n}: {primes_till_n(n)}")

print(f"First {n} prime numbers: {first_n_primes(n)}")

#the input 7 or 4 or any number
