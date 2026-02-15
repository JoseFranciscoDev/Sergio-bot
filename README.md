# Sergio Bot

O Sergio Bot é um bot para Telegram que irá te ajudar a resolver seus problemas com suas finanças pessoais

## Ambiente Virtual

Caso prefira usar pip, crie o ambiente virtual com 

```bash
python -m venv venv
```

E ative com:

```bash
.venv/Scripts/Activate
```

## Instalação

Você pode instalar as dependências usando pip

```bash
pip install -r requirements.txt
```
Ou usando uv
```bash
uv sync
```

## Usage
Após instalar as dependências, você deve criar um bot ou inserir e/ou inserir o Token de um bot seu já existente(caso não saiba como criar um bot e pegar o Token, recomendo: https://youtu.be/EDhSC1Rt3p8?si=-TQjnpBXtpWBg4gV)
e a sua chave de api da google ai studio, conforme o exemplo no .env.exemple.

Com tudo instalado e as variaveis configuradas, rode o seu bot com
```python
uv run python main.py
```
ou 
```python
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
