# -*- encoding:utf-8 -*-

import requests
import json
import random
import datetime
import sys,io
import pytz
week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
color = ["#27408B", "#FFA500", "#FFD700", "#00FF7F", "#FFC0CB", "#DDA0DD", "#8968CD","#90EE90"]
perlist = {
     'oFWR76FtOJRxJFW_DBzZSk6QhDGE':"LBoKBDf-nm6ur73Gmr8WJWUXGNpUbUB8orpXelVzQdQ", #ckt
     'oFWR76Hy8wfrV76FadVOwkMFZd_I':"LBoKBDf-nm6ur73Gmr8WJWUXGNpUbUB8orpXelVzQdQ", #xcj
     #"oFWR76M4vNGh62_KexeaVZIZfpEo":"B6Y0SsU0R-z42JfLyAbRq9J47-ChmRU0zFEyXivwgvk", #cms
     #"oFWR76Fq3sfhYhmN3nnHkqF5_XX0":"B6Y0SsU0R-z42JfLyAbRq9J47-ChmRU0zFEyXivwgvk", #zy
     #"oFWR76BcIHiK-NDjUgySCcdsWuJU":"B6Y0SsU0R-z42JfLyAbRq9J47-ChmRU0zFEyXivwgvk", #ljl
}


class Temp():
    def __init__(self):
        tz=pytz.timezone("Asia/Shanghai")
        nowtime = datetime.datetime.now(tz)
        nowyear = nowtime.year
        zaiyiqidays = (nowtime.date() - datetime.date(2020,8,23)).days
        nexttorday = datetime.date(year=nowyear, month=8, day=23)
        if nowtime.date() > nexttorday:
            nexttorday = datetime.date(year=nowyear + 1, month=8, day=23)
        #print(nowtime.hour)
        if nowtime.hour >= 8 and nowtime.hour <= 11:
            xiabantime = "12:00:00"
        elif nowtime.hour >= 14 and nowtime.hour <= 17:
            xiabantime = "18:00:00"
        else:
            xiabantime = 0
        #print(xiabantime)
        kkbri = datetime.date(year=nowyear, month=2, day=25)
        if nowtime.date() > kkbri:
            kkbri = datetime.date(year=nowyear + 1, month=2, day=25)
        mybri = datetime.date(year=nowyear, month=7, day=10)
        if nowtime.date() > mybri:
            mybri = datetime.date(year=nowyear + 1, month=7, day=10)
        # print(nexttorday,nowtime.strftime("%H:%M:%S"))
        self.main_temp = {
            "data": {
                "xingqi":{
                  "value":  week_list[nowtime.weekday()]+(("  周末可以休息啦"
                                                           "") if nowtime.weekday() == 5 or nowtime.weekday() == 6 else (''))
                },
                "time":{
                    "value":nowtime.strftime('%Y-%m-%d %H:%M:%S'),
                },
                "zaiyiqi":{
                    "value":(nowtime.date() - datetime.date(2020,8,23)).days,
                },
                "zaiyiqinian":{
                    "value":("距离在一起"+str(int(zaiyiqidays / 365) + 1)+"周年还有"+str((nexttorday-nowtime.date()).days)+"天噢") if (nexttorday - nowtime.date()).days!= 0 else ("今天是我们在一起的"+str(int(zaiyiqidays / 365))+"周年纪念日噢~节日快乐嘿嘿"),
                },
                "kkb":{
                    "value":('距离kk的生日还有'+str((kkbri - nowtime.date()).days)+"天")if (kkbri -nowtime.date()).days!=0 else ("！！祝kt小朋友生日快乐！！！"),
                },
                "myb":{
                    "value":('距离我的生日还有'+str((mybri - nowtime.date()).days)+"天")if (mybri -nowtime.date()).days!=0 else ("！！嘿嘿~祝我自己生日快乐！！"),
                },
                "happy":{
                    "value": "        Have a happy day!        ",
                    "color": color[random.randint(0, 7)],
                },
                #"main": {
                    #"value":
                     #"天是{}\n\n现在是{}\n今天也是想你的一天！\n\n我们在一起已经有{}天了💝\n{}\n\n{}\n\n{}\n\n今天也要开心哦!!        \n\n".format(
                     #week_list[nowtime.weekday()] + (
                       #("  周末可以休息啦🤩") if nowtime.weekday() == 5 or nowtime.weekday() == 6 else ('')),
                     #  "   今天也要好好学习噢！📚")
                     #"    寒假快乐QAQ~~"),
                     #nowtime.strftime('%Y-%m-%d %H:%M:%S'),
                     #(nowtime.date() - datetime.date(2020,8,23)).days,
                     #("距离在一起"+str(int(zaiyiqidays / 365) + 1)+"周年还有"+str((nexttorday-nowtime.date()).days)+"天噢") if (nexttorday - nowtime.date()).days!= 0 else ("今天是我们在一起的"+str(int(zaiyiqidays / 365))+"周年纪念日噢~\n🎊节日快乐嘿嘿🎉🥳"),
                     #('🎂距离kk的生日还有'+str((kkbri - nowtime.date()).days)+"天🎂")if (kkbri -nowtime.date()).days!=0 else ("🥳！！祝kt小朋友生日快乐！！！🎉"),
                     #('🎂距离我的生日还有'+str((mybri - nowtime.date()).days)+"天🎂")if (mybri -nowtime.date()).days!=0 else ("🥳！！嘿嘿~祝我自己生日快乐！！🎉"),

                     #),
                    #'color': "#000000"
                #}
                # "other": {
                #    "value": "❤        Have a happy day!        ❤",
                #    "color": color[random.randint(0, 7)],
                # }
            }
        }
        self.shunshun_temp = {
            "data": {
                "data": {
                    "value": "今天是{}\n\n现在是{}\n\n今天也要记得微哨打卡噢~\n\n{}  \n\n顺顺的小卡片在这里提示您要及时陪健健玩游戏噢😊\n\n\n".format(
                        week_list[nowtime.weekday()] + (
                            "  周末可以休息啦🤩" if nowtime.weekday() == 5 or nowtime.weekday() == 6 else "   今天也要好好学习噢！📚"),
                        nowtime.strftime('%Y-%m-%d %H:%M:%S'),
                        ("距离下班还有" + str(datetime.datetime.strptime(xiabantime, '%H:%M:%S') - datetime.datetime.strptime(nowtime.strftime("%H:%M:%S"),"%H:%M:%S")) + " ‍💻") if xiabantime != 0 and nowtime.weekday() != 5 and nowtime.weekday() != 6 else ("现在不用上班 欸嘿嘿~😍"), ),
                    'color': "#000000",
                },
                "other": {
                    "value": "❤        Have a happy day!        ❤",
                    "color": color[random.randint(0, 7)],
                }
            }
        }


class SendMessage():
    def __init__(self):
        self.appID = 'wxdb30fe05a5c5f739'
        self.appsecret = 'b7b9b92317b0019c02b05c1b4f217184'
        self.access_token = self.get_access_token()
        self.opend_ids = 0

    def get_access_token(self):
        """
        获取微信公众号的access_token值
        """
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'. \
            format(self.appID, self.appsecret)
        #print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
        }
        response = requests.get(url, headers=headers).json()
        access_token = response.get('access_token')
        #print(access_token)
        return access_token

    def get_openid(self):
        """
        获取所有粉丝的openid
        """
        next_openid = ''
        url_openid = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=%s' % (
            self.access_token, next_openid)
        ans = requests.get(url_openid)
        #print(ans.content)
        open_ids = json.loads(ans.content)['data']['openid']
        #print(open_ids)
        return open_ids

    def sendmsg(self, msg):
        """
        给所有粉丝发送文本消息
        """
        # self.access_token='T22HbpGDHxBv_U_uk5pmnqT14qWT_t-JKol-2rMNfh8'
        # url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}".format(self.access_token)
        url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(self.access_token)
        print(url)
        self.opend_ids = self.get_openid()
        if self.opend_ids != '':
            for open_id in perlist:
                if open_id == 'oFWR76M4vNGh62_KexeaVZIZfpEo':
                    body = {
                        "touser": open_id,
                        "msgtype": "text",
                        "text":
                            {
                                "content": msg
                            }
                    }
                    data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
                    print(data)
                    response = requests.post(url, data=data)
                    # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
                    result = response.json()
                    print(result)
        else:
            print("当前没有用户关注该公众号！")

    def sendtemp(self, tempid=""):
        """
        给所有粉丝发送文本消息
        """
        # self.access_token='T22HbpGDHxBv_U_uk5pmnqT14qWT_t-JKol-2rMNfh8'
        # url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}".format(self.access_token)
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(self.access_token)
        myTemp = Temp()
        #print(url)
        # print(self.opend_ids)
        for open_id in perlist.keys():
            template = {
                "touser": open_id,
                "template_id": perlist[open_id],
            }
            if perlist[open_id] == 'LBoKBDf-nm6ur73Gmr8WJWUXGNpUbUB8orpXelVzQdQ':
                template.update(myTemp.main_temp)
            #else:
            #    template.update(myTemp.shunshun_temp)
            data = bytes(json.dumps(template).encode('utf-8'))
            #print(data)
            #print(data)
            response = requests.post(url,data=data)
            # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
            result = response.json()
            #print(result)
            #template = {
            #    "touser": "oFWR76Hy8wfrV76FadVOwkMFZd_I",
            #    "template_id": "B6Y0SsU0R-z42JfLyAbRq9J47-ChmRU0zFEyXivwgvk",
            #}
            #template.update(myTemp.shunshun_temp)
            #print(template)
            #data = bytes(json.dumps(template, ensure_ascii=False).encode('utf-8'))
            #print(data)
            #response = requests.post(url, data=data)
            # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
            #result = response.json()
            #print(result)

    def upload_media(self, media_type, media_path):
        """
        上传临时文件到微信服务器，并获取该文件到meida_id
        """
        url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token={}&type={}'.format(self.access_token,
                                                                                              media_type)
        print(url)
        meida = {
            'media': open(media_path, 'rb')
        }
        rsponse = requests.post(url, files=meida)
        parse_json = json.loads(rsponse.content.decode())
        print(parse_json)
        return parse_json.get('media_id')

    def send_media_to_user(self, media_type, media_path):
        """
        给所有粉丝发送媒体文件，媒体文件以meida_id表示
        """
        media_id = self.upload_media(media_type, media_path)
        url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(self.access_token)
        self.opend_ids=perlist.keys()
        if self.opend_ids != '':
            for open_id in self.opend_ids:
                if media_type == "image":
                    body = {
                        "touser": open_id,
                        "msgtype": "image",
                        "image":
                            {
                                "media_id": media_id
                            }
                    }
                if media_type == "voice":
                    body = {
                        "touser": open_id,
                        "msgtype": "voice",
                        "voice":
                            {
                                "media_id": media_id
                            }
                    }
                data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
                print(data)
                response = requests.post(url, data=data)
                # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
                result = response.json()
                print(result)
        else:
            print("当前没有用户关注该公众号！")

    def getbuttom(self):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={}'.format(self.access_token)
        pack = {
            "button": [
                {
                    "name":"菜单1",
                    "sub_button":[
                        {
                            "type": "view",
                            "name": "场库",
                            "url": "https://www.xinpianchang.com/channel?vmovier=1"
                        },
                        {
                            "type": "view",
                            "name": "Creative Mass",
                            "url": "https://creativemass.cn/#/"
                        },
                        {
                            "type": "view",
                            "name": "沙画",
                            "url": "https://thisissand.com/"
                        },
                        {
                            "type": "view",
                            "name": "人生重开模拟器（new）",
                            "url": "https://liferestart.syaro.io/ "
                        },
                        {
                            "type": "view",
                            "name": "公共交通辐射图",
                            "url": "https://bus.daibor.com/#/"
                        }
                    ]
                },
                {
                    "name": "菜单2",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "万能网站",
                            "url": "https://www.baidu.com/"
                        },
                        {
                            "type": "view",
                            "name": "狗屁不通文章生成器",
                            "url": "https://suulnnka.github.io/BullshitGenerator/index.html"
                        },
                        {
                            "type": "view",
                            "name": "中午吃什么",
                            "url": "http://chishenme.xyz/"
                        },
                        {
                            "type": "view",
                            "name": "解压小网站",
                            "url": "http://fff.cmiscm.com/#!/main"
                        },
                        {
                            "type": "view",
                            "name": "线条骑士",
                            "url": "https://www.linerider.com/"
                        },

                    ]
                }]
        }
        data = bytes(json.dumps(pack, ensure_ascii=False).encode('utf-8'))
        print(data)
        response = requests.post(url, data=data)
        # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
        result = response.json()
        print(result)
if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    sends = SendMessage()
    #sends.getbuttom()
    sends.sendtemp("")
    #sends.send_media_to_user("image", './test.jpg')
