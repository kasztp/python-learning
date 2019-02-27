filename = 'words.txt'
db = open(filename, encoding='utf-8')
words = db.read().splitlines()
if "apple" in words:
    print("Apple found in word database!")
db.close()

