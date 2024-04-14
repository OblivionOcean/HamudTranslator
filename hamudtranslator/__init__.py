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
                ham[ham.index(i)] = random.choice(['么么哒米诺', '诶乌兹', ' all in ', '卧槽', '溜冰', '抬杠', '打野', '走位'])
            elif flags[ham.index(i)] == 'a':
                ham[ham.index(i)] = random.choice(['欧西给', '哈比下', '阿黑路西', '溜大', 'CJB'])
            elif flags[ham.index(i)] == 'd':
                ham[ham.index(i)] = random.choice(['哈姆', '欧西给'])
    return ''.join(ham)

test = '''这是一个测试句子，用来测试chs2ham函数的效果。这个函数的作用是将中文文本转换为哈姆语言，即将文本中的名词、动词、形容词、副词替换为哈姆语言中的对应词汇。哈姆语言是一种由易拉罐创造的语言，用于表达牛魔之间的情感和交流。通过这个函数，我们可以将普通的中文文本转换为哈姆语言，增加文本的趣味性和可读性。在实际应用中，我们可以将这个函数应用到社交媒体、聊天软件等场景中，让用户在交流中更加愉快和有趣。'''
test2 = '''务必要结婚，娶个好女人，你会很快乐，娶个坏女人，你会成为哲学家。'''
if __name__ == '__main__':
    print(chs2ham(test2,0.2))
