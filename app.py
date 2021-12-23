from flask import Flask,render_template, request, abort
from requests_oauthlib import OAuth1Session
import sys
import os
import json
import threading
import time
import datetime
import timeint
import readCSV
import testtime

ACCESS_TOKEN = os.environ['access_token']
ACCESS_TOKEN_SECRET = os.environ['access_token_secret']


consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']

access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

global t_time
global path
global time_p
global WBGT
path = 'data/'
global time_data 
global time__data

errorMs="WBGTの更新が確認できませんでした。WBGTの値を確認したい場合一番近い投稿の数値をご参考ください。"
level5="運動は原則中止 : 特別の場合以外は運動を中止する。特に子どもの場合には中止すべき。"
level4="厳重警戒（激しい運動は中止）: 熱中症の危険性が高いので、激しい運動や持久走など体温が上昇しやすい運動は避ける。10～20分おきに休憩をとり水分・塩分の補給を行う。暑さに弱い人は運動を軽減または中止。"
level3="警戒（積極的に休憩）: 熱中症の危険が増すので、積極的に休憩をとり適宜、水分・塩分を補給する。激しい運動では、30分おきくらいに休憩をとる。"
level2="注意（積極的に水分補給）: 熱中症による死亡事故が発生する可能性がある。熱中症の兆候に注意するとともに、運動の合間に積極的に水分・塩分を補給する。"
level1="ほぼ安全（適宜水分補給) : 通常は熱中症の危険は小さいが、適宜水分・塩分の補給は必要である。市民マラソンなどではこの条件でも熱中症が発生するので注意。"


def timer_nit():
    t=threading.Timer(60,timer_nit)
    dt_now_jst_aware = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    global t_time
    global time_data 
    global hour_data
    global hour__data
    time__data = testtime.intmin()
    hour_data=testtime.inttime()
    if t_time == dt_now_jst_aware.time().hour:
        t_time = t_time + 1
    time__data = testtime.intmin()
    if  time__data % 60 == 0 and time_data != time__data and hour_data >=7 and hour_data <=17:
        time_data = testtime.intmin()
        hour__data=testtime.inttime()
        time_p = timeint.readtime()
        WBGT1,WBGT2,WBGT3 = readCSV.readWBGTdata(1,time_p,path)
        coment1,coment2,coment3 = WBGTLevel(WBGT1,WBGT2,WBGT3)
        sendMessage(hour_data,WBGT1,coment1,"体育館")
        sendMessage(hour_data,WBGT2,coment2,"運動場[日向]")
        sendMessage(hour_data,WBGT3,coment3,"運動場[日陰]")
        
        
        

    t.start()
    
    


app = Flask(__name__)

#herokuへのデプロイが成功したかどうかを確認するためのコード
@app.route("/")
def main_page():
    return render_template("WBGT.html")
  
def sendMessage(time,wbgt,Ms,pl):
    if wbgt==999:
        message=Ms
    else:
       message=('%d時のWBGT(%s)の数値は%dです。\n%s'%(time,pl,wbgt,Ms))
    payload = {"text":message}
    response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
    )
    if response.status_code != 201:
     raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

def WBGTLevel(wbgt,wbgt2,wbgt3):
    if wbgt == 999 :
        message1 =errorMs
    elif wbgt >= 31 :
        message1=level5
    elif wbgt >= 28 and wbgt < 31 :
        message1=level4
    elif wbgt >= 25 and wbgt < 28 :
        message1=level3
    elif wbgt >= 21 and wbgt < 25 :
        message1=level2
    elif wbgt < 21 :
        message1=level1
    
    if wbgt2 == 999 :
        message2 =errorMs
    elif wbgt2 >= 31 :
        message2=level5
    elif wbgt2 >= 28 and wbgt2 < 31 :
        message2=level4
    elif wbgt2 >= 25 and wbgt2 < 28 :
        message2=level3
    elif wbgt2 >= 21 and wbgt2 < 25 :
        message2=level2
    elif wbgt2 < 21 :
        message2=level1
    
    if wbgt3 == 999 :
        message3 =errorMs
    if wbgt3 >= 31 :
        message3=level5
    elif wbgt3 >= 28 and wbgt3 < 31 :
        message3=level4
    elif wbgt3 >= 25 and wbgt3 < 28 :
        message3=level3
    elif wbgt3 >= 21 and wbgt3 < 25 :
        message3=level2
    elif wbgt3 < 21 :
        message3=level1

    return message1,message2,message3

        


   
# ポート番号の設定
if __name__ == "__main__":
    #定期タイマー実行部分
    t = threading.Thread(target=timer_nit)
    dt_now_jst_aware = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    t_time = dt_now_jst_aware.time().hour
    time_data = testtime.intmin()
    hour__data=testtime.inttime()
    t.start()
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
