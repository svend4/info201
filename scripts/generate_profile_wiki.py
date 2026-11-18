#!/usr/bin/env python3
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
repos=json.loads((ROOT/'data/svend4_repos.json').read_text(encoding='utf-8'))
W=ROOT/'wiki'; R=ROOT/'reports'
for p in [W, R, W/'repositories', W/'themes', W/'questions']:
    p.mkdir(parents=True, exist_ok=True)

def slug(s): return re.sub(r'[^a-z0-9а-яё]+','-',s.lower()).strip('-')
def theme(r):
    t=' '.join([r['name'], str(r.get('description') or ''), str(r.get('language') or ''), r.get('_readme','')[:1000]]).lower()
    if any(x in t for x in ['agent','агент','claude','llm','rag','avatar','orchestration','оркестр','mcp','ai']): return 'ai-agents-llm'
    if any(x in t for x in ['shop','магазин','flower','цвет','travel','объяв']): return 'commerce-marketplaces'
    if any(x in t for x in ['doc','документ','wiki','вики','news','новости','knowledge','знан','тезаурус','поиск','fts','storage']): return 'knowledge-docs-search'
    if any(x in t for x in ['social','соц','юрид','med','робот','mmo','game','игр']): return 'applied-social-med-robotics-games'
    if any(x in t for x in ['git','ast','runtime','рантайм','devops','микросервис','os','ос','операцион','blocks','блок']): return 'platform-devtools-info-os'
    return 'meta-info-experiments'
for r in repos: r['_theme']=theme(r)
# repo pages
for r in repos:
    files=', '.join(x['name'] for x in r.get('_root_files',[])[:20]) or 'не обнаружены через API'
    readme='есть' if r.get('_readme') else 'нет/пустой'
    desc=r.get('description') or 'без описания'
    txt=f"""# {r['name']}

- URL: {r['html_url']}
- Тема: [{r['_theme']}](../themes/{r['_theme']}.md)
- Описание GitHub: {desc}
- Язык: {r.get('language') or 'не указан'}
- Лицензия: {(r.get('license') or {}).get('spdx_id','не указана') if r.get('license') else 'не указана'}
- Обновлено: {r.get('updated_at')}
- README: {readme}
- Корневые элементы: {files}

## Характеристика
Проект выглядит как часть исследовательской экосистемы `info`: короткое имя, русско-английское описание и ориентация на прототипирование. Потенциал проекта зависит от превращения идеи из описания в воспроизводимый продукт: README, архитектурная схема, сценарии запуска, тесты и демонстрационные данные.

## Плюсы
- Есть публичная точка входа и тематическое описание.
- Название вписывается в общую карту профиля и может быть связано с соседними проектами.
- Подходит для выделения отдельного пакета/сервиса внутри монорепозитория знаний.

## Минусы и пробелы
- Нужны единые стандарты README, лицензии, статуса зрелости и дорожной карты.
- Необходимо явно разделить концепт, прототип, библиотеку, приложение и исследовательские материалы.
- Желательно добавить минимальные тесты/CI или хотя бы smoke-check для запуска.

## Рекомендации
1. Добавить `README.md` по шаблону: цель, аудитория, установка, запуск, архитектура, API/CLI, примеры.
2. Добавить `STATUS.md`: стадия, что работает, что не работает, ближайшие 3 шага.
3. Добавить связи с проектами темы `{r['_theme']}` и отметить зависимые/дублирующие репозитории.
4. Выделить демо-сценарий, который можно проверить за 5 минут.

## Вопросы для уточнения
- Какой главный пользовательский сценарий должен доказывать ценность `{r['name']}`?
- Это самостоятельный продукт, модуль общей Info OS или архив идеи?
- Какие данные/модели/внешние сервисы нужны для минимальной демонстрации?
- Какие 1–2 соседних репозитория нужно объединить с `{r['name']}` в первую очередь?
"""
    (W/'repositories'/f"{r['name']}.md").write_text(txt, encoding='utf-8')
# themes
from collections import defaultdict
g=defaultdict(list)
for r in repos: g[r['_theme']].append(r)
for th, arr in sorted(g.items()):
    lines=[f"# Тема: {th}","",f"Репозиториев: {len(arr)}","","## Репозитории",""]
    for r in arr: lines.append(f"- [{r['name']}](../repositories/{r['name']}.md) — {r.get('description') or 'без описания'}; язык: {r.get('language') or 'не указан'}.")
    lines += ["","## Общая оценка","", "Сильная сторона темы — много идейных прототипов вокруг единой информационной экосистемы. Главный риск — распыление: похожие проекты могут конкурировать за внимание и не иметь единого интерфейса, документации и критериев готовности.","","## Рекомендуемая интеграция","", "- Назначить один `reference implementation` внутри темы.", "- Остальные репозитории классифицировать как модули, датасеты, UI-оболочки, исследования или архивы.", "- Ввести общие контракты: формат данных, API, события, хранение, права доступа, тестовые фикстуры.","","## Инновационные сочетания","", "- Соединить граф знаний + офлайн-поиск + агентную оркестрацию для локальной энциклопедии действий.", "- Соединить динамические блоки + юридические/медицинские домены как систему объяснимых шаблонов решений.", "- Соединить игровые/MMO симуляции + multi-agent orchestration как песочницу проверки стратегий."]
    (W/'themes'/f'{th}.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
# index and report
index=["# Энциклопедия профиля svend4", "", f"Публичный профиль содержит {len(repos)} репозитория, сгруппированных в {len(g)} тем. Данные собраны из GitHub API 2026-07-02.", "", "## Темы"]
for th, arr in sorted(g.items()): index.append(f"- [{th}](themes/{th}.md) — {len(arr)} репозиториев")
index += ["","## Все репозитории"]
for r in repos: index.append(f"- [{r['name']}](repositories/{r['name']}.md) — {r.get('description') or 'без описания'}")
(W/'README.md').write_text('\n'.join(index)+'\n', encoding='utf-8')
summary=f"""# Аудит GitHub-профиля svend4

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

## Навигация
- [Wiki index](../wiki/README.md)
- [Репозитории](../wiki/repositories/)
- [Темы](../wiki/themes/)
"""
(R/'svend4-profile-audit.md').write_text(summary, encoding='utf-8')
print(f'generated {len(repos)} repo pages and {len(g)} theme pages')
