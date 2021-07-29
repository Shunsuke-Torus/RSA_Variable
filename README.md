#Shunsuke-Torus/RSA_Variable

#1.概要  
  -RSA暗号とディジタル署名をpythonで作ってみよう  

2.このプログラムに求めるもの  
  -RSA暗号に対応  
  -ディジタル署名に対応  
  -ASC2にも対応  
  -ランダムで入力できるように対応  
  -自分でも入力できるように対応  

3.必要なモジュール・ライブラリ  
  -モジュール  
    -utils_rsa2
    -utils_insert
  -ライブラリ
    -importlib
    -sympy
    
4.注目ポイント
  文字から数字、数字から文字の時において、制御文字を回避するために(0~31)の計32文字を引いたり最後に足したりした。

  数字から文字の際、最後の最小正剰余を文字に戻すことができなかったため、
  ifの文を使い 数字//95<95とすることによって、ほぼ全ての数字を文字に表すことができました。

  平文を暗号化すると暗号文から平文に戻すといった流れがあるため以前の平文と暗号文をそれぞれ記憶しておく必要がある。
  以前の状態を記憶することにより文を入力せずとも計算できるようにした事。

5.反省点
  ➀utils_insert()では数字から文字の際、if文を付けることによって最後の最小正剰余の追加を可能にしたが形が不細工であるため
  次はもっときれいなプログラムを書きたいと考える。
  特に、shogo-ppt/rsaのencryptの部分は私から見るときれいなプログラムだなと感じたので参考にしていきたいと考える。

  ➁main()では、プログラムの見やすさを追求した理由から余計な引数が増えた。

  ➂sympy.gcdex()はinteger型とは知らなかった。
    utils_rsa2ではsympy.gcdex(e,L)を用いて一次不定方程式を書いた。
    当時はinteger型とは知らずにint型だと思っていた。
    しかし、TypeError: unsupported operand type(s) for pow(): 'int', 'Integer', 'int'
    と表示され間違っていることは分かったが周辺のプログラムは全てint型だったため気づくことができなかった。
    ↓
  ➃関数が他の関数を呼び出しているためエラー箇所が分からなかった。
    エラーメッセージが表示された場所はdencryptの部分で生じている。
    一方で元々の原因はsecret_key(e,L)を作る際にsympyを使用しているため問題のある箇所を把握するのが難しかった。
    対応策として、次のプログラムを作る際はそれぞれの型の特徴を知っておくことや
    関数の接続先に目印となるものを付けることによって、エラーが発生したとしても対応できるようにすればいいと考える。
  
6.最近新しく学んでいる事
  -web認証(セキュリティ)
    -ストレッチング
    -hash
  -共通鍵暗号方式
  -他の人のプログラムを自分風にいじる
  など勉強しています。
  -資格
  また、4月に落ちた基本情報技術者試験を10月にまた受ける予定です。
7.参考文献
