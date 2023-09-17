import jieba
s=input("输入文本：")
print("中文字符数为{0}，中文词语数为{1}。".format(len(s),len(jieba.lcut(s))))