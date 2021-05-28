# -*- coding = utf-8 -*-
# @Time : 2021/4/12 23:46
# @Author : D-code
# @File : auto_tools.py
# @Software : PyCharm


# 替换函数，在使用CatE工具时我们希望他能使用到auto-phrase的结果，
# 所以将原文中的auto_phrase已经挖掘出来的短语词组用下划线连接来保证cate可以用
def auto_replace_words():
    # 新建两个列表用来存储：替换词汇（带下划线的）、被替换词汇
    replace_text = []
    replaced_text = []

    # 把替换词汇从txt文件拿到后转成iterable
    with open("replace_text.txt", "r", encoding='utf-8') as infile2:  # 打开文件
        for line in infile2:
            replace_text.append(line)
        for i in range(len(replace_text)):
            replace_text[i] = replace_text[i].replace('\n', '')
        # 使用sorted进行排序，避免先替换较短的短语导致长短语无法匹配，从而无法替换
        replace_text = sorted(replace_text, key=lambda x: len(x), reverse=True)
        # print(replace_text)

    # 把待替换词汇从txt文件拿到后转成iterable列表
    with open("replaced_text.txt", "r", encoding='utf-8') as infile3:
        for line in infile3:
            replaced_text.append(line)
        for i in range(len(replace_text)):
            replaced_text[i] = replaced_text[i].replace('\n', '')
        replaced_text = sorted(replaced_text, key=lambda x: len(x), reverse=True)
        # print(len(replaced_text))

    # 打开corpus，开始进行替换
    with open("Corpus.txt", 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换是主要耗时
    print('==========replacing==========')
    for i in range(len(replace_text)):
        content = content.replace(replaced_text[i], replace_text[i])
        print('replacing...')  # 用来显示程序运行状态

    # 完成替换后生成新文本，存入新文件
    f2 = open("replace_result.txt", 'w', encoding='utf-8')
    f2.write(content)

    print('文本已经保存!')


if __name__ == '__main__':
    auto_replace_words()
