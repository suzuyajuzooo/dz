s = input().strip().lower()
s = s.replace('ё', 'е') 
if not s:
    print(0)
else:
    max_count = 0
    for i in range(len(s)):
        char = s[i]
        seen_before = False
        for j in range(i):
            if s[j] == char:
                seen_before = True
                break
        if not seen_before:
            count = 0
            for c in s:
                if c == char:
                    count += 1
            if count > max_count:
                max_count = count
    print(max_count)