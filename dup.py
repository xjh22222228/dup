from fire import Fire
import sys
import os

lineMap = {}


def parse_command(filein='./example.txt', fileout='./out.txt'):
    if not filein:
        sys.exit(0)

    abspath_filein = os.path.abspath(filein)
    abspath_fileout = os.path.abspath(fileout)

    try:
        os.remove(abspath_fileout)
    except FileNotFoundError as e:
        pass

    with open(abspath_filein) as filein_obj:
        if not filein_obj.readable():
            print('当前文件无权限读取')
            sys.exit(0)

        for lineVal in filein_obj.readlines():
            if lineVal != '':
                lineMap[lineVal] = True

    with open(abspath_fileout, 'a') as fileout_obj:
        if not fileout_obj.writable():
            print('当前文件无法写入:' + abspath_fileout)
            sys.exit(0)

        for lineVal in lineMap.keys():
            print(fileout_obj.write(lineVal))


if __name__ == '__main__':
    Fire(parse_command)
