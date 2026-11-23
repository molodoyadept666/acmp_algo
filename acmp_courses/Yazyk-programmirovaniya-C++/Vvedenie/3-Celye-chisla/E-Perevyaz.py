bandage_length = int(input())
if bandage_length % 10 != 0:
    print(bandage_length // 10 + 1)
else:
    print(bandage_length // 10)
