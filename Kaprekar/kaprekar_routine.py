def k_finder(n, b):
    count = 0
    while n > 0:
        count = count + 1
        n = n // b
    return count


def getdigits(n, b, init_k):
    k = k_finder(n, b)
    digits = []
    while n > 0:
        digits.append(n % b)
        n = n // b
    for i in range(k, init_k):
        digits.append(0)
    return digits


def number_make(digits, b):
    result = 0
    for i in range(0, len(digits)):
        result = result * b + digits[i]
    return result


def ascdec(n, b, init_k):
    descending = number_make(sorted(getdigits(n, b, init_k), reverse=True), b)
    ascending = number_make(sorted(getdigits(n, b, init_k)), b)
    return descending - ascending


def solution(n, b):
    n = int(str(n), b)
    init_k = k_finder(n, b)
    n_list = []
    while n_list.count(n) < 2:
        n_list.append(n)
        n = ascdec(n, b, init_k)
    positions = [i for i, z in enumerate(n_list) if z == n]
    a = positions[0]
    b = positions[1]
    c = b - a
    return c

