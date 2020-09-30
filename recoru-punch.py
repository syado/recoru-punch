import requests

class RecoRu:
    def __init__(self,):
        self.headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        }
        self.session = requests.session()

    def login(self,contractId,authId,password):
        res = self.session.get("https://app.recoru.in/ap/logout")
        # print(res.status_code)
        self.login_info = {
            "title":"ログイン",
            "tmpServletPathAndParams":None,
            "contractId":contractId,
            "authId":authId,
            "password":password,
            "idSaveChecked":True,
            "_idSaveChecked":"on"
        }
        res = self.session.post("https://app.recoru.in/ap/login", data=self.login_info,headers=self.headers,allow_redirects=False)
        # print(res.status_code)
        # print(session.cookies)
        return res
    def punch(self,punchButtonId:str,memo:str):
        """punchButtonId 1:出勤 2:退勤"""
        data = {
            "punchButtonId": punchButtonId,
            "punchMemo": memo,
            "searchedVersionNo": "1"
        }
        res = self.session.post("https://app.recoru.in/ap/home/doPunch",json=data,headers=self.headers)
        # print(res.status_code)
        # print(session.cookies)
        return res


    def in_(self,memo=""):
        """出勤"""
        return self.punch(punchButtonId="1",memo=memo)

    def out_(self,memo=""):
        """退勤"""
        return self.punch(punchButtonId="2",memo=memo)

if __name__ == "__main__":
    import sys
    arg=sys.argv[1:]
    contractId="0000000" #契約ID
    authId="id or mail" #IDまたはメールアドレス
    password="xxxxxxxxx" #パスワード
    rec=RecoRu()
    rec.login(contractId,authId,password)
    if len(arg) >= 2:
        memo = " ".join(arg[1:])
    else:
        memo = ""
    if arg[0] == "in":
        rec.in_(memo=memo) #出勤
    elif arg[0] == "out":
        rec.out_(memo=memo) #退勤