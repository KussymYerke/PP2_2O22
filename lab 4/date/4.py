from datetime import date

def diff_dates(date1, date2):
    return abs(date2-date1).days

d1 = date(2013,1,1)
d2 = date(2013,9,13)
result1 = diff_dates(d2, d1) * 86400
print(result1)