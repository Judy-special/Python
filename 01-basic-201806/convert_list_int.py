# coding = utf8
def convert_list_num(the_arr):
    """
    本函数用来将输入的list转化为整数
    :param list = [1, 2, 3]
    :return: 输出123
    """
    num = 0 
    for i in range(len(the_arr)):
        num = num * 10 + the_arr[i]
    return num
