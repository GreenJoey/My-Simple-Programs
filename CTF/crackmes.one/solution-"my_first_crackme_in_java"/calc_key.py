from string import ascii_lowercase, ascii_uppercase


def calc_values_from_name(name, n1=ord('a'), n2=ord('n'), n3=ord('d')):
    print("Calculated values for the give name " + name)
    name_sum = 0
    for i in name:
        if i in ascii_lowercase+ascii_uppercase:
            name_sum += ord(i)

    name_sum <<= 2
    c2 = name_sum & 255
    c3 = c2 ^ name_sum
    c4 = c3 | name_sum

    d = (((((c2 * 2) + (c3 * 3)) + (c4 * 4)) + (n1 * 10)) + (n2 * 11)) + (n3 * 12)

    print(f"name_sum = {name_sum}\nc2       = {c2}\nc3       = {c3}")
    print(f"c4       = {c4}\nd        = {d}")

    return d


def calc_key(y, y1):
    a = [[2, 2, y], [4, 6, 2], [3, 4, 4]]
    b = [[2, 2, 3], [8, 9, 5], [6, 2, 2]]
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            c[i][j] = 0
            for k in range(3):
                c[i][j] = c[i][j] + (a[i][k] * b[k][j])

    print("Key for the given values is: ", y1 * c[2][2])


if __name__ == '__main__':
    y1 = calc_values_from_name("Ritam")
    y = int(str(y1)[:3])

    calc_key(y, y1)
