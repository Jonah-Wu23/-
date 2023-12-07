'''处理数据的函数库'''

import json
from pathlib import Path
import sys

# 初始化路径,用于path函数
sbmaj_path = Path('user_sbmajor.json')
maj_path = Path('user_change_major.json')


def change_information(name,key,new_infor,infor_path):
    '''改变指定名字的人的各种信息(写入嵌套字典的列表)'''
    try:
        # 将json文件内容转换成嵌套字典的列表
        infor_json = infor_path.read_text()
        tot_messages = json.loads(infor_json)
    except:
        # 如果文件里空空如也
        new_dict = {}
        new_lst = []
        # 写入字典的值
        new_dict['姓名'] = name
        new_dict[key] = new_infor
        # 将新字典追加到列表末尾
        new_lst.append(new_dict)
        # 将新的大列表转换成json格式并写入json文件
        infor_path.write_text(json.dumps(new_lst,indent=4,ensure_ascii=False))
        print("更改成功！")
    else:
        # 遍历列表
        for person_messages in tot_messages:
            # 如果列表元素只有一个并且名字不在字典的值中：
            if len(tot_messages) == 1 and name not in person_messages.values():
                # 就要新建一个对应这个名字的字典
                new_dict = {}
                # 写入字典的值
                new_dict['姓名'] = name
                new_dict[key] = new_infor
                # 将新字典追加到列表末尾
                tot_messages.append(new_dict)
                # 将新的大列表转换成json格式并写入json文件
                infor_path.write_text(json.dumps(tot_messages,indent=4,ensure_ascii=False))
                print("更改成功！") 
            # 如果名字在字典的值中，就是对应名字的字典
            if name in person_messages.values():
                # 更改新值
                person_messages[key] = new_infor
                # 将新的大列表转换成json格式并写入json文件
                infor_path.write_text(json.dumps(tot_messages,indent=4,ensure_ascii=False))
                print("更改成功！") 

def write_dict(name,new_infor,infor_path,infor_pathstr):
    '''将一个含有新的键值对的字典写入指定的文件中(以名字为键)'''
    if infor_path.exists():
        # 把里面的字典提取出来
        try:
            _dict = json.loads(infor_path.read_text())
        except:
            _dict = {}
        # 键为名字，值为申请的新信息
        _dict[name] = new_infor
        # 生成json文件
        _json = json.dumps(_dict,indent=4,ensure_ascii=False)
        # 写入json文件
        open(infor_pathstr,"w").write(_json)
    
def show_information(name,infor_path):
    '''展示指定名字的人的各种信息(遍历嵌套字典的列表和里面的字典并输出)'''
    # 将json文件内容转换成嵌套字典的列表
    infor_json = infor_path.read_text()
    tot_messages = json.loads(infor_json)
    # 遍历列表
    for person_messages in tot_messages:
        # 遍历字典
        for value in person_messages.values():
            # 找到对应人名的字典
            if value == name:
                # 遍历这个字典并输出里面的内容
                for k,v in person_messages.items():
                    print(f"{k}：{v},\n")

def put_infor(infor_pathstr,*mgs):
        '''将信息以列表形式储存到各种信息文件中'''
        tot_messages = list(mgs)
        open(infor_pathstr,"w").write(json.dumps(tot_messages,indent=4,ensure_ascii=False))

def read_maj_infor(name,maj_type):
    '''返回一个以名字作为键的字典的值（转专业或辅修数据库）
       \nmaj_type = 's' : 辅修，maj_type = 'cm' : 转专业'''
    # 如果是转专业数据库
    if maj_type == 'cm':
        # 提取字典
        _dict = json.loads(maj_path.read_text())
    # 如果是辅修数据库
    elif maj_type == 's':    
        # 提取字典
        _dict = json.loads(sbmaj_path.read_text())
    # 提取字典中键为名字的值
    value = _dict[name]
    # 返回这个值（想转去的专业或者是想辅修的专业）
    return value

def return_information(name,key):
    '''返回指定名字的人的各种信息(返回学生信息数据中指定键的值)'''
    # 读取学生信息数据文件的路径
    infor_path = Path('user_infor.json')
    # 将json文件内容转换成嵌套字典的列表
    infor_json = infor_path.read_text()
    tot_messages = json.loads(infor_json)
    # 遍历列表
    for person_messages in tot_messages:
        # 遍历字典
        for value in person_messages.values():
            # 找到对应人名的字典
            if value == name:
                # 返回学生信息数据中指定键的值
                return person_messages[key]