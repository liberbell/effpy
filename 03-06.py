import tempfile

tempFile = tempfile.TemporaryFile()

tempFile.write(b'Save this special number for me: 5678309')
tempFile.seek(0)

print(tempFile.read)
