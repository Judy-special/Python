# coding = utf8
def two_sum(the_arry,target):
    """
    本函数用来找出list中和为target的两个元素及其下标
    """
    d = {} # 存放已经访问过的元素及其下标
    result = []
    for i in range(len(the_arry)):
        diff = target - the_arry[i]
        if diff in d:
            result.append((d[diff], i))
        
        d[the_arry[i]] = i
    return result
