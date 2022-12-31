from datetime import datetime, date, timedelta


def get_all_dates_in_year():
    dates = []
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)

    delta = end_date - start_date

    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        dates.append(day)

    return dates


def get_unix_time(dt, time):
    ms = datetime(dt.year, dt.month, dt.day, time[0], time[1], time[2]).timestamp() * 1000
    return int(ms)