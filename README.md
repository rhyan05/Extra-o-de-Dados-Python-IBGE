# 📊 Análise de Popularidade do Nome "Gabriel" nos Municípios de SP (IBGE API)

Este projeto consulta a [API pública do IBGE](https://servicodados.ibge.gov.br/api/docs/) para identificar em **quais municípios do estado de São Paulo (SP)** o nome **Gabriel** está entre os **10 nomes mais comuns**, e quantas vezes ele aparece como o **nome mais popular** (1º lugar).

---

## 🔧 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Requests](https://pypi.org/project/requests/) (biblioteca para requisições HTTP)
- API REST pública do IBGE

---

## 📁 Arquivos do Projeto

- `main.py`: script principal que executa o processo de coleta, análise e salvamento dos dados.
- `gabriel_top10.json`: arquivo gerado com os municípios onde o nome Gabriel está entre os 10 mais populares, ordenados por frequência.

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
Instale as dependências:

```bash
pip install requests
```

Execute o script:
```bash
python main.py
```
Ao final, será gerado o arquivo gabriel_top10.json com os resultados.

# 🧠 O Que o Script Faz
Obtém todos os municípios do estado de São Paulo via API.

Para cada município:

Consulta os 10 nomes mais populares.

Verifica se o nome Gabriel está presente.

Se estiver, salva a frequência.

Conta quantas vezes ele aparece em 1º lugar.

Ordena os resultados pela frequência do nome "Gabriel".

Salva tudo em um arquivo JSON.

