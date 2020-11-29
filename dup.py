"""
Author: xiejiahe
Repo: https://github.com/xjh22222228/dup
Version: v1.2.0
"""

import os
import sys
import time

from colorama import init
from fire import Fire
from tqdm import tqdm

start_timestamp = time.time()
# 已过滤后的文本
text_content_map = {}
# 重复文本
dup_text_list = []
dup_text_file_path = os.path.abspath('重复文本.txt')


# 删除文件
def remove_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError as e:
        pass


def parse_command(filein='./example.txt', fileout='./out.txt'):
    if not filein:
        sys.exit(0)

    abspath_filein = os.path.abspath(filein)
    abspath_fileout = os.path.abspath(fileout)

    print('Reading ' + abspath_filein + '\n')

    # Remove out.txt
    remove_file(abspath_fileout)
    remove_file(dup_text_file_path)

    with open(abspath_filein, encoding='utf-8') as filein_obj:
        if not filein_obj.readable():
            print('无权限读取')
            sys.exit(0)

        lines = filein_obj.readlines()
        before_total = len(lines)

        with tqdm() as pbar:
            for text in lines:
                pbar.update(1)
                if text != '':
                    if text_content_map.get(text):
                        dup_text_list.append(text)

                    text_content_map[text] = 1

    # 过滤后的文本写进 out.txt
    with open(abspath_fileout, 'a') as fileout_obj:
        # 不可写
        if not fileout_obj.writable():
            print('当前文件无法写入:' + abspath_fileout)
            sys.exit(0)

        with tqdm() as pbar:
            for text in text_content_map.keys():
                pbar.update(1)
                fileout_obj.write(text)

    after_total = len(text_content_map.keys())
    end_timestamp = time.time()

    print('原文本共: {} 行, 过滤后: {} 行'.format(before_total, after_total))
    print('总共重复: {} 行'.format(before_total - after_total))
    print('消耗时间: {} s'.format(round(end_timestamp - start_timestamp, 5)))


if __name__ == '__main__':
    init()
    Fire(parse_command)

    if len(dup_text_list) != 0:
        with open(dup_text_file_path, 'a') as file:
            file.writelines(dup_text_list)
            print('重复文本已写入 ' + dup_text_file_path)
