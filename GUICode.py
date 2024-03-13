import streamlit as st

# def test():
#     st.title("This is a test")
#
# def test1():
#     with st.container():
#         st.title("This is a test")
#         prompt = st.chat_input("Say something")
#         if prompt:
#             st.write(f"User has sent the following prompt: {prompt}")
#
#     with st.container():
#         st.sidebar.title("测试")
#         opt=st.sidebar.selectbox("选择",["测试1","测试2"])
#         print(opt)

class GLMui():
    def __init__(self):
        self.prompt = "这里是聊天内容"

    def loaclGLMPage(self):


        with st.container():
            #标题页面的容器
            st.header("JJCK_GLM调试页面",divider="blue")
            # st.title("本地GLM调试页面")

        with st.container():
            # 侧边栏的容器
            funclist=st.sidebar.container(height=520,border=False)
            # st.sidebar.title("功能列表")
            # st.session_state["chatlist"]=st.sidebar.selectbox("用户对话",["对话1","对话2"])
            # opt=st.sidebar.selectbox("提示词模板选择",["袁祖成","梁桂和","基础模板"])
            # print(opt)
            funclist.title("GLM功能列表")
            st.session_state["chatlist"] = funclist.selectbox("用户对话", ["对话1", "对话2"])
            opt = funclist.selectbox("提示词模板选择", ["袁祖成", "梁桂和", "基础模板"])
            print(opt)
            buttonlist=st.sidebar.container(height=100,border=False)
            buttonlist.button("清空历史会话")


        with st.container():
            # 聊天框内容
            messages = st.container(height=450,border=False)
            if st.session_state.chatlist=="对话1":
            # 初始化输入框和输出框
            #     messages.chat_message(name="user", avatar="user")
                    # input_placeholder = st.empty()
                # with st.chat_message(name="assistant", avatar="assistant"):
                #     message_placeholder = st.empty()
                if "chat1history" not in st.session_state:
                    st.session_state["chat1history"] = []  # 把用户输入的prompt存入session_state，形成历史记录
                if prompt := st.chat_input("用户输入问题，按回车发送，shinf+回车换行"):
                    st.session_state["chat1history"].append({"User": {prompt}})
                    # input_placeholder.markdown(f"User: {prompt}")
                    # print(messages)
                    for user_message in st.session_state["chat1history"]:
                        messages.markdown(f"User: {user_message['User']}")
                        print(user_message['User'])
            else:
                st.markdown("这是另外一个页面了")