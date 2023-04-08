''' 郭、王两位大侠同上终南山习武，两人最初的战力值均为100。
王大侠骨骼清奇，天赋较高，每练功一天，战力增加2‰，
郭大侠比较愚笨，每练功一天，战力增加1‰。
如果休假一天不练，两人的战力均减少1‰。
相较于王大侠，郭大侠更加勤奋，日日练功，从不休息，
而王大侠，则三天打渔，两天晒网，也就是每5天的前三天练功，后两天休假。
那么，10年（3650天）之后，郭大侠和王大侠战力分别是多少？并绘出两人的战力增长曲线。
'''
guoPowers = []    #天天练的郭大侠战力列表，开始为空列表
wangPowers = []   #三天打渔、两天晒网的王大侠

guoPower,wangPower = 100,100 # 给两人功力赋初值

for x in range(365*10): # for循环，逐天计算两位大侠的新战力，并置入各自的战力列表
    guoPower *= 1.001   # guoPower = guoPower * 1.001
    if x % 5 in [0,1,2]: #判断第x天是王大侠的打渔日还是晒网日
        wangPower *= 1.002  # 三天打渔
    else:
        wangPower *= 0.999  # 两天晒网
    # 把当天的战力添加到战力列表尾部
    guoPowers.append(guoPower) 
    wangPowers.append(wangPower)

print(guoPower,wangPower)

# 用matplotlib模块画图
from asyncio.windows_utils import pipe
import collections
from gc import collect
from gettext import install
import pipes
from matplotlib import pyplot as plt
plt.plot(list(range(365*10)),guoPowers,label="Master GUO")
plt.plot(list(range(365*10)),wangPowers,label="Master WANG")
plt.legend()  # 图例
plt.show()    # 显示
