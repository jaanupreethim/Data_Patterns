from datetime import datetime

def check_dates(date_str1, date_str2):
    d1 = datetime.strptime(date_str1, "%b %d %Y")
    d2 = datetime.strptime(date_str2, "%b %d %Y")
    if d1 > d2:
        d1, d2 = d2, d1
    
    is_exact_month = False
    if d1.day == d2.day:
        if d2.year == d1.year and d2.month == d1.month + 1:
            is_exact_month = True
        elif d2.year == d1.year + 1 and d1.month == 12 and d2.month == 1:
            is_exact_month = True
            
    if is_exact_month:
        return "Exactly 1 month apart"
    
    total_days_in_d1_month = (datetime(d1.year + (1 if d1.month == 12 else 0), 1 if d1.month == 12 else d1.month + 1, 1) - datetime(d1.year, d1.month, 1)).days
    delta_days = (d2 - d1).days
    
    if delta_days < total_days_in_d1_month:
        return "Less than 1 month apart"
    return "More than 1 month apart"

if __name__ == "__main__":
    dt1 = input("Enter Date 1 (e.g. June 06 2011 -> Jun 06 2011): ")
    dt2 = input("Enter Date 2 (e.g. July 06 2011 -> Jul 06 2011): ")
    print(check_dates(dt1, dt2))
