import re, json, sys, requests, concurrent.futures as cf
from bs4 import BeautifulSoup
H={"User-Agent":"Mozilla/5.0 (compatible; AISLABZ-audit)"}
urls=[]
for sm in ["page-sitemap.xml","treatments-sitemap.xml"]:
    x=requests.get("https://lumosclinics.com/"+sm,headers=H,timeout=30).text
    urls+=re.findall(r"<loc>([^<]+)</loc>",x)
def get(u):
    try:
        r=requests.get(u,headers=H,timeout=40,allow_redirects=True)
    except Exception as e:
        return {"url":u,"err":str(e)}
    s=BeautifulSoup(r.text,"html.parser")
    t=s.title.get_text(strip=True) if s.title else ""
    md=s.find("meta",attrs={"name":"description"})
    rb=s.find("meta",attrs={"name":"robots"})
    can=s.find("link",rel="canonical")
    types=[]
    for sc in s.find_all("script",type="application/ld+json"):
        try:
            d=json.loads(sc.string or "{}")
            items=d.get("@graph",[d]) if isinstance(d,dict) else d
            for i in items:
                tt=i.get("@type") if isinstance(i,dict) else None
                types+= tt if isinstance(tt,list) else [tt]
        except Exception: types.append("PARSE_ERR")
    imgs=s.find_all("img"); noalt=[i for i in imgs if not (i.get("alt") or "").strip()]
    for x in s(["script","style","noscript"]): x.decompose()
    words=len(s.get_text(" ").split())
    return {"url":u,"final":r.url,"code":r.status_code,"bytes":len(r.content),"title":t,"tlen":len(t),
      "desc":md.get("content","") if md else "","robots":rb.get("content","") if rb else "",
      "canonical":can.get("href") if can else "","h1":[h.get_text(" ",strip=True)[:80] for h in s.find_all("h1")],
      "h2n":len(s.find_all("h2")),"schema":[x for x in types if x],"imgs":len(imgs),"noalt":len(noalt),"words":words}
with cf.ThreadPoolExecutor(8) as ex: res=list(ex.map(get,urls))
json.dump(res,open("crawl.json","w"),indent=1)
print(len(res))
