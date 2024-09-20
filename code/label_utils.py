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

        # 打印原始请求和返回结果以调试
        print("原始请求:")
        print(final_prompt)
        print("标注结果:")
        print(labeled_texts)

        # 清理和分割标注结果
        labeled_texts = labeled_texts.strip().split('\n')
        # 去除多余的空行
        labeled_texts = [text for text in labeled_texts if text.strip()]

        # 如果标注结果少于原始文本数量，则用空字符串填充
        while len(labeled_texts) < len(raw_texts):
            labeled_texts.append("")

        if len(labeled_texts) != len(raw_texts):
            raise ValueError("标注结果长度与输入文本行数不匹配")

        return labeled_texts

