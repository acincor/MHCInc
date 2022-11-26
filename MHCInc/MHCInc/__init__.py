import subprocess
import requests
import os
from lxml import etree
from bs4 import BeautifulSoup
if not os.path.exists("MHCInc"):
        os.mkdir("MHCInc")
path1 = "MHCInc/200bpm%E6%AD%BB%E4%BA%A1%E4%B9%8B%E6%9B%B2 2.flac"
path2 = "MHCInc/8bq.png"
if not os.path.exists(path1):
        url = "https://wx.mail.qq.com/ftn/download?func=3&key=9d9ce332085a5ef6afef4f3235663735be2bd73237663735474c54530605550756564c5400005318560050571a040507014e0251530705045555550b5304063550535150470b12705446207612247510275744707643760447265517755f120d20462404125f75102051410019005b5401776f9efe5f9b05326c47ff309e0fc683d8c088dbe2&code=bca27f75&k=9d9ce332085a5ef6afef4f3235663735be2bd73237663735474c54530605550756564c5400005318560050571a040507014e0251530705045555550b5304063550535150470b12705446207612247510275744707643760447265517755f120d20462404125f75102051410019005b5401776f9efe5f9b05326c47ff309e0fc683d8c088dbe2&fweb=1&cl=1"
        request = requests.get(url)
        #print(request.content.decode("utf-8"))
        html0 = etree.HTML(request.content.decode("utf-8"))
        block = html0.xpath("//*[@nonce]")[5].xpath("text()")[0].split(" = ")[9].split("\"")[1]
        with open(path1,"wb") as f:
                f.write(requests.get(block).content)

if not os.path.exists(path2):
        url = "https://wx.mail.qq.com/ftn/download?func=3&key=cbce6d375b080bfaf9bd1b3766346239a7f9203764346239111e505652015100045018565055501400540600490c03000c1c02025500575c55020052575165390c534419145a052df0f09f5c32b2183db56a152f367f46f7bda82f8e&code=4157d4b9&k=cbce6d375b080bfaf9bd1b3766346239a7f9203764346239111e505652015100045018565055501400540600490c03000c1c02025500575c55020052575165390c534419145a052df0f09f5c32b2183db56a152f367f46f7bda82f8e&fweb=1&cl=1"
        request = requests.get(url)
        #print(request.content.decode("utf-8"))
        html0 = etree.HTML(request.content.decode("utf-8"))
        block = html0.xpath("//*[@nonce]")[5].xpath("text()")[0].split(" = ")[9].split("\"")[1]
        with open(path2,"wb") as f:
                f.write(requests.get(block).content)
class module:
    def main():
        from MHCInc import copyright
        copyright.copyright_Swift()
    def caterpillar():
        from MHCInc import caterpillar
    def 单词九连猜():
        from MHCInc import 单词九连猜
    def nineWordGuessing():
        from MHCInc import 单词九连猜
    def 加密消息():
        from MHCInc import 加密消息
    def secretMessage():
        from MHCInc import 加密消息
    def snap():
        from MHCInc import 快照抓拍
    def 快照抓拍():
        from MHCInc import 快照抓拍
    def 螺旋万花筒():
        from MHCInc import 螺旋万花筒
    def spiralKaleidoscope():
        from MHCInc import 螺旋万花筒
    def 星光夜空():
        from MHCInc import 星光夜空
    def starlightNight():
        from MHCInc import 星光夜空
    def 圆筒万花筒():
        from MHCInc import 圆筒万花筒
    def cylinderKaleidoscope():
        from MHCInc import 圆筒万花筒
    def animal_guess():
        from MHCInc import animal_guess
    def caterpillar2():
        from MHCInc import caterpillar2
    def copyright():
        from MHCInc import copyright
    def eggCatcherPerfect():
        from MHCInc import egg_catcher_perfect
    def eggCatcher():
        from MHCInc import egg_catcher
    def GuessGame():
        from MHCInc import GuessGame
    def GuessGameEasy():
        from MHCInc import GuessGameEasy
    def GuessGameSecondary():
        from MHCInc import GuessGameSecondary
    def matchmaker():
        from MHCInc import matchmaker
    def MITLicense():
        from MHCInc import MITLicense
    def PHYSICAL_CONDITION_APPLET():
        from MHCInc import PHYSICAL_CONDITION_APPLET
    def Python3学习示例():
        from MHCInc import Python3学习示例
    from MHCInc import random
    def rectangle():
        from MHCInc import rectangle
    def robotBuilder():
        from MHCInc import robot_builder
    def screenPet():
        from MHCInc import screen_pet
    from MHCInc import swift

