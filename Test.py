import openai
import streamlit as st

if __name__ == "__main__":
    up_file = st.file_uploader("File upload")
    print(up_file)

    # openai.api_key = "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"
    #
    # """
    # model: Specify model.
    # message:
    #     role:
    #         1.system: input conditions.
    #         2.user: input what you want to ask.
    #         3.assistant: output from ChatGTP.
    #     content: input some question and conditions.
    #
    # """
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system",
    #          "content": "あなたは役に立つアシスタントです。"
    #
    #          },
    #         {"role": "user",
    #          "content": "自然言語処理のTransformerについて説明してください"
    #
    #          }
    #
    #     ]
    #
    # )
    #
    # print(response["choices"][0]["message"]["content"])
