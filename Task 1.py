from datetime import datetime

def get_days_from_today(date):
    choosen_date= datetime.strptime(date, "%Y-%m-%d")
    current_date=datetime.today()
    delta = current_date - choosen_date
    return delta.days
choosen_date= ("2024-05-20")
print(get_days_from_today(choosen_date))

