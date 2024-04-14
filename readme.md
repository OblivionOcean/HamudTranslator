# hamudtranslator

能把中文翻译成古神语的翻译机！

<sub>(鸣谢伟大的 <a href="https://github.com/RimoChan/yinglish">RimoChan 的淫语翻译机</a> )</sub>


## 样例

```python
import hamudtranslator

s = '你已经站在宏观的角度进行哲学思考了。'
print(hamudtranslator.chs2ham(s))
# 你哈姆站在冰的角度进行哲学思考了。

s2 = '务必要结婚，娶个好女人，你会很快乐，娶个坏女人，你会成为哲学家。'
print(hamudtranslator.chs2ham(s2))
# 务必要结婚，走位个好电棍，你会很快乐，么么哒米诺个坏女人，你会成为哲学家。
```


## 接口说明

```python
def chs2ham(s, abstract=0.2):
```

s 是原字符串，abstract 是 0~1 之间的实数，越大越抽象，表示古神语出现的概率。


## 安装

```bash 
pip install hamudtranslator
```


