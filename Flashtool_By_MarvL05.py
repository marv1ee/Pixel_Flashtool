#coding:utf-8


import os
import wget
import webbrowser


title1 = "┏━━━┳┓╋╋╋╋╋╋┏┓╋┏━━━━┓╋╋╋╋╋┏┓\n┃┏━━┫┃╋╋╋╋╋╋┃┃╋┃┏┓┏┓┃╋╋╋╋╋┃┃\n┃┗━━┫┃┏━━┳━━┫┗━╋┛┃┃┗╋━━┳━━┫┃\n┃┏━━┫┃┃┏┓┃━━┫┏┓┃╋┃┃╋┃┏┓┃┏┓┃┃\n┃┃╋╋┃┗┫┏┓┣━━┃┃┃┃╋┃┃╋┃┗┛┃┗┛┃┗┓\n┗┛╋╋┗━┻┛┗┻━━┻┛┗┛╋┗┛╋┗━━┻━━┻━┛\n┏━━┓╋╋╋╋╋┏━┓┏━┓╋╋╋╋╋╋╋┏┓╋╋┏━━━┳━━━┓\n┃┏┓┃╋╋╋╋╋┃┃┗┛┃┃╋╋╋╋╋╋╋┃┃╋╋┃┏━┓┃┏━━┛\n┃┗┛┗┳┓╋┏┓┃┏┓┏┓┣━━┳━┳┓┏┫┃╋╋┃┃┃┃┃┗━━┓\n┃┏━┓┃┃╋┃┃┃┃┃┃┃┃┏┓┃┏┫┗┛┃┃╋┏┫┃┃┃┣━━┓┃\n┃┗━┛┃┗━┛┃┃┃┃┃┃┃┏┓┃┃┗┓┏┫┗━┛┃┗━┛┣━━┛┃\n┗━━━┻━┓┏┛┗┛┗┛┗┻┛┗┻┛╋┗┛┗━━━┻━━━┻━━━┛\n╋╋╋╋┏━┛┃\n╋╋╋╋┗━━┛"

title2 = "欢迎使用酷安@铭灏MarvL05制作的自动化解锁+刷机工具，该软件专为小白设计，\n如大佬们有什么意见可以到Github提issue 项目名:Flashtool_By_MarvL05\n该软件目前支持Sony和Pixel的部分设备，如未适配还请谅解\n（毕竟作者是个高二狗\n"

content = "==============================================\n====================主菜单====================\n==============================================\n1.安装Android驱动         5.酷安个人主页传送门\n2.解锁BootLoader          6.Github项目传送门\n3.刷入全量包              7.作者QQ传送门\n4.刷入面具Patch.img\n\n0.退出\n"

alltitle = title1 + "\n" + title2 + "\n" + content
print(alltitle)

while True:

    inn = input("输入你的选项：")

    if inn == "1":
        while True:
            os.system("cls")
            print("\nEmmmm，我能力有限，请自行进入Android_Driver文件夹右击android_winusb.inf安装\n↓如果安装后发现fastboot不生效请参考此教程↓")
            tip = input("是否打开教程？（Y/n）：")
            if tip == "y" or tip == "Y":
                webbrowser.open("http://s.marvl05.site:88/tjQn", new=0, autoraise=True)
                os.system("cls")
                print(alltitle)
                break
            elif tip == "n" or tip == "N":
                os.system("cls")
                print(alltitle)
                break
            else:
                print("达咩！请重新输入！")
    elif inn == "2":
        os.system("cls")
        print("\n注意！!请确认驱动已经安装正确且开发者选项中‘OEM解锁’已开启\n解锁Bootloader会清除用户数据，请在执行之前妥善备份")
        print("\n1.Sony设备\n2.Pixel设备\n\n0.返回上一级")
        while True:
            unlock = input("\n输入你的选项：")
            if unlock == "1":
                os.system("cls")
                print("\n注意！！Sony设备解锁需要Bootloader unlock allowed显示Yes，否则无法解锁\n如果显示 < waiting for any device > 请检查驱动程序")
                print("tips:Sony设备关机后按住音量上键插入数据线（另一端已连接电脑）即可进入Fastboot（蓝灯模式）")
                print("\n请确认设备已进入Fastboot（蓝灯模式），确认后回车继续")
                os.system("pause")
                code = input("\n请输入你的解锁码：")
                os.system("fastboot oem unlock 0x" + code)
                print("出现success则表明解锁成功")
                os.system("pause")
                os.system("cls")
                print(alltitle)
                break
            elif unlock == "2":
                os.system("cls")
                print("\n注意！！Pixel设备请确认开发者选项内的OEM解锁可以正常打开（有锁机无法解锁）")
                print("tips:Pixel设备关机后长按电源键+音量下键即可进入Bootloader")
                print("\n请确认设备已进入Bootloader，确认后回车继续")
                os.system("pause")
                os.system("fastboot flashing unlock")
                print("出现success则表明解锁成功")
                os.system("pause")
                os.system("cls")
                print(alltitle)
                break
            elif unlock == "0":
                os.system("cls")
                print(alltitle)
                break
            else:
                print("达咩！请重新输入！")
    elif inn == "3":
        os.system("cls")
        print("\n此功能尚未完善，在酷安多给作者点赞可能更新会快点哦\n\n0.返回上一级")
        while True:
            flash = input("\n输入你的选项：")
            if flash == "0":
                os.system("cls")
                print(alltitle)
                break
            else:
                print("达咩！请重新输入！")
    elif inn == "4":
        os.system("cls")
        device_content = "\n如果显示 < waiting for any device >，请检查驱动程序\n请选择你的设备：\n\n1.Pixel 3\n2.Pixel 3XL\n3.Pixel 3a\n4.Pixel 3aXL\n5.Pixel 4\n6.Pixel 4XL\n7.Pixel 4a\n8.Pixel 4a(5G)\n9.Pixel 5\na.手动刷入\n\n0.返回上一级"
        print(device_content)
        while True:
            while True:
                device = input("\n输入你的选项：")
                if device == "1":
                    wget.download("http://kod.marvl05.site:88/?explorer/share/fileDownload&shareID=7LoPZVyg&path=%7BshareItemLink%3A7LoPZVyg%7D%2FGoogle%20Pixel%203%2Fpatch.img&s=RQ0aI","patch.img")
                    ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
                    if ask == "Y" or ask == "y":
                        os.system("fastboot flash boot patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(device_content)
                    elif ask == "N" or ask == "n":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "2":
                    wget.download("http://kod.marvl05.site:88/?explorer/share/fileDownload&shareID=7LoPZVyg&path=%7BshareItemLink%3A7LoPZVyg%7D%2FGoogle%20Pixel%203%20XL%2Fpatch.img&s=Kl9Zm","patch.img")
                    ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
                    if ask == "Y" or ask == "y":
                        os.system("fastboot flash boot patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(device_content)
                    elif ask == "N" or ask == "n":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "3":
                    wget.download("http://kod.marvl05.site:88/?explorer/share/fileDownload&shareID=7LoPZVyg&path=%7BshareItemLink%3A7LoPZVyg%7D%2FGoogle%20Pixel%203a%2Fpatch.img&s=dJky2","patch.img")
                    ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
                    if ask == "Y" or ask == "y":
                        os.system("fastboot flash boot patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(device_content)
                    elif ask == "N" or ask == "n":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "4":
                    wget.download("http://kod.marvl05.site:88/?explorer/share/fileDownload&shareID=7LoPZVyg&path=%7BshareItemLink%3A7LoPZVyg%7D%2FGoogle%20Pixel%203a%20XL%2Fpatch.img&s=Tupss","patch.img")
                    ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
                    if ask == "Y" or ask == "y":
                        os.system("fastboot flash boot patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(device_content)
                    elif ask == "N" or ask == "n":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "5":
                    wget.download("http://kod.marvl05.site:88/?explorer/share/fileDownload&shareID=7LoPZVyg&path=%7BshareItemLink%3A7LoPZVyg%7D%2FGoogle%20Pixel%204%2Fpatch.img&s=S4eX0","patch.img")
                    ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
                    if ask == "Y" or ask == "y":
                        os.system("fastboot flash boot patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(device_content)
                    elif ask == "N" or ask == "n":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "6":
                    wget.download("http://kod.marvl05.site:88/?explorer/share/fileDownload&shareID=7LoPZVyg&path=%7BshareItemLink%3A7LoPZVyg%7D%2FGoogle%20Pixel%204%20XL%2Fpatch.img&s=VaNL1","patch.img")
                    ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
                    if ask == "Y" or ask == "y":
                        os.system("fastboot flash boot patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(device_content)
                    elif ask == "N" or ask == "n":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "7":
                    wget.download("http://kod.marvl05.site:88/?explorer/share/fileDownload&shareID=7LoPZVyg&path=%7BshareItemLink%3A7LoPZVyg%7D%2FGoogle%20Pixel%204a%2Fpatch.img&s=kUB6B","patch.img")
                    ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
                    if ask == "Y" or ask == "y":
                        os.system("fastboot flash boot patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(device_content)
                    elif ask == "N" or ask == "n":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "8":
                    wget.download("http://kod.marvl05.site:88/?explorer/share/fileDownload&shareID=7LoPZVyg&path=%7BshareItemLink%3A7LoPZVyg%7D%2FGoogle%20Pixel%204a(5G)%2Fpatch.img&s=VcPfj","patch.img")
                    ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
                    if ask == "Y" or ask == "y":
                        os.system("fastboot flash boot patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(device_content)
                    elif ask == "N" or ask == "n":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "9":
                    wget.download("http://kod.marvl05.site:88/?explorer/share/fileDownload&shareID=7LoPZVyg&path=%7BshareItemLink%3A7LoPZVyg%7D%2FGoogle%20Pixel%205%2Fpatch.img&s=tABWo","patch.img")
                    ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
                    if ask == "Y" or ask == "y":
                        os.system("fastboot flash boot patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(device_content)
                    elif ask == "N" or ask == "n":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "a" or device == "A":
                    os.system("cls")
                    manual = input("手动刷入需要将文件名改为patch.img并放入工具箱目录内，确认已完成？（Y/n）")
                    if manual == "Y" or manual == "y":
                        os.system("fastboot flash patch.img")
                        print("出现success则表明刷入成功")
                        os.system("pause")
                        os.system("cls")
                        print(alltitle)
                    elif manual == "n" or manual == "N":
                        os.system("cls")
                        print(device_content)
                    break
                elif device == "0":
                    os.system("cls")
                    print(alltitle)
                    break
                else:
                    print("达咩！请重新输入！")
    elif inn == "5":
        webbrowser.open("http://www.coolapk.com/u/1925252", new=0, autoraise=True)
        os.system("cls")
        print(alltitle)
    elif inn == "6":
        webbrowser.open("https://github.com/MarvL05/Flashtool_By_MarvL05", new=0, autoraise=True)
        os.system("cls")
        print(alltitle)
    elif inn == "7":
        webbrowser.open("http://wpa.qq.com/msgrd?v=3&uin=2627599936&site=qq&menu=yes", new=0, autoraise=True)
        os.system("cls")
        print(alltitle)
    elif inn == "0":
        exit()
    else:
        print("达咩！请重新输入！")
