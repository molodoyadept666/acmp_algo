schoolch, apples = map(int, input().split())
apples_each_first = apples // schoolch
if apples % schoolch != 0:
    remainder_first = apples - (apples_each_first * schoolch)
    if apples % schoolch != 0:
        offended_second = schoolch - remainder_first
        print(apples_each_first, remainder_first, offended_second)
    else:
        print(apples_each_first, remainder_first, 0)
else:
    print(apples_each_first, 0, 0)