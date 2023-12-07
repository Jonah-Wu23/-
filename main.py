import user_admin
import m_aux

while True:
    print("\n欢迎来到学生信息管理系统")
    
    while True:
        print("(按'q'退出)")
        # 登录界面：询问是管理员还是用户
        answer = input("\n请问您是管理员还是用户？ A.管理员 B.用户")
        m_aux.quit(answer)
        # 管理员
        if answer == 'A':
            # 生成admin实例
            admin = user_admin.Admin()
            # 输入账号
            input_name = input("请输入账号名称：")
            m_aux.quit(input_name)
            
            # 判断账号名称正误
            if input_name != admin.name:
                print("您不是管理员！请切换用户登录！\n")
                # 返回开头界面
                break
            else:
                # 输入密码
                input_password = input("请输入密码：(初始密码为123456)")
                m_aux.quit(input_password)
                # 判断密码正误
                if input_password == admin.password:

                    print("\n密码正确，进入系统")
                    # 系统主循环
                    while True:
                        print("\n(按'q'回到用户组选择界面)")
                        # 选择相应功能
                        choise = input("请选择相应功能：\nA.查看和修改学生个人信息 B.查看和修改学生考试情况 C.查看和修改课表\nD.审批学生转专业申请 E.审批学生辅修申请 F.修改密码")
                        # 回到登陆界面
                        if choise == 'q':
                            break
                        # 主功能选择代码块
                        elif choise == 'A':
                            m_aux.a_choice_a(admin)
                        elif choise == 'B':
                            m_aux.a_choice_b(admin)
                        elif choise == 'C':
                            m_aux.a_choice_c(admin)
                        elif choise == 'D':
                            m_aux.a_choice_d(admin)
                        elif choise == 'E':
                            m_aux.a_choice_e(admin)
                        elif choise == 'F':
                            admin.change_password()
                        else:
                            print("\n请输入各功能之前的字母！")
                
                # 密码错误
                else:
                    # 返回密码输入
                    print("密码错误！请重新输入\n")
                    continue
        # 用户
        elif answer == 'B':
            # 输入账号
            user_name = input("请输入账号名称：")
            m_aux.quit(user_name)
            # 生成user实例
            user = user_admin.User(user_name)

            # 判断账号名称正误
            try: 
                user_name = user.name
            except:    
                print("不存在此用户！\n")
                # 返回开头界面
                break
            else:
                # 输入密码
                user_password = input("请输入密码：(初始密码为123456)")
                m_aux.quit(user_password)
                # 判断密码正误
                if user_password == user.password:
                
                    print("\n密码正确，进入系统")
                    # 系统主循环
                    while True:
                        print("\n(按'q'回到用户组选择界面)")
                        # 选择相应功能
                        choise = input("请选择相应功能：\nA.查看学生个人信息 B.查看学生考试情况 C.查看课表 D.申请转专业 E.申请辅修专业\nF.查看转专业申请结果 G.查看辅修申请结果 H.修改密码")
                        # 回到登陆界面
                        if choise == 'q':
                            break
                        # 主功能选择代码块
                        elif choise == 'A':
                            m_aux.b_choice_a(user)
                        elif choise == 'B':
                            m_aux.b_choice_b(user)
                        elif choise == 'C':
                            m_aux.b_choice_c(user)
                        elif choise == 'D':
                            m_aux.b_choice_d(user)
                        elif choise == 'E':
                            m_aux.b_choice_e(user)
                        elif choise == 'F':
                            m_aux.b_choice_f(user)
                        elif choise == 'G':
                            m_aux.b_choice_g(user)
                        elif choise == 'H':
                            user.change_password()
                        else:
                            print("\n请输入各功能之前的字母！")

                # 密码错误
                else:
                    # 返回密码输入
                    print("密码错误！请重新输入\n")
                    continue
        # 异常输入
        else:
            print("请输入'A' 或者是'B'！\n")