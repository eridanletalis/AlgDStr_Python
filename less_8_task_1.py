def rabin_karp_set(_string):
    subs = set()
    for i in range(0, len(_string) - 1):
        for j in range(1, len(_string) + 1):
            a = _string[j - 1:j + i]
            subs.add(hash(_string[j - 1:j + i]))
    return len(subs)


print(rabin_karp_set("Hello, world! Hello! Hi! Beautiful Worlds of Py"))
