# 📌 MVP - Safe Flow

## 🎯 Objetivo do MVP
 
- **Qual problema resolve?**  
  O MVP tem como objetivo tornar os dados referentes ao transporte de cargas perigosas mais acessíveis, por meio de visualizações interativas e claras, facilitando sua análise e interpretação.

- **Qual hipótese será validada?**  
  A organização e visualização dos dados do IBAMA em um dashboard interativo possibilitam identificar padrões de movimentação, principais modais e rotas, contribuindo para análises logísticas mais eficientes.

- **Qual valor será entregue ao usuário final?**  
  Disponibilização de um dashboard interativo em Power BI que permite a visualização e análise de indicadores logísticos, como modais, origens, destinos e evolução temporal das cargas perigosas.

---

## 📝 Descrição da Solução
  
- **Funcionalidades principais incluídas**  
  O Safe Flow apresenta uma página inicial com gráficos e indicadores claros sobre o transporte de cargas perigosas, incluindo volumes, regiões e relações de origem-destino.

- **Limitações conhecidas**  
  O sistema ainda possui limitações relacionadas à aplicação de filtros mais específicos e refinados, o que pode restringir análises mais aprofundadas das informações.

- **Escopo reduzido**  
  O escopo do MVP está concentrado no desenvolvimento da página inicial de um dashboard interativo, contemplando apenas as informações essenciais necessárias para validação da proposta e do valor do projeto.

---

## 👥 Personas / Usuários-Alvo

<p align="justify">
<strong>Jean Costa:</strong> Professor e orientador acadêmico do projeto, responsável por acompanhar e avaliar o desenvolvimento da plataforma de Business Intelligence voltada ao fluxo de cargas especiais e perigosas. Atua na validação metodológica, garantindo que o projeto esteja alinhado às práticas ágeis, à qualidade da documentação e à aplicação correta dos conceitos logísticos e de análise de dados.
</p>

<p align="justify">
<strong>Marcus Nascimento:</strong> Cliente do projeto, atuando como principal elo entre a necessidade real e o desenvolvimento da solução. Responsável por validar os dados, orientar os requisitos práticos e garantir que a plataforma atenda às demandas de análise e fiscalização do fluxo de cargas perigosas.
</p>

<p align="justify">
<strong>IPEM (Instituto de Pesos e Medidas):</strong> Órgão público cliente institucional do projeto, responsável pela fiscalização, controle e análise de dados relacionados à movimentação de cargas perigosas. Atua como principal beneficiário da solução, utilizando a plataforma para apoiar decisões estratégicas e otimizar processos de fiscalização.
</p>

---

## 🔑 User Stories (Backlog do MVP)

| Rank | Prioridade | Pergunta | User Story | Estimativa |
|------|------------|----------|------------|------------|
| 1 | Alta | Quais as principais cargas movimentadas? | Como analista, quero identificar as principais cargas movimentadas para apoiar decisões logísticas | 7 |
| 2 | Média | Quais os tipos de cargas mais transportadas? | Como analista, quero analisar os tipos de cargas mais transportadas para entender padrões operacionais | 5 |
| 3 | Média | Quais cargas têm o maior grau de risco? | Como analista, quero identificar cargas com maior grau de risco para melhorar a segurança no transporte | 8 |
| 7 | Alta | Quais são as principais origens e destinos? | Como analista, quero visualizar as principais origens e destinos para análise de fluxo | 7 |
| 9 | Baixa | Quais cidades mais recebem cargas? | Como analista, quero identificar as cidades que mais recebem cargas para análise de distribuição | 4 |
---

## 📅 Sprint(s) Relacionadas

| Sprint | Entregas Principais | Status |
|--------|--------------------|--------|
| 01 | Coleta e unificação dos dados do IBAMA | Concluído |
| 01 | Limpeza e tratamento dos dados em Python | Concluído |
| 01 | Estruturação da base de dados | Concluído |
| 01 | Desenvolvimento do dashboard inicial (visão geral) | Concluído |
| 01 | Implementação de gráficos principais (cargas, origem-destino e distribuição) | Concluído |
| 01 | Identificação das principais cargas movimentadas | Concluído |
| 01 | Organização das principais origens e destinos (OD) | Concluído |
| 01 | Identificação das cidades com maior recebimento de cargas | Concluído |

---

## 📊 Critérios de Aceitação

- O MVP deve permitir ao usuário visualizar os dados de forma centralizada em uma interface interativa.  
- O sistema deve apresentar informações essenciais sobre as rotas, como volume transportado, tipos de carga e principais origens e destinos (ODs).  
- Interface clara, tempo de resposta adequado, cruzamento de dados intuitivo e confiabilidade das informações.

---

## 📈 Métricas de Validação

- **Número de usuários que testaram o MVP**
  - Exigência estabelecida: mínimo de 3 usuários diferentes.

- **Feedback qualitativo (positivo/negativo)**
  - Registro do feedback: em aguardo.

- **Indicadores de negócio (ex: % de adesão, redução de custo, etc.)**
  - Registro do feedback: em aguardo.

---

## 🚀 Próximos Passos

- Implementação de melhorias com base no feedback dos usuários  
- Ajustes de usabilidade e interface  
- Expansão das funcionalidades para próximas versões  

---

## 📂 Anexos / Evidências

- Prints do dashboard  
- Fluxos ou protótipos  
- from pathlib import Path

