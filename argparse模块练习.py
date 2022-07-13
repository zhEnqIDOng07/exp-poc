import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()
# print(args.echo)

# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print(args.echo)

# parser = argparse.ArgumentParser(description='这是个脚本文件')
#
# parser.parse_args()

# 位置参数
# parser = argparse.ArgumentParser(description='这是个脚本文件')
# parser.add_argument('url')
# args = parser.parse_args()
# print(args.url)

# parser = argparse.ArgumentParser(description='这是个脚本文件')
# parser.add_argument("url", help="input a url",type=str)
# args = parser.parse_args()
# print(args.url)

# 可选参数
# parser = argparse.ArgumentParser()
# parser.add_argument('--url',help='input url')
# args = parser.parse_args()
# print(args.url)

# 短选项
# parser = argparse.ArgumentParser()
# parser.add_argument('-u','--url',help='input the url')
# args = parser.parse_args()
# print(args.url)

# 设置dest关键字
# parser = argparse.ArgumentParser('1')
# parser.add_argument('-u','--url',dest='URL',type=str,default=1,help='input the url',action='store')
# args = parser.parse_args()
#
# print(args.URL)

# 小模版
# import argparse
# import textwrap
#
#
# def main(url, cmd):
#     # 简易模仿代码
#     """真正具体对指定url执行命令的代码"""
#     print(f"正在对{url} 网站执行{cmd} 这条系统命令")
#     print("命令执行完成,命令的回显: root")
#
#
# if __name__ == '__main__':
#     banner = """
#  _   _     _       _          _          ____
# | |_| |__ (_)_ __ | | ___ __ | |__  _ __| ___|   _ __ ___ ___
# | __| '_ \| | '_ \| |/ / '_ \| '_ \| '_ \___ \  | '__/ __/ _ \\
# | |_| | | | | | | |   <| |_) | | | | |_) |__) | | | | (_|  __/
#  \__|_| |_|_|_| |_|_|\_\ .__/|_| |_| .__/____/  |_|  \___\___|
#                        |_|         |_|
# """
#     print(banner)
#     parser = argparse.ArgumentParser(description='thinkphp5 rce exp', formatter_class=argparse.RawDescriptionHelpFormatter,
#                                      epilog=textwrap.dedent('''example:
#         cve-2022-4334-rce.py -u http://192.168.1.108 -c id
#         '''))
#     parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.mhx.com")
#     parser.add_argument("-c", "--cmd", dest="cmd", type=str, default="whoami", help="default=whoami example: id")
#     args = parser.parse_args()
#
#     main(args.url, args.cmd)


# parser = argparse.ArgumentParser(description="CVE--2022-26134",
#                                 formatter_class=argparse.RawDescriptionHelpFormatter,
#                                 )
# parser.add_argument('file', type=argparse.FileType(mode='r',encoding='u8'))
# args = parser.parse_args()
#
# with args.file as file:
#     res = file.readlines()
#     for i in res:
#         print(i)

