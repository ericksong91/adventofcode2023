raw_input = open('data.txt', 'r').read().split('\n')

def alg_parse(str):
    i = 0
    h = len(str) - 1
    num_list = []

    while i < len(str):
        if str[i].isdigit():
            num_list.append(str[i])
            break
        else:
            i += 1

    while h >= i:
        if str[h].isdigit():
            num_list.append(str[h])
            break
        # elif str[h].isdigit() and h == i:
        #     num_list.append(str[h])
        #     break
        else:
            h -= 1

    # print(''.join(num_list))

    return int(''.join(num_list))

def parse_list(list):
    i = 0
    full_list = []

    while i < len(list):
        full_list.append(alg_parse(list[i]))
        i += 1

    print(sum(full_list))

    return sum(full_list)


# parse_list(raw_input)

# list = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

parse_list(raw_input)