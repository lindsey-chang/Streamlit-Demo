import streamlit as st

# 设置页面标题
st.title("Streamlit Tutorial App")

# 在页面上显示一段文本
st.write("This is my new app")

# 创建一个按钮
button1 = st.button("Click Me")

# 如果按钮被点击，显示一条消息
if button1:
    st.write("Button Clicked.")

# 创建一个复选框，询问用户是否喜欢这个应用
like = st.checkbox("Do you like this app?")

# 创建另一个提交按钮
button2 = st.button("Submit")
if button2:
    # 根据复选框的结果显示不同的消息
    if like:
        st.write("Thanks. I like it too.")
    else:
        st.write("I'm sorry. You have bad tastes.")

# 创建一个带有单选按钮的区域，让用户选择他们最喜欢的动物
st.header("Start of the Radio Button Section")
animal = st.radio("What animal is your favorite?", ("Lion", "Tiger", "Bear"))

# 创建一个按钮提交用户的动物选择
button3 = st.button("Submit Animal")
if button3:
    st.write(animal)
    if animal == "Lion":
        st.write("ROAR!")

# 创建一个下拉选择框让用户再次选择喜欢的动物
st.header("Start of the Selectbox Section")
animal2 = st.selectbox("What animal is your favorite?", ("Lion", "Tiger", "Bear"))

# 创建一个按钮提交用户的选择
button4 = st.button("Submit Animal 2")
if button4:
    st.write(animal2)
    if animal2 == "Lion":
        st.write("ROAR!")

# 创建一个多选框让用户选择多个他们喜欢的动物
st.header("Start of the Multiselect Section")
options = st.multiselect("What animals do you like?", ["Lion", "Tiger", "Bear"])

# 创建一个按钮来显示用户的选择
button5 = st.button("Print Animals")
if button5:
    st.write(options)

# 创建一个滑动条让用户选择一个数字（代表epochs）
st.header("Start of the Slider Section")
epochs_num = st.slider("How many epochs?", 1, 100, 10)

# 创建一个按钮来显示滑动条的值
if st.button("Slider Button"):
    st.write(epochs_num)

# 创建一个文本输入框让用户输入他们最喜欢的电影
st.header("Start of the Text Input Section")
user_text = st.text_input("What's your favorite movie?", "Hello World")

# 创建一个按钮来显示用户输入的文本
if st.button("Text Button"):
    st.write(user_text)

# 创建一个数字输入框让用户输入他们最喜欢的数字
user_num = st.number_input("What's your favorite number?")

# 创建一个按钮来显示用户输入的数字
if st.button("Number Button"):
    st.write(user_num)

# 定义一个函数用于运行情感分析
def run_sentiment_analysis(txt):
    st.write(f"Analysis Done. {txt}")

# 创建一个文本区域让用户输入文本，然后运行情感分析
txt = st.text_area('Text to analyze', '''It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair''')
st.write('Sentiment:', run_sentiment_analysis(txt))
