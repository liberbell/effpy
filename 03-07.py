import zipfile

zip = zipfile.ZipFile('Archive.zip', 'r')
print(zip.namelist())
