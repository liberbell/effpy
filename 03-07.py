import zipfile

zip = zipfile.ZipFile('Archive.zip', 'r')
print(zip.namelist())

for meta in zip.infolist():
    print(meta)

info = zip.getinfo('purchased.txt')
print(info)
