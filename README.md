# info201 — svend4 profile audit wiki

Этот репозиторий теперь служит монорепозиторием-навигатором для аудита публичных репозиториев GitHub-профиля [`svend4`](https://github.com/svend4?tab=repositories).

## Что внутри

- `data/svend4_repos.json` — снимок публичных метаданных репозиториев и README, полученный через GitHub API.
- `reports/svend4-profile-audit.md` — основной обзор профиля, выводы и рекомендуемая структура монорепозитория.
- `reports/domain-synthesis.md` — подробный тематический синтез по AI, документам, commerce, social/legal, medical, robotics, games и devtools.
- `wiki/README.md` — энциклопедический индекс всех репозиториев и тем.
- `wiki/repositories/` — карточка для каждого репозитория: характеристика, плюсы, минусы, рекомендации и вопросы.
- `wiki/themes/` — тематические страницы с группировкой репозиториев и идеями интеграции.
- `wiki/questions/strategic-questions.md` — стратегические вопросы, варианты ответов и следующие действия.
- `scripts/fetch_github_profile.py` — скрипт сбора публичных данных GitHub.
- `scripts/generate_profile_wiki.py` — генератор wiki-страниц из собранных метаданных.

## Быстрый старт

```bash
python3 scripts/fetch_github_profile.py
python3 scripts/generate_profile_wiki.py
```

После генерации откройте [`wiki/README.md`](wiki/README.md) и [`reports/svend4-profile-audit.md`](reports/svend4-profile-audit.md).

## Главный вывод

Профиль `svend4` выглядит как R&D-экосистема вокруг Info OS: local/offline-first документы, GraphRAG, агентная оркестрация, Claude/MCP, AI-generated code runtime, commerce/flower-shop, social/legal documents, triage, robotics и terminal/MMO simulation. Основная рекомендация — не добавлять ещё один изолированный проект, а упаковать 3–5 flagship-линий и связать их общей wiki, схемой метаданных, roadmap и воспроизводимыми demos.
