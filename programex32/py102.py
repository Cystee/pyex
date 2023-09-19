s = input("请输入中文和字母的组合: ")
count = 0
for c in s:
    if "\u4e00" <= c <= "\u9fff":
        count += 1
print(count)

# \u4e00 \u9fff
