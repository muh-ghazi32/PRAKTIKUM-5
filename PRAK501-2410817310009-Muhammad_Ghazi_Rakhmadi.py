def max_bilangan(a, b, c, d):
    return max(a, b, c, d)

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    hasil = max_bilangan(a, b, c, d)
    print(hasil)