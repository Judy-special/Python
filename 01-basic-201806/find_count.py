def find_count(the_arry):
    """
    本函数用来统计list中元素出现的次数
    """
    d = {}   # 用字典来存储每个元素出现的次数，key为元素，value为出现的次数
    for i in range(len(the_arry)):
        d[the_arry[i]] = d.get(the_arry[i], 0) + 1   # .get() 可以获取字典指定元素的value
    return d
