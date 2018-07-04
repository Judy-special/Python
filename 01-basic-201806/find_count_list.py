def find_count_list(the_arry, count):
    """
        本函数用来找出list中元素出现次数达到n次以上的元素
    """
    d = {}
    result = []
    for i in range(len(the_arry)):
        d[the_arry[i]] = d.get(the_arry[i], 0) + 1

    for k in d:
        if d[k] > count:
            result.append(k)
    return result
