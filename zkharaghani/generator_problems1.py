# Range to generate: range(2.3, 3.78, 0.01)
def frange(start, stop=None, step=None):
    count = 0
    start = float(start)
    while True:
        temp = float(start + count)
        if 0 < stop <= temp:
            break
        elif temp <= stop < 0:
            break
        temp = '{:.2f}'.format(temp)
        yield temp
        count += step


if __name__ == '__main__':
    for number in frange(2.3, 3.78, 0.01):
        print(number)


