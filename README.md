# 退屈なことはPythonにやらせよう
書籍 "退屈なことはPythonにやらせよう Automate the boring stuff with python" by Al Swigart のpythonプログラムを実装したものです。

フォルダは章を表します。

# 3章　関数
### 3.11.1 コラッツ数列
偶数ならn/2，奇数なら3*n+1を繰り返すことで1に収束するコラッツ数列を計算

### 3.11.2 入力の妥当性検証
コラッツ数列のプログラムの入力が整数でない場合に、整数を促すメッセージを表示

# 4章　リスト
### 4.10.1 コンマ付け
リストの要素をカンマとスペースで並べ，最後の要素の前にandを挿入

### 4.10.2 絵文字グリッド
リストを受け取り，絵として表示

# 5章　辞書とデータ構造
### 5.6.1 ファンタジーゲームの持ち物リスト
持ち物リスト（辞書型）の表示

### 5.6.2 ファンタジーゲームの持ち物リスト用にリストから辞書に移す関数
持ち物リストにアイテムを追加

# 6章　文字列操作
### 6.7.1 表の表示
文字列のリストを右揃えに成形して表示

# 7章　正規表現によるパターンマッチング
### 7.18.1 強いパスワードの検出
正規表現を用いて，パスワードの強さを判定  
強いパスワード（８文字以上，大文字と小文字を含む，１つ以上の数字を含む）

### 7.18.2 正規表現を用いたstrip()メソッド
文字列メソッドのstrip()と同等の動きをする関数を定義  
文字列の先頭と末尾から指定した文字を除去（デフォルトは空白文字）

# 8章　ファイルの読み書き
## 8.7 マルチクリップボード
8.7_MultiClipBoard.py - クリップボードのテキストを保存・復元  
引数 "save <keyword>"：クリップボードをキーワードに紐づけて保存
引数 "<keyword>"：キーワードに紐づけられたテキストをクリップボードにコピー
引数 "list"：全キーワードをクリップボードにコピー

## 8.10 演習
### 8.10.1 マルチクリップボードを拡張
マルチクリップボードのプログラムを引数 "delete <keyword>"でシェルフからキーワードを削除できるように

### 8.10.2 作文ジェネレータ
### 8.10.3 正規表現探索