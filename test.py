def fibonacci(n):
    if n == 0:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence[:n]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def primes_in_range(a, b):
  if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
    raise ValueError("a and b must be non-negative integers")
  if a > b:
    a, b = b, a
  return [n for n in range(a, b+1) if is_prime(n)]
