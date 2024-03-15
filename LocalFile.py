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
        with open(self.file_path, 'r') as file:
            if self.file_path.endswith('.yaml') or self.file_path.endswith('.yml'):
                prompt = yaml.safe_load(file)
                prompt_content=prompt.get("Prompt",{})
            else:
                raise ValueError("Unsupported file format. Supported formats are .json, .yaml, and .yml.")
            return prompt_content

