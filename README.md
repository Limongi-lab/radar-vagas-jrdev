# Radar de Vagas Jr Dev

![Tests](https://github.com/Limongi-lab/radar-vagas-jrdev/actions/workflows/tests.yml/badge.svg)

Uma API + dashboard que rastreia vagas reais de desenvolvedor júnior, extrai as skills mais pedidas no mercado e compara com o meu perfil técnico atual — pra transformar "o que estudar a seguir" numa decisão baseada em dado, não em achismo.

Sou estudante de Engenharia de Computação e Gestão da Informação, treinando o backend. Em vez de adivinhar quais tecnologias valem a pena aprender, construí uma ferramenta que responde isso com dados: coleta vagas de fontes públicas, identifica as skills que mais aparecem, e mostra exatamente o gap entre o que o mercado pede e o que eu já sei.

## Stack

Python · Django REST Framework · PostgreSQL (SQLite em dev) · pytest · Docker · Chart.js · GitHub Actions

## Rodando local

```bash
python -m venv venv
venv\Scripts\activate          
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_skills
python manage.py seed_perfil
python manage.py runserver
```

- `http://127.0.0.1:8000/` — dashboard
- `http://127.0.0.1:8000/api/docs/` — documentação da API (Swagger)
- `http://127.0.0.1:8000/admin/` — administração dos dados

## Rodando com Docker

```bash
docker compose up --build
```

## Coletando dados novos

```bash
python manage.py coletar_vagas          
python manage.py coletar_vagas_adzuna   
python manage.py gerar_snapshot         
```

## Testes

```bash
pytest
```


## Algumas decisões que valem explicar

Uso duas fontes de vaga, não uma, porque descobri no meio do processo que o mercado remoto global (Remotive) praticamente não tem vaga júnior — quase tudo é pleno/sênior. O Adzuna, focado no Brasil, tem bem mais. Isso virou parte da própria análise, não só um detalhe técnico.

Skill é uma tabela própria, não um campo de texto solto. Isso evita o problema clássico de "React", "ReactJS" e "React.js" virarem três coisas diferentes na contagem — e faz o cálculo de gap ser um diff direto entre IDs, não uma comparação de string.

O nível da vaga (júnior/pleno/sênior) é inferido olhando título *e* descrição, porque boa parte das vagas brasileiras não deixa isso claro no cargo.
