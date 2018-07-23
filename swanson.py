import random

from quotes import quotes

def get_random_quote():
    return random.choice(quotes)

if __name__ == '__main__':
    random_quote = get_random_quote()

    print(random_quote)
