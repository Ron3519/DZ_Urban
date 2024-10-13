def all_variants(text):
    col_sim = 0
    while True:
        col_sim += 1
        for i in range(len(text)):
            if i + col_sim > len(text):
                continue
            else:
                yield text[i:i + col_sim]
        if col_sim > len(text):
                break



a = all_variants("abc")
for i in a:
    print(i)