import streamlit as st
from LocalFile import LocalPromptYml

class GLMui():
    def chatGLMPahe(self):
        chatpage,promppage=st.tabs(["GLM对话","提示词配置"]) #对页面进行标签分页
        if "promtnamelist" not in st.session_state:
            st.session_state["promtnamelist"] = ["袁祖成模板", "梁桂和模板", "基础模板"]

        # 侧边栏
        with st.sidebar:
            st.header("功能按钮")
            functionare = st.container(height=300)  # 定义功能按钮区域
            selectresult = functionare.selectbox("提示词模板", st.session_state["promtnamelist"])  # 提示词模板选择

            st.button("清空会话记录", on_click=self._historymessage, args=(True,))  # 点击清空历史记录,优雅的实现
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
            st.header("提示词模板信息")
            prompt_msgcontainer = st.container(height=320,border=False)
            _ymlcontent=self._readpromptcontent()
            #根据选择标签选择模板信息的逻辑，根据选择的标签读取相应的提示词模板
            for promtname in st.session_state["promtnamelist"]: #标签组与选择组循环比对
                #根据标签名称读取不同人员的模板内容，人员列表是固定的。
                if selectresult ==promtname:
                    if promtname=="袁祖成模板":
                        prompt_content = prompt_msgcontainer.text_area(f"{selectresult}内容", value=_ymlcontent.get("yzc"),height=300)
                        _ymlcontent["yzc"]=prompt_content #赋值到写入本地文档的方法
                        # prompt_input=prompt_content #获取更新后的Yml文件内容
                    elif promtname=="梁桂和模板":
                        prompt_content = prompt_msgcontainer.text_area(f"{selectresult}内容", value=_ymlcontent.get("lgh"))
                        _ymlcontent["lgh"]=prompt_content
                        # prompt_input=prompt_content
                    elif promtname=="基础模板":
                        prompt_content = prompt_msgcontainer.text_area(f"{selectresult}内容", value=_ymlcontent.get("base"))
                        _ymlcontent["base"]=prompt_content
                        # prompt_input=prompt_content
                    # print(_ymlcontent)
            but1,but2,but3=st.columns([1,1,5]) #实现两个按钮能整齐排列
            if 'clicked' not in st.session_state:
                st.session_state.clicked = False
            but1.button("修改模板",on_click=self._writepromptcontent,args=(_ymlcontent,))
            if st.session_state.clicked:
                # The message and nested widget will remain on the page
                st.write('Button clicked!')
                # st.slider('Select a value')
            but2.button("取消修改") #其实这个没啥用





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

    def _readpromptcontent(self):
        localyml = LocalPromptYml(user_input_path="prompt.yaml")
        return localyml.read_prompt()
    def _writepromptcontent(self,promptcontent:dict):
        """
        将用户输入的更改内容写入yaml写入prompt.yaml文件
        :param promptcontent: 用户传入的yml内容,必须是{'yzc': 'test', 'base': 'test1', 'lgh': '123456'} 这个类型的才可以
        :return:
        """

        st.session_state.clicked = True
        print(f"这是用户输入{promptcontent}")
        localyml = LocalPromptYml(user_input_path="prompt.yaml")
        localyml.write_prompt(promptcontent)