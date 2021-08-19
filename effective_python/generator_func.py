'''
考虑用生成器来改写直接返回列表的函数
'''
def index_words(txt):
    '''
    查找字符串中的每个首字母
    :param txt:
    :return:
    '''
    result = []
    if txt:
        result.append(0)
    for index, letters in enumerate(txt):
        if letters == ' ':
            result.append(index + 1)
    return result

address = 'FOUR SCORE AND SEVEN YEARS AGO...'
result = index_words(address)
print(result[:3])

'''
#!=====================================================
# 上面这样写的问题
# 1. 代码拥挤
# 2. 每次找到新的结果需要index+1, 另外收尾创建和返回列表
========================================================
# 1.把函数改成生成器写会更加好
# 2.生成器通过yield表达式的函数,调用生成器的函数时,并不会真正的运行,而
# 是返回迭代器.每次在这个迭代器上面调用内置的next函数,迭代器会把生成
# 器推进下一个yield表达式里, 生成器传给yield的每一个值,都由迭代器返
# 回给调用者!
'''
def index_words_iter(txt):
    '''
    通过迭代器实现
    :param txt:
    :return:
    '''
    if txt:
        yield 0
    for index, letter in enumerate(txt):
        if letter == ' ':
            yield index + 1

class IndexWords:
    '''
    容器类
    '''
    def __init__(self, txt):
        self.txt = txt
    def __iter__(self):
        if self.txt:
            yield 0
        for index, letter in enumerate(self.txt):
            if letter == ' ':
                yield index + 1


def normalize(numbers: iter):
    total = sum(numbers) #第一次迭代
    result = []
    for value in numbers:  #第二次迭代
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
result = index_words_iter(visits)
print(normalize(result)) # []

'''
迭代器只会产生一轮结果,在抛出StopIteration异常的迭代器或生成器继续迭代第二轮是没有结果的 直接返回[]
如果想多次使用可以用一下几种方法:
1. 复制一份到列表 numbers = list(numbers)
2. 通过参数接受列一个函数
3. 实现一个迭代器协议的容器类46行
'''
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():  # 第二次迭代
        percent = 100 * value / total
        result.append(percent)
    return result
#每次调用 可以传入lambda表达式,该表达式会调用生成器,以便每次产生新的迭代器.
percentage = normalize_func(lambda: index_words_iter(address))
print(percentage)

def normalize_defensive(numbers):
    '''
    判断输入值是否为迭代器对象, 如果是就抛出TypeError异常
    :param numbers:
    :return:
    '''
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
visits = [15, 35, 80]
result = index_words_iter(visits)
print(id(iter(result)))
print(id(iter(result)))
# print(iter(result))
print(id(iter(visits)))
print(id(iter(visits)))
# print(iter(visits))
# normalize_defensive(result)
