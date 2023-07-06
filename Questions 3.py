from datetime import datetime, timezone

current_time = datetime.now(timezone.utc)

# Convert the time to a string format
current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S GMT")

#display the current time in GMT
print("Current time in GMT:")
print(current_time_str)


