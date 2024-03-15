
from GUICode import GLMui
from LocalFile import LocalPromptYml


if __name__ == '__main__':
    # ui=GLMui()
    # ui.chatGLMPahe()
    # ui.loaclGLMPage()
    localyml=LocalPromptYml(user_input_path="prompt.yaml")
    localyml.read_prompt()
