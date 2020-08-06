import colorama
import random
import sys

def bannerTop():
    banner = '''
 _____    _         __  __       _ _    ____
| ____|__| |_   _  |  \/  | __ _(_) |  / ___| ___ _ __
|  _| / _` | | | | | |\/| |/ _` | | | | |  _ / _ \ '_ \\
| |__| (_| | |_| | | |  | | (_| | | | | |_| |  __/ | | |_
|_____\__,_|\__,_| |_|  |_|\__,_|_|_|  \____|\___|_| |_(_)
      Github Repo - https://git.io/JJisT/\n\n
'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]

    return ''.join(colored_chars)