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


print(count_max_repeating_string("abcabcabcabc"))