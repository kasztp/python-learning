# Check if a specific word is in the SCOWL-wl en_US word list
import random
import itertools

filename = 'words.txt'
db = open(filename, encoding='utf-8')
words = db.read().splitlines()


def find_word(word):
    if word in words:
        print('{} found in word database!'.format(word))
    # else:
    #     print('{} NOT found in word database!'.format(word))


# Build language specific tile set - without the 2 blanks
def build_tileset(lang):
    if lang == 'EN':
        tile_set = ['a']*9 + ['b']*2 + ['c']*2 + ['d']*4 + ['e']*12 + ['f']*2 + ['g']*3 + ['h']*2 + ['i']*9 + ['j'] +\
                   ['k'] + ['l']*4 + ['m']*2 + ['n']*6 + ['o']*8 + ['p']*2 + ['q'] + ['r']*6 + ['s']*4 + ['t']*6 +\
                   ['u']*4 + ['v']*2 + ['w']*2 + ['x'] + ['y']*2 + ['z']
    if len(tile_set) == 98:
        print('Tile set generated OK!')
        return tile_set
    else:
        print('ERROR: Tile set generation error with length: {}'.format(len(tile_set)))
        return len(tile_set)


# Draw n number of random tiles from the tile set
def draw(tileset, n):
    if n >= 1:
        own_tiles = random.sample(tileset,k=n)
        print('Tiles drawn: {}'.format(own_tiles))
        return own_tiles
    else:
        print('ERROR: Tile number less than 1!')


# Generate possible words (tile permutations)
def word_gen(owntiles, l):
    if l >= 1:
        permutations = list(itertools.permutations(owntiles, r=l))
        textperm = []
        for element in permutations:
            textperm += [''.join(element)]
        print('Possible words generated: {}'.format(len(textperm)))
        return textperm
    else:
        print('ERROR: Word length parameter less than 1!')


keyword = 'apple'
language = 'EN'

tiles = build_tileset('EN')
# print(tiles)
# tile_draw = draw(tiles, 7)
tile_draw = ['a', 'p', 'p', 'l', 'e', 'y', 's']
word_candidates = word_gen(tile_draw, 5)
for keyword in word_candidates:
    find_word(keyword)
db.close()
