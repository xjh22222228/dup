"""
Author: xiejiahe
Repo: https://github.com/xjh22222228/dup
Version: v1.1.0
"""

import os
import sys
import time

from colorama import init, Fore
from fire import Fire

lineMap = {}
start_timestamp = time.time()


def parse_command(filein='./example.txt', fileout='./out.txt'):
    if not filein:
        sys.exit(0)

    abspath_filein = os.path.abspath(filein)
    abspath_fileout = os.path.abspath(fileout)

    try:
        os.remove(abspath_fileout)
    except FileNotFoundError as e:
        pass

    with open(abspath_filein, encoding='utf-8') as filein_obj:
        if not filein_obj.readable():
            print('当前文件无权限读取')
            sys.exit(0)

        lines = filein_obj.readlines()
        before_total = len(lines)
        for lineVal in lines:
            if lineVal != '':
                lineMap[lineVal] = True

    with open(abspath_fileout, 'a') as fileout_obj:
        if not fileout_obj.writable():
            print('当前文件无法写入:' + abspath_fileout)
            sys.exit(0)

        for lineVal in lineMap.keys():
            fileout_obj.write(lineVal)

    after_total = len(lineMap.keys())
    end_timestamp = time.time()

    print('Before Line: {}, After Line: {}'.format(before_total, after_total))
    print('Total: {} duplicates'.format(before_total - after_total))
    print(Fore.GREEN + 'Time: {} s'.format(round(end_timestamp - start_timestamp, 5)))


if __name__ == '__main__':
    init()
    Fire(parse_command)
