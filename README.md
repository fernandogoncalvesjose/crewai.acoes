# CrewAI Ações

Projeto de demonstração de orquestração de agentes usando `crewai` em Python, com foco em criação de agentes, definição de tarefas colaborativas e utilização de API externa para busca de preços de ações.

## Objetivo

Este projeto foi desenvolvido para demonstrar o uso de `crewai` como motor de orquestração de agentes inteligentes. A ideia principal é:

- criar múltiplos agentes com papéis especializados
- definir tarefas que cada agente deve executar
- fazer a coordenação desses agentes em um fluxo de trabalho
- integrar dados externos a partir da API do Yahoo Finance

## Tecnologias usadas

- Python
- crewai
- crewai_tools
- langchain
- langchain_community
- yfinance
- python-dotenv
- Jupyter Notebook (`recomendacao.ipynb`)

## Componentes principais

### Agentes

A arquitetura do projeto é construída em torno de agentes com funções específicas, por exemplo:

- `gerente_cliente`: primeiro contato com o cliente, obtém perguntas e informações da carteira
- `analista_acoes`: analisa preços e tendências da ação
- `analista_noticias`: busca e analisa notícias relevantes
- `analista_chefe`: combina insights de preços e notícias para gerar recomendação final
- `redator`: transforma a recomendação em um relatório claro para o cliente

### Tarefas

Cada agente executa tarefas próprias. Exemplos de tarefas:

- `obter_carteira_cliente`
- `obter_preco_acao`
- `obter_noticias`
- `recomendar_acao`
- `escrever_boletim`

Essas tarefas são usadas para estruturar e limitar as responsabilidades de cada agente.

### Orquestração

O `Crew` é usado para orquestrar os agentes e tarefas:

- define o fluxo de execução
- controla os agentes disponíveis
- reúne as saídas em uma recomendação
- permite configurar modo de execução, iterações e compartilhamento de estado

## Integração com API externa

A parte de dados externos deste projeto utiliza o `yfinance` para buscar informações de preços de ações do Yahoo Finance. Isso permite:

- obter cotações históricas
- analisar tendências de preço
- comparar o preço atual com o preço médio pago pelo cliente

## Instalação

1. Crie e ative um ambiente virtual Python
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Defina sua chave de API no arquivo `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## Uso

O principal notebook do projeto é `recomendacao.ipynb`. Ele contém a definição dos agentes, ferramentas, tarefas e a execução do `Crew`.

### Passos gerais

1. Carregar variáveis de ambiente
2. Criar agentes com `crewai.Agent`
3. Definir tarefas com `crewai.Task`
4. Criar `Crew` para orquestrar agentes e tarefas
5. Executar e gerar recomendação

## Destaque do projeto

O foco deste projeto não é apenas analisar ações, mas mostrar como usar `crewai` para:

- montar uma cadeia de agentes especializados
- dividir problemas em tarefas bem definidas
- orquestrar a colaboração entre agentes
- conectar inteligência artificial com dados financeiros externos

## Arquivos principais

- `recomendacao.ipynb`: notebook principal com todo o fluxo de trabalho
- `requirements.txt`: dependências do projeto
- `ativos.csv`: arquivo de carteira de ações de exemplo

---

Este projeto serve como base para criar fluxos de automação de análise de investimentos usando agentes inteligentes e dados reais de mercado.
