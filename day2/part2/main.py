import re

# Find the fewest numbers of cubes for each color
# for each game, find the power of the min amount of games (R * G * B)
# Add all the powers together

# I need to regather the arrays that I already made
# lets find the max number in that array

red_max = 12
green_max = 13
blue_max = 14

find_red = re.compile(r'\d+\s*red?')
find_green = re.compile(r'\d+\s*green?')
find_blue = re.compile(r'\d+\s*blue?')

raw_input = open('../data.txt', 'r').read().split('\n')

def alg_parse(str):
    green = ' '.join(find_green.findall(str))
    red = ' '.join(find_red.findall(str))
    blue = ' '.join(find_blue.findall(str))

    red = [int(s) for s in re.findall(r'\b\d+\b', red)]
    green = [int(s) for s in re.findall(r'\b\d+\b', green)]
    blue = [int(s) for s in re.findall(r'\b\d+\b', blue)]

    print(max(red) * max(green) * max(blue))

    return max(red) * max(green) * max(blue)


def parse_list(data):
    i = 0
    list = []

    while i < len(data):
        power = alg_parse(data[i])

        list.append(power)
        i += 1
    
    print("Power Sum:", sum(list))

    return list

str = "Game 100: 15 blue, 6 red; 1 green, 2 red; 12 blue, 8 green, 1 red; 1 red, 7 blue"

alg_parse(str)
# parse_list(raw_input)