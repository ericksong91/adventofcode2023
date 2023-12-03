import re

# Max # of cubes is 12 red cubes, 13 green cubes, and 14 blue cubes
# How do I parse the input? 
# How do I keep track of total # of cubes per game?
# I should just use hardcut offs for variables

red_max = 12
green_max = 13
blue_max = 14

find_red = re.compile(r'\d+\s*red?')
find_green = re.compile(r'\d+\s*green?')
find_blue = re.compile(r'\d+\s*blue?')

# Lets parse each line, lets also check the inputs

raw_input = open('../data.txt', 'r').read().split('\n')

# I should grab each line, separate it by game
# After separating it, use RegEx to grab the numbers 

def alg_parse(str):
    green = ' '.join(find_green.findall(str))
    red = ' '.join(find_red.findall(str))
    blue = ' '.join(find_blue.findall(str))

    red = [int(s) for s in re.findall(r'\b\d+\b', red)]
    green = [int(s) for s in re.findall(r'\b\d+\b', green)]
    blue = [int(s) for s in re.findall(r'\b\d+\b', blue)]

    # print(next((x for x in red if int(x) > red_max), None))
    # print(next((x for x in green if int(x) > green_max), None))
    # print(next((x for x in blue if int(x) > blue_max), None))

    if next((x for x in red if int(x) > red_max), None) or next((x for x in green if int(x) > green_max), None) or next((x for x in blue if int(x) > blue_max), None):
        return False
    else:
        return True


def parse_list(data):
    i = 0
    list = []

    while i < len(data):
        result = alg_parse(data[i])

        if result == True:
            list.append(i + 1)
            i += 1
        else:
            i += 1
    
    print("Only games:", sum(list))

    return list


# str = "Game 100: 1 blue, 6 red; 1 green, 2 red; 1 blue, 8 green, 1 red; 1 red, 7 blue"

# alg_parse(str)
parse_list(raw_input)