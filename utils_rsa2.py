# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:08:59 2021
公開鍵暗号方式
C≡P^e(mod n) 暗号化
P≡C^d(mod n)　復号化

ディジタル署名
C≡P^d(mod n) 暗号化
P≡C^e(mod n)　復号化

n=p*q

L=LCM(p-1,q-1)=p-1*q-1/gcd(p,q)

Max{p,q}<e<L and L e が互いに素な数

gcd(l,e)=1

# MAX{p,q}<e<Lに必要

暗号文C =平文^e mod N

平文P   =暗号文^d mod N

Nを可変ではなく　ASC2にのっとって作成　str_listに直接　P,Cを書き込める　時間の短縮が可能になる。(文字入力の)

平文       N     d 
暗号文     N   e
公開鍵     N L e d 
秘密鍵     N L e d
参考文献
https://www.unisys.co.jp/tec_info/tr64/6403.pdf
https://ja.wikipedia.org/wiki/RSA%E6%9A%97%E5%8F%B7#n_%E3%82%92%E6%B3%95%E3%81%A8%E3%81%99%E3%82%8B%E5%86%AA%E5%89%B0%E4%BD%99%E3%81%AE%E8%A8%88%E7%AE%97


努力したポイント
毎回modeの中で平文を入力するようなプログラムにした。
見栄えが悪くなったり処理スピードが落ちたりするらしいが
以前の平文や暗号文を使えるようにするために入れないようにした。

見栄えをよくするためにmode3以降は例え使わないものであったとしても引数に無駄なデータを与えた。
このおかげにより、引数及び戻り値においてのケアレスミスは少なくなった。

http://ictsr4.com/sw/gcdex/
@author: shun
"""
import sympy
import importlib
import utils_insert
          
def rsa():
    try:
        importlib.reload(utils_insert)
        print("RSA")
        p_judge = int(input("pを持っているなら入力:0,持っていない:1 \n p:"))
        q_judge = int(input("qを持っているなら入力:0,持っていない:1 \n q:"))
        e_judge = int(input("eを持っているなら入力:0,持っていない:1 \n e:"))
        if(p_judge==1):
            p = sympy.randprime(pow(10,299),pow(10,300))#sympy.randprime(a,b)a以上b未満の素数を返す。未満だったので300と書いてもok
        elif(p_judge==0):
            p = int(input("p:"))
        
        if(q_judge==1):
            q = sympy.randprime(pow(10,299),pow(10,300))
        elif(q_judge==0):
            q = int(input("q:"))
        
        while(p==q):
            p = sympy.randprime(pow(10,299),pow(10,300))
        #n
        n = p*q
    
        #L
        L = int(sympy.lcm(p-1,q-1))#最小公倍数を返すsympy
    
        #e
        max_num =max(p,q)#どちらか一方
    
        if(e_judge==1):#eの作成
            while(1):
                e = sympy.randprime(max_num,L)
                if sympy.gcd(max_num,L) and max_num < e < L:
                    break
        elif(e_judge==0):
            e = int(input("e:"))
        
        P,C = None,None #str defで宣言されていないと言われるため+汎用性を高めるため+見やすくするため、後で変えるからあらかじめ宣言しておく。
    except ValueError:
        print("Input Error")
        
    return n,e,p,q,L,P,C
  
def mode1(n,e,p,q,L):
    print(F"公開鍵n:\n{n}\n公開鍵e:\n{e}")

def mode2(n,e,p,q,L):
    d = secret_key(e,L)
    print(F"公開鍵n:\n{n}\n公開鍵e:\n{e}")
    print(F"秘密鍵p:\n{p}\n秘密鍵q:\n{q}\n秘密鍵L:\n{L}\n秘密鍵d:\n{d}")

def mode3(n,e,p,q,L,P,C):
    #P　平文
    try: 
        mode_decryption = int(input("以前の平文を利用するなら:0を入力してください。以外なら:1 \n P:"))
        if mode_decryption==0:
            P = utils_insert.char_to_int(P)
            C = encrypt(P,e,n)
            C = utils_insert.int_to_char(C)
            print("暗号文:",C)
        elif mode_decryption==1:
            P = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
            if len(P) == 0:
                raise ValueError("平文の文字列が入力できてません。")
            P = utils_insert.char_to_int(P)
            C = encrypt(P,e,n)
            C = utils_insert.int_to_char(C)
            print("暗号文:",C)
        else:
            raise ValueError("0,1のみです。もう一度記入してください。")
            
    except ValueError as display:
        print(display)
        
    return P,C
    
def mode4(n,e,p,q,L,P,C):
    d = secret_key(e,L)
    try:
        mode_cryptogram = int(input("以前の暗号を利用するなら:0を入力してください。以外なら:1 \n C:"))
        if mode_cryptogram==0:
            C = utils_insert.char_to_int(C)
            P = dencrypt(C,d,n)
            P = utils_insert.int_to_char(P)
            print("P平文:",P)
        elif mode_cryptogram==1:
            C = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
            if len(C) == 0:
                raise ValueError("暗号文の文字列が入力できてません。")
            C = utils_insert.char_to_int(C)
            P = dencrypt(C,d,n)
            P = utils_insert.int_to_char(P)
            print("\n P平文:",P)
        else:
            raise ValueError("0,1のみです。もう一度記入してください。")
    except ValueError as display:
        print(display)
    return P,C
     
def mode5(n,e,p,q,L,P,C):
    #C　暗号文
    try:
        d = secret_key(e,L)
        mode_decryption = int(input("以前の平文を利用するなら:0を入力してください。以外なら:1 \n P:"))
        if mode_decryption==0:
            P = utils_insert.char_to_int(P)
            C = digital_encrypt(P,d,n)
            C = utils_insert.int_to_char(C)
            print("ディジタル署名作成:",C)
        elif mode_decryption==1:   
            P = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
            if len(P) == 0:
                raise ValueError("平文の文字列が入力できてません。")
            P = utils_insert.char_to_int(P)
            C = digital_encrypt(P,d,n)
            C = utils_insert.int_to_char(C)
            print("ディジタル署名作成:",C)
        else:
            raise ValueError("0,1のみです。もう一度記入してください。")
    except ValueError as display:
        print(display)
        
    return P,C

def mode6(n,e,p,q,L,P,C):
    try:
        mode_cryptogram = int(input("以前の暗号を利用するなら:0を入力してください。以外なら:1 \n C:"))
        if mode_cryptogram==0:
            C = utils_insert.char_to_int(C)
            P = digital_dencrypt(C,e,n)
            P = utils_insert.int_to_char(P)
            print("ディジタル署名確認:",P)
        elif mode_cryptogram==1:
            C = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
            if len(C) == 0:
                    raise ValueError("暗号文の文字列が入力できてません。")
            C = utils_insert.char_to_int(C)
            P = digital_dencrypt(C,e,n)
            P = utils_insert.int_to_char(P)
            print("ディジタル署名確認:",P)
        else:
            raise ValueError("0,1のみです。もう一度記入してください。")
            
    except ValueError as display:
        print(display)
    return P,C
"""
Integer object of sympy.core.numbers.moduleとなりdがinteger型になるため
int型にキャスト変換を行った。
最初はエラーメッセージを見ても何を意味しているのか分からなかった。
なぜならこの関数の場所でエラーが出るわけではなく、
他のモジュールに引数に渡し演算をさせる際にエラーが出るため気づかなかった。

イメージ
dencryptの時
P = pow(C,d,n)　
TypeError: unsupported operand type(s) for pow(): 'int', 'Integer', 'int'
今見たら一瞬で分かるが当時は、intとintegerが何者かをあまりよく分からなかった。(nullを代入できるなど便利機能がinteger>int)

一時不定方程式
ex+Ly = 1
"""
def secret_key(e,L):#秘密鍵　作成
    x,y,t = sympy.gcdex(e,L)#shogoありがとう
    d = int(x) % L
    return d
"""
暗号化
公開鍵で鍵を掛ける。
C = ( P ^ e ) % n
"""
def encrypt(P,e,n):#暗号化
    C = pow(P,e,n)#P^e %n
    return C
"""
復号化
秘密鍵で鍵を外す。
P = ( C ^ d ) % n
"""   
def dencrypt(C,d,n):#復号化
    P = pow(C,d,n)
    return P
"""
ディジタル署名作成
秘密鍵で鍵を掛ける。
C = ( P ^ d ) % n
"""    
def digital_encrypt(P,d,n):#ディジタル署名作成
    C = pow(P,d,n)
    return C
"""
ディジタル署名確認
公開鍵で鍵を外す。
P = ( C ^ e ) % n
"""
def digital_dencrypt(C,e,n):#ディジタル署名確認
    P = pow(C,e,n)
    return P
