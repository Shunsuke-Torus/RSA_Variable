# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:08:59 2021

@author: shun
"""
import sympy
             
def rsa():
    
    print("RSA")
    p_judge = int(input("pを持っているなら入力:p,持っていない:0 \n p:"))
    q_judge = int(input("qを持っているなら入力:q,持っていない:0 \n q:"))
    e_judge = int(input("eを持っているなら入力:e,持っていない:0 \n e:"))
    if(p_judge==0):
        p = sympy.randprime(pow(10,299),pow(10,300))#sympy.randprime(a,b)a以上b未満の素数を返す。未満だったので300と書いてもok
    else:
        p = p_judge
        
    if(q_judge==0):
        q = sympy.randprime(pow(10,299),pow(10,300))
    else:
        q = q_judge
        
    while(p==q):
        p = sympy.randprime(pow(10,299),pow(10,300))
    #n
    n = p*q
    
    #L
    L = int(sympy.lcm(p-1,q-1))#最小公倍数を返すsympy
    
    #e
    max_num =max(p,q)#どちらか一方
    
    if(e_judge==0):#eの作成
        while(1):
            e = sympy.randprime(max_num,L)
            if sympy.gcd(max_num,L) and max_num < e < L:
                break
    else:
        e = e_judge
        
    P,C = "0","0" #str defで宣言されていないと言われるため汎用性を高めるため、後で変えるからあらかじめ宣言しておく。
    return n,e,p,q,L,P,C
      
def mode1(n,e,p,q,L):
    print(F"公開鍵n:\n{n}\n公開鍵e:\n{e}")
    
def mode2(n,e,p,q,L):
    d = secret_key(e,L)
    print(F"公開鍵n:\n{n}\n公開鍵e:\n{e}")
    print(F"秘密鍵p:\n{p}\n秘密鍵q:\n{q}\n秘密鍵L:\n{L}\n秘密鍵d:\n{d}")

def mode3(n,e,p,q,L,P,C):
    #P　平文
    mode_decryption = int(input("以前の平文を利用するなら:0を入力してください。以外なら:1 \n P:"))
    if mode_decryption==0:
        P = char_to_int(P)
        C = encrypt(P,e,n)
        C = int_to_char(C)
        print("暗号文:",C)
    elif mode_decryption==1:
        P = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
        P = char_to_int(P)
        C = encrypt(P,e,n)
        C = int_to_char(C)
        print("暗号文:",C)
    return P,C
    
def mode4(n,e,p,q,L,P,C):
    d = secret_key(e,L)
    mode_cryptogram = int(input("以前の暗号を利用するなら:0を入力してください。以外なら:1 \n C:"))
    if mode_cryptogram==0:
        C = char_to_int(C)
        P = dencrypt(C,d,n)
        P = int_to_char(P)
        print("P平文:",P)
    elif mode_cryptogram==1:
        C = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
        C = char_to_int(C)
        P = dencrypt(C,d,n)
        P = int_to_char(P)
        print("\n P平文:",P)
    return P,C
 
def mode5(n,e,p,q,L,P,C):
    #C　暗号文
    d = secret_key(e,L)
    mode_decryption = int(input("以前の平文を利用するなら:0を入力してください。以外なら:1 \n P:"))
    if mode_decryption==0:
        P = char_to_int(P)
        C = digital_encrypt(P,d,n)
        C = int_to_char(C)
        print("ディジタル署名作成:",C)
    elif mode_decryption==1:   
        P = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
        P = char_to_int(P)
        C = digital_encrypt(P,d,n)
        C = int_to_char(C)
        print("ディジタル署名作成:",C)
    return P,C

def mode6(n,e,p,q,L,P,C):
    mode_cryptogram = int(input("以前の暗号を利用するなら:0を入力してください。以外なら:1 \n C:"))
    if mode_cryptogram==0:
        C = char_to_int(C)
        P = digital_dencrypt(C,e,n)
        P = int_to_char(P)
        print("ディジタル署名確認:",P)
    elif mode_cryptogram==1:
        C = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n"))
        C = char_to_int(C)
        P = digital_dencrypt(C,e,n)
        P = int_to_char(P)
        print("ディジタル署名確認:",P)
    return P,C
     
def secret_key(e,L):#秘密鍵　作成
    x,y,t = sympy.gcdex(e,L)#shogoありがとう
    #d
    d = int(x) % L
    return d

def encrypt(P,e,n):#暗号化
    C = pow(P,e,n)#P^e %n
    return C

def dencrypt(C,d,n):#復号化
    P = pow(C,d,n)
    return P
    
def digital_encrypt(P,d,n):#ディジタル署名作成
    C = pow(P,d,n)
    return C

def digital_dencrypt(C,e,n):#ディジタル署名確認
    P = pow(C,e,n)
    return P

def char_to_int(P_C: str)->int:

    P_C_list = list(P_C)#1文字ずつ格納。""
    P_C_size = len(P_C_list)#長さを入力
    total = 0
    num_list = []
    for i in range(0,P_C_size):
        num_list.append(ord(P_C_list[i])-32)#128-32=96 SPは除いていない
    num_list.reverse()#1番　小さな数字をする
    
    num_list_size = len(num_list)#OZ　ありがとう　L144とL151の書き方を統一したよ7/5
    
    for i in range(0,num_list_size):
        total += num_list[i]*pow(95,i)#asc2*95^i 文字　数字　etc 95種類
    return total
    
def int_to_char(P_C_int: int) ->chr: #数字から文字 N=95
    #ユークリッドの互除法　数字を割って最小正剰余で表示
    qlist = []#商の保存先 quotient
    rlist = []#余り remainder
    while(P_C_int>=95):
        q,r = divmod(P_C_int,95)
        #q = P_C_int // 95
        #r = P_C_int % 95
        qlist.append(q)#商と余りを式の番号ごとに保存
        rlist.append(r)
        P_C_int = q
    if P_C_int // 95 < 95:#最後の追加の処理は上ではされない設計のため
        r = P_C_int % 95
        rlist.append(r)  
        
    rlist.reverse()#反転して1の位から入れる。
    
    char_list = []#数字を文字にする
    for i in range (0,len(rlist)):
        char_list.append(chr(rlist[i]+32))#+32で元の文字に戻す。特殊文字を避けるため
    P_C_char = "".join(char_list)#"",""を結合する
    
    return P_C_char


if __name__ == "__main__":
    main()
