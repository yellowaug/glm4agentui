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
            st.session_state["chatlist"] = funclist.selectbox("用户对话", ["袁祖成", "梁桂和"])
            opt = funclist.selectbox("提示词模板选择", ["袁祖成", "梁桂和", "基础模板"])
            print(opt)
            buttonlist=st.sidebar.container(height=100,border=False)
            if buttonlist.button("清空历史会话"):
                st.session_state["chat1history"] = []


        with st.container():
            # 聊天框内容
            messages = st.container(height=450,border=False)
            if st.session_state.chatlist=="袁祖成":
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
                    print(st.session_state["chat1history"])
                    for user_message in st.session_state["chat1history"]:
                        # messages.markdown(f"User: {user_message['User']}")
                        messages.chat_message("uesr").write(user_message['User'])
                        print(user_message['User'])
            else:
                st.markdown("这是另外一个页面了")
    def chatGLMPahe(self):
        chatpage,promppage=st.tabs(["GLM对话","提示词配置"]) #对页面进行标签分页

        #主页面
        with chatpage:
            st.header("对话信息")
            messages=st.container(height=350,border=False)
            # st.session_state["userhistory"]=[]
            # if user_message := st.chat_input("用户输入问题，按回车发送，shinf+回车换行"):
            #     st.session_state["userhistory"].append({"User": {user_message}})
            #     #用户历史记录打印
            #     # for _message in st.session_state["userhistory"]:
            #     #     messages.chat_message("user").write(_message["User"]) #显示用户输入的
            #     print(st.session_state["userhistory"])

            # 聊天历史记录打印在网页上
            userinput_history_dict = self._historymessage()
            if userinput_history_dict != None:
                for _message in userinput_history_dict:
                    messages.chat_message("user").write(_message["User"]) #显示用户输入的
        with promppage:
            st.header("提示词信息")

        #侧边栏
        with st.sidebar:
            st.header("功能按钮")
            functionare = st.container(height=300) #定义功能按钮区域
            selectresult=functionare.selectbox("提示词模板",["袁祖成模板","梁桂和模板","基础模板"]) #提示词模板选择

            st.button("清空会话记录",on_click=self._historymessage,args=(True,)) #点击清空历史记录,优雅的实现

    def _historymessage(self,clear_msg=False):
        """
        获取用户输入的历史记录,并返回聊天历史记录,内有清空聊天记录的功能
        :return: 聊天记录数组
        """
        if clear_msg:
            del st.session_state["chat1history"]
        else:
            if "chat1history" not in st.session_state:
                st.session_state["chat1history"] = []  # 把用户输入的prompt存入session_state，形成历史记录
            if prompt := st.chat_input("用户输入问题，按回车发送，shift+回车换行"):
                st.session_state["chat1history"].append({"User": prompt})
                # input_placeholder.markdown(f"User: {prompt}")
                # print(messages)
                print(st.session_state["chat1history"])
                return st.session_state["chat1history"]

