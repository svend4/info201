#!/usr/bin/env python3
import base64, json, time, urllib.error, urllib.request
from pathlib import Path
USER='svend4'
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'
OUT.mkdir(exist_ok=True)

def get(url):
    req=urllib.request.Request(url, headers={'Accept':'application/vnd.github+json','User-Agent':'info201-audit'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())
repos=[]; page=1
while True:
    batch=get(f'https://api.github.com/users/{USER}/repos?per_page=100&page={page}&type=owner&sort=updated')
    if not batch: break
    repos.extend(batch); page+=1
for repo in repos:
    full=repo['full_name']
    try:
        readme=get(f'https://api.github.com/repos/{full}/readme')
        content=base64.b64decode(readme.get('content','')).decode('utf-8', 'replace')
    except Exception as e:
        content=''
    repo['_readme']=content[:20000]
    try:
        contents=get(f'https://api.github.com/repos/{full}/contents')
        repo['_root_files']=[{'name':x['name'],'type':x['type'],'path':x['path']} for x in contents]
    except Exception:
        repo['_root_files']=[]
    time.sleep(0.1)
(OUT/'svend4_repos.json').write_text(json.dumps(repos, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'fetched {len(repos)} repos -> {OUT/"svend4_repos.json"}')
