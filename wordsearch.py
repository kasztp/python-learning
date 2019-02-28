filename = 'words.txt'
db = open(filename, encoding='utf-8')
words = db.read().splitlines()


def findword(word):
    if word in words:
        print('{} found in word database!'.format(word))


keyword = 'apple'
findword(keyword)

db.close()
