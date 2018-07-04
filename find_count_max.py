# coding=utf8
def find_count_max(the_arry):
    """
    本函数用来查找list中出现次数最多的元素
    """
    d = {}
    for i in range(len(the_arry)):
        d[the_arry[i]] = d.get(the_arry[i], 0) + 1   # d.get() 获取字典d中指定key的value，找不到的话默认为0

    temp_value = 0
    result = ''
    for k in d:
        if d[k] > temp_value:
            temp_value = d[k]
            result = k
    return result, temp_value
