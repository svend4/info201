# Аудит GitHub-профиля svend4

Дата аудита: 2026-07-02.
Источник: публичный GitHub API и страница профиля `svend4`.

## Краткий вывод
Профиль похож на лабораторию прототипов вокруг `info`/Info OS: агентные системы, RAG/графы знаний, динамические блоки, офлайн-поиск, магазины, социально-юридические сценарии, медицина, робототехника, игры и devtools. Ценность портфеля — ширина идей и повторяющиеся мотивы, из которых можно собрать монорепозиторий-платформу. Главный долг — стандартизация, дедупликация и доказуемые демо.

## Рекомендуемая структура монорепозитория

```text
apps/                 # runnable demos and products
packages/             # reusable libraries and contracts
services/             # agents, search, storage, orchestration
knowledge/            # wiki, ontologies, questions, datasets
domains/              # shop, social/legal, med, robotics, games
docs/                 # architecture, ADR, roadmap
experiments/          # archived prototypes and notebooks
```

## Приоритетные следующие шаги
1. Выбрать 5 якорных проектов: `info40`, `infom`, `ingit`, `daten20`, `info10`/`daten2`.
2. Для каждого якоря добавить воспроизводимое демо и README.
3. Свести дублирующие `info*`, `data*`, `daten*`, `meta*` в карту модулей.
4. Создать общий словарь терминов: Info OS, динамический блок, псевдо-RAG, граф-RAG, агент, шаблон, рационал-программа.
5. Ввести матрицу зрелости: idea → sketch → prototype → demo → product.

## Дополнительные отчёты
- [Синтез по доменам](domain-synthesis.md)
- [Стратегические вопросы](../wiki/questions/strategic-questions.md)

## Навигация
- [Wiki index](../wiki/README.md)
- [Репозитории](../wiki/repositories/)
- [Темы](../wiki/themes/)
