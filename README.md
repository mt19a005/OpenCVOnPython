# OpenCVOnPython
Pythonで作ったOpenCVの雑多な処理群

## OpenCV
### Bitwise
- 2画像の四則演算とBitwise４種類を実行する。  
- 入力 : 2画像  
出力 : 1画像  

### Canny
- Cannyアルゴリズムを入力画像に適用し出力する。  
- 入力 : 2画像  
出力 : 1画像  

### MOG
- MOG2を利用した動体検出(MOG.py)
- 背景差分を利用した動体検出(MOG1.py)  
- 入力 : 2画像  
出力 : 1画像

### PixelAccess
- 画像のピクセル(行列)にアクセスする。それを利用して、画像の黒い部分を取り除く  
- 入力 : 2画像  
出力 : 1画像  


### Stitching
- 画像を結合
- 画像1と画像2の位置関係はどうでも良くした。  
- 入力 : 2画像  
出力 : 1画像  

## OpenCV以外
### Heiretu
- 並列処理
- クラスを共有メモリにして、2プロセス間で共有する。
- 入力 : なし  
出力 : なし

### Msgpack
- Msgpackモジュールを利用した、ファイル間での変数の共有
- 入力 : なし  
出力 : バイナリデータが入った.msgファイル

### Threading
- 並列処理
- threadingモジュールを利用した、ファイル間での変数の共有

- 入力 : なし  
出力 : なし 

## Requirement
* Python 3.8.4
## Author
Motoharu Taguwa
