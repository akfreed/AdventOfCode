import hashlib


def getInput():
    with open('day4.txt', 'r') as file:
        return file.readline().strip()


def has_n_leading_zeros(hex_string: str, n: int):
    if len(hex_string) < n:
        print(len(hex_string))
        assert False
    for i in range(n):
        if hex_string[i] != '0':
            return False
    return True


def day4a(n: int):
    secret = getInput()
    i = 1
    while True:
        if i % 10000 == 0:
            print(i)
        to_hash = "{}{}".format(secret, i)
        hex_string = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
        if has_n_leading_zeros(hex_string, n):
            print("{} : {}".format(to_hash, hex_string))
            print(i)
            break
        i += 1


def day4b():
    day4a(6)


if __name__ == '__main__':
    #day4a(5)
    day4b()
