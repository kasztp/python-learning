# Check if a specific word is in the SCOWL-wl en_US word list
filename = 'words.txt'
db = open(filename, encoding='utf-8')
words = db.read().splitlines()


def findword(word):
    if word in words:
        print('{} found in word database!'.format(word))


keyword = 'apple'
findword(keyword)

db.close()
