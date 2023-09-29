import datetime
from openpyxl import Workbook #устанавливаем в терминале коммандой pip install openpyxl
wb = Workbook()

ws = wb.active

y = 2023
dt = datetime.datetime(y, 9, 1)
exported_dates = []

while dt.month >= 5 and dt.year == y or dt.month<=5 and dt.year == y+1:

    first_forbidden_period = datetime.datetime(y, 10, 9)<dt<datetime.datetime(y, 10,15) or datetime.datetime(y, 11, 20)<dt<datetime.datetime(y, 11,26) or datetime.datetime(y, 12, 18)<dt<datetime.datetime(y, 12,22) or dt == datetime.datetime(y, 11, 4) or datetime.datetime(y+1, 1, 1)<dt<datetime.datetime(y+1, 1,7) or datetime.datetime(y+1, 2, 19)<dt<datetime.datetime(y+1, 2,25) or datetime.datetime(y+1, 4, 8)<dt<datetime.datetime(y+1, 4,14) or dt == datetime.datetime(y+1, 1, 8) or dt == datetime.datetime(y, 3, 8) or dt == datetime.datetime(y+1, 5, 1) or dt == datetime.datetime(y+1, 5, 9) 

    multiple_dates = 2#СЮДА ВНОСИТЬ КОЛИЧЕСТВО УРОКОВ В ДЕНЬ(ЕСЛИ ДВА УРОКА = 2, ОДИН УРОК = 1)
    if dt.weekday()==1 or dt.weekday()==3:#СЮДА ВНОСИТЬ ДНИ НЕДЕЛИ В КОТОРЫЕ ЕСТЬ УРОКИ ПН==0, ВТ==1...., если есть еще дни добавить условие  or dt.weekday()==4
        if first_forbidden_period:
            dt+=datetime.timedelta(days=1)
            continue
        else:
            while multiple_dates>0:
                exported_dates.append(dt.strftime("%d.%m.%y"))
                multiple_dates-=1
    dt+=datetime.timedelta(days=1)
for i in range(len(exported_dates)):
    ws[f'A{i+1}'] = exported_dates[i]

wb.save("dates.xlsx")