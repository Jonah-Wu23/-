'''包含用户类和管理员类'''

import json
from pathlib import Path

import data

# 初始化路径,用于path函数
sbmaj_path = Path('user_sbmajor.json')
infor_path = Path('user_infor.json')
tst_path = Path('user_test_infor.json')
cls_path = Path('user_cls_infor.json')
maj_path = Path('user_change_major.json')
admin_path = Path('admin_infor.json')

# 初始化路径字符串,用于open函数
sb_maj_pathstr = 'user_sbmajor.json'
maj_pathstr = 'user_change_major.json'
infor_pathstr = 'user_infor.json'
admin_pathstr = 'admin_infor.json'


class User():
    '''模拟用户的一个简单尝试'''

    def __init__(self,name):
        '''初始化用户信息'''
        infor_json = infor_path.read_text()
        messages = json.loads(infor_json)
        for person_messages in messages:
            if person_messages['姓名'] == name:
                self.name = person_messages['姓名']
                self.password = person_messages['密码']
                self.grade = person_messages['年级']
                self.stu_id = person_messages['学号']
                self.school = person_messages['学院']
                self.major = person_messages['专业']
                self.cls_num = person_messages['班级']
                self.phn_num = person_messages['手机号']
                self.qq_num = person_messages['QQ号']
                self.situation = person_messages['学籍情况']

    def show_user_infor(self):
        '''显示用户信息'''
        print(f"姓名：{self.name},年级：{self.grade},学号：{self.stu_id}"+
              f"\n学院：{self.school},专业：{self.major},班级：{self.cls_num}"+
              f"\n手机号:{self.phn_num},QQ号：{self.qq_num},学籍情况：{self.situation}")
        
    def show_test_infor(self):
        '''显示考试情况'''
        data.show_information(self.name,tst_path)

    def show_class_infor(self):
        '''显示课表情况'''
        data.show_information(self.name,cls_path)

    def apply_for_change_major(self,new_major):
        '''申请转专业'''
        data.write_dict(self.name,new_major,maj_path,maj_pathstr)

    def apply_for_sbmajor(self,sbmajor):
        '''申请辅修专业'''
        data.write_dict(self.name,sbmajor,sbmaj_path,sb_maj_pathstr)

    def show_major_infor(self):
        '''显示转专业情况'''
        result = data.read_maj_infor(self.name,'cm')
        return result
    
    def show_sbmaj_infor(self):
        '''显示辅修专业情况'''
        result = data.read_maj_infor(self.name,'s')
        return result
    
    def change_password(self):
        '''修改密码'''
        while True:
            input1_password = input("\n请输入您的新密码：")
            if input1_password == 'q':
                break
            input2_password = input("请再次确认您的新密码：")
            if input2_password == 'q':
                break
            if input1_password == input2_password:
                new_password = input2_password
            else:
                print("两次输入的密码不一样！请重新输入")
                continue
            data.change_information(self.name,'密码',new_password,infor_path)
            print(f"您的密码已被更改！\n请牢记您的新密码：{new_password}")
            break

class Admin():
    '''模拟管理员的一个简单尝试'''

    def __init__(self):
        '''初始化管理员信息'''
        admininfor_json = admin_path.read_text()
        messages = json.loads(admininfor_json)
        for message_dict in messages:
            self.name = message_dict['名字']
            self.password = message_dict['密码']

    def change_user_infor(self,name,key,new_user_infor):
        '''改变用户信息'''
        data.change_information(name,key,new_user_infor,infor_path)
        
    def change_test_infor(self,name,key,new_tst_infor):
        '''改变考试情况'''
        data.change_information(name,key,new_tst_infor,tst_path)

    def change_class_infor(self,name,key,new_cls_infor):
        '''改变课表情况'''
        data.change_information(name,key,new_cls_infor,cls_path)

    def ctrl_change_major(self,name):
        '''审批转专业,返回yes/no'''
        # 读取json文件，并转化为字典
        infors = json.loads(maj_path.read_text())
        # 遍历字典，键是名字，值是申请转去的专业
        for person_name,req_sbmaj in infors.items():
            # 找到指定人名
            if person_name == name:
                # 让管理员审批
                result = input(f"想要让{name}转去{req_sbmaj}专业吗？(yes/no)")
        # 返回yes/no
        return result

    def ctrl_sbmajor(self,name):
        '''审批辅修专业,返回yes/no'''
        # 读取json文件，并转化为字典
        infors = json.loads(sbmaj_path.read_text())
        # 遍历字典，键是名字，值是申请的辅修专业
        for person_name,req_sbmaj in infors.items():
            # 找到指定人名
            if person_name == name:
                # 让管理员审批
                result = input(f"想要让{name}辅修{req_sbmaj}专业吗？(yes/no)")
        # 返回yes/no
        return result
    
    def get_user_infor(self,user_name):
        '''返回用户数据,以字典形式输出'''
        infor_json = infor_path.read_text()
        messages = json.loads(infor_json)
        for person_messages in messages:
            if person_messages['姓名'] == user_name:
                return person_messages
    
    def put_user_infor(self,*mgs):
        '''将信息储存到用户信息文件中'''
        tot_messages = list(mgs)
        open(infor_pathstr,"w").write(json.dumps(tot_messages,indent=4,ensure_ascii=False))

    def user_name(self,name):
        '''初始化指定名称的用户'''
        # 读取json文件，并转化为列表
        tot_infors = json.loads(infor_path.read_text())
        # 遍历列表
        for infors in tot_infors:
            # 遍历字典的值
            for person_name in infors.values():
                # 如果指定的名称是字典的一个值
                if person_name == name:
                    # 生成对应的用户的实例
                    user = User(person_name)
                    return user
                
    def change_password(self):
        '''修改密码'''
        while True:
            input1_password = input("\n请输入您的新密码：")
            if input1_password == 'q':
                break
            input2_password = input("请再次确认您的新密码：")
            if input2_password == 'q':
                break
            if input1_password == input2_password:
                new_password = input2_password
            else:
                print("两次输入的密码不一样！请重新输入")
                continue
            data.change_information(self.name,'密码',new_password,admin_path)
            print(f"您的密码已被更改！\n请牢记您的新密码：{new_password}")
            break