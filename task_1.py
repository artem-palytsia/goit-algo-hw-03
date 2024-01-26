from datetime import datetime as dtdt

def get_days_from_today(date):
    try:
        date_object=dtdt.strptime(date, '%Y-%m-%d').date()
        current_date =  dtdt.now()
        difference = current_date.toordinal() - date_object.toordinal()
        return difference
    except Exception as error:
        print('Введіть дату у форматі: РРРР-ММ-ДД')
        return None

print(get_days_from_today('2024-01-12'))



    