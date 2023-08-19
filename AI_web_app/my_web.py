from api.AI import AIAPI
import streamlit as st
from PIL import Image


def main():
    st.title("2023-Summer-Project")

    # OCR API를 활용한 이미지 내 텍스트 추출
    st.subheader("1. OCR API를 활용한 이미지 내 텍스트 추출")
    st.markdown("- 텍스트를 추출하고 싶은 이미지를 업로드해주세요.")

    query = st.file_uploader('Input Image')
    if query is not None:
        st.image(query)
        response = AIAPI.query_image2text(query, query)
        st.markdown("**API Output**")
        st.write(response)

    st.markdown("---")

    # ChatGPT API를 활용한 텍스트 요약
    st.subheader("2. ChatGPT API를 활용한 텍스트 요약")

    if query is not None:
        st.text(query)
        title, summary = AIAPI.query_text2text(response, response)
        st.markdown("**API Output**")
        st.subheader(title)
        st.write(summary)


if __name__ == '__main__':
    main()
