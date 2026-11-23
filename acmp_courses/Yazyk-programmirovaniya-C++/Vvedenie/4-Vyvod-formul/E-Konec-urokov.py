lesson_number = int(input())
start_time_minutes = 9 * 60
lessons_duration = lesson_number * 45
long_breaks_durations = (lesson_number - 1) // 2 * 15
short_breaks_durations = lesson_number // 2 * 5
final_time_minutes = start_time_minutes + lessons_duration + long_breaks_durations + short_breaks_durations
lesson_end_hours = final_time_minutes // 60
lesson_end_minutes = final_time_minutes % 60
print(lesson_end_hours, lesson_end_minutes)