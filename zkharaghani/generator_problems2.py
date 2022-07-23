
# Range to generate: range(c, x, 2)
def alphabet(start, stop, step):
    for i in range(ord(start), ord(stop), step):
        yield chr(i).upper()


if __name__ == '__main__':
    for ch in alphabet('c', 'x', 2):
        print(ch)
