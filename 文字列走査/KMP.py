def kmp(text, pattern):
    n = len(text)
    m = len(pattern)

    # prepare shift
    shift = [0] * m
    shift[0] = 1
    k = 0
    for j in range(1, m):
        if pattern[j] == pattern[k]:
            k += 1
            shift[j] = k + 1
        else:
            k = 0
            shift[j] = k + 1
    print(shift)
    
    # find pattern
    i = j = 0
    while i < n:
        while j < m and text[i+j] == pattern[j]:
            j += 1
        if j == m:
            return i
        print(shift[j])
        i = i + shift[j]
        j = max(j - shift[j], 0)
        print(i, j)
    return -1


def main():
    T = "ababbaabaca"
    P = "abac"
    print(kmp(T, P))


if __name__ == "__main__":
    main()