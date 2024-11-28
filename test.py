def fibonacci(n):
    if n == 0:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence[:n]

def is_prime(n):
  if not isinstance(n, int) or n <= 0:
    raise ValueError("n must be a non-negative integer")
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

def rotate_array(arr, n):
    if not isinstance(arr, list) or not isinstance(n, int):
      raise ValueError("Invalid arguments")
    if len(arr) == 0:
      return arr
    n = n % len(arr)
    return arr[-n:] + arr[:-n]

def split_into_threes(text):
  if not isinstance(text, str):
    raise ValueError("Invalid argument")
  return [text[i:i+3] for i in range(0, len(text), 3)]

def vowels_and_consonants(text):
  if not isinstance(text, str):
    raise ValueError("Invalid argument")
  vowels = [c for c in text if c.lower() in 'aeiou' and c.isalpha()]
  consonants = [c for c in text if c.lower() not in 'aeiou' and c.isalpha()]
  return vowels, consonants
  def count_vowels_and_consonants(text):
    if not isinstance(text, str):
      raise ValueError("Invalid argument")
    vowels = 'aeiou'
    counts = {'vowels': 0, 'consonants': 0}
    for char in text.lower():
      if char.isalpha():
        if char in vowels:
          counts['vowels'] += 1
        else:
          counts['consonants'] += 1
    return counts