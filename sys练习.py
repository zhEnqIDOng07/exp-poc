# import sys
# print(sys.argv) # 通过命令行传入参数，参数间用空格间隔，传入参数用列表收集，列表第一个索引是该文件位置
#
# def main(url,cmd):
#     print(f'正在对{url}网站执行{cmd}命令')
#     print("命令执行完成，命令回显：root")
# if __name__ == '__main__':
#     banner = '''welcome use cve-2012-2222-rce
# 使用方法:python3 cve-2012-2222-rce.py
# http://www.mhx.com id\n'''
#     print(banner)
#     if len(sys.argv) == 3:
#         url = sys.argv[1]
#         cmd = sys.argv[2]
#         main(url,cmd)
#     else:
#         print("输入参数有误，请按照提示输入")

