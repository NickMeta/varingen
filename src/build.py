# -*- coding: utf-8 -*-
"""Bygger de fyra designförslagen till ../site/forslag-N-namn/index.html"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *
from themes import THEMES

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def logo(band="currentColor", mark="currentColor", bg="#fff", size=56, cls="logo"):
    return f'''<svg class="{cls}" viewBox="0 0 100 100" width="{size}" height="{size}" role="img" aria-label="Väringens logotyp: runslinga kring ett hustak och ett V">
<path d="M24.3 80.6 A40 40 0 1 1 66.9 86.3" fill="none" stroke="{band}" stroke-width="8.5" stroke-linecap="round"/>
<path d="M33.1 86.3 A40 40 0 0 1 24.3 80.6" fill="none" stroke="{band}" stroke-width="4" stroke-linecap="round"/>
<path d="M24.3 80.6 A40 40 0 1 1 66.9 86.3" fill="none" stroke="{bg}" stroke-width="1.3" stroke-dasharray="5 3.2" opacity=".75"/>
<ellipse cx="70.5" cy="84" rx="7.2" ry="5.6" transform="rotate(-28 70.5 84)" fill="{band}"/>
<circle cx="72.6" cy="82.4" r="1.3" fill="{bg}"/>
<path d="M27 52 L50 29 L73 52" fill="none" stroke="{mark}" stroke-width="6" stroke-linecap="square" stroke-linejoin="miter"/>
<path d="M35 45 L50 73 L65 45" fill="none" stroke="{mark}" stroke-width="6" stroke-linecap="square" stroke-linejoin="miter"/>
</svg>'''

ROUTER_JS = """<script>
(function(){
 var pages=[].slice.call(document.querySelectorAll('.page'));
 function show(){
  var h=(location.hash||'#hem').slice(1); if(!document.getElementById(h)) h='hem';
  pages.forEach(function(p){p.hidden=p.id!==h});
  [].forEach.call(document.querySelectorAll('[data-nav]'),function(a){a.classList.toggle('active',a.getAttribute('href')==='#'+h)});
  document.body.setAttribute('data-page',h);
  var t=document.getElementById(h); var c=t&&t.style.getPropertyValue('--c'); if(c) document.body.style.setProperty('--page-c',c);
  window.scrollTo(0,0);
  var m=document.querySelector('.menu-open'); if(m) m.classList.remove('menu-open');
 }
 window.addEventListener('hashchange',show); show();
 [].forEach.call(document.querySelectorAll('[data-print]'),function(b){b.addEventListener('click',function(){try{window.print()}catch(e){}})});
 [].forEach.call(document.querySelectorAll('[data-menu]'),function(b){b.addEventListener('click',function(){document.body.classList.toggle('menu-open')})});
})();
</script>"""

def build(theme):
    colors = dict((t[0], t[3]) for t in TOPICS)
    colors.update(theme.get("colors", {}))
    on = theme.get("on_c", {})
    def style(pid):
        s = f"--c:{colors.get(pid, theme['accent'])}"
        if pid in on: s += f";--on-c:{on[pid]}"
        return s
    pages_html = []
    for i, (pid, name, short, _c, desc) in enumerate(TOPICS, 1):
        p = PAGES[pid]
        head = theme["page_head"](pid, name, p["lead"], i, colors[pid])
        pdf = pdf_bar(pid) if pid not in ("forum",) else ""
        pages_html.append(f'<section class="page" id="{pid}" style="{style(pid)}" hidden aria-label="{name}">{head}{pdf}<div class="content">{p["body"]}</div></section>')
    home = theme["home"](colors, logo)
    pages = f'<section class="page" id="hem" style="--c:{theme["accent"]}" aria-label="Start">{home}</section>' + "".join(pages_html)
    html = theme["shell"](pages, colors, logo)
    doc = f'''<!DOCTYPE html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Samfälligheten Väringen – {theme['title']}</title>
<meta name="description" content="Anläggningssamfälligheten Väringen, Runslingan 1–11 i Täby. Information till medlemmarna.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{theme['fonts']}" rel="stylesheet">
<style>{BASE_CSS}{theme['css']}</style></head>
<body class="theme-{theme['slug']}">{html}{ROUTER_JS}</body></html>'''
    return doc

from themes import BASE_CSS

if __name__ == "__main__":
    out = os.path.join(ROOT, "site")
    for n, th in enumerate(THEMES, 1):
        d = os.path.join(out, th["folder"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(build(th))
        print("byggd:", d)
    # logga som fristående fil
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)
    open(os.path.join(out, "assets", "logo-varingen.svg"), "w", encoding="utf-8").write(
        logo("#1f1b16", "#1f1b16", "#ffffff", 200).replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1))
