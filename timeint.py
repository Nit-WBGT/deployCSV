import datetime
def readtime():
 dt=datetime.datetime.now()
 timey=dt.year
 timem=dt.month
 timed=dt.day
 timeh=dt.hour
 timey=str(timey)
 time_year=timey
 time_month=str(timem)
 time_day=str(timed)
 time_hour=str(timeh)
 timepath = datetime.date.today()
 timepath = timepath.strftime("%Y-%m-%d")
 return  timepath

def time_folder_path():
 dt=datetime.datetime.now()
 timey=dt.year
 timem=dt.month
 timed=dt.day
 timeh=dt.hour
 timey=str(timey)
 time_year=timey
 time_month=str(timem)
 time_day=str(timed)
 time_hour=str(timeh)
 timepath = datetime.date.today()
 folderpath = timepath.strftime("%Y-%m")
 return  folderpath


