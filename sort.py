## Todo
## -------------------------------------------------------
## Ensure that files that dont match are skipped
## Error Handling
##
import os, shutil
path = os.getcwd()
names = os.listdir(path)
increment=0
def ParseName(unsplit):
    try:
        split_Name=unsplit.split(' - ')
        unsplit=unsplit.replace(' ','')
        season_and_episode=split_Name[1].split('x')
        season=season_and_episode[0]
        split_Name[1]='S'+season
        return split_Name
    except:
        print ('Sorry'+unsplit+'is not a valid file')
for files in names:
    if files.endswith(".mp4") or files.endswith(".m4v") or files.endswith('.mkv')or files.endswith('.avi'):
        try:
            filename=ParseName(files)
            dest_dir= os.path.join(path,str(filename[0]),str(filename[1]))
            print (dest_dir)
            if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
            shutil.move(path+os.sep+files,dest_dir)
            print(path+os.sep+files + '-->' + dest_dir)
            increment=increment+1
        except:
            print('Sorry an error occurred')
print(increment,'Files were moved. Have a nice day')
