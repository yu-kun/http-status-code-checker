# http-status-code-checker
Check the HTTP status codes (404 and 200) from bulk URLs.

## 準備

urls.txtにチェック対象URLを記載。1行1URL。

例: 
~~~
https://yukun.info
https://yukun.info/kcfinder/browse.php
・
・
・
~~~

## 実行結果

"数字".txtの形式でURLのHTML Body部が保管
~~~
1.txt
2.txt
・
・
・
~~~

result.txtにHTTP status code結果と対象URLが','区切りで出力

~~~
200,https://yukun.info
404,https://yukun.info/kcfinder/browse.php
~~~
