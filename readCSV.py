import csv
import datetime as dt
import timeint

#WBGTのcsvデータを読み込み、そのcsvファイルの最後の計測データ(一行 , リスト型)を返します
#引数 : wbgtNum(整数型) ... WBGT1のフォルダのデータを読み込みたい場合は「1」を入力する。 2,3,4も同様 例 1
#       date(【注意】文字列型) ... 読み込むcsvの日付を指定します。例 "2021-05-06"
#       path(文字列型) ... WBGT1 ~ 5のフォルダがあるディレクトリまで行けるように入力してください(例 "test/WBGTdata")
#           　　　　　WBGT1 ~ 5があるディレクトリにコードがある場合は、空白を入力(例 "")
#
#入力例 : WBGT計測器 ナンバー1の、2021年5月6日のデータを読み込みたい。
#         そして、実行ファイルがWBGTフォルダと同じ場所におかれている場合
#         readWBGTdata(1,"2021-05-06","")

def readWBGTdata(wbgtNum,date,path):
    time_p = timeint.readtime()
    f_path=timeint.time_folder_path()
    #引数のエラー処理
    if isinstance(wbgtNum,int) == False:
        print("[readWBGTdata]wbgtNumがint型ではありません。int型で入力してください。")
        return -1;
    elif isinstance(date,str) == False:
        print("[readWBGTdata]dateがstr型ではありません。str型で入力してください。")
        return -1;
    elif isinstance(path,str) == False:
        print("[readWBGTdata]pathがstr型ではありません。str型で入力してください。")
        return -1;

    #csvから最新データを読み込み
    #ファイルを開いてリスト形式で読み込み
    for counter in range(1,4):
       num=str(counter)
       try:
          csv_file = open(path + "WBGT" + num + "/"  + date + ".csv", "r", encoding="ms932", errors="", newline="" )
          
       except OSError as e:
          if counter == 1:
             data=999
          if counter == 2:
             data2=999
          if counter == 3:
             data3=999
       else:
          f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
       #csvを最後まで読み込み、最後のデータのみを抽出する
          if counter == 1:
             for row in f:
                 data = row
             data=int(data[4])

          if counter == 2:
             for row in f:
                 data2 = row
             data2=int(data2[4])

          if counter == 3:
             for row in f:
                 data3 = row
             data3=int(data3[4])
          csv_file.close()
            
    
    

    #データを返す
    return data,data2,data3

################
