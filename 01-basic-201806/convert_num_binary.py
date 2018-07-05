# coding = utf8
def convert_num_binary(num):
    """
    本函数用来将输入的整数转化为二进制list
    :param num:17
    :return: 输出[1, 0, 0, 0, 1]
    """ 
    quot = num # 用来存储除以2的商
    mod = num # 用来存储除以2的余数
    result = []
    while quot > 0 :
        mod = quot % 2
        quot = int(quot/2)
        result.insert(0, mod) # 在result的下标0的位置插入mod

    return result
