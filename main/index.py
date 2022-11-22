#!/usr/bin/python3
import os
index = open('INDEX','a')
for file in os.listdir('.'):
    if not os.path.isdir(file):
        if not file.endswith('.py') and not file.endswith('.tmp'):
            reader = open(file, 'r')
            pkgName = ''
            pkgVersion = ''
            for line in reader.readlines():
                if line.startswith('name'):
                    print(line)
                    pkgName = line.split(': ')[1].strip()
                if line.startswith('version'):
                    pkgVersion = line.split(': ')[1].strip()

            reader.close()
            index.write(pkgName + ' ' + pkgVersion + '\n')
