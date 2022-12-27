from collections import defaultdict
from datetime import datetime, timedelta


all_birthdays = [{"name": "Nick", 'birthday': datetime(year=1987, month=12, day=31)},{"name": "Dmytrii", 'birthday': datetime(year=1987, month=12, day=29)}, {"name": "Anastasiia", 'birthday': datetime(year=1995, month=12, day=29)}]


def get_birthdays_per_week(staff_list):
    today = datetime.now()
    upcoming_birthdays = defaultdict(list)
    week_interval = {((today + timedelta(days=n)).day,(today + timedelta(days=n)).month): (today + timedelta(days=n)).strftime('%A') for n in range(0,7)}

    for person in staff_list:
        birth_date = (person["birthday"].day, person["birthday"].month)
     
        if birth_date in week_interval and week_interval[birth_date] in ['Saturday', 'Sunday']:
            upcoming_birthdays["Monday"].append(person["name"])
        elif birth_date in week_interval:
            upcoming_birthdays[week_interval[birth_date]].append(person["name"])    
  
    for day, names in upcoming_birthdays.items():
        print(f"{day}: {', '.join(names)}")    

get_birthdays_per_week(all_birthdays)