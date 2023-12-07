'''用于辅助主程序运行的函数库'''
import sys
from pathlib import Path

import data

# 初始化路径,用于path函数
sbmaj_path = Path('user_sbmajor.json')
maj_path = Path('user_change_major.json')

# 初始化路径字符串,用于open函数
sb_maj_pathstr = 'user_sbmajor.json'
maj_pathstr = 'user_change_major.json'


def quit(input_):
    '''如果输入是'q'就退出程序'''
    if input_ == 'q':
        sys.exit()


def a_choice_a(admin):
    '''查看和修改学生个人信息'''
    while True:
        user_name = input("请输入您要查看和修改的学生的姓名：")
        if user_name == 'q':
            break
        # 初始化指定名称的用户
        user = admin.user_name(user_name)
        # 如果返回值是None，则没有该用户
        if user == None:
            print("\n没有该用户！")
            continue
        # 否则就有该用户
        else:
            # 显示用户信息
            user.show_user_infor()
            whether_chg = input("\n您想要修改这个学生的信息吗？(yes/no) ")
            if whether_chg == 'q':
                break
            elif whether_chg == 'yes':
                key = input("请输入您要修改该学生哪一方面的信息：")
                if key == 'q':
                    break
                new_user_infor = input(f"请输入该学生{key}方面的新信息：")
                if new_user_infor == 'q':
                    break
                # 改变用户信息
                admin.change_user_infor(user_name,key,new_user_infor)
            elif whether_chg == 'no':
                break


def a_choice_b(admin):
    '''查看和修改学生考试信息'''
    while True:
        user_name = input("请输入您要查看和修改考试信息的学生的姓名：")
        if user_name == 'q':
            break
        # 初始化指定名称的用户
        user = admin.user_name(user_name)
        # 显示用户考试信息
        user.show_test_infor()
        whether_chg = input("\n您想要修改这个学生的考试信息吗？(yes/no) ")
        if whether_chg == 'q':
            break
        elif whether_chg == 'yes':
            key = input("请输入您要修改该学生哪一方面的考试信息：")
            if key == 'q':
                break
            new_tst_infor = input(f"请输入该学生考试{key}方面的新信息：")
            if new_tst_infor == 'q':
                break
            # 改变用户考试信息
            admin.change_test_infor(user_name,key,new_tst_infor)
        elif whether_chg == 'no':
            break


def a_choice_c(admin):
    '''查看和修改学生课表信息'''
    while True:
        user_name = input("请输入您要查看和修改课表信息的学生的姓名：")
        if user_name == 'q':
            break
        # 初始化指定名称的用户
        user = admin.user_name(user_name)
        # 显示用户课表信息
        user.show_class_infor()
        whether_chg = input("\n您想要修改这个学生的课表信息吗？(yes/no) ")
        if whether_chg == 'q':
            break
        elif whether_chg == 'yes':
            key = input("请输入您要修改该学生哪一方面的课表信息：")
            if key == 'q':
                break
            new_cls_infor = input(f"请输入该学生考试{key}方面的新信息：")
            if new_cls_infor == 'q':
                break
            # 改变用户课表信息
            admin.change_class_infor(user_name,key,new_cls_infor)
        elif whether_chg == 'no':
            break


def a_choice_d(admin):
    '''审批学生转专业申请'''
    while True:
        user_name = input("请输入您要审批学生转专业申请信息的学生的姓名：")
        if user_name == 'q':
            break
        # 看看数据库里有没有东西
        try:
            # 审批转专业,返回yes/no
            choise = admin.ctrl_change_major(user_name)
        # 如果没有
        except:
            print("目前没有人想要转专业！")
        # 如果有
        else:
            if choise == 'yes':
                # 从转专业数据库中读取 学生想转去的专业 的信息
                new_major = data.read_maj_infor(user_name,'cm')
                # 修改学生的专业信息
                admin.change_user_infor(user_name,'专业',new_major)
                print("\n该学生转专业已经成功！")
                break
            elif choise == 'no':
                # 写入提示信息
                data.write_dict(user_name,"很抱歉，您的转专业请求不成功！",maj_path,maj_pathstr)
                print("\n已拒绝该学生的转专业请求！")
                break
            elif choise == 'q':
                break


def a_choice_e(admin):
    '''审批学生辅修申请'''
    while True:
        user_name = input("请输入您要审批学生辅修申请信息的学生的姓名：")
        if user_name == 'q':
            break
        # 看看数据库里有没有东西
        try:
            # 审批辅修申请,返回yes/no
            choise = admin.ctrl_sbmajor(user_name)
        # 如果没有
        except:
            print("目前没有人想要辅修！")
        # 如果有
        else:
            if choise == 'yes':
                # 从辅修数据库中读取 学生想辅修的专业 的信息
                new_major = data.read_maj_infor(user_name,'s')
                # 读取学生原来的专业信息
                old_major = data.return_information(user_name,'专业')
                # 修改学生的专业信息(原来专业+辅修专业)
                admin.change_user_infor(user_name,'专业',old_major+' 辅修： '+new_major)
                print("\n该学生辅修专业已经成功！")
                break
            elif choise == 'no':
                # 写入提示信息
                data.write_dict(user_name,"很抱歉，您的辅修请求不成功！",maj_path,maj_pathstr)
                print("\n已拒绝该学生的辅修请求！")
                break
            elif choise == 'q':
                break


def b_choice_a(user):
    '''查看学生个人信息'''
    while True:
        user.show_user_infor()
        input("\n（按任意键返回选择页面）")
        break


def b_choice_b(user):
    '''查看学生考试情况'''
    while True:
        user.show_test_infor()
        input("\n（按任意键返回选择页面）")
        break


def b_choice_c(user):
    '''查看课表'''
    while True:
        user.show_class_infor()
        input("\n（按任意键返回选择页面）")
        break


def b_choice_d(user):
    '''申请转专业'''
    while True:
        new_major = input("您想转去哪个专业？ ")
        if new_major == 'q':
            break
        user.apply_for_change_major(new_major)
        print("转专业申请已经递交给管理员，请等待审批！")
        input("\n（按任意键返回选择页面）")
        break


def b_choice_e(user):
    '''申请辅修专业'''
    while True:
        new_major = input("您想辅修哪个专业？ ")
        if new_major == 'q':
            break
        user.apply_for_sbmajor(new_major)
        print("辅修申请已经递交给管理员，请等待审批！")
        input("\n（按任意键返回选择页面）")
        break


def b_choice_f(user):
    '''查看转专业申请结果'''
    while True:
        try:
            result = user.show_major_infor()
        except KeyError:
            print("\n您还未进行过任何转专业申请！")
            break
        else:
            print(f"目前您的转专业申请情况：{result}")
            user.apply_for_change_major('')
            input("\n（按任意键返回选择页面）")
            break


def b_choice_g(user):
    '''查看辅修申请结果'''
    while True:
        try:
            result = user.show_sbmaj_infor()
        except KeyError:
            print("\n您还未进行过任何辅修申请！")
            break
        else:
            print(f"目前您的辅修专业申请情况：{result}")
            user.apply_for_sbmajor('')
            input("\n（按任意键返回选择页面）")
            break


