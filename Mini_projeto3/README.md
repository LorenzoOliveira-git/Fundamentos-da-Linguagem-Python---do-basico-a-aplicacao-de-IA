# 📊 Análise de Dados para Marketing de E-commerce

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Concluído-green)
![Área](https://img.shields.io/badge/Área-Data%20Analytics%20%7C%20Marketing-orange)
![Fonte](https://img.shields.io/badge/Fonte-DSA-lightgrey)

---

## 📌 Visão Geral do Projeto
Aplicação analítica para decisão estratégica no setor de marketing usando o NumPy. Esse projeto serve para o aprendizado prático da biblioteca de manipulação de arrays e para uma noção geral de uma análise estatística na área do marketing. Se você é um estudante que quer entender o uso dessa ferramenta na prática com geração de dados e análises certeiras de negócio, você está no lugar certo!

---

## 🏪 Problema de Negócio
Uma plataforma de e-commerce coleta um volume significativo de dados sobre a interação dos usuários com o site, incluindo o número de visitas, a duração da sessão, a atividade de adição de produtos ao carrinho e os valores de compra finalizados. No entanto, esses dados estão sendo subutilizados. Atualmente, as decisões sobre campanhas de marketing, promoções e melhorias na experiência do usuário (UX) são tomadas com base em intuição e métricas de alto nível, sem uma compreensão aprofundada dos padrões de comportamento que impulsionam os resultados.

A empresa enfrenta o desafio de compreender profundamente os padrões de comportamento que diferenciam os clientes de alto valor dos visitantes que abandonam o site sem comprar. Essa falta de clareza resulta em:

- **Marketing Genérico**  
  Nossas campanhas de marketing são de "tamanho único", resultando em baixo engajamento e desperdício de orçamento, pois não conseguimos personalizar as ofertas para os segmentos de clientes corretos.

- **Perda de Oportunidades**  
  Não conseguimos identificar e engajar proativamente os clientes com maior potencial de compra ou criar estratégias para converter os visitantes que demonstram interesse, mas não finalizam a compra.

- **Decisões Não Embasadas**  
  As estratégias de produto e de experiência do usuário carecem de uma base quantitativa sólida sobre quais comportamentos (ex: tempo no site, frequência de visitas) estão mais fortemente correlacionados com o sucesso das vendas.

🔎 **Problema central:** falta de clareza sobre os padrões de comportamento dos usuários, impedindo decisões de marketing personalizadas, inteligentes e baseadas em evidências.

---

## 🎯 Objetivos de Negócio
Este projeto tem como objetivo utilizar a análise estatística dos dados de navegação e compra para segmentar clientes, identificar os principais indicadores de comportamento que levam à conversão e fornecer insights acionáveis para as equipes de marketing e produto, respondendo às seguintes perguntas fundamentais:

- **Qual é o perfil do nosso usuário?**  
  Identificar a média de visitas, tempo de navegação e ticket médio dos usuários da plataforma.

- **Quem são os clientes de Alto Valor?**  
  Descobrir as características e comportamentos distintos que definem esse segmento.

- **Onde está a oportunidade de conversão?**  
  Analisar o comportamento dos usuários que visitam o site, mas não realizam nenhuma compra.

- **O que impulsiona as compras?**  
  Verificar se existe correlação entre tempo no site, itens no carrinho e valor final da compra.

---

## 🧠 Solução Técnica
Mesmo em projetos simples, aplicar um **fluxo estruturado de dados** é um dos fundamentos da área de dados. A solução adotada seguiu as etapas abaixo:

1. **Geração dos dados**  
   Os dados foram **gerados aleatoriamente em distribuição normal** para fins de estudo, simulando o comportamento real de usuários.

2. **Análise estatística**  
   Exploração dos dados com foco direto em responder às perguntas de negócio definidas, utilizando NumPy como ferramenta central.

3. **Segmentação de clientes**  
   Criação de segmentos como "Clientes de Alto Valor" e "Visitantes Engajados sem Compra" para direcionamento de campanhas personalizadas.

Ao final, foram gerados **insights acionáveis**, permitindo que as equipes de marketing e produto tomem decisões com base em uma fundação quantitativa sólida.

---

## 📊 Perguntas Respondidas pela Análise
Os resultados da análise permitiram gerar os seguintes insights de negócio:

- **Segmentação Aprimorada**  
  Criação de segmentos de clientes para direcionamento de campanhas de marketing personalizadas, aumentando o engajamento e reduzindo o desperdício de orçamento.

- **Otimização de Marketing**  
  Direcionamento do orçamento de marketing para ações focadas nos comportamentos que mais se correlacionam com compras de alto valor, aumentando o **ROI**.

- **Melhoria da Experiência do Usuário (UX)**  
  Fornecimento à equipe de produto de dados que justificam testes A/B ou melhorias em áreas do site frequentadas por usuários que não convertem.

---

## 🚀 Como Utilizar a Solução

### 🔧 Pré-requisitos
Recomenda-se a criação de um **ambiente virtual**, garantindo isolamento e organização do projeto:
```bash
conda create --name nome_do_ambiente
```

Caso não tenha o Anaconda instalado, faça o download gratuito em:
https://www.anaconda.com/download

### 📥 Instalação

Clone o repositório:
```
git clone <URL_HTTPS_DO_REPOSITORIO>
```

Acesse a pasta do projeto:
```
cd Mini_projeto3
```

Instale as dependências:
```
pip install -r requirements.txt
```

### ▶️ Execução
Execute o script principal:
```
python main.py
```

### ⚠️ Observações
Esta análise é válida para a modelagem de dados utilizada no projeto.

Para aplicar a solução em um cenário real, serão necessárias adaptações nos dados e regras de negócio.

---

## 🛠️ Tecnologias Utilizadas

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## 🙌 Agradecimentos
Agradeço à **Data Science Academy (DSA)** por disponibilizar um curso gratuito de alta qualidade, que serviu como base para os estudos e projetos presentes neste repositório.