# Синтез аудита по доменам svend4

Дата: 2026-07-02.

## 1. AI / агенты / LLM / локальная разработка

**Ключевые проекты:** `info40`, `info100`, `info30`, `info20`, `infom`, `daten22`, `universal-file-storage-mcp`, `ingit`, `meta1`, `meta10`, `info2`, `in4`, `data50`.

**Характеристика:** это самый стратегический слой профиля. Он может стать общей платформой для остальных направлений: агенты получают доступ к файлам через MCP, знания через GraphRAG/псевдо-RAG, задачи и документацию через Git/YAML, а кодовые изменения — через воспроизводимый runtime.

**Плюсы:**
- Сильная философия offline/local-first.
- Есть современные строительные блоки: MCP, GraphRAG, agent orchestration, deterministic runtime, AST-инструменты.
- Хорошо сочетается с личной wiki и DMS.

**Минусы:**
- Много пересекающихся репозиториев без явного флагмана.
- Нужны installation guides, CI, smoke demos, topics, maturity badges.
- Требуется единая терминология: agent, skill, block, graph, pseudo-RAG, Info OS.

**Рекомендация:** назначить `info40` runtime/marketplace-слоем, `info100` лабораторией проверки агентов, `infom` графовым знанием, `ingit` оболочкой управления проектами, `universal-file-storage-mcp` файловым адаптером.

## 2. Документы / wiki / знания / поиск

**Ключевые проекты:** `daten20`, `daten11`, `data70`, `data10`, `meta2`, `information`, `info15`, `info4`, `info3`, `info5`, `daten22`.

**Характеристика:** профиль содержит основу для Personal Knowledge & Document OS: импорт документов, OCR, восстановление фрагментов, метаданные, поиск, wiki-экспорт, архив разговоров и тематические энциклопедии.

**Плюсы:**
- `data70` может стать демонстрационным корпусом для индексации и GraphRAG.
- `daten20` и `meta2` закрывают разные уровни документного пайплайна.
- `data10` подходит для юридических/нормативных текстов как динамических блоков.

**Минусы:**
- Риск knowledge sprawl: много баз знаний без единой схемы идентификаторов.
- Нужна унификация JSON/YAML/frontmatter/SQLite.
- Нужны правила приватности, анонимизации и цитирования источников.

**Рекомендация:** создать `metadata.schema.json`, общий словарь терминов и pipeline: import → OCR/text → metadata → index → graph → wiki → agent answers with citations.

## 3. Commerce / flower shop / marketplace

**Ключевые проекты:** `data40`, `daten2`, `meta4`, `info10`, `daten23`, `info7`, `daten6`, `daten8`.

**Характеристика:** самый понятный прикладной демо-домен: цветочный магазин, каталог, корзина, заказы, доставка, CRM, конкурентный мониторинг, AI-флорист.

**Плюсы:**
- Ясный пользователь и бизнес-сценарий.
- Можно быстро показать UI/demo.
- Хорошо использует алгоритмы оптимизации маршрутов и динамические каталоги.

**Минусы:**
- Неясно, какой репозиторий является canonical flower shop.
- Требуются платежи, доставка, CRM, privacy policy, deployment.
- Часть проектов выглядит как дубликаты/заготовки.

**Рекомендация:** выбрать `data40` как витрину/PWA, `daten2` как backend reference, `info7` как AI-бот, `daten8` как мониторинг рынка.

## 4. Social / legal / public service

**Ключевые проекты:** `soz150`, `data4`, `daten20`, `data10`, `info15`, `information`, `meta2`, `ingit`.

**Характеристика:** направление может стать local-first Legal/Social Document OS: документы, шаблоны заявлений, динамические блоки законов, аудит версий и помощь в сборе пакетов документов.

**Плюсы:**
- Реальная прикладная боль: документы, обращения, сроки, доказательства.
- Хорошо сочетается с DMS, OCR, wiki, Git-versioned case files.
- Можно строить объяснимые шаблоны вместо непрозрачных ответов LLM.

**Минусы:**
- Высокие требования к точности, юрисдикции, отказам от юридической консультации.
- Требуется контроль персональных данных, шифрование, audit trail.
- Нужно различать информационную помощь и профессиональную консультацию.

**Рекомендация:** начать с генерации черновиков и чеклистов, не с юридических выводов; все ответы привязывать к источникам, версии шаблона и юрисдикции.

## 5. Medical / triage / rehabilitation

**Ключевые проекты:** `info150`, `data2`, `daten20`, `infon`, `robot`.

**Характеристика:** потенциально сильная R&D-линия: triage, home care, rescue, sport safety, driver monitoring, low-bandwidth terminal communication and robot-assisted workflows.

**Плюсы:**
- Уникальная комбинация triage + terminal video + document/case management.
- Cross-domain adaptations повышают исследовательскую ценность.
- Можно использовать как simulation/training tool.

**Минусы:**
- Медицинский риск: необходимы disclaimers, validation, clinical evidence, privacy.
- Нельзя позиционировать как замену специалиста.
- Нужны тестовые сценарии, ground truth, error analysis.

**Рекомендация:** маркировать как research/decision-support/training, а не clinical product; сделать демонстрацию на синтетических данных.

## 6. Robotics / embodied AI

**Ключевые проекты:** `robot`, `data2`, `info150`, `info40`, `infon`.

**Характеристика:** направление skill marketplace для роботов, домашние/медицинские/спасательные сценарии, экономика навыков, governance и возможная телеметрия/телеприсутствие.

**Плюсы:**
- Есть не только кодовая, но и экономико-управленческая постановка: store, licensing, governance.
- Хорошо сочетается с agent marketplace.
- Может использовать medical/home-care use cases.

**Минусы:**
- Неясна целевая платформа: ROS2, Unitree, Hyundai, simulator.
- Нужны sandboxing, permissions, safety certification, rollback.
- Вероятно много концептов и мало executable SDK.

**Рекомендация:** начать с simulator-first SDK и каталога навыков с метаданными совместимости/риска.

## 7. Games / MMO / simulation

**Ключевые проекты:** `data7`, `infon`, `daten1`, `pro2`, `meta`, `info150`.

**Характеристика:** игровая ветка может быть лабораторией симуляции: AI director, terminal shared worlds, quest optimization, economy balancing, rescue/triage training.

**Плюсы:**
- Игры дают безопасную среду для проверки агентов и оптимизаторов.
- `data7` может переиспользоваться для маршрутизации доставки и спасательных сценариев.
- `infon` даёт необычный low-bandwidth UI.

**Минусы:**
- Нужны runnable simulations/benchmarks.
- Нужно отделить алгоритмическую библиотеку от игрового frontend.
- Требуются метрики качества и воспроизводимые сценарии.

**Рекомендация:** сделать один terminal simulation demo: карта, задачи, AI director, маршрут, оценка усталости/экономики.

## 8. Главные инновационные комбинации

1. **AI Dev Workbench:** `ingit` + `meta1` + `info40` + `info100` + `meta10` + `universal-file-storage-mcp`.
2. **Personal Knowledge & Document OS:** `daten20` + `daten11` + `infom` + `data70` + `info30`.
3. **Legal/Social Document OS:** `daten20` + `data10` + `soz150` + `ingit` + `meta2`.
4. **Flower Commerce OS:** `data40` + `daten2` + `info7` + `daten8` + `data7`.
5. **Remote Triage & Rescue:** `info150` + `infon` + `daten20` + `robot` + `data2`.
6. **Terminal AI Simulation Lab:** `data7` + `infon` + `meta` + `pro2` + `info150`.

## 9. Рекомендуемый monorepo map

```text
apps/
  flower-commerce/
  legal-social-assistant/
  triage-simulation/
  terminal-mmo-lab/
packages/
  metadata-schema/
  dynamic-blocks/
  code-thesaurus/
  ast-tools/
services/
  file-storage-mcp/
  document-processor/
  graph-rag/
  agent-orchestrator/
knowledge/
  profile-wiki/
  repo-cards/
  glossary/
  questions/
domains/
  commerce/
  social-legal/
  medical-triage/
  robotics/
  games/
experiments/
  archived-info-data-daten-meta/
```
