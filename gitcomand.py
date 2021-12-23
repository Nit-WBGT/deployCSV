import os
from datetime import datetime
def git():
   # Commit comment
   now = datetime.now()
   comment = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")

   # Push
   os.system('git add data')
   os.system('git commit -m {}'.format(comment))
   os.system('git push origin master')