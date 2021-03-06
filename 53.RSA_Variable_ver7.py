"""
参考文献
import系　https://qiita.com/mriho/items/52f53559ba7fe7ef06ff
公開鍵暗号系　https://qiita.com/kunichiko/items/ef5efdb41611d6cf7775#%E7%94%A8%E8%AA%9E
リポジトリの作成系　https://docs.github.com/ja/github/getting-started-with-github/quickstart/create-a-repo
asc2 コード　https://www.k-cube.co.jp/wakaba/server/ascii_code.html
gcdex http://ictsr4.com/sw/gcdex/

概要
    RSA暗号をpythonで作ってみよう。
    
必要なモジュール・ライブラリ　モジュールとは、pythonのファイル、ライブラリはいつくかのパッケージをまとめてインストールできるようにしたもの
モジュール
    utils_rsa2
    utils_insert
ライブラリ
    importlib
    sympy
"""

import importlib

import utils_rsa2


def main():   
    
    importlib.reload(utils_rsa2)
    
    n,e,p,q,L,P,C = utils_rsa2.rsa()
    
    while(1):#bit,p,q,L,e
        try:
            mode = (int(input("公開鍵:1,秘密鍵:2,暗号化:3,復号化:4, \n  ディジタル署名を生成する　秘密鍵:5,\n ディジタル署名を確認する　公開鍵:6,終了:7 \n input:")))
            
            if mode == 1:
                
                utils_rsa2.mode1(n,e,p,q,L)
                
            elif mode ==2:
                
                utils_rsa2.mode2(n,e,p,q,L)
                
            elif mode ==3:
                
                P,C = utils_rsa2.mode3(n,e,p,q,L,P,C)
                            
            elif mode ==4:
                
                P,C = utils_rsa2.mode4(n,e,p,q,L,P,C) 
                    
            elif mode ==5:
                
                P,C = utils_rsa2.mode5(n,e,p,q,L,P,C) 
                
            elif mode ==6:
            
                P,C = utils_rsa2.mode6(n,e,p,q,L,P,C)
            
            elif mode ==7:
                break
            
            else:
                raise ValueError
                
        except ValueError:
             print('入力値が不正です') 
             
if __name__ == '__main__':
    main()
