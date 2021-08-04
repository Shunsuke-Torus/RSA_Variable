# -*- coding: utf-8 -*-
#他のプログラムで使用可能であるため分けた。RSA専用ではない。
"""
人間verフローチャート
char_to_int
処理開始
↓
文字列が来る
↓
0~n(要素数)に応じて無限ループ
↓
1文字ずつ文字列を数字に書き換える(ASC2コード表より-32にすると特別な意味を持つコマンドが指定されないため←point)
↓
１文字目から要素数までの(n=0~要素数)95^nを足し合わせる。
↓
合計値を求める
↓
処理終了

point
できるだけ短くしたかったが見やすさを考慮するためにプログラムが長くなってしまった。
"""
def char_to_int(P_C: str)->int:
    P_C_list = list(P_C)#1文字ずつ格納。
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


"""
int_to_char
人間verフローチャート
処理開始
↓
数字が来る。
↓
ユークリッドの互除法を用いる。
↓
割り切れなくなるまで無限ループする。
↓
商と余りをそれぞれ記憶する。
↓
余り=最小正剰余(mod 95)を文字に変換する。
↓
文字列が完成する。
↓
処理終了

point
whileの処理の際、どうしても最後の95以下になったときの文字の処理がなされないため
ifをつけるような不細工な形になってしまった。
また、１文字目から出力できるように文字(現在数字)のリストを反転させ元の文字に戻した。
"""
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
    if P_C_int // 95 < 95:
        r = P_C_int % 95#point
        rlist.append(r)  
        
    rlist.reverse()#反転して1の位から入れる。
    
    char_list = []#数字を文字にする
    for i in range (0,len(rlist)):
        char_list.append(chr(rlist[i]+32))#+32で元の文字に戻す。特殊文字を避けるため
    P_C_char = "".join(char_list)#"",""を結合する
    
    return P_C_char
