import spacy

# 加载 spaCy 英文模型
nlp = spacy.load("en_core_web_sm")

def parse_prompt(prompt: str):
    """
    对用户输入的 prompt 进行句法分析，
    返回包含 token 索引、词性、依存关系等信息的结构化列表。
    """
    doc = nlp(prompt)

    result = []
    for i, token in enumerate(doc):
        result.append({
            "index": i,
            "text": token.text,
            "pos": token.pos_,       # 词性，如 NOUN / VERB
            "dep": token.dep_,       # 依存关系，如 ROOT / dobj
            "head": token.head.text  # 当前 token 的依附词
        })

    return result

