def count_max_repeating_string(s):
    temp = ''
    for character in s:
        temp += character
        divider = float(len(s)) / len(temp)
        if divider.is_integer():
            temp2 = temp * int(divider)
            if s == temp2:
                result = int(divider)
                return result

# print(count_max_repeating_string("abcabcabcabc"))


def distribute_coins(num):
    def fibonacci(n, cache={0: 0, 1: 1}):
        if n not in cache:
            cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
        return cache[n]

    def smallest(amount):
        henchman = 0
        while True:
            if (amount - 2 ** henchman) >= 0:
                amount = amount - 2 ** henchman
                henchman += 1
            else:
                return henchman + 1

    def largest(amount):
        henchmen = 0
        for i, henchman in enumerate(range(100)):
            distribution = fibonacci(henchman)
            if (amount - distribution) >= 0:
                amount = amount - distribution
                henchmen += 1
            else:
                return henchmen

    return largest(num) - smallest(num)

# print(distribute_coins(10))
# print(distribute_coins(143))


def count_salutes(s):
    left = 0
    right = 0
    for index, item in enumerate(s):
        if (item == '<') & (right != 0):
            left += s.count('>', 0, index)
        elif item == '>':
            right += s.count('<', index + 1)
    salutes = left + right
    return salutes

# print(count_salutes("--->-><-><-->-"))
# print(count_salutes(">----<"))
# print(count_salutes("<<>><"))


def bombs(mach, facula):
    mach = int(mach)
    facula = int(facula)
    iterations = 0
    while min(mach, facula) != 1:
        if max(mach, facula) % min(mach, facula) == 0:
            return "impossible"

        iterations += max(mach, facula) // min(mach, facula)
        (mach, facula) = (max(mach, facula) % min(mach, facula), min(mach, facula))
    return str(iterations + max(mach, facula) - 1)

# print(bombs("2", "1"))
# print(bombs("4", "7"))


def codes(l):
    triplet = []
    for i, first in enumerate(l):
        for j in range(1, len(l)):
            if j in l[i + 1:]:
                second = first * j
                if second in l[i + 1:]:
                    for k in range(1, len(l)):
                        if k in l[i + 1:]:
                            third = second * k
                            if third in l[i + 2:]:
                                triplet.append((first, second, third))
    return len(triplet)


def answer(l):
    def multiples(l, i):
        current_divider = l[i]
        return [item for item in l[i + 1:] if item % current_divider == 0]

    def dividers(l, i):
        current_dividend = l[i]
        return [item for item in l[:i] if current_dividend % item == 0]

    size = len(l)
    result = 0
    while size >= 2:
        size -= 1
        result += len(dividers(l, size)) * len(multiples(l, size))

    return result


# print(codes([1, 2, 3, 4, 5, 6]))
# print(answer([1, 2, 3, 4, 5, 6]))
# print(codes([1, 1, 1]))
# print(codes(range(1, 2000)))
# print(answer(range(1, 2000)))


def pellets(s):
    num = int(s)
    steps = 0
    if num == 1:
        return steps
    else:
        if num == 0:
            return 1
        else:
            while num != 1:
                if num % 2 == 0:
                    num /= 2
                elif num == 3 or num % 4 == 1:
                    num -= 1
                else:
                    num += 1
                steps += 1
    return steps


# print(pellets("4"))
# print(pellets("15"))
# print(pellets("59"))


def shots(dimensions, your_position, trainer_position, distance):
    import math

    def mirror_map(node, dimensions, distance):
        node_mirrored = []
        for i in range(len(node)):
            points = []
            for j in range(-(distance // dimensions[i]) - 1, (distance // dimensions[i] + 2)):
                points.append(get_mirror(j, node[i], dimensions[i]))
            node_mirrored.append(points)
        return node_mirrored

    def get_mirror(mirror, coordinates, dimensions):
        result = coordinates
        mirror_rotation = [2 * coordinates, 2 * (dimensions - coordinates)]
        if mirror < 0:
            for i in range(mirror, 0):
                result -= mirror_rotation[(i + 1) % 2]
        else:
            for i in range(mirror, 0, -1):
                result += mirror_rotation[i % 2]
        return result

    mirrored = [mirror_map(your_position, dimensions, distance),
                mirror_map(trainer_position, dimensions, distance)]

    valid_paths = set()
    angles_dist = {}

    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam = math.atan2((your_position[1] - k), (your_position[0] - j))
                l = math.sqrt((your_position[0] - j) ** 2 + (your_position[1] - k) ** 2)
                if [j, k] != your_position and distance >= l:
                    if (beam in angles_dist and angles_dist[beam] > l) or beam not in angles_dist:
                        if i == 0:
                            angles_dist[beam] = l
                        else:
                            angles_dist[beam] = l
                            valid_paths.add(beam)
    return len(valid_paths)


# print(shots([3, 2], [1, 1], [2, 1], 4))
# print(shots([300, 275], [150, 150], [185, 100], 500))
