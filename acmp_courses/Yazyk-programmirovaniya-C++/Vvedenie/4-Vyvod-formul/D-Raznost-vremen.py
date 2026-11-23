h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())

start = s1 + m1 * 60 + h1 * 3600
end = s2 + m2 * 60 + h2 * 3600
print(end - start)