# coding = utf8
def convert_list_interval(the_arry):
    """
    本函数用来将排好序的list转化为连续的数组段
    :param 数组[1, 2, 3, 5, 6, 7, 9]
    :return 输出[[1, 3], [5, 7], [9]]

    """
    temp_list = []
    result = []
    for i in range(the_arry):
        if len(temp_list) > 0 and the_arry[i] - temp_list[-1] != 1:
            result.append([temp_list[0],temp_list[-1]])
            temp_list = []
        temp_list.append(the_arry[i])
    result.append(temp_list)

    return result
