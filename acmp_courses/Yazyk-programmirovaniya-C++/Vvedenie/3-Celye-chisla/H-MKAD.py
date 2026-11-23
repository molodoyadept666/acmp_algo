velocity, time = map(int, input().split())
start_position = 1
distance = velocity * time
answer = (start_position + distance) % 109

if answer == 0:
    answer = 109

print(answer)