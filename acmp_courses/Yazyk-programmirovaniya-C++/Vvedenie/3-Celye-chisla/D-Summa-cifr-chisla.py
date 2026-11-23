number = int(input())
units = tens = hundreds = number

units %= 10
tens = (tens // 10) % 10
hundreds //= 100

print(units + tens + hundreds)