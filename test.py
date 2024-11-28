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




  def class_and_break_time(start_class, end_class):
      if not isinstance(start_class, int) or not isinstance(end_class, int):
          raise ValueError("Invalid arguments")
      if start_class < 1 or end_class < 1 or start_class > end_class:
          raise ValueError("Invalid class range")
      if start_class > 8 or end_class > 8:
          raise ValueError("Arguments must be between 1 and 8")
  
      class_time = (end_class - start_class + 1) * 45
  
      break_times = [0, 5, 10, 20, 10, 10, 5, 0]
      break_time = sum(break_times[start_class:end_class+1])
  
      return class_time, break_time