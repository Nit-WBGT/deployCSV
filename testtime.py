import datetime

def inttime():
 dt=datetime.datetime.now()
 timeh=dt.hour
 time_hour=int(timeh)
 return time_hour
 
def filename():
 dt=datetime.datetime.now()
 timepath = datetime.date.today()
 timepath = timepath.strftime("%Y-%m-%d")
 return timepath

def foldername():
 dt=datetime.datetime.now()
 timepath = datetime.date.today()
 timepath = timepath.strftime("%Y-%m")
 return timepath

def intmin():
 dt=datetime.datetime.now()
 timem=dt.minute
 time_min=int(timem)
 return time_min

def event_timer():
 dt=datetime.datetime.now()
 timeh=dt.hour
 timem=dt.minute
 time_hour=int(timeh*100)
 time_min=int(timem)
 time_ev = time_hour + time_min
 return time_ev
