# coding =  utf8
def bubble_sort(the_arry):
    """
    本函数用来实现冒泡排序
    """
    reslut = the_arry
    for j in range(len(the_arry) - 1):
        for i in range(len(the_arry) - 1):
            if the_arry[i + 1] < the_arry[i]:
                temp = the_arry[i]
                result[i] = the_arry[i + 1]
                result[i + 1] = temp
    return result
 
