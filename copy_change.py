
import sys
import os
import os.path
import datetime
import shutil
import filecmp

assert(len(sys.argv) > 2), "Insufficient number of input arguments"
for i in range(1, len(sys.argv)):
    assert(os.path.exists(os.getcwd() + "\\" + sys.argv[i])), f"Invalid input argument {i}"

subdirs = {}
cwd = os.getcwd()

for dir in sys.argv[1:]:
        subdirs[dir] = {}
        files = os.listdir("./" + dir)
        dir_ctime = os.path.getctime(cwd + "\\" + dir)
        dir_mtime = os.path.getmtime(cwd + "\\" + dir)
        for file in files:
            creation_time = os.path.getctime(cwd + "\\" +  dir + "\\" + file)
            modified_time = os.path.getmtime(cwd + "\\" +  dir + "\\" + file)
            ctime = datetime.datetime.fromtimestamp(creation_time)
            mtime = datetime.datetime.fromtimestamp(modified_time)
            subdirs[dir][file] = {"ctime": f"{ctime}", "mtime": f"{mtime}"}

files = os.listdir("./" + sys.argv[1])
for file in files:
    for dir in sys.argv[2:]:
        if (file not in subdirs[dir] or
           not os.path.exists(cwd + "\\" + dir + "\\" + file) or
           not filecmp.cmp(cwd + "\\example\\" + file, cwd + "\\" +  dir + "\\" + file)
           ):
                shutil.copy(cwd + "\\example\\" + file, cwd + "\\" +  dir + "\\" + file)