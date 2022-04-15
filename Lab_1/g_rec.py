def bin_to_dec(a):
    if a == 1 or a == 0:
        return a

    l = len(str(a))
    fi = a // pow(10, l - 1)

    return (pow(2, l - 1) * fi) + bin_to_dec(a % pow(10, l - 1))


bin = int(input())
dec = bin_to_dec(bin)

print(dec)