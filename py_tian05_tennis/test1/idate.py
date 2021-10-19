import datetime
t = datetime.datetime.now()
itoday = t.strftime("%Y%m%d")
i7d = (datetime.datetime.now()+datetime.timedelta(days=7)).strftime("%Y%m%d")
print(itoday)
print(i7d)