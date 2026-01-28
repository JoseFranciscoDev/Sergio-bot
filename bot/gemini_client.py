from google.genai import Client, types


class GeminiClient(Client):
    """
        Inicializa o cliente customizado.
        Args:
            api_key (str): Sua chave de API do Google AI Studio.
            instructions (str): As instruções de sistema (prompt) para o modelo.
            model_name (str): O nome do modelo (ex: 'gemini-2.5-flash').
        """
    def __init__(self, api_key, instructions, model):
        super().__init__(api_key=api_key)
        self.model = model
        self.instructions = instructions
        
    def question(self, contents, opcional_instructions = None, model=None) -> str:
        """
            Envia um prompt para o modelo. Por padrão você precisa mandar apenas o conteúdo do prompt,
            mas caso queira alterar de alguma forma as intruções do modelo, você pode alterar através
            do paramêtro 'opcional_instructions' para instruir o modelo ou usar o model para trocar de modelo
            para aquela pergunta(ex: 'gemini-2.5-pro' para operações que exijam raciocinio)
            Args:
                contents (str): O conteúdo do prompt que será enviado para o modelo 
                opcional_instructions (str): Instruções adicionais
                model (str): modelo que será usado na pergunta
        """
        response = self.models.generate_content(model=model if model else self.model, contents=contents,config=types.GenerateContentConfigDict(system_instruction=self.instructions + opcional_instructions if opcional_instructions else self.instructions))
        return str(response.text)