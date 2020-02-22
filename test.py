def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0): # here creates binary
        d[l] = n % 2
        n //= 2
        l += 1

    print(d)
    for p in range(1, (l//2) + 1):
        ok = True
        for i in range(l - p):
            print('p')
            print(p)
            print(d[(l-1) - i])
            print(d[(l-1) - i - p])
            print('-----------')
            if d[(l-1) - i] != d[(l-1) - i - p]:
                ok = False
                break
        if ok:
            return p


    return -1

if __name__ == '__main__':
    n = 954
    print(solution(n))

    print('-------')

    a = '{0:08b}'.format(954)
    print('{0:08b}'.format(954))
    print(len(a))