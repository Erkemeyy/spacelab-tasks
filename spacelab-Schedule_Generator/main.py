from datetime import datetime, timedelta


def generate_schedule(days, work_days, rest_days, current_date):
    schedule = []

    while len(schedule) < days - 1:
        # Add work days
        for i in range(work_days):
            schedule.append(current_date)
            current_date += timedelta(days=1)
        # Add rest days
        for i in range(rest_days):
            current_date += timedelta(days=1)

    return schedule


start_date = datetime(2001, 1, 30)
print(generate_schedule(5, 2, 1, start_date))
