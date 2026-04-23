import re
import json
import urllib.request
import urllib.parse as up

base = "https://fptshop.com.vn/may-tinh-xach-tay/macbook-neo-13-inch-8gb-256gb"
headers = {"User-Agent": "Mozilla/5.0"}

def get_html(url: str) -> str:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=25) as resp:
        return resp.read().decode("utf-8", "ignore")

def extract_ids(html: str):
    normalized = html.replace('\\\\"', '"').replace('\\\\/', '/')
    m = re.search(r'"comment":(\{.*?"totalCount":\d+.*?\})\s*,\s*"policyProduct"', normalized, flags=re.S)
    if not m:
        return None, []
    payload = json.loads(m.group(1))
    ids = [it.get("id") for it in payload.get("items", []) if isinstance(it, dict) and it.get("id") is not None]
    return payload.get("totalCount"), ids

base_total, base_ids = extract_ids(get_html(base))
print("BASE", base_total, len(base_ids), base_ids[:6])

keys = ["page", "commentPage", "comment_page", "reviewPage", "review_page", "cpage", "p", "currentPage", "offset"]
for k in keys:
    for v in [2, 3, 4, 50]:
        sp = up.urlsplit(base)
        q = dict(up.parse_qsl(sp.query, keep_blank_values=True))
        q[k] = str(v)
        url = up.urlunsplit((sp.scheme, sp.netloc, sp.path, up.urlencode(q), sp.fragment))
        total, ids = extract_ids(get_html(url))
        changed = (ids[:3] != base_ids[:3]) if ids and base_ids else False
        print(f"{k}={v} total={total} n={len(ids)} changed={changed}")
