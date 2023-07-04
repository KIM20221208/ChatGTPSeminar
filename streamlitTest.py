# streamlitライブラリをインポート。
import streamlit as st

if __name__ == "__main__":
    # ファイルをアップロードする部品を実装する。
    up_file = st.file_uploader("File upload")
    # ターミナルでアップロードしたファイルの情報を出力。
    print(up_file)
