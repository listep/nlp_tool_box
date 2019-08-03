'''
函数作用：
输入一个“中文、英文、数字、特殊符号”组成的字符串，返回两个list。
输出：特殊符号会被过滤，返回英文数字list，中文list。

'''
import re
def split_english_number_chinese(text):

    text_English_num = re.sub(r'[\u4e00-\u9fa5]', ' ', text)   #汉字变为分隔符
    text_English_num = re.sub(r'[^\w]', ' ', text_English_num)  # 特殊字符变为分隔符
    text_English_num = re.split(r'[\s]', text_English_num)      # 分割符号为空格
    text_English_num = list(filter(None, text_English_num))  # 过滤掉list中的空字符串

    text_Chinese = re.sub(r'[^\u4e00-\u9fa5]', ' ', text)   #非汉字变为分隔符
    text_Chinese = re.split(r'[\s]', text_Chinese)
    text_Chinese = list(filter(None, text_Chinese))  # 过滤掉list中的空字符串

    return text_English_num, text_Chinese

text_eng_num , text_chi = split_english_number_chinese('vivo.*?nike哇哈哈*mac&&iPhone9s（（耐克')

print(text_eng_num , text_chi)

# 返回
# ['vivo', 'nike', 'mac', 'iPhone9s'] ['哇哈哈', '耐克']