from langchain.prompts import PromptTemplate
from prompt import label_prompt
from llm_utils import DouBaoClient
from env_fri_words import env_fri_words

debug = False
env_fri_words = env_fri_words
label_prompt = label_prompt
if debug:
    print(label_prompt)
    print(env_fri_words)


class LabelUtils:
    """
    用于对文本进行标签化的工具类
    """
    def __init__(self):
        self.client = DouBaoClient()
        self.env_fri_words = env_fri_words

    def label_multiple(self, raw_texts):
        """对多个文本进行标注"""
        prompt = PromptTemplate(template=label_prompt, input_variables=["env_fri_words", "raw_texts"])
        final_prompt = prompt.format(env_fri_words=self.env_fri_words, raw_texts="\n".join(raw_texts))
        labeled_texts = self.client.get_standard_response("", final_prompt)
        # 分割标注结果并确保与输入文本行数匹配
        labeled_texts = labeled_texts.split('\n')
        if len(labeled_texts) != len(raw_texts):
            raise ValueError("标注结果长度与输入文本行数不匹配")
        return labeled_texts


if __name__ == '__main__':
    label_utils = LabelUtils()
    labeled_text = label_utils.label("环保非常重要")
    print(labeled_text)


