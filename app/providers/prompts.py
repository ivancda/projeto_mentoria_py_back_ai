def build_review_prompt(code: str) -> str:
    return f"""
    Você é um especialista em revisão de código. Sua tarefa é revisar o seguinte código, ou responder a pergunta relacionada à programação:

    {code}
    
    Responda de maneira objetiva em apenas um parágrafo, com exemplos mínimos. Responda em português brasileiro.
    """