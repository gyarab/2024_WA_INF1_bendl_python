def fibonacci(n):
    if n == 0:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence[:n]
print(fibonacci(10))