import yaml

class LocalPromptYml:
    def __init__(self,*,user_input_path):
        """
        初始化
        :param user_input_path: 文件路径以及文件名称
        """
        self.file_path=user_input_path
    def read_prompt(self):
        """
        读取本地yml文件
        :return: 返回读取内容的数组
        """
        with open(self.file_path, 'r',encoding='utf-8') as file:
            if self.file_path.endswith('.yaml') or self.file_path.endswith('.yml'):
                prompt = yaml.safe_load(file)
                # prompt_content=prompt.get("Prompt",{})
            else:
                raise ValueError("Unsupported file format. Supported formats are .json, .yaml, and .yml.")
            return prompt

    def write_prompt(self,prompt_content):
        """
        写入yml文件
        :param prompt_content: 写入的内容
        :return:
        """
        with open(self.file_path, 'w',encoding='utf-8') as file:
            if self.file_path.endswith('.yaml') or self.file_path.endswith('.yml'):
                yaml.safe_dump(prompt_content, file,default_flow_style=False, allow_unicode=True)
            else:
                raise ValueError("Unsupported file format. Supported formats are .json, .yaml, and .yml.")