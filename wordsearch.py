filename = 'words.txt'
db = open(filename, encoding='utf-8')
words = db.read().splitlines()
keyword = 'apple'


def findword(word):
    if word in words:
        print('{} found in word database!'.format(word))


findword(keyword)

db.close()
