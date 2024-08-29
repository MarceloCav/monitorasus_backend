# Documentação do Projeto - Observatório de Gestão do SUS no RN

## Descrição do Projeto
Este projeto é uma API desenvolvida em Django que fornece dados sobre internações do SUS no Rio Grande do Norte, utilizando um banco de dados MongoDB. A API é executada em um ambiente Docker e oferece endpoints para acessar quatro indicadores principais relacionados às internações.

## Estrutura do Projeto
- **Backend**: Django REST Framework
- **Banco de Dados**: MongoDB
- **Containerização**: Docker

## Endpoints da API

### 1. Média de Dias de Internação por Especialidade
- **Endpoint**: `/api/media_dias_internacao/`
- **Método**: `GET`
- **Parâmetros de Consulta**:
  - `especialidade`: (opcional) Código da especialidade.
  - `cnes`: (opcional) Código do estabelecimento de saúde.
  - `mes_ano_inicio`: (opcional) Data de início no formato `YYYYMM`.
  - `mes_ano_fim`: (opcional) Data de fim no formato `YYYYMM`.
  - `municipio_res`: (opcional) Código do município de residência.
  - `municipio_mov`: (opcional) Código do município de movimentação.
- **Descrição**: Retorna a média de dias de internação agrupada por especialidade.

### 2. Número e Percentual de Internações por Causa (CID-10)
- **Endpoint**: `/api/numero_percentual_internacoes/`
- **Método**: `GET`
- **Parâmetros de Consulta**:
  - `capitulo_cid`: (obrigatório) Capítulo da CID-10.
  - `cnes`: (opcional) Código do estabelecimento de saúde.
  - `mes_ano_inicio`: (opcional) Data de início no formato `YYYYMM`.
  - `mes_ano_fim`: (opcional) Data de fim no formato `YYYYMM`.
  - `municipio_res`: (opcional) Código do município de residência.
  - `municipio_mov`: (opcional) Código do município de movimentação.
- **Descrição**: Retorna o número e percentual de internações agrupadas por causa (CID-10).

### 3. Valor Médio da Internação por Especialidade
- **Endpoint**: `/api/valor_medio_internacao/`
- **Método**: `GET`
- **Parâmetros de Consulta**:
  - `especialidade`: (opcional) Código da especialidade.
  - `cnes`: (opcional) Código do estabelecimento de saúde.
  - `mes_ano_inicio`: (opcional) Data de início no formato `YYYYMM`.
  - `mes_ano_fim`: (opcional) Data de fim no formato `YYYYMM`.
  - `municipio_res`: (opcional) Código do município de residência.
  - `municipio_mov`: (opcional) Código do município de movimentação.
- **Descrição**: Retorna o valor médio das internações agrupadas por especialidade.

### 4. Taxa de Ocupação Hospitalar por Estabelecimento
- **Endpoint**: `/api/taxa_ocupacao/`
- **Método**: `GET`
- **Parâmetros de Consulta**:
  - `cnes`: (obrigatório) Código do estabelecimento de saúde.
  - `mes_ano`: (obrigatório) Mês e ano no formato `YYYYMM`.
- **Descrição**: Retorna a taxa de ocupação hospitalar para o estabelecimento especificado.


## Execução do Projeto
Para executar o projeto, siga os passos abaixo:


## Primeiros Passos da API de Internações

### 1. Preparação do Ambiente

Para começar, certifique-se de estar na branch `feature/api_internacoes` do seu repositório.

1.1. Inicie os containers Docker executando o comando abaixo no terminal:

```bash
docker-compose up -d
```

Este comando iniciará o banco de dados MongoDB juntamente com a aplicação Django.

### 2. Banco de Dados MongoDB

Inicialmente, o banco de dados MongoDB estará vazio. No entanto, temos dois arquivos de amostra para popular o banco:

- `internacoes_rn.feather`
- `leitos_rn.feather`


### 3. Popular o MongoDB

Ao subir os containers do docker compose, voce certamente verá 4 containers rodando

onde dois deles serao algo parecido com 

- populatemongo_leitos

- populatemongo_internacoes

Para popular o banco com os dados, apenas rode o seguinte comando para os dois containers

`docker exec -it <id do container> bash`

quando estiver dentro do bash, rode `python populatemongo_internacoes.py` para o container internacoes 

fazer o mesmo para o container leitos

### Conclusão

Após seguir estes passos, o ambiente estará pronto e configurado para rodar a API de Internações com a aplicação Django e o banco de dados MongoDB.

*OBS.: os arquivos feather sao uma conversao compactada, sem perda de dados, dos arquivos dbf.

