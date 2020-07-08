example = [5, 1, 8, 9, 7, 2, 3, 6, 4]

a = 0
b = len(example) - 1


def quickSort(number, head, tail):
    if (head < tail):
        base = division(number, head, tail)
        # print(number[base],"\n")
        quickSort(number, head, base - 1)
        quickSort(number, base + 1, tail)
    else:
        print(number)


def division(number, head, tail):
    base = number[head]
    while (head < tail):
        while (head < tail and number[tail] >= base):
            tail -= 1
        number[head] = number[tail]
        while (head < tail and number[head] <= base):
            head += 1
        number[tail] = number[head]
    number[head] = base
    return head


if __name__ == '__main__':
    quickSort(example, a, b)