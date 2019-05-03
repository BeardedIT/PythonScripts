#! Python 3.7.3
## Todo
## -------------------------------------------------------
## Error Handling
##

# Script requires filename to be in format
#(Show) - (Season#)x(Episode#) - (Episode Title)
# Built using python 3.7.3
import os, shutil, re
base_path = os.getcwd()
file_names = os.listdir(base_path)
increment=0
def ParseName(unsplit):
    try:
        print(unsplit)
        parsed_Name=unsplit.split(' - ')
        unsplit=unsplit.replace(' ','')
        season_and_episode=parsed_Name[1].split('x')
        season=season_and_episode[0]
        parsed_Name[1]='S'+season
        return parsed_Name
    except:
        print ('Sorry '+unsplit+' is not a valid file')
for files in file_names:
    if files.endswith(".mp4") or files.endswith(".m4v") or files.endswith('.mkv')or files.endswith('.avi'):
        match=re.search(r".+[ - ]\d+[x]\d+[ - ].+",files)
        if match:
            try:
                filename=ParseName(files)
                dest_dir= os.path.join(base_path,str(filename[0]),str(filename[1]))
                if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                shutil.move(base_path+os.sep+files,dest_dir)
                #print(base_path+os.sep+files + '-->' + dest_dir)
                increment+=1
            except:
                print('File move failed')
        else:
            print()
        print(increment,'Files were moved. Have a nice day')
