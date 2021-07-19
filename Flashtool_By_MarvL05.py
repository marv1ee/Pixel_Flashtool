#coding:utf-8


import os
import wget
import webbrowser


print("┏━━━┳┓╋╋╋╋╋╋┏┓╋┏━━━━┓╋╋╋╋╋┏┓\n┃┏━━┫┃╋╋╋╋╋╋┃┃╋┃┏┓┏┓┃╋╋╋╋╋┃┃\n┃┗━━┫┃┏━━┳━━┫┗━╋┛┃┃┗╋━━┳━━┫┃\n┃┏━━┫┃┃┏┓┃━━┫┏┓┃╋┃┃╋┃┏┓┃┏┓┃┃\n┃┃╋╋┃┗┫┏┓┣━━┃┃┃┃╋┃┃╋┃┗┛┃┗┛┃┗┓\n┗┛╋╋┗━┻┛┗┻━━┻┛┗┛╋┗┛╋┗━━┻━━┻━┛\n┏━━┓╋╋╋╋╋┏━┓┏━┓╋╋╋╋╋╋╋┏┓╋╋┏━━━┳━━━┓\n┃┏┓┃╋╋╋╋╋┃┃┗┛┃┃╋╋╋╋╋╋╋┃┃╋╋┃┏━┓┃┏━━┛\n┃┗┛┗┳┓╋┏┓┃┏┓┏┓┣━━┳━┳┓┏┫┃╋╋┃┃┃┃┃┗━━┓\n┃┏━┓┃┃╋┃┃┃┃┃┃┃┃┏┓┃┏┫┗┛┃┃╋┏┫┃┃┃┣━━┓┃\n┃┗━┛┃┗━┛┃┃┃┃┃┃┃┏┓┃┃┗┓┏┫┗━┛┃┗━┛┣━━┛┃\n┗━━━┻━┓┏┛┗┛┗┛┗┻┛┗┻┛╋┗┛┗━━━┻━━━┻━━━┛\n╋╋╋╋┏━┛┃\n╋╋╋╋┗━━┛\n")

print("欢迎使用酷安@铭灏MarvL05制作的自动化解锁+刷机工具，该软件专为小白设计，\n如大佬们有什么意见可以到Github提issue 项目名:Flashtool_By_MarvL05\n该软件目前支持Sony和Pixel的部分设备，如未适配还请谅解\n（毕竟作者是个高二狗\n")

content = "====================\n=======主菜单=======\n====================\n1.安装Android驱动\n2.解锁BootLoader\n3.刷入全量包\n4.刷入面具Patch.img\n5.Github项目传送门"
print(content)

while True:

    inn = input("\n输入你的选项：")

    if inn == "1":
        while True:
            print("\nEmmmm，我能力有限，请自行进入Android_Driver文件夹右击android_winusb.inf安装\n↓如果安装后发现fastboot不生效请参考此教程↓")
            tip = input("是否打开教程？（Y/n）：")
            if tip == "y" or tip == "Y":
                webbrowser.open("https://www.coolapk.com/feed/28517160?shareKey=MjI2ZTc5MTQwZDA5NjBmNTJmMDY~&shareUid=1925252&shareFrom=com.coolapk.market_11.2.6.1", new=0, autoraise=True)
                print(content)
                break
            elif tip == "n" or tip == "N":
                print(content)
                break
            else:
                print("输入错误！请重新输入")
    elif inn == "2":
        print("注意！!请确认驱动已经安装正确且开发者选项中‘OEM解锁’已开启")
        print("1.Sony设备\n2.Pixel设备")
        while True:
            unlock = int(input("输入你的选项："))
            if unlock == 1:
                print("注意！！Sony设备解锁需要Bootloader unlock allowed显示Yes，否则无法解锁\n如果显示<waiting for any device>请检查驱动程序")
                print("请确认设备已进入Fastboot(蓝灯模式)，确认后回车继续")
                os.system("pause")
                code = input("请输入你的解锁码：")
                os.system("fastboot oem unlock 0x" + code)
            elif unlock == 2:
                print("请确认设备已进入Bootloader，确认后回车继续")
                os.system("pause")
                os.system("fastboot flashing unlock")
            else:
                print("奇怪的数字")
    elif inn == "3":
        print("你输入了3")
    elif inn == "4":
        print("你输入了4")
    elif inn == "5":
        webbrowser.open("")
    else:
        print("达咩！请重新输入！")

