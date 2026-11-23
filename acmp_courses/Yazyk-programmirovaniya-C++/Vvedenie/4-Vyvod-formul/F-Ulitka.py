pole_height, velocity_upward, velocity_downward = map(int, input().split())
if pole_height > velocity_upward:
    velocity_per_day = velocity_upward - velocity_downward
    print(((pole_height - velocity_upward) + velocity_per_day - 1) // velocity_per_day + 1)
else:
    print(1)