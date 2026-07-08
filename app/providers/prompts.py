def build_review_prompt(code: str) -> str:
    return f"""
    Você é um especialista em revisão de código. Sua tarefa é revisar o seguinte código:

    {code}
    
    Forneça uma revisão e sugira alternativas ou melhorias específicas para o código fornecido. Responda em português brasileiro.
    """