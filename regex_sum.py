import re

print(sum([int(number) for number in re.findall('[0-9]+', open('regex_sum_392593.txt').read())]))
