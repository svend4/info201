# info201 — Аудит GitHub-профиля `svend4` (wiki и генераторы)

На ветке `main` сейчас находятся только файл лицензии [`LICENSE`](LICENSE) и корневой `README.md`. Все скрипты сбора данных, снимок метаданных и сгенерированная русскоязычная wiki-энциклопедия по публичным репозиториям профиля `svend4` размещены в открытой невлитой ветке [`codex`](https://github.com/svend4/info201/tree/codex) (PR [#1](https://github.com/svend4/info201/pull/1)).

## Структура проекта (по ветке `codex`)

```text
.
├── .gitignore                          # Исключения для __pycache__/ и *.py[cod]
├── README.md                           # Обзор проекта на ветке codex
├── data/
│   └── svend4_repos.json               # Снимок метаданных и README 62 репозиториев (2026-07-02)
├── reports/
│   ├── svend4-profile-audit.md         # Сводный аудит профиля и структура монорепозитория
│   └── domain-synthesis.md             # Тематический синтез по доменам
├── scripts/
│   ├── fetch_github_profile.py         # Сбор метаданных и README через GitHub REST API
│   └── generate_profile_wiki.py        # Генерация wiki/ и reports/svend4-profile-audit.md
└── wiki/
    ├── README.md                       # Индекс 62 репозиториев по 6 темам
    ├── questions/strategic-questions.md # Стратегические вопросы и следующие шаги
    ├── repositories/                   # 62 карточки репозиториев (<repo>.md)
    └── themes/                         # 6 тематических обзоров
```

### Тематические группы в `wiki/themes/` (ветка `codex`)

1. `ai-agents-llm.md` (26 репозиториев)
2. `knowledge-docs-search.md` (13 репозиториев)
3. `meta-info-experiments.md` (9 репозиториев)
4. `applied-social-med-robotics-games.md` (6 репозиториев)
5. `commerce-marketplaces.md` (6 репозиториев)
6. `platform-devtools-info-os.md` (2 репозитория)

## Проверенный стек и команды запуска (ветка `codex`)

- **Технологический стек**: Python 3 с использованием только стандартной библиотеки (`urllib.request`, `json`, `base64`, `re`, `pathlib`, `collections`, `time`). Внешние зависимости не требуются.
- **Сбор снимка данных через GitHub API и генерация wiki** (выполнять на ветке `codex`):

```bash
python3 scripts/fetch_github_profile.py
python3 scripts/generate_profile_wiki.py
```

- **Базовые проверки корректности** (указаны и проверены в PR [#1](https://github.com/svend4/info201/pull/1)):

```bash
python3 -m json.tool data/svend4_repos.json
python3 -m py_compile scripts/fetch_github_profile.py scripts/generate_profile_wiki.py
```

## Ветки репозитория

- `main` — базовая ветка, содержит только [`LICENSE`](LICENSE) и корневой `README.md`.
- `codex` — открытый PR [#1](https://github.com/svend4/info201/pull/1) («Add svend4 profile audit wiki and generation scripts»): добавляет `.gitignore`, `data/svend4_repos.json`, Python-скрипты `scripts/`, отчёты `reports/` и 62 карточки в `wiki/`.
- `readme-overview-20261118` — открытый черновик PR [#2](https://github.com/svend4/info201/pull/2) с кратким описанием текущего состояния `main`.
- `claude/audit-wave1` — ветка указывает на тот же коммит, что и `main`, без дополнительных изменений.

## Лицензия

В ветке `main` проект сопровождается лицензией **GNU Affero General Public License v3.0 (AGPL-3.0)** — см. файл [`LICENSE`](LICENSE).
