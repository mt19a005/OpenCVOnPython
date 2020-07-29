# -*- coding: utf-8 -*-

import os
from PIL import Image
import shutil

# 変換対象ファイルを格納したディレクトリ
gifDir = 'yalefaces'
# 変換対象ファイルの拡張子
gifExt = 'gif'
# 変換後のファイルを格納するディレクトリ
pngDir = 'Png'
# 変換後のファイルの拡張子
pngExt = 'png'

# ディレクトリを作成
os.mkdir(pngDir)

# 「.」と拡張子を合わせた文字列長
gifExtLen = len(gifExt) + 1

for dirame, dirNames, fileNames in os.walk(gifDir):
    for fileName in fileNames:
        # 変換対象ファイルのパス
        gifPath = gifDir + '/' + fileName

        # 返還後のファイルパス
        if len(fileName) > gifExtLen and \
            fileName[-gifExtLen:] == '.' + gifExt:
            fileName = fileName[0:-gifExtLen]
        pngPath = pngDir + '/' + fileName + '.' + pngExt

        try:
            # 変換実行
            Image.open(gifPath).save(pngPath)
        except IOError:
            print('cannot convert :', gifPath)