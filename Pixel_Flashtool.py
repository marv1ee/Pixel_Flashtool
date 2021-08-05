# coding:utf-8


import os
from tkinter import *
from tkinter.filedialog import askopenfilename
import wget
import webbrowser
import time

title1 = "╭━━━┳━━┳━╮╭━┳━━━┳╮╱╱╱╭━━━┳╮╱╱╱╱╱╱╭╮╭━━━━╮╱╱╱╱╭╮\n" \
         "┃╭━╮┣┫┣┻╮╰╯╭┫╭━━┫┃╱╱╱┃╭━━┫┃╱╱╱╱╱╱┃┃┃╭╮╭╮┃╱╱╱╱┃┃\n" \
         "┃╰━╯┃┃┃╱╰╮╭╯┃╰━━┫┃╱╱╱┃╰━━┫┃╭━━┳━━┫╰┻┫┃┃┣┻━┳━━┫┃\n" \
         "┃╭━━╯┃┃╱╭╯╰╮┃╭━━┫┃╱╭╮┃╭━━┫┃┃╭╮┃━━┫╭╮┃┃┃┃╭╮┃╭╮┃┃\n" \
         "┃┃╱╱╭┫┣┳╯╭╮╰┫╰━━┫╰━╯┃┃┃╱╱┃╰┫╭╮┣━━┃┃┃┃┃┃┃╰╯┃╰╯┃╰╮\n" \
         "╰╯╱╱╰━━┻━╯╰━┻━━━┻━━━╯╰╯╱╱╰━┻╯╰┻━━┻╯╰╯╰╯╰━━┻━━┻━╯\n\n"

title2 = "\n欢迎使用酷安@铭灏MarvL05制作的半自动化解锁+刷机工具，\n" \
         "该软件专为小白设计，大佬们看看就好\n" \
         "教程链接和部分下载链接可以输入a获取，\n" \
         "教程都有了不要屁大点事都来问作者/群主\n\n\n"

content = "================================================\n" \
          "=====================主菜单=====================\n" \
          "================================================\n" \
          "1.ADB&Fastboot基本指令      7.Github项目传送门\n" \
          "2.安装Android驱动           8.交流群传送门\n" \
          "3.解锁BootLoader            a.获取教程与下载链接\n" \
          "4.刷入第三方ROM             d.请作者喝奶茶\n" \
          "5.刷入面具Patch.img\n" \
          "6.酷安个人主页传送门\n\n\n0.退出\n"

allcontent = title1 + "\n" + title2 + "\n" + content


def cls_printall():  # 清屏 + 打印主页
    os.system("cls")
    print(allcontent)


def ospause():  # cmd暂停
    os.system("pause")


def web_open(weburl):  # 打开网页
    webbrowser.open(weburl, new=0, autoraise=True)


def print_error():  # 输入报错
    print("达咩！请重新输入！")


def file_select(filetype, endname, flash_cmd):
    root = Tk()
    root.withdraw()
    filename = askopenfilename(filetypes=[(filetype, endname)])
    while True:
        print("\n你选择的文件是：\n" + filename)
        if filetype == "Boot Image":
            select_confirm = input("\n确认/重新选择/跳过（Y/R/N）：")
        else:
            select_confirm = input("\n确认/重新选择/返回（Y/R/N）：")
        if select_confirm == "Y" or select_confirm == "y":
            os.system(flash_cmd + filename)
            ospause()
            if filetype == "Boot Image":
                print("\n现在请控制音量键+-选择，当看到Recovery Mode的时候按电源键确认"
                      "\n进入Recovery后选择Apply update-Apply from ADB，完成后回车选择ROM文件")
            break
        elif select_confirm == "R" or select_confirm == "r":
            filename = askopenfilename(filetypes=[(filetype, endname)])
            continue
        elif select_confirm == "N" or select_confirm == "n":
            break
        else:
            print_error()


def download_img(img_filename):  # 下载patch.img并询问是否刷入 函数
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


if os.path.isdir("platform-tools"):
    print("\n看起来你好像还没有设置环境变量，\n"
          "因为当前目录内存在着platform-tools文件夹\n"
          "如果你未曾设置过环境变量请输入Y，否则请输入n\n"
          "输入n将重命名目录内的platform-tools文件夹\n"
          "如不需要请自行删除\n"
          "ps:只有设置了环境变量才可正常使用本程序")
    while True:
        path = input("\n是否要设置环境变量？（Y/n）：")
        if path == "y" or path == "Y":
            os.system("md C:\Windows\platform-tools")
            os.system("xcopy platform-tools C:\Windows\platform-tools /e")
            os.system('setx /M path "%path%;C:\Windows\platform-tools\"')
            os.system("rmdir /S /Q platform-tools")
            print("成功！三秒后将关闭程序，此后打开可正常使用")
            time.sleep(3)
            exit()
        elif path == "n" or path == "N":
            os.system("rename platform-tools platform-tool")
            print("成功！三秒后将关闭程序，此后打开可正常使用")
            time.sleep(3)
            exit()
        else:
            print_error()
else:
    print(allcontent)
    while True:
        inn = input("输入你的选项：")
        if inn == "1":
            os.system("cls")
            cmd_content = "\nADB & Fastboot基本指令\n\n" \
                          "a.检测ADB设备\nb.检测Fastboot设备\n" \
                          "ADB:\n1.重启手机至系统\n2.重启手机至Fastboot\n3.重启手机至Recovery\n4.关闭手机\n" \
                          "Fastboot:\n5.重启手机至系统\n6.重启手机至Fastboot\n7.重启手机至Recovery\n8.关闭手机\n\n" \
                          "c.安装酷安\nm.安装Magisk Manager\nz.自行安装app\n\n9.自行输入命令\n0.返回上一级"
            print(cmd_content)


            def cmd_function():  # 清屏 + 打印命令目录
                os.system("cls")
                print(cmd_content)


            def cmd_input(cmdln):  # 执行指定命令
                os.system(cmdln)
                print("执行成功")
                ospause()


            while True:
                cmd = input("\n输入你的选项：")
                if cmd == "a" or cmd == "A":
                    os.system("adb devices")
                    print("如果没有显示一串字符和device，请检查驱动，反之则连接成功；\n"
                          "如果显示一串字符和unauthorized，请在手机上允许调试，若手机没有提示就点击开发者内的撤销USB调试授权")
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
                    apkin = Tk()
                    apkin.withdraw()
                    apk = askopenfilename(filetypes=[("Apk File", "*.apk")])
                    os.system("adb install " + apk)
                    print("出现success即安装成功！")
                    ospause()
                    cmd_function()
                elif cmd == "9":
                    while True:
                        cmd_in = input("输入ADB或Fastboot指令(输入exit退出)：")
                        if cmd_in == "exit" or cmd_in == "Exit" or cmd_in == "EXIT":
                            break
                        else:
                            os.system(cmd_in)
                    cmd_function()
                elif cmd == "0":
                    cls_printall()
                    break
                else:
                    print_error()
        elif inn == "2":
            os.system("cls")
            print("\nEmmmm，暂时还没有好的自动解决方案，\n"
                  "请在Android_Driver文件夹右击android_winusb.inf安装\n"
                  "↓如果安装后发现fastboot不生效请参考此教程↓")
            os.system("start Android_Driver")
            while True:
                tips = input("是否打开教程？（Y/n）：")
                if tips == "y" or tips == "Y":
                    web_open(weburl="http://marvl05.site:88/tjqn")
                    print("若图片无法加载请用手机扫描旁边的二维码浏览")
                    ospause()
                    os.system("devmgmt.msc")
                    print("\n已为你打开设备管理器\n")
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
            print("\n注意！!请确认驱动已经安装正确且开发者选项中‘OEM解锁’已开启\n"
                  "解锁Bootloader会清除用户数据，请在执行之前妥善备份\n"
                  "请先重启进入Fastboot模式（可在主菜单第一项内重启）")
            print("\n1.Sony设备\n2.Pixel设备\n\n0.返回上一级")
            while True:
                unlock = input("\n输入你的选项：")
                if unlock == "1":
                    os.system("cls")
                    print("\n注意！！Sony设备解锁需要Bootloader unlock allowed显示Yes，否则无法解锁\n"
                          "如果显示 < waiting for any device > 请检查驱动程序")
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
        elif inn == "4":
            os.system("cls")
            print("\n先更新一个手动刷入的版本（虽然预计不会更新提供下载的功能）\n"
                  "手动刷入需要接下来分别在弹出窗口中选择.img和.zip文件\n\n"
                  "！！！                       注意                        ！！！\n"
                  "！！！刷入第三方ROM首先要刷入对应安卓底层版本的官方线刷包！！！\n\n"
                  "确认完成以上操作？（Y/n）")

            while True:
                romconfirm = input("\n输入你的选项：")
                if romconfirm == "y" or romconfirm == "Y":
                    print("\n请选择设备状态：1.系统；2.Bootloader")
                    while True:
                        ph_status = input("\n输入你的选项：")
                        if ph_status == "1":
                            os.system("adb devices")
                            print("\n显示一串字符及device才能继续，否则请检查驱动和USB调试状态")
                            romagain = input("\n可以继续？（Y/n）：")
                            if romagain == "y" or romagain == "Y":
                                os.system("adb reboot bootloader")
                                print("若未进入Fastboot模式请手动进入")
                                ospause()

                                print("\n请选择第三方ROM提供的Boot.img或Recovery.img")
                                file_select(filetype="Boot Image", endname="*.img", flash_cmd="fastboot flash boot ")

                                ospause()
                                print("\n请选择第三方的OTA升级包，zip压缩包文件")
                                file_select(filetype="OTA Image", endname="*.zip", flash_cmd="adb sideload ")
                                cls_printall()
                                break
                            elif romagain == "n" or romagain == "N":
                                cls_printall()
                                break
                        elif ph_status == "2":
                            print("\n请选择第三方ROM提供的Boot.img或Recovery.img")
                            file_select(filetype="Boot Image", endname="*.img", flash_cmd="fastboot flash boot ")
                            ospause()
                            print("\n请选择第三方的OTA升级包，zip压缩包文件")
                            file_select(filetype="OTA Image", endname="*.zip", flash_cmd="adb sideload ")
                            cls_printall()
                            break
                        else:
                            print_error()
                elif romconfirm == "n" or romconfirm == "N":
                    cls_printall()
                    break
                else:
                    print_error()
                break
        elif inn == "5":
            os.system("cls")
            device_content = "\n请先重启进入Fastboot模式（可在主菜单第一项内重启）\n" \
                             "如果显示 < waiting for any device >，请检查驱动程序\n请选择你的设备：\n\n" \
                             "1.Pixel 3\n2.Pixel 3XL\n3.Pixel 3a\n4.Pixel 3aXL\n5.Pixel 4\n6.Pixel 4XL\n7.Pixel 4a\n8.手动刷入\n\n0.返回上一级"
            img_url = "http://one.marvl05.site:88/Pixel_PatchImage/"
            print("\n！！！这里的面具修补包仅限Android 12 Beta 3 版本刷入！！！\n"
                  "！！！               其他版本不得靠近               ！！！\n"
                  "！！！                推荐使用Beta 3                ！！！")
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
                        flash = Tk()
                        flash.withdraw()
                        manual = askopenfilename(filetypes=[("Boot Image", "*.img")])
                        os.system("fastboot flash boot " + manual)
                        os.system("fastboot reboot")
                        ospause()
                        cls_printall()
                        os.system("cls")
                        print(device_content)
                    elif device == "0":
                        cls_printall()
                        break
                    else:
                        print_error()
                break
        elif inn == "6":
            web_open(weburl="http://marvl05.site:88/jaz6")  # 打开酷安个人主页
            cls_printall()
        elif inn == "7":
            web_open(weburl="https://github.com/MarvL05/Flashtool_By_MarvL05/")  # 打开Github项目
            cls_printall()
        elif inn == "8":
            web_open(weburl="http://marvl05.site:88/36yx")  # 加入交流群
            cls_printall()
        elif inn == "a" or inn == "A":
            wget.download("http://one.marvl05.site:88/help/links.txt", "links.txt")
            os.system("cls")
            links = open("links.txt", "r", encoding="utf-8")
            print("\n" + links.read() + "\n")
            links.close()
            os.system("del links.txt")
            ospause()
            cls_printall()
        elif inn == "d" or inn == "D":
            web_open(weburl="http://p.marvl05.site:88/qrcode.jpg")
            cls_printall()
        elif inn == "0":
            exit()
        else:
            print_error()
