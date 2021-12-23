import os
import shutil
import timeint
time_p = timeint.readtime()
f_path=timeint.time_folder_path()

def copy():
   for num in range(1, 4):
       num_p=str(num)
       try:
          shutil.copy("data/WBGT"+num_p+"/"+f_path+"/"+time_p+".csv","data/WBGT"+num_p+"/"+time_p+".csv")
       except OSError:
          print("ファイルが見つからないか、保存先がないためファイルをコピーできません")
       
def delete():
   for num in range(1, 4):
       num_p=str(num)
       try:
          os.remove("data/WBGT"+num_p+"/"+time_p+".csv")
       except OSError:
          print("ファイルが見つからないか、保存先がないためファイルをコピーできません")