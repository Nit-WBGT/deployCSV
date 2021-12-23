from flask import Flask,render_template, request, abort
from requests_oauthlib import OAuth1Session
import sys
import os
import json
import threading
import time
import datetime
import timeint
import testtime
import gitcomand
import ops_csv


global t_time
global path
global time_p
global WBGT
global time_data 
global time__data


def timer_nit():
    t=threading.Timer(60,timer_nit)
    dt_now_jst_aware = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    global t_time
    global time_data 
    time__data = testtime.intmin()
    if t_time == dt_now_jst_aware.time().hour:
        t_time = t_time + 1
    time__data = testtime.intmin()
    if  time__data % 1 == 0 and time_data != time__data:
        time_data = testtime.intmin()
        time_p = timeint.readtime()
        ops_csv.copy()
        gitcomand.git()
        ops_csv.delete()
        

    t.start()
    
    


app = Flask(__name__)

#herokuへのデプロイが成功したかどうかを確認するためのコード
@app.route("/")
def main_page():
    return render_template("WBGT.html")

   
# ポート番号の設定
if __name__ == "__main__":
    #定期タイマー実行部分
    t = threading.Thread(target=timer_nit)
    dt_now_jst_aware = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    t_time = dt_now_jst_aware.time().hour
    time_data = testtime.intmin()
    t.start()
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
