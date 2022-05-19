
import os
import os.path
import datetime
import shutil

# times_path = os.getcwd() + '\\times.txt'
file_systems = {}
cwd = os.getcwd()
for dir in ['example', 'output']:
    with open(dir + '_times.txt', 'w') as times_files:
        file_systems[dir] = {}
        files = os.listdir("./" + dir)
        dir_ctime = os.path.getctime(os.getcwd() + "\\" + dir)
        dir_mtime = os.path.getmtime(os.getcwd() + "\\" + dir)
        # print(datetime.datetime.fromtimestamp(dir_ctime))
        # print(datetime.datetime.fromtimestamp(dir_mtime))
        for file in files:
            creation_time = os.path.getctime(os.getcwd() + "\\" +  dir + "\\" + file)
            modified_time = os.path.getmtime(os.getcwd() + "\\" +  dir + "\\" + file)
            ctime = datetime.datetime.fromtimestamp(creation_time)
            mtime = datetime.datetime.fromtimestamp(modified_time)
            file_time = (file, ctime, mtime)
            file_systems[dir][file] = {"ctime": f"{ctime}", "mtime": f"{mtime}"}
            # file_systems[dir].add({f{"{file}": {"ctime": ctime, "mtime": mtime}})
            times_files.write(f"{file}, {creation_time}, {modified_time} \n")

        print(file_systems)
# tests start
## addfilesiffilesindictbutnotinfolder
### file_systems['output'] = file_systems['example']

# tests end
files = os.listdir("./example")
for file in files:
    for dir in ['output']:
        file_ctime = os.path.getctime(cwd + "\\" +  dir + "\\" + file)
        file_mtime = os.path.getmtime(cwd + "\\" +  dir + "\\" + file)
        ctime = datetime.datetime.fromtimestamp(file_ctime)
        mtime = datetime.datetime.fromtimestamp(file_mtime)
        if (file not in file_systems[dir] or
           not os.path.exists(cwd + "\\" + dir + "\\" + file) or
           (file_systems['example'][file]["ctime"] > file_systems[dir][file]["ctime"] and
            file_systems['example'][file]["ctime"] > file_systems[dir][file]["mtime"]) or
           (file_systems['example'][file]["mtime"] > file_systems[dir][file]["ctime"] and
            file_systems['example'][file]["mtime"] > file_systems[dir][file]["mtime"])
           ):
                shutil.copy(os.getcwd() + "\\example\\" + file, os.getcwd() + "\\" +  dir + "\\" + file)
                file_systems[dir][file] = {"ctime": f"{ctime}", "mtime": f"{mtime}"}
print(file_systems)