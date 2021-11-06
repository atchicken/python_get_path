import os
import pathlib

from glob import glob

def main():
    
    # path.pyにおける絶対パスを取得
    path = os.path.abspath(__file__)
    print("Absolute Path: {}".format(path))
    
    # [0]: ディレクトリ, [1]: ファイル
    path = os.path.split(__file__)
    print("Directry: {}, FileName: {}".format(path[0], path[1]))
    
    # ディレクトリ名取得
    dire = os.path.dirname(__file__)
    print("Directry: {}".format(dire))
    
    # ファイル名取得
    fname = os.path.basename(__file__)
    print("FileName: {}".format(fname))

    
    print("===================")

    
    # 相対パス -> 絶対パス
    absPath = pathlib.Path("./path.py").resolve()
    print("Absolute Path: {}".format(absPath))

    
    # 絶対パス -> 相対パス
    relPath = pathlib.Path(__file__).relative_to(os.getcwd())
    print("Relative Path: {}".format(relPath))

    print("===================")
    
    files = glob("test/*.py")
    for f in files:
        print("File: {}".format(f))
    print("-------------------")
    
    for f in sorted(files):
        print("File: {}".format(f))
    
    return


if __name__ == "__main__":
    main()
