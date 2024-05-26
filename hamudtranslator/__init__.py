import random

import jieba
import jieba.posseg as pseg
jieba.setLogLevel(20)


def chs2ham(s, abstract=0.1):
    words = list(pseg.cut(s))
    print(words)
    ham = []
    flags = []
    for word, flag in words:
        ham.append(word)
        flags.append(flag)
    for i in ham:
        if random.choices([0,1], [1-abstract, abstract])[0]:
            if flags[ham.index(i)] == 'n':
                ham[ham.index(i)] = random.choice(['萨米', '好汉', '欧内的手', '冰', '安修·奥克苏恩', '电棍', '炫狗', '山泥若', '若子', '杠精'])
            elif flags[ham.index(i)] == 'v':
                ham[ham.index(i)] = random.choice(['说的道理', '诶乌兹', ' all in ', '卧槽', '溜冰', '抬杠', '打野', '走位'])
            elif flags[ham.index(i)] == 'a':
                ham[ham.index(i)] = random.choice(['欧西给', '哈比下', '阿黑路西', '溜大', 'CJB'])
            elif flags[ham.index(i)] == 'd':
                ham[ham.index(i)] = random.choice(['哈姆', '欧西给'])
    return ''.join(ham)

if __name__ == '__main__':
    print(chs2ham(input("请输入将要翻译的句子 > "), 0.25))
    input("按任意键退出。")
