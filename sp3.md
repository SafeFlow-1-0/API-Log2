# 📌 MVP - SafeFlow

## 🎯 Objetivo do MVP

- **Qual problema resolve?**  
  A Sprint 3 tem como objetivo aprofundar a análise estratégica do transporte de cargas perigosas, permitindo identificar as principais empresas movimentadoras, analisar a evolução da movimentação ao longo do tempo e compreender o comportamento das operações em diferentes regiões. Atualmente, essas informações encontram-se dispersas em bases extensas, dificultando a identificação de tendências, desempenho empresarial e padrões de segurança.

- **Qual hipótese será validada?**  
  A disponibilização de indicadores temporais e empresariais em um dashboard interativo permitirá identificar tendências de movimentação, destacar as principais empresas atuantes no setor e fornecer informações relevantes para apoiar processos de fiscalização, monitoramento e tomada de decisão.

- **Qual valor será entregue ao usuário final?**  
  O usuário terá acesso a análises temporais e empresariais capazes de demonstrar a evolução da movimentação das cargas perigosas ao longo dos anos, identificar as empresas com maior participação nas operações, visualizar a atuação regional dos transportadores e apoiar avaliações relacionadas à segurança e eficiência das operações logísticas.

---

## 📝 Descrição da Solução

- **Funcionalidades principais incluídas**  
  O SafeFlow ampliará suas análises com foco em indicadores empresariais e temporais, permitindo visualizar a evolução da movimentação de cargas perigosas ao longo dos anos, identificar as principais empresas movimentadoras, analisar sua participação no mercado e acompanhar tendências operacionais.

  O dashboard também contará com análises regionais específicas, incluindo informações relacionadas ao transporte de cargas perigosas no Vale do Paraíba, além de indicadores voltados à avaliação da segurança das operações realizadas pelas empresas transportadoras.

- **Limitações conhecidas**  
  Algumas análises dependem da disponibilidade e qualidade das informações declaradas nas bases públicas do IBAMA. A avaliação da segurança das empresas será baseada nos dados disponíveis e nos critérios estabelecidos para o projeto, podendo não representar integralmente todos os fatores operacionais envolvidos.

- **Escopo reduzido**  
  O escopo da Sprint 3 está concentrado na implementação de análises empresariais, temporais e regionais, complementando as funcionalidades desenvolvidas nas sprints anteriores e agregando maior valor estratégico ao dashboard.

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
| 11 | Alta | Como foi a evolução da movimentação ao longo do tempo? | Como analista, quero analisar a evolução da movimentação ao longo do tempo para identificar tendências | 8 |
| 12 | Alta | Quais as principais empresas movimentadoras de cargas perigosas com declaração realizada? | Como analista, quero identificar as principais empresas movimentadoras de cargas perigosas para análise de mercado | 6 |
| 13 | Média | Qual empresa é responsável pelo transporte no Vale do Paraíba? | Como analista, quero identificar a empresa responsável pelo transporte no Vale do Paraíba para análise regional | 7 |
| 14 | Alta | Dentre todas as empresas, quais fazem o transporte mais seguro? | Como analista, quero avaliar quais empresas realizam o transporte mais seguro para apoiar decisões estratégicas | 8 |

---

## 📅 Sprint(s) Relacionadas

| Sprint | Entregas Principais | Status |
|--------|--------------------|--------|
| 03 | Implementação da análise temporal da movimentação de cargas |  Concluído |
| 03 | Identificação das principais empresas movimentadoras |  Concluído |
| 03 | Análise regional das operações no Vale do Paraíba |  Concluído |
| 03 | Desenvolvimento de indicadores empresariais |  Concluído |
| 03 | Implementação de análises relacionadas à segurança operacional | Concluído |

---

## 📊 Critérios de Aceitação

- O dashboard deve apresentar a evolução da movimentação das cargas ao longo dos anos.
- O sistema deve identificar as principais empresas movimentadoras de cargas perigosas.
- O usuário deve conseguir visualizar informações específicas relacionadas ao Vale do Paraíba.
- O dashboard deve disponibilizar indicadores que auxiliem na avaliação da segurança das operações.
- O sistema deve manter navegação intuitiva, desempenho adequado e informações confiáveis.

---

## 📈 Métricas de Validação

- Número de usuários que testaram o MVP
  - Exigência mínima: 3 usuários diferentes.

- Feedback qualitativo (positivo/negativo)
  - Registro do feedback: em andamento.

- Indicadores de negócio
  - Facilidade na identificação de tendências operacionais.
  - Redução do esforço manual para análise empresarial e regional.
  - Apoio à tomada de decisão estratégica.

---

## 🚀 Próximos Passos

- Refinamento dos indicadores empresariais.
- Expansão das análises de segurança.
- Inclusão de novos filtros estratégicos.
- Aprimoramento visual do dashboard.
- Integração de novas bases de dados.

---

## 📂 Anexos / Evidências

- Prints de tela
- Fluxos ou protótipos
- Vídeo (MVP)
- 📄 Script Python: [`tratamento_dados.py`](./tratamento_dados.py)
