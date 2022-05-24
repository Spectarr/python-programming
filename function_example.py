def convert_days_to_seconds(days):
    hours = 24*days
    minutes = hours * 60
    seconds = minutes * 60
    return seconds

total_seconds = convert_days_to_seconds(365)
milliseconds = total_seconds * 1000
print(f"всего миллисекунд в году: {milliseconds}")
print(f"всего секунд в году: {total_seconds}")
