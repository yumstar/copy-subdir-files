
import os
import datetime

# times_path = os.getcwd() + '\\times.txt'
for dir in ['example', 'output']:
    with open(dir + '_times.txt', 'w') as times_files:
        files = os.listdir("./" + dir)
        dir_ctime = os.path.getctime(os.getcwd() + "\\" + dir)
        dir_mtime = os.path.getmtime(os.getcwd() + "\\" + dir)
        print(datetime.datetime.fromtimestamp(dir_ctime))
        print(datetime.datetime.fromtimestamp(dir_mtime))
        for file in files:
            ctime = os.path.getctime(os.getcwd() + "\\" +  dir + "\\" + file)
            mtime = os.path.getmtime(os.getcwd() + "\\" +  dir + "\\" + file)
            creation_time = datetime.datetime.fromtimestamp(ctime)
            modified_time = datetime.datetime.fromtimestamp(mtime)
            file_time = (file, ctime, mtime)
            times_files.write(f"{file}, {creation_time}, {modified_time} \n")



