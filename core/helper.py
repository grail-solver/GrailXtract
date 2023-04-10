from utils.protocol.prompt_builder import prompt
from utils.llm.gpt import gpt


def extract_data(problem: str):
    # get prompt using our protocol
    formatted_prompt = prompt.replace('<problem>', problem)

    # extract data using GPT-LLM
    data = gpt(formatted_prompt)
    print(data)
    return data


if __name__ == '__main__':
    extract_data('PyCharm')
