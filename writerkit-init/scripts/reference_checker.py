import re
import urllib.request
import urllib.error
import urllib.parse
import json
from typing import Dict

# SCRIPT DE VALIDAÇÃO DE REFERÊNCIAS (Reference Checker)
# Objetivo: Garantir a veracidade de artigos citados no livro, prevenindo alucinações da IA.

def check_paper_existence(title: str, first_author: str = "") -> bool:
    base_url = "https://api.crossref.org/works?"
    query_params = {"query.title": title, "rows": 3}
    if first_author:
        query_params["query.author"] = first_author
        
    url = base_url + urllib.parse.urlencode(query_params)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'WriterKit-Antigravity/1.0'})
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                items = data.get("message", {}).get("items", [])
                if items:
                    return True
                return False
    except urllib.error.URLError as e:
        print(f"Erro ao acessar CrossRef: {e}")
        return False

def validate_bibtex(bibtex_content: str) -> Dict[str, str]:
    results = {}
    entries = bibtex_content.split("@")
    for entry in entries[1:]:
        title_match = re.search(r'title\s*=\s*[{"]([^}"]+)[}"]', entry, re.IGNORECASE)
        author_match = re.search(r'author\s*=\s*[{"]([^}"]+)[}"]', entry, re.IGNORECASE)
        id_match = re.search(r'^[^\{]+\{([^,]+),', entry)
        
        if title_match and id_match:
            ref_id = id_match.group(1).strip()
            title = title_match.group(1).strip()
            author = author_match.group(1).split(' and ')[0].strip() if author_match else ""
            
            print(f"Verificando referência [{ref_id}]: {title}...")
            is_valid = check_paper_existence(title, author)
            results[ref_id] = "VERIFICADA_E_VALIDA" if is_valid else "FALHA_NA_VERIFICACAO"
            
    return results
