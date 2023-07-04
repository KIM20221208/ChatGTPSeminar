# ファイルのアプロード機能実装（P162-P170）  


## Step1（コード）:
```
# streamlitライブラリをインポート。
import streamlit as st

if __name__ == "__main__":
    # ファイルをアップロードする部品を実装する。
    up_file = st.file_uploader("File upload")
    # ターミナルでアップロードしたファイルの情報を出力。
    print(up_file)
```
file_uploaderの詳細な情報：

![file_uploader exp](https://github.com/KIM20221208/ChatGTPSeminar/assets/120079883/de2742d5-a2a6-4d78-8909-62c0112b1fa1)

Official document:
https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options


## Step2（ターミナル）:
パソコンのterminal（cmd）を開く。
```
streamlit run [.py directory path] [ARGUMENTS]
```
- .py directory path(absolute direcotory): Step1のコードを書いたPythonファイルルート。  
- ARGUMENTS(--server.port=portNumber): ウエブアプリ起動に使いたいポート（原則としては任意、参考に本では：5003、自分は：8501）。  
- よって、私の場合ターミナルに入力するコマンドは以下になる：
```
streamlit run C:\Users\JCY\repositories\ForchatgtpSeminar\streamlitTest.py --server.port=8501
```
入力が間違いなければWebアプリケーションが自動的にpop upされる。
![WebAPP](https://github.com/KIM20221208/ChatGTPSeminar/assets/120079883/cec8ab25-993a-48cd-b094-c73cd353799e)



## Step3（アップロードするConfigファイルを用意）:
- URL: https://www.cisco.com/c/ja_jp/support/docs/routers/1700-series-modular-access-routers/71462-rtr-l2l-ipsec-split.html  での「ルータA」部分（「RouterA#show running-config」の行から最後の「end」まで ）を全部コピペして拡張子が「.conf」のテキストファイルを作る。
- URLが開けない場合、私が作ったgithub (URL: https://github.com/KIM20221208/ChatGTPSeminar) でのファイルをダウンロード（ファイル名：cisco.conf）。

## Step4（Configファイルをアップロード）:
Step3で作ったファイルをWebアプリケーションにアップロードする（ドラッグ＆ドロップ / Brows filesブタンをクリック）。

- アップロードの方法:  
![uploadfile](https://github.com/KIM20221208/ChatGTPSeminar/assets/120079883/2548a90d-39e7-4479-8e31-48c19f48fe5c)  
- アップロード後ファイル名が表示される:  
![uploadedfile](https://github.com/KIM20221208/ChatGTPSeminar/assets/120079883/ae19f9a7-48cf-4573-9c43-1e43833fe67b)  
- ターミナルではアップロードしたファイルの詳細が出力される:  
![uploadedfileInTerminal](https://github.com/KIM20221208/ChatGTPSeminar/assets/120079883/3e6aef5c-fefc-49a5-ad05-2460018a1020)  
