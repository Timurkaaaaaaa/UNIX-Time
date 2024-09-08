import eel
import os
import datetime 
from datetime import datetime
from datetime import date, time


@eel.expose
def get_unix(d, m, y, h, minute, second):
	day=d
	print("Запущено")
	print(day, m, y, h, minute, second)

	day=int(day)
	m=int(m)
	y=int(y)
	h=int(h)
	minute=int(minute)
	second=int(second)
	if day <=31 and m <=12 and minute<=59 and second<=59 and h<=11:
		d = date(y, m, day )
		t = time(h, minute, second)

		date1 = date(d.year, d.month, d.day)
		time1 = time(t.hour, t.minute, t.second)
		print(date1, time1)

		date_time = str(date1) + " " + str(time1)
		unixdatetime = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
		unixdatetime = unixdatetime.timestamp()
		unixdatetime = int(unixdatetime)

		print("UNIX - ", unixdatetime)
		return "Результат:\n" + str(unixdatetime)
	else:
		eel.error()  
		return "Результат: Ошибка"
	
 
eel.init("web")

eel.start("main.html", size=(600, 790)) 