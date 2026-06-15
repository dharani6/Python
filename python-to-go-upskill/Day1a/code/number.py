n = -1234
sign = -1 if n < 0 else 1
print(sign * int(str(abs(n))[::-1]))
# Input  : -1234
# Output : -4321
