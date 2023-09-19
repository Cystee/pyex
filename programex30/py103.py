std = [['张三',90,87,95],['李四',83,80,87],['王五',73,57,55]]
modl = "亲爱的{}, 你的考试成绩是: 英语{}, 数学{}, Python语言{}, 总成绩{}.特此通知."
ttl=0
for i in range(len(std)):
    for t in range(1,4):
        ttl+=std[i][t]
    print(modl.format(std[i][0],std[i][1],std[i][2],std[i][3],ttl))
    ttl=0
