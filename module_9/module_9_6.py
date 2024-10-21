def all_variants(text):
    x = 1
    while x < len(text) + 1:
        for start in range(len(text)):
            if start + x > len(text):
                continue
            yield text[start:start + x]
        x += 1


a = all_variants("abc")
for i in a:
    print(i)
