number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# 3 numbers with 3 letters
# 3 numbers with 4 letters
# 3 numbers with 5 letters
# do a get with number_dict.get("string being found", None)
# every time it returns None, keep going until string length is 5, then move onto next five

# For algo, check first three characters on either end. If it encounters ANY numbers, it just returns
# the number and exits out. If it doesnt see anything in the first three that matches one two, etc and 3 
# letters of the other numbers, it just keeps going

# concatenate the string to check

# analyze left to right

# raw_input = open('data.txt', 'r').read().split('\n')

def alg_parse(str):
    i = 0
    num_list = []
    
    while i < len(str):
        if str[i].isdigit():
            num_list.append(str[i])
            break
        elif i + 2 < len(str) and number_dict.get(f"{str[i]}" + f"{str[i + 1]}" + f"{str[i + 2]}"):
            num_list.append(number_dict.get(f"{str[i]}" + f"{str[i + 1]}" + f"{str[i + 2]}"))
            break
        elif i + 3 < len(str) and number_dict.get(f"{str[i]}" + f"{str[i + 1]}" + f"{str[i + 2]}" + f"{str[i + 3]}"):
            num_list.append(number_dict.get(f"{str[i]}" + f"{str[i + 1]}" + f"{str[i + 2]}" + f"{str[i + 3]}"))
            break
        elif i + 4 < len(str) and number_dict.get(f"{str[i]}" + f"{str[i + 1]}" + f"{str[i+2]}" + f"{str[i+3]}" + f"{str[i+4]}"):
            num_list.append(number_dict.get(f"{str[i]}" + f"{str[i + 1]}" + f"{str[i+2]}" + f"{str[i+3]}" + f"{str[i+4]}"))
            break
        else:
            i += 1
    
    h = len(str) - 1 if len(str) - 1 > 0 else i

    while h >= i:
        if str[h].isdigit():
            num_list.append(str[h])
            break
        elif h - 2 > 0 and number_dict.get(f"{str[h - 2]}" + f"{str[h - 1]}" + f"{str[h]}"):
            num_list.append(number_dict.get(f"{str[h - 2]}" + f"{str[h - 1]}" + f"{str[h]}"))
            break
        elif h - 3 > 0 and number_dict.get(f"{str[h - 3]}" + f"{str[h - 2]}" + f"{str[h - 1]}" + f"{str[h]}"):
            num_list.append(number_dict.get(f"{str[h - 3]}" + f"{str[h - 2]}" + f"{str[h - 1]}" + f"{str[h]}"))
            break
        elif h - 4 > 0 and number_dict.get(f"{str[h - 4]}" + f"{str[h - 3]}" + f"{str[h - 2]}" + f"{str[h - 1]}" + f"{str[h]}"):
            num_list.append(number_dict.get(f"{str[h - 4]}" + f"{str[h - 3]}" + f"{str[h - 2]}" + f"{str[h - 1]}" + f"{str[h]}"))
            break
        else:
            h -= 1

    return int(''.join(num_list))

def parse_list(list):
    i = 0
    full_list = []

    while i < len(list):
        full_list.append(alg_parse(list[i]))
        i += 1

    return sum(full_list)

# parse_list(raw_input)

# str = "fourfourthreehnbhkmscqxdfksg64bvpppznkh"

# alg_parse(str)