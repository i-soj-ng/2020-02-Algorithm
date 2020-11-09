year = int(input("연도를 입력하세요: "))
month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_days = 0

for year_item in range(1, year):
    total_days = total_days + 365

    if (year_item % 400 == 0 and month >= 3) or ((year_item % 4 == 0 and month >= 3) and (not (year_item % 100 == 0))):
        total_days = total_days + 1

for month_index in range(1, month):
    total_days = total_days + month_days[month_index]

total_days = total_days + day

if total_days % 7 == 0:
    print("토요일")
elif total_days % 7 == 1:
    print("일요일")
elif total_days % 7 == 2:
    print("월요일")
elif total_days % 7 == 3:
    print("화요일")
elif total_days % 7 == 4:
    print("수요일")
elif total_days % 7 == 5:
    print("목요일")
elif total_days % 7 == 6:
    print("금요일")
