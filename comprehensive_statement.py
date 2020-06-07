
alpha = [chr(i) for i in range(ord('a'), ord('a')+26)]
print(alpha)

# [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

numbers = [ i * (i-1) for i in range(1, 10)]

print(numbers)

factors  = [ i for i in range(1, 100) if 100%i == 0 ]
print(factors)