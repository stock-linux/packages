import os
index = open('INDEX.new','w')
for file in os.listdir('.'): 
    if file != "INDEX" and file != "INDEX.new" and file != 'bins' and file != "index.py":
        pkgName = ""
        pkgVersion = ""
        for line in open(file, 'r').readlines():
            if line.startswith('name'):
                pkgName = line.split(': ')[1].strip()
                continue
            if line.startswith('version'):
                pkgVersion = line.split(': ')[1].strip()
                continue
        index.write(pkgName + ' ' + pkgVersion + '\n')
