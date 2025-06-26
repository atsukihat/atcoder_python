## atcoder_python
### Description
* Reproduction of python3 and pypy environment in atcoder on VSCode.
* The atcoder-cli and online-judge-tools for automated testing and submission.

### Reference repository
  ```
  https://github.com/gomatofu/atcoder_python
  ```

## Assumption
The VS Code extension "Remote-Containers" is intended to be used.

### Usage
Clone this repository
 ```
 git clone https://github.com/amoon46/atcoder_python.git
 ```
Open in VSCode
 ```
 code atcoder_python
 ```
Open the command palette on VSCode and select `Remote-Containers: Reopen in Container`.

Commands for question creation, automated testing, and automated testing are introduced at the following sites.
[atcoder-cli-command](http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/)

written more details on the community blog if you would like to take a look.
https://qiita.com/gomatofu/items/1adae9b7cd79b0f8044f


## explain atcoder-cli and alias 

### ログイン
 ```oj login https://atcoder.jp/contests```

※ AtCoder側の仕様変更により、ログインがうまくいかない場合があります。
その際は以下の記事を参考にしてセッション情報の取得を行ってください：
https://kaiyou9.com/acc_and_oj_login_failed/


### テストケースなどを取得
 ```acc new abc251 -c all```

### PyPy3でのテスト実施
 alias test='oj t -c "pypy3 main.py" -d ./tests/'
 
### Pythonでのテスト実施
 alias test2='oj t -c "python3 main.py" -d ./tests/'

### PyPy3での解答提出
 alias sb='acc s main.py -- --guess-python-interpreter pypy'

### Pythonでの解答提出
 alias sb2='acc s main.py'

### コンテストフォルダへ移動
 alias c='cd contest'

### main.pyを開く
 alias o='code main.py'
 
### 出力確認用
 alias d='python main.py'
