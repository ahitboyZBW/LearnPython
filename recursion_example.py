# _*_ coding: utf-8 _*_ 

# 10进制转2-16进制的数
def to_str(n,base):
    conversionStr = '0123456789ABCDEF'
    if n < base:
        return conversionStr[n]
    else:
        return to_str(n//base,base) + conversionStr[n%base]

print(to_str(1456,16))

def str_inverse(str):
    if len(str) == 1:
        return str
    else:
        return str_inverse(str[1:]) + str[0]

def huiwen_judge(str):
    """判断一个字符串是否为回文，正反都一样"""
    return str==str_inverse(str)

    
print(str_inverse('123456'))
print(huiwen_judge('12321'))
print(huiwen_judge('12345'))