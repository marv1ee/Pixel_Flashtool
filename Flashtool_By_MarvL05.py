#coding:utf-8


import os
import wget
import webbrowser


title1 = "┏━━━┳┓╋╋╋╋╋╋┏┓╋┏━━━━┓╋╋╋╋╋┏┓\n┃┏━━┫┃╋╋╋╋╋╋┃┃╋┃┏┓┏┓┃╋╋╋╋╋┃┃\n┃┗━━┫┃┏━━┳━━┫┗━╋┛┃┃┗╋━━┳━━┫┃\n┃┏━━┫┃┃┏┓┃━━┫┏┓┃╋┃┃╋┃┏┓┃┏┓┃┃\n┃┃╋╋┃┗┫┏┓┣━━┃┃┃┃╋┃┃╋┃┗┛┃┗┛┃┗┓\n┗┛╋╋┗━┻┛┗┻━━┻┛┗┛╋┗┛╋┗━━┻━━┻━┛\n┏━━┓╋╋╋╋╋┏━┓┏━┓╋╋╋╋╋╋╋┏┓╋╋┏━━━┳━━━┓\n┃┏┓┃╋╋╋╋╋┃┃┗┛┃┃╋╋╋╋╋╋╋┃┃╋╋┃┏━┓┃┏━━┛\n┃┗┛┗┳┓╋┏┓┃┏┓┏┓┣━━┳━┳┓┏┫┃╋╋┃┃┃┃┃┗━━┓\n┃┏━┓┃┃╋┃┃┃┃┃┃┃┃┏┓┃┏┫┗┛┃┃╋┏┫┃┃┃┣━━┓┃\n┃┗━┛┃┗━┛┃┃┃┃┃┃┃┏┓┃┃┗┓┏┫┗━┛┃┗━┛┣━━┛┃\n┗━━━┻━┓┏┛┗┛┗┛┗┻┛┗┻┛╋┗┛┗━━━┻━━━┻━━━┛\n╋╋╋╋┏━┛┃\n╋╋╋╋┗━━┛"

title2 = "欢迎使用酷安@铭灏MarvL05制作的自动化解锁+刷机工具，该软件专为小白设计，\n如大佬们有什么意见可以到Github提issue 项目名:Flashtool_By_MarvL05\n该软件目前支持Sony和Pixel的部分设备，如未适配还请谅解\n（毕竟作者是个高二狗\n"

content = "==============================================\n====================主菜单====================\n==============================================\n1.ADB&Fastboot基本指令    5.刷入面具Patch.img\n2.安装Android驱动         6.酷安个人主页传送门\n3.解锁BootLoader          7.Github项目传送门\n4.刷入全量包              8.作者QQ传送门\n\n0.退出\n"

all = title1 + "\n" + title2 + "\n" + content

print(all)

def cls_printall():         #清屏 + 打印主页
    os.system("cls")
    print(all)

def ospause():              #cmd暂停
    os.system("pause")

def web_open(weburl):       #打开网页
    webbrowser.open(weburl, new=0, autoraise=True)

def print_error():          #输入报错
    print("达咩！请重新输入！")


while True:

    inn = input("输入你的选项：")
    if inn == "1":
        os.system("cls")
        cmd_content = "\nADB & Fastboot基本指令\n\na.检测ADB设备\nb.检测Fastboot设备\nADB:\n1.重启手机至系统\n2.重启手机至Fastboot\n3.重启手机至Recovery\n4.关闭手机\nFastboot:\n5.重启手机至系统\n6.重启手机至Fastboot\n7.重启手机至Recovery\n8.关闭手机\n\nc.安装酷安\nm.安装Magisk Manager\nz.自行安装app\n\n9.自行输入命令\n0.返回上一级"
        print(cmd_content)
        def cmd_function():         #清屏 + 打印命令目录
            os.system("cls")
            print(cmd_content)
        def cmd_input(cmdln):       #执行指定命令
            os.system(cmdln)
            print("执行成功")
            ospause()
        while True:
            cmd = input("\n输入你的选项：")
            if cmd == "a" or cmd == "A":
                os.system("adb devices")
                print("如果没有显示一串字符和device，请检查驱动，反之则连接成功；\n如果显示一串字符和unauthorized，请在手机上允许调试，若手机没有提示就点击开发者内的撤销USB调试授权")
                ospause()
                cmd_function()
            elif cmd == "b" or cmd == "B":
                os.system("fastboot devices")
                print("显示一串字符和fastboot即为连接成功，反之请检查驱动")
                ospause()
                cmd_function()
            elif cmd == "1":
                cmd_input(cmdln="adb reboot")
                cmd_function()
            elif cmd == "2":
                cmd_input(cmdln="adb reboot bootloader")
                cmd_function()
            elif cmd == "3":
                cmd_input(cmdln="adb reboot recovery")
                cmd_function()
            elif cmd == "4":
                cmd_input(cmdln="adb shell reboot -p")
                cmd_function()
            elif cmd == "5":
                cmd_input(cmdln="fastboot reboot")
                cmd_function()
            elif cmd == "6":
                cmd_input(cmdln="fastboot reboot bootloader")
                cmd_function()
            elif cmd == "7":
                cmd_input(cmdln="fastboot reboot recovery")
                cmd_function()
            elif cmd == "8":
                print("\nSony设备拔下数据线即关机\nPixel设备点按音量键选择Power off点按电源键关机")
                ospause()
                cmd_function()
            elif cmd == "c" or cmd == "C":
                wget.download("http://one.marvl05.site:88/apks/Coolapk.apk", "Coolapk.apk")
                print()
                os.system("adb install Coolapk.apk")
                print("出现success即安装成功！")
                ospause()
                os.system("del Coolapk.apk")
                cmd_function()
            elif cmd == "m" or cmd == "M":
                wget.download("http://one.marvl05.site:88/apks/Magisk-v23.0.apk", "Magisk.apk")
                print()
                os.system("adb install Magisk.apk")
                print("出现success即安装成功！")
                ospause()
                os.system("del Magisk.apk")
                cmd_function()
            elif cmd == "z" or cmd == "Z":
                apk = input("\n请将安装包直接拖进命令行窗口然后回车：")
                os.system("adb install " + apk)
                print("出现success即安装成功！")
                ospause()
                cmd_function()
            elif cmd == "9":
                cmd_in = input("输入ADB或Fastboot指令：")
                os.system(cmd_in)
                ospause()
                cmd_function()
            elif cmd == "0":
                cls_printall()
                break
            else:
                print_error()
    elif inn == "2":
        os.system("cls")
        print("\nEmmmm，暂时还没有好的自动解决方案，\n请自行进入Android_Driver文件夹右击android_winusb.inf安装\n↓如果安装后发现fastboot不生效请参考此教程↓")
        while True:
            tips = input("是否打开教程？（Y/n）：")
            if tips == "y" or tips == "Y":
                web_open(weburl="http://marvl05.site:88/tjqn")
                print("若图片无法加载请用手机扫描旁边的二维码浏览")
                ospause()
                cls_printall()
                break
            elif tips == "n" or tips == "N":
                cls_printall()
                break
            else:
                print_error()
    elif inn == "3":
        os.system("cls")
        print("\n注意！!请确认驱动已经安装正确且开发者选项中‘OEM解锁’已开启\n解锁Bootloader会清除用户数据，请在执行之前妥善备份\n请先重启进入Fastboot模式（可在主菜单第一项内重启）")
        print("\n1.Sony设备\n2.Pixel设备\n\n0.返回上一级")
        while True:
            unlock = input("\n输入你的选项：")
            if unlock == "1":
                os.system("cls")
                print("\n注意！！Sony设备解锁需要Bootloader unlock allowed显示Yes，否则无法解锁\n如果显示 < waiting for any device > 请检查驱动程序")
                print("tips:Sony设备关机后按住音量上键插入数据线（另一端已连接电脑）即可进入Fastboot（蓝灯模式）")
                print("\n请确认设备已进入Fastboot（蓝灯模式），确认后回车继续")
                ospause()
                code = input("\n请输入你的解锁码：")
                os.system("fastboot oem unlock 0x" + code)
                ospause()
                cls_printall()
                break
            elif unlock == "2":
                print("\n注意！！Pixel设备请确认开发者选项内的OEM解锁可以正常打开（有锁机无法解锁）")
                print("tips:Pixel设备关机后长按电源键+音量下键即可进入Bootloader")
                print("\n请确认设备已进入Bootloader，确认后回车继续")
                ospause()
                os.system("fastboot flashing unlock")
                ospause()
                cls_printall()
                break
            elif unlock == "0":
                cls_printall()
                break
            else:
                print_error()
    elif inn == "5":
        os.system("cls")
        device_content = "\n请先重启进入Fastboot模式（可在主菜单第一项内重启）\n如果显示 < waiting for any device >，请检查驱动程序\n请选择你的设备：\n\n1.Pixel 3\n2.Pixel 3XL\n3.Pixel 3a\n4.Pixel 3aXL\n5.Pixel 4\n6.Pixel 4XL\n7.Pixel 4a\n8.手动刷入\n\n0.返回上一级"
        img_url = "http://one.marvl05.site:88/Pixel_PatchImage/Beta3/"
        print("\n！！！这里的面具修补包仅限Android 12 Beta 2/3 版本刷入！！！\n！！！                其他版本不得靠近                ！！！")
        print(device_content)
        def download_img(img_filename):         #下载patch.img并询问是否刷入 函数
            wget.download(img_url + img_filename, img_filename)
            ask = input("\nboot文件下载完成，确认刷入吗（Y/n）：")
            if ask == "Y" or ask == "y":
                os.system("fastboot flash boot " + img_filename)
                os.system("fastboot reboot")
                ospause()
                os.system("del " + img_filename)
                os.system("cls")
                print(device_content)
            elif ask == "N" or ask == "n":
                os.system("cls")
                print(device_content)
        while True:
            while True:
                device = input("\n输入你的选项：")
                if device == "1":
                    download_img(img_filename="3.img")
                elif device == "2":
                    download_img(img_filename="3xl.img")
                elif device == "3":
                    download_img(img_filename="3a.img")
                elif device == "4":
                    download_img(img_filename="3axl.img")
                elif device == "5":
                    download_img(img_filename="4.img")
                elif device == "6":
                    download_img(img_filename="4xl.img")
                elif device == "7":
                    download_img(img_filename="4a.img")
                elif device == "8":
                    os.system("cls")
                    manual = input("手动刷入需要将文件名改为patch.img并放入工具箱目录内，确认已完成？（Y/n）")
                    if manual == "Y" or manual == "y":
                        os.system("fastboot flash boot patch.img")
                        os.system("fastboot reboot")
                        ospause()
                        cls_printall()
                    elif manual == "n" or manual == "N":
                        os.system("cls")
                        print(device_content)
                elif device == "0":
                    cls_printall()
                    break
                else:
                    print_error()
            break
    elif inn == "6":
        web_open(weburl="http://marvl05.site:88/jaz6")  #打开酷安个人主页
        cls_printall()
    elif inn == "7":
        web_open(weburl="https://github.com/MarvL05/Flashtool_By_MarvL05/")   #打开Github项目
        cls_printall()
    elif inn == "8":
        web_open(weburl="http://wpa.qq.com/msgrd?v=3&uin=2627599936&site=qq&menu=yes")   #添加作者QQ
        cls_printall()
    elif inn == "0":
        exit()
    else:
        print_error()
