import re
import os
import json_tools
import requests


ppssj = 'https://ppssj.xdf.cn'
onepiece = ''
wxbackend = 'https://wxbackend.xdf.cn'
read_chunk = 1024 * 1024
access_log = 'access.log'


# def log_parse(file):
#     with open(file) as f:
#         lines = f.readlines()
#         pattern = re.compile(r".*GET\s(.*?)\s.*")
#         for line in lines:
#             line = line.strip('\n')
#             print(line)
#             matched = pattern.match(line)
#             if matched:
#                 print(matched.group(1))

def log_parse(file):
    with open(file) as f:
        logs = f.read()
        pattern = re.compile(r"GET\s(.*?)\s")
        urls = re.findall(pattern, logs)
        return urls


def get_json(url):
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'}
    return requests.get(url, headers=headers).json()


def get_diffs(ppssj, onepiece):
    diffs = []
    for key, value in ppssj.items():
        if key in onepiece:



    return


def diff(urls):
    for url in urls:
        try:
            ppssj_res = get_json(ppssj + url)
            onepiece_res = get_json((wxbackend + url))
            result = json_tools.diff(ppssj_res, onepiece_res)
        except:
            pass
    print(result)


a = {"a":1, "b":2, "c": 3}
b = {"a":2, "b":1}

def main():
    urls = log_parse(access_log)
    diff(urls)
    # diff(urls)

# main()
print(get_noise(a, b))