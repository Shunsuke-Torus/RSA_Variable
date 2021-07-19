# -*- coding: utf-8 -*-



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
