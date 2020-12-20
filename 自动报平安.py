import requests
from bs4 import BeautifulSoup

# ****************登录*******************

# 自己的账号密码
# key为推送消息的
users = eval(os.environ['users'])
# '49bdb9375842537a41ebc635a09229b2'
logUrl = "http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do"
[['2019112404', '285017', '49bdb9375842537a41ebc635a09229b2']]


def sentMsg(msg, key):
    if key == null
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://qmsg.zendee.cn/send/"+key+"?msg=" + msg
    return requests.post(api_url, headers=headers).content


for username, pas, key in users:
    # start_new_thread(report,(usr,pas,))
    sentOne(username, password, key)
    # print(log[-1][-1])


def sentOne(username, password, key):
    header = {
        # origin:http://yiqing.ctgu.edu.cn
        # "Content-Type": "application/json;charset=UTF-8",
        'Referer': "http://yiqing.ctgu.edu.cn/wx/index/login.do?currSchool=ctgu&CURRENT_YEAR=2019",
        # 模仿谷歌浏览器的登录
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    yiqingSession = requests.session()

    postData = {
        "username": username,
        "password": password
    }

    responseRes = yiqingSession.post(logUrl, data=postData, headers=header)

    # *******从提交页面获取 表单信息**********

    # 构建表单（默认身体健康)
    postData = {
        "ttoken":  '',
        "province":  "",
        "city":      "",
        "district":  "",
        "adcode":    "",
        "longitude": "0",
        "latitude":  "0",
        "sfqz": "否",
        "sfys": "否",
        "sfzy": "否",
        "sfgl": "否",
        "status": "1",
        "sfgr": "否",
        "szdz": "",
        "sjh": "",
        "lxrxm": '',
        "lxrsjh": '',
        "sffr": "否",
        "sffy": "否",
        "sfgr": "否",
        "qzglsj": '',
        "qzgldd": '',
        "glyy": '',
        "mqzz": '',
        "sffx": "否",
        "qt": "",
    }

    getFormurl = "http://yiqing.ctgu.edu.cn/wx/health/toApply.do"
    responseRes = yiqingSession.get(getFormurl, timeout=None)

    # 获取必要信息填入表单
    soup = BeautifulSoup(responseRes.text, "html.parser")
    getFormlist = soup.find_all('input')[0:15]

    for Formdata in getFormlist:
        postData[Formdata.attrs['name']] = Formdata.attrs['value']

    # *************提交最终表单***********

    postFormurl = "http://yiqing.ctgu.edu.cn/wx/health/saveApply.do"

    header['Referer'] = "http://yiqing.ctgu.edu.cn/wx/health/toApply.do"

    responseRes = yiqingSession.post(
        postFormurl, data=postData, headers=header, timeout=None)

    print(responseRes.text)
    sentMsg(responseRes.text, key)
