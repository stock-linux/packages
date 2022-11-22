import os
index = open('INDEX.new','r')
packages = {}
for line in index.readlines(): 
    packages[line.split(' ')[0]] = line.split(' ')[1].strip()
print(packages)

count = 0
for file in os.listdir('bins'):
    arr = file.split('-')
    del arr[-1]
    pkgName = '-'.join(arr)
    if pkgName in packages:
        print('Package found !')
        del packages[pkgName]
        count += 1
    else:
        os.remove('bins/' + file)
print(count)
print(packages)
