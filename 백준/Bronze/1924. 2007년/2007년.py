day = 0
day_for_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
x, y = map(int,input().split())
 
for i in range(x-1):
    day = day + day_for_month[i]
day = (day + y) % 7
 
print(day_of_week[day])