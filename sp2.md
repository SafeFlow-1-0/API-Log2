# 📌 MVP - SafeFlow

## 🎯 Objetivo do MVP

- **Qual problema resolve?**  
  O MVP tem como objetivo aprofundar a análise logística do transporte de cargas perigosas, permitindo identificar os principais modais, meios de transporte, rodovias e cidades envolvidas na movimentação das cargas.
  O dashboard busca centralizar essas informações em uma interface visual clara, organizada e de fácil interpretação.

- **Qual hipótese será validada?**  
  A ampliação das análises logísticas no dashboard possibilitará uma compreensão mais detalhada das rotas utilizadas, dos padrões de transporte e da distribuição das cargas perigosas no território nacional. 

- **Qual valor será entregue ao usuário final?**  
  Entregará novos indicadores logísticos e filtros analíticos capazes de apresentar informações sobre os principais modais utilizados, meios de transporte, rodovias mais recorrentes e cidades envolvidas no transporte de cargas perigosas.
  O usuário terá acesso a uma análise mais aprofundada e estratégica dos dados, permitindo identificar padrões operacionais, regiões críticas e tendências logísticas de maneira visual, intuitiva e centralizada.

---

## 📝 Descrição da Solução
  
- **Funcionalidades principais incluídas**  
  O SafeFlow apresenta um dashboard interativo desenvolvido em Power BI, integrado a bases públicas do IBAMA relacionadas ao transporte de cargas perigosas e resíduos sólidos. A solução contempla análises sobre principais cargas movimentadas, modais de transporte, origens e destinos (OD), cidades com maior movimentação, distribuição regional e indicadores logísticos relevantes.  
   
  Os dados passam por processos de limpeza, padronização, tratamento e unificação em Python, permitindo gerar uma base analítica estruturada para visualização e cruzamento das informações no dashboard.

- **Limitações conhecidas**  
  O sistema ainda possui limitações relacionadas à qualidade e completude de algumas bases públicas disponibilizadas pelo IBAMA, o que pode impactar determinadas análises. Além disso, alguns filtros avançados e análises mais específicas ainda estão em processo de desenvolvimento, limitando parte do aprofundamento analítico nesta versão do MVP.

- **Escopo reduzido**  
  O escopo atual do MVP está concentrado no desenvolvimento de uma solução funcional voltada à análise logística do transporte de cargas perigosas. Nesta etapa, o foco está na construção dos principais indicadores visuais, estruturação da base unificada de dados, identificação de padrões logísticos e disponibilização de informações estratégicas em uma interface interativa e intuitiva.
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
| 6 | Alta | Quais os principais modais utilizados? | Como analista, quero visualizar os principais modais utilizados para otimizar a análise logística | 8 |
| 7 | Baixa | Quais os principais meios de transporte utilizados? | Como analista, quero analisar os principais meios de transporte utilizados para melhor compreensão logística | 5 |
| 8 | Média | Quais as principais rodovias utilizadas? | Como analista, quero identificar as principais rodovias utilizadas para avaliar rotas logísticas | 8 |
| 9 | Baixa | Quais cidades fazem o transporte de carga? | Como analista, quero identificar as cidades responsáveis pelo transporte de cargas para entender a origem logística | 4 |

---

## 📅 Sprint(s) Relacionadas

| Sprint | Entregas Principais | Status |
|--------|--------------------|--------|
| 02 | Implementação de análise por modais de transporte | Em andamento |
| 02 | Identificação dos principais meios de transporte | Em andamento |
| 02 | Análise das principais rodovias utilizadas | Em andamento |
| 02 | Identificação das cidades responsáveis pelo transporte de cargas | Em andamento |
| 02 | Expansão dos filtros e refinamento das análises | Em andamento |

---

## 📊 Critérios de Aceitação

- O dashboard deve permitir visualizar os principais modais e meios de transporte utilizados.  
- O sistema deve apresentar análises relacionadas às rodovias e cidades envolvidas na movimentação das cargas.  
- O usuário deve conseguir realizar cruzamentos de informações logísticas de maneira intuitiva.  
- O dashboard deve manter navegação clara, organizada e responsiva.

---

## 📈 Métricas de Validação

- Número de usuários que testaram o MVP
  - Exigência mínima: 3 usuários diferentes.

- Feedback qualitativo (positivo/negativo)
  - Registro do feedback: em andamento.

- Indicadores de negócio
  - Facilidade na identificação de padrões logísticos.
  - Redução do esforço manual para análise de rotas e modais.

---

## 🚀 Próximos Passos

- Expansão das análises regionais  
- Inclusão de indicadores de segurança no transporte  
- Implementação de filtros avançados  
- Refinamento visual do dashboard  
- Integração de novas bases de dados  

---

## 📂 Anexos / Evidências
- Prints de tela  
- Fluxos ou protótipos  
- Vídeo (MVP)  
