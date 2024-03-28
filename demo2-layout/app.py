import streamlit as st

st.title("Lesson 01.02: Intro to Layout and Images")

def clean_text(text):
    text=text.replace("`","").replace("-\n","").replace("\n"," ").strip()
    return text


st.sidebar.image("meow.gif")
# sidebar 边栏 header边栏的标题
st.sidebar.header("Options")

text=st.sidebar.text_area("Paste Text Here", value="`hi bro`")

button1= st.sidebar.button("Clean Text")

if button1:
    col1,col2=st.columns(2)

    col1_expander=col1.expander("Expand Original")
    with col1_expander:
        col1_expander.header("Original Text")
        col1_expander.write(text)

    col2.header("Cleaned Text")
    clean=clean_text(text)
    col2.write(clean)
    

