# coding = utf8
def is_Palindrome(the_str):
    """
    本函数用来判别是否为回文字符串
    """
    l = len(the_str) - 1
    n = int(l/2)
    if len(the_str) == 0:
        print("The String is Null")
    elif len(the_str) > 0:
        temp = []
        for i in range(n):
            if the_str[i]==the_str[l-i]:
                temp.append("True")
            elif the_str[i] != the_str[l-i]:
                temp.append("False")

    if 'False' in temp:
        print("No,the string is not palindrome")
    else:
        print("Yse,the string is palindrome")

