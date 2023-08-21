import datetime

dt = datetime.datetime(day = 4, month=11, year=2020, hour=14, minute=53, second=0)
print(dt)
print(dt.strftime("%y/%B/%d %H:%M:%S"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print("Dia de la semana:", dt.isoweekday())
print("Dia del año:", dt.timetuple().tm_yday)
print("Semana en el año:", dt.isocalendar()[1])