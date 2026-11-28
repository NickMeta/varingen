from photo_b64 import SRC as PHOTO
# -*- coding: utf-8 -*-
from content import TOPICS, NEWS, DATES, icon, photo, TOPIC

BASE_CSS = r"""
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:var(--font-body);color:var(--ink);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased;font-size:16.5px}
a{color:inherit}img,svg{max-width:100%}
.page[hidden]{display:none!important}
.tbd{background:#fff1bf;color:#5a4500;padding:.05em .4em;border-radius:4px;font-size:.9em;border:1px dashed #d4ac34;font-weight:500}
h1,h2,h3{font-family:var(--font-head);line-height:1.15;margin:0;font-weight:var(--head-w,600)}
.content h2{font-size:1.5rem;margin:2.6rem 0 1rem}
.content p{margin:.6rem 0}
.muted,.note{color:var(--muted)}.note{font-size:.9rem}
.grid{display:grid;gap:1rem}.g2{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}.g3{grid-template-columns:repeat(auto-fit,minmax(210px,1fr))}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:1.25rem 1.35rem}
.card h3{font-size:1.1rem;margin-bottom:.5rem;display:flex;align-items:center;gap:.55rem}
.card p{margin:.3rem 0}.card.ok{box-shadow:inset 0 4px 0 #3f8a3c}.card.no{box-shadow:inset 0 4px 0 #c0452b}
.dot{width:.8rem;height:.8rem;border-radius:50%;display:inline-block;flex:none}
.list{margin:.4rem 0;padding-left:1.15rem}.list li{margin:.28rem 0}
.list.check{list-style:none;padding:0}.list.check li{padding-left:1.75rem;position:relative}
.list.check li:before{content:"";position:absolute;left:.25rem;top:.5em;width:.75rem;height:.4rem;border-left:2px solid var(--c);border-bottom:2px solid var(--c);transform:rotate(-45deg)}
.callout{display:block;margin:1.6rem 0;padding:1.15rem 1.35rem;border-radius:var(--radius);background:color-mix(in srgb,var(--c) 9%,var(--surface));border-left:4px solid var(--c)}
.callout strong{display:block;margin-bottom:.3rem;font-family:var(--font-head);font-size:1.05rem}
.callout .list{margin-bottom:0}.callout.warn{--c:#c27a12}
.facts{margin:1.2rem 0;border-top:1px solid var(--line)}
.facts>div{display:grid;grid-template-columns:minmax(150px,230px) 1fr;gap:1rem;padding:.8rem 0;border-bottom:1px solid var(--line)}
.facts dt{color:var(--muted);font-size:.93rem}.facts dd{margin:0;font-weight:500}
.table{border-top:1px solid var(--line)}
.table>div{display:flex;justify-content:space-between;gap:1rem;padding:.8rem 0;border-bottom:1px solid var(--line)}.table span{color:var(--muted);text-align:right}
.sched>div{display:grid!important;grid-template-columns:5rem 1fr 1fr;gap:1rem}.sched .sh{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}.sched span{text-align:left!important}
.steps{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.6rem}
.steps li{padding:1rem 1.1rem;border-radius:var(--radius);border:1px solid var(--line);background:var(--surface);display:flex;flex-direction:column}
.steps li span{color:var(--muted);font-size:.92rem}.steps li.done{border-color:var(--c)}
.steps li.now{background:var(--c);color:var(--on-c,#fff);border-color:var(--c)}.steps li.now span{color:inherit;opacity:.85}
.projects{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:.8rem}
.projects>div{padding:1rem 1.1rem;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface)}
.projects p{margin:.2rem 0 0;color:var(--muted);font-size:.92rem}.projects b{display:block;margin-top:.55rem}
.chip{display:inline-block;font-size:.7rem;letter-spacing:.07em;text-transform:uppercase;font-weight:700;padding:.22rem .6rem;border-radius:99px;background:var(--c);color:var(--on-c,#fff);white-space:nowrap}
.chip.soft{background:transparent;color:var(--c);border:1px solid var(--c)}
details{border-bottom:1px solid var(--line);padding:.85rem 0}summary{cursor:pointer;font-weight:600}
.date-card{padding:1.35rem 1.5rem;border-radius:var(--radius);background:var(--c);color:var(--on-c,#fff);display:flex;flex-direction:column}
.date-card b{font-family:var(--font-head);font-size:1.7rem;line-height:1.2}.date-card small{opacity:.8}
.docs h3{margin:1.7rem 0 .5rem;font-size:.78rem;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);font-family:var(--font-body)}
.docs a{display:grid;grid-template-columns:1fr auto;padding:.9rem 1.1rem;border:1px solid var(--line);border-radius:var(--radius);margin:.45rem 0;text-decoration:none;background:var(--surface);transition:border-color .15s}
.docs a span{color:var(--muted);font-size:.9rem;grid-column:1}
.docs a em{grid-row:1/3;grid-column:2;align-self:center;font-style:normal;font-size:.72rem;font-weight:700;color:var(--c);border:1px solid var(--c);border-radius:6px;padding:.25rem .55rem}
.docs a:hover{border-color:var(--c)}
.welcome{list-style:none;padding:0;counter-reset:w}
.welcome li{counter-increment:w;position:relative;padding:.85rem 0 .85rem 3.3rem;border-bottom:1px solid var(--line)}
.welcome li:before{content:counter(w);position:absolute;left:0;top:.75rem;width:2.25rem;height:2.25rem;border-radius:50%;background:var(--c);color:var(--on-c,#fff);display:grid;place-items:center;font-weight:700;font-family:var(--font-head)}
.bars{display:grid;gap:.6rem;margin:1.1rem 0}
.bar{display:grid;grid-template-columns:minmax(160px,240px) 1fr 84px;align-items:center;gap:.9rem;font-size:.93rem}
.bar i{display:block;height:.7rem;border-radius:99px;background:linear-gradient(90deg,var(--c) var(--w),color-mix(in srgb,var(--c) 12%,transparent) var(--w))}
.bar b{text-align:right;font-variant-numeric:tabular-nums;font-weight:600}
.timeline{list-style:none;padding:0;border-left:2px solid var(--c);margin:1rem 0 1rem .5rem}
.timeline li{padding:.35rem 0 1rem 1.5rem;position:relative}
.timeline li:before{content:"";position:absolute;left:-8px;top:.7rem;width:14px;height:14px;border-radius:50%;background:var(--bg);border:2px solid var(--c)}
.timeline b{display:block;font-family:var(--font-head);font-size:1.1rem}.timeline span{color:var(--muted)}
.prose{max-width:68ch}
.photo{margin:1rem 0;border-radius:var(--radius);background:repeating-linear-gradient(135deg,color-mix(in srgb,var(--c) 11%,var(--surface)) 0 14px,color-mix(in srgb,var(--c) 5%,var(--surface)) 14px 28px);display:grid;place-items:center;border:1px dashed color-mix(in srgb,var(--c) 40%,transparent);color:var(--muted);font-size:.88rem;min-height:140px}
.photo span{display:flex;gap:.5rem;align-items:center;background:var(--surface);padding:.45rem .9rem;border-radius:99px}
.threads a{display:flex;align-items:center;gap:1rem;padding:1rem 1.1rem;border:1px solid var(--line);border-radius:var(--radius);margin:.5rem 0;background:var(--surface);flex-wrap:wrap;text-decoration:none}
.threads b{flex:1;min-width:200px}.threads small{color:var(--muted)}
.pdfbar{display:flex;gap:.6rem;flex-wrap:wrap;margin:1.5rem 0 .5rem}
.btn{display:inline-flex;align-items:center;gap:.5rem;padding:.62rem 1.05rem;border-radius:var(--btn-r,99px);font:inherit;font-size:.9rem;font-weight:600;cursor:pointer;text-decoration:none;border:1px solid transparent;line-height:1.2}
.btn-pdf{background:var(--c);color:var(--on-c,#fff)}.btn-ghost{background:transparent;border-color:var(--line);color:var(--ink)}
.btn:focus-visible,a:focus-visible{outline:2px solid var(--c);outline-offset:2px}
.ico{flex:none}
@media(max-width:640px){.facts>div{grid-template-columns:1fr;gap:.1rem}.bar{grid-template-columns:1fr 76px}.bar i{grid-column:1/3;grid-row:2}.table>div{flex-direction:column;gap:.1rem}.table span{text-align:left}.content h2{font-size:1.3rem}}
@media print{header,nav,footer,aside.sidebar,.tabs,.pdfbar,.no-print{display:none!important}body{background:#fff!important;color:#000!important}.page{display:block}.page[hidden]{display:none!important}}
"""

def nav_links(cls="", show_icon=False, short=False, colors=None, extra_home=True):
    out = []
    if extra_home:
        out.append(f'<a href="#hem" data-nav class="{cls}" style="--c:var(--accent)">{icon("hem",18) if show_icon else ""}<span>Start</span></a>')
    for pid, name, sh, c, _ in TOPICS:
        c = (colors or {}).get(pid, c)
        out.append(f'<a href="#{pid}" data-nav class="{cls}" style="--c:{c}">{icon(pid,18) if show_icon else ""}<span>{sh if short else name}</span></a>')
    return "".join(out)

def news_items(colors, tpl):
    return "".join(tpl(when, title, text, pid, colors[pid]) for when, title, text, pid in NEWS)

# =====================================================================
# 1. RUNSTEN – ljus, redaktionell, serif
# =====================================================================
RUNE_BAND = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='10'%3E%3Cpath d='M0 9 L7 1 L14 9 L21 1 L28 9' fill='none' stroke='%238e3b2e' stroke-width='1.2'/%3E%3C/svg%3E\")"

T1_CSS = r"""
:root{--bg:#f5f1e8;--surface:#fffdf8;--ink:#1f1b16;--muted:#6d655a;--line:#e2dacb;--radius:3px;--btn-r:2px;--accent:#8e3b2e;--font-head:'Fraunces',Georgia,serif;--font-body:'Inter',system-ui,sans-serif;--head-w:500}
.topline{font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);text-align:center;padding:.55rem 1rem;border-bottom:1px solid var(--line)}
.masthead{text-align:center;padding:2.2rem 1rem 1.2rem}
.masthead a{text-decoration:none;display:inline-flex;flex-direction:column;align-items:center;gap:.5rem}
.masthead .word{font-family:var(--font-head);font-size:clamp(2.2rem,5vw,3.4rem);letter-spacing:.02em;line-height:1}
.masthead .tag{font-size:.78rem;letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
.band{height:10px;background:RUNEBAND repeat-x center;opacity:.55;margin:0 auto;max-width:1120px}
nav.main{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
nav.main .in{max-width:1180px;margin:0 auto;display:flex;gap:.2rem;overflow-x:auto;padding:0 1rem;scrollbar-width:none;justify-content:safe center}
nav.main a{white-space:nowrap;text-decoration:none;font-size:.86rem;padding:.9rem .7rem;display:flex;align-items:center;gap:.45rem;border-bottom:2px solid transparent;color:var(--muted)}
nav.main a:before{content:"";width:7px;height:7px;background:var(--c)}
nav.main a:hover,nav.main a.active{color:var(--ink);border-bottom-color:var(--c)}
main{max-width:1120px;margin:0 auto;padding:0 1.25rem 5rem}
.page:not(#hem){max-width:860px;margin:0 auto;padding-top:3.2rem}
.phead{border-left:5px solid var(--c);padding-left:1.4rem}
.kicker{font-size:.75rem;letter-spacing:.18em;text-transform:uppercase;color:var(--c);font-weight:600;display:flex;align-items:center;gap:.5rem}
.phead h1{font-size:clamp(2.3rem,5vw,3.4rem);margin:.4rem 0 .7rem}
.phead .lead{font-size:1.2rem;color:var(--muted);margin:0;font-family:var(--font-head);font-weight:300;line-height:1.45}
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:3rem;align-items:center;padding:3.5rem 0 3rem}
.hero h1{font-size:clamp(2.4rem,5.4vw,4.2rem);font-weight:400;line-height:1.04;letter-spacing:-.01em}
.hero h1 em{font-style:italic;color:var(--accent)}
.hero p{font-size:1.15rem;color:var(--muted);max-width:48ch;margin:1.2rem 0 1.6rem}
.hero-img{margin:0;border-radius:var(--radius);overflow:hidden;aspect-ratio:4/3;box-shadow:0 20px 40px -24px rgba(31,27,22,.5)}.hero-img img{width:100%;height:100%;object-fit:cover;object-position:42% 62%;display:block}
.btn-solid{background:var(--ink);color:var(--bg)}.btn-line{border-color:var(--ink);color:var(--ink)}
.sec-title{display:flex;align-items:baseline;justify-content:space-between;border-top:1px solid var(--ink);padding-top:.8rem;margin:3.5rem 0 1.5rem}
.sec-title h2{font-size:1.6rem}.sec-title span{font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.news{display:grid;grid-template-columns:repeat(4,1fr);gap:1.8rem}
.news a{text-decoration:none;border-top:3px solid var(--c);padding-top:1rem;display:block}
.news small{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--c);font-weight:600}
.news h3{font-size:1.3rem;margin:.4rem 0 .5rem}.news p{color:var(--muted);font-size:.95rem;margin:0}
.cal{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid var(--line);background:var(--surface)}
.cal div{padding:1.4rem;border-right:1px solid var(--line)}.cal div:last-child{border:0}
.cal b{font-family:var(--font-head);font-size:2.6rem;font-weight:300;line-height:1;display:block}
.cal i{font-style:normal;font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.cal p{margin:.6rem 0 0;font-size:.95rem}.cal em{font-size:.75rem;color:var(--accent);font-style:normal}
.index{display:grid;grid-template-columns:1fr 1fr;column-gap:3rem}
.index a{display:grid;grid-template-columns:3rem 1fr auto;align-items:baseline;gap:.4rem;padding:1.1rem 0;border-bottom:1px solid var(--line);text-decoration:none}
.index .n{font-family:var(--font-head);color:var(--c);font-size:1.05rem}
.index b{font-family:var(--font-head);font-weight:500;font-size:1.3rem;display:block}.index span{color:var(--muted);font-size:.9rem}
.index .arr{color:var(--c);transition:transform .2s}.index a:hover .arr{transform:translateX(4px)}
footer{background:#1f1b16;color:#d9d1c2;padding:3rem 1.25rem}
footer .in{max-width:1120px;margin:0 auto;display:flex;gap:2rem;justify-content:space-between;flex-wrap:wrap;align-items:center}
footer .word{font-family:var(--font-head);font-size:1.6rem;color:#fff}footer small{color:#a39a8b}
footer a{color:#e8d9c0}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero-img{aspect-ratio:16/10}.news,.cal{grid-template-columns:1fr 1fr}.index{grid-template-columns:1fr}.cal div:nth-child(2){border-right:0}.cal div{border-bottom:1px solid var(--line)}}
@media(max-width:520px){.news,.cal{grid-template-columns:1fr}}
""".replace("RUNEBAND", RUNE_BAND)

ROMAN = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV"]

def t1_head(pid, name, lead, i, c):
    return f'<div class="phead"><div class="kicker">{icon(pid,16)} Väringen · {ROMAN[i-1]}</div><h1>{name}</h1><p class="lead">{lead}</p></div>'

def t1_home(colors, logo):
    news = news_items(colors, lambda w,t,x,p,c: f'<a href="#{p}" style="--c:{c}"><small>{w}</small><h3>{t}</h3><p>{x}</p></a>')
    cal = "".join(f'<div><b>{a}</b><i>{b}</i><p>{t}</p><em>{n}</em></div>' for a,b,t,n in DATES)
    idx = "".join(f'<a href="#{pid}" style="--c:{colors[pid]}"><span class="n">{ROMAN[i]}</span><div><b>{name}</b><span>{d}</span></div><span class="arr">→</span></a>' for i,(pid,name,s,c,d) in enumerate(TOPICS))
    return f'''<div class="hero"><div><div class="kicker" style="--c:var(--accent)">Runslingan 1–11 · Täby kyrkby</div>
<h1 style="margin-top:.8rem">Tjugoåtta hus. <em>En</em> gemensam gård.</h1>
<p>Här hittar du allt som rör Väringen – från sophämtning och parkering till städdagar, laddstolpar och årsstämmans protokoll.</p>
<div style="display:flex;gap:.6rem;flex-wrap:wrap"><a class="btn btn-solid" href="#ny-har">Ny i Väringen</a><a class="btn btn-line" href="#kontakt">Kontakta styrelsen</a></div></div>
<figure class="hero-img"><img src="{PHOTO}" alt="Husen och garagelängorna på Runslingan en solig vårdag"></figure></div>
<div class="sec-title"><h2>Aktuellt</h2><span>Hösten 2026</span></div><div class="news">{news}</div>
<div class="sec-title"><h2>Kalender</h2><span>Kommande</span></div><div class="cal">{cal}</div>
<div class="sec-title"><h2>Allt om föreningen</h2><span>Tretton avsnitt</span></div><div class="index">{idx}</div>'''

def t1_shell(pages, colors, logo):
    return f'''<div class="topline">Anläggningssamfälligheten Väringen · Runslingan 1–11 · Täby</div>
<header class="masthead"><a href="#hem">{logo("#1f1b16","#1f1b16","#f5f1e8",76)}<span class="word">Väringen</span><span class="tag">Anläggningssamfälligheten · Täby</span></a></header>
<div class="band"></div>
<nav class="main" aria-label="Huvudmeny"><div class="in">{nav_links(colors=colors, short=True)}</div></nav>
<main>{pages}</main>
<footer><div class="in"><div style="display:flex;gap:1rem;align-items:center">{logo("#f5f1e8","#f5f1e8","#1f1b16",48)}<div><div class="word">Väringen</div><small>Anläggningssamfälligheten Väringen · Runslingan 1–11, Täby</small></div></div>
<div><small>Frågor? <a href="#kontakt">Kontakta styrelsen</a> · <a href="https://varinge.wordpress.com/">Gamla hemsidan</a></small></div></div></footer>'''

# =====================================================================
# 2. FJÄLL – modern, bento-rutnät, färgstarka kort
# =====================================================================
T2_CSS = r"""
:root{--bg:#f1f2f4;--surface:#fff;--ink:#101317;--muted:#5b636e;--line:#e3e6ea;--radius:18px;--accent:#101317;--font-head:'Plus Jakarta Sans',system-ui,sans-serif;--font-body:'Plus Jakarta Sans',system-ui,sans-serif;--head-w:700}
h1,h2,h3{letter-spacing:-.025em}
.bar-top{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.86);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.bar-top .in{max-width:1240px;margin:0 auto;display:flex;align-items:center;gap:1rem;padding:.6rem 1.25rem}
.brand svg{flex:none}.brand{display:flex;align-items:center;gap:.6rem;text-decoration:none;font-weight:800;font-size:1.15rem;letter-spacing:-.02em}
.brand small{display:block;font-weight:500;font-size:.72rem;color:var(--muted);letter-spacing:0}
.pills{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:.3rem;margin-left:auto;padding:.2rem}
@media(max-width:980px){.pills{flex-wrap:nowrap;justify-content:flex-start;overflow-x:auto;scrollbar-width:none;padding-right:2.4rem;-webkit-mask-image:linear-gradient(90deg,#000 calc(100% - 3rem),transparent);mask-image:linear-gradient(90deg,#000 calc(100% - 3rem),transparent)}.bar-top .in{position:relative;flex-wrap:wrap;row-gap:.3rem}.pills{order:3;width:100%;margin-left:0}.bar-top .in:after{content:"›";position:absolute;right:.9rem;bottom:.45rem;font-size:1.6rem;font-weight:700;color:var(--muted);pointer-events:none}}
.pills a{white-space:nowrap;text-decoration:none;font-size:.82rem;font-weight:600;padding:.45rem .8rem;border-radius:99px;display:flex;align-items:center;gap:.4rem;color:var(--muted)}
.pills a:before{content:"";width:8px;height:8px;border-radius:50%;background:var(--c)}
.pills a:hover{background:var(--bg);color:var(--ink)}.pills a.active{background:var(--c);color:var(--on-c,#fff)}.pills a.active:before{background:currentColor}
main{max-width:1240px;margin:0 auto;padding:1.4rem 1.25rem 5rem}
.hero2{background:#101317;color:#fff;border-radius:28px;padding:clamp(1.8rem,5vw,3.6rem);display:grid;grid-template-columns:1.3fr .7fr;gap:2rem;align-items:end;position:relative;overflow:hidden}
.hero2 h1{font-size:clamp(2.2rem,5vw,3.8rem);line-height:1.02;font-weight:800}
.hero2 p{color:#b9c0c9;font-size:1.1rem;max-width:46ch}
.hero2 .bg{position:absolute;right:-60px;top:-60px;opacity:.09}
.hero2 .q{display:flex;flex-direction:column;gap:.5rem;position:relative}
.hero2 .q a{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:.8rem 1rem;text-decoration:none;display:flex;justify-content:space-between;font-weight:600}
.hero2 .q a:hover{background:rgba(255,255,255,.14)}
.bento{display:grid;grid-auto-flow:dense;grid-template-columns:repeat(4,1fr);grid-auto-rows:170px;gap:1rem;margin:1rem 0}
.tile{background:var(--c);color:var(--on-c,#fff);border-radius:22px;padding:1.3rem;text-decoration:none;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden;transition:transform .2s}
.tile:hover{transform:translateY(-3px)}
.tile .ico{width:30px;height:30px}
.tile h3{font-size:1.25rem}.tile p{margin:.25rem 0 0;font-size:.85rem;opacity:.82;line-height:1.4}
.tile.big{grid-column:span 2;grid-row:span 2}.tile.big h3{font-size:2rem}.tile.big .ico{width:44px;height:44px}.tile.big p{font-size:1rem;max-width:30ch}
.tile.wide{grid-column:span 2}
.tile .go{position:absolute;right:1.1rem;top:1.1rem;width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,.18);display:grid;place-items:center}
.row2{display:grid;grid-template-columns:1.6fr 1fr;gap:1rem;margin-top:1rem}
.panel{background:var(--surface);border-radius:22px;padding:1.5rem;border:1px solid var(--line)}
.panel h2{font-size:1.25rem;margin-bottom:1rem}
.newsl a{display:grid;grid-template-columns:auto 1fr;gap:.9rem;padding:.85rem 0;border-top:1px solid var(--line);text-decoration:none;align-items:start}
.newsl .ic{width:40px;height:40px;border-radius:12px;background:var(--c);color:var(--on-c,#fff);display:grid;place-items:center}
.newsl small{color:var(--muted);font-weight:600;font-size:.75rem}.newsl b{display:block}.newsl p{margin:.1rem 0 0;color:var(--muted);font-size:.9rem}
.cal2 div{display:grid;grid-template-columns:56px 1fr;gap:.9rem;align-items:center;padding:.6rem 0}
.cal2 .d{background:var(--bg);border-radius:14px;text-align:center;padding:.4rem 0;line-height:1.1}
.cal2 .d b{display:block;font-size:1.25rem}.cal2 .d i{font-style:normal;font-size:.7rem;text-transform:uppercase;color:var(--muted);font-weight:700}
.cal2 em{font-style:normal;font-size:.75rem;color:var(--muted)}
.page:not(#hem){margin-top:-.2rem}
.phead2{background:var(--c);color:var(--on-c,#fff);border-radius:28px;padding:clamp(1.8rem,5vw,3.2rem);position:relative;overflow:hidden}
.phead2 .ic{width:58px;height:58px;border-radius:18px;background:rgba(255,255,255,.16);display:grid;place-items:center;margin-bottom:1.1rem}
.phead2 .ic .ico{width:30px;height:30px}
.phead2 h1{font-size:clamp(2.2rem,5vw,3.4rem);font-weight:800}.phead2 p{font-size:1.15rem;opacity:.86;max-width:52ch;margin:.6rem 0 0}
.phead2 .num{position:absolute;right:2rem;top:1rem;font-size:8rem;font-weight:800;opacity:.08;line-height:1}
.page:not(#hem) .pdfbar{margin:-4.2rem clamp(1.5rem,5vw,3.2rem) 0;position:relative}
.page:not(#hem) .btn-pdf{background:#fff;color:#101317}.page:not(#hem) .btn-ghost{border-color:rgba(255,255,255,.4);color:var(--on-c,#fff)}
.page:not(#hem) .content{background:var(--surface);border-radius:24px;padding:clamp(1.3rem,4vw,2.6rem);margin-top:1.2rem;border:1px solid var(--line)}
.content>h2:first-child,.content>*:first-child{margin-top:0}
footer{max-width:1240px;margin:0 auto;padding:2rem 1.25rem 3rem;color:var(--muted);font-size:.85rem;display:flex;justify-content:space-between;flex-wrap:wrap;gap:1rem}
@media(max-width:980px){.bento{grid-template-columns:repeat(2,1fr)}.hero2,.row2{grid-template-columns:1fr}}
@media(max-width:560px){.bento{grid-template-columns:1fr 1fr;grid-auto-rows:150px}.tile.big{grid-column:span 2;grid-row:span 1}.tile.big h3{font-size:1.5rem}.tile p{display:none}.tile.big p{display:block}.brand small{display:none}}
"""

def t2_head(pid, name, lead, i, c):
    return f'<div class="phead2"><div class="ic">{icon(pid,30)}</div><h1>{name}</h1><p>{lead}</p><div class="num">{i:02d}</div></div>'

def t2_home(colors, logo):
    sizes = {}
    tiles = "".join(f'<a class="tile {sizes.get(pid,"")}" href="#{pid}" style="--c:{colors[pid]}">{icon(pid,30)}<div><h3>{name}</h3><p>{d}</p></div><span class="go">↗</span></a>' for pid,name,s,c,d in TOPICS if pid!="kontakt")
    news = news_items(colors, lambda w,t,x,p,c: f'<a href="#{p}" style="--c:{c}"><span class="ic">{icon(p,20)}</span><div><small>{w}</small><b>{t}</b><p>{x}</p></div></a>')
    cal = "".join(f'<div><span class="d"><b>{a}</b><i>{b}</i></span><span>{t}<br><em>{n or "&nbsp;"}</em></span></div>' for a,b,t,n in DATES)
    return f'''<div class="hero2"><div class="bg">{logo("#fff","#fff","#101317",420)}</div><div style="position:relative"><span class="chip" style="--c:#2a3038">Runslingan 1–11 · Täby</span>
<h1 style="margin:.9rem 0 .8rem">Allt om Väringen.<br>På ett ställe.</h1><p>Information för oss 28 hushåll – sopor, parkering, laddning, städdagar och föreningens dokument.</p></div>
<div class="q"><a href="#ny-har">Ny i området? <span>→</span></a><a href="#dokument">Stadgar & protokoll <span>→</span></a><a href="#kontakt">Kontakta styrelsen <span>→</span></a><a href="mailto:varingen@proton.me" style="font-weight:500;color:#b9c0c9">varingen@proton.me <span>✉</span></a></div></div>
<div class="bento">{tiles}</div>
<div class="row2"><div class="panel"><h2>Aktuellt</h2><div class="newsl">{news}</div></div><div class="panel"><h2>Kalender</h2><div class="cal2">{cal}</div></div></div>'''

def t2_shell(pages, colors, logo):
    return f'''<header class="bar-top"><div class="in"><a class="brand" href="#hem">{logo("#101317","#101317","#fff",40)}<span>Väringen<small>Anläggningssamfälligheten</small></span></a>
<nav class="pills" aria-label="Huvudmeny">{nav_links(colors=colors, short=True)}</nav></div></header>
<main>{pages}</main>
<footer><span>© Anläggningssamfälligheten Väringen · Runslingan 1–11, Täby</span><span>Styrelsen: <a href="mailto:varingen@proton.me">varingen@proton.me</a> · <a href="#kontakt">Kontakt</a> · <a href="https://varinge.wordpress.com/">Gamla hemsidan</a></span></footer>'''

# =====================================================================
# 3. NATTVÄRING – mörk, mässing, sidomeny
# =====================================================================
T3_COLORS = {"sophantering":"#b5835c","parkering":"#5f97d8","laddstolpar":"#e6e0d2","projekt":"#d8714f","stadning":"#74b36d","grasklippning":"#a6c94a",
             "tv-bredband":"#9c8ade","dokument":"#c9a45c","ny-har":"#e2ad3f","maklare":"#93a4b8","historik":"#c96553","forum":"#45b6b0","kontakt":"#86a3cf"}
T3_ON = {k:"#121416" for k in T3_COLORS}

T3_CSS = r"""
:root{--bg:#111315;--surface:#181b1e;--ink:#ece7dd;--muted:#9b958a;--line:#2a2e33;--radius:12px;--accent:#c9a45c;--font-head:'Cormorant Garamond',Georgia,serif;--font-body:'Inter',system-ui,sans-serif;--head-w:600}
.tbd{background:#3a3115;color:#f3d98a;border-color:#7a6424}
aside.sidebar{position:fixed;inset:0 auto 0 0;width:272px;background:#0c0e10;border-right:1px solid var(--line);display:flex;flex-direction:column;padding:1.6rem 1.1rem;overflow-y:auto}
.sb-brand{display:flex;flex-direction:column;align-items:center;text-align:center;text-decoration:none;gap:.6rem;padding-bottom:1.4rem;border-bottom:1px solid var(--line);margin-bottom:1rem}
.sb-brand b{font-family:var(--font-head);font-size:1.7rem;letter-spacing:.32em;font-weight:600;color:var(--accent);padding-left:.32em}
.sb-brand small{font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.sidebar nav a{display:flex;align-items:center;gap:.75rem;padding:.55rem .75rem;border-radius:8px;text-decoration:none;color:var(--muted);font-size:.9rem;position:relative}
.sidebar nav a .ico{color:var(--c);opacity:.85}
.sidebar nav a:hover{background:#16191c;color:var(--ink)}
.sidebar nav a.active{background:#1b1f23;color:var(--ink)}.sidebar nav a.active:after{content:"";position:absolute;left:0;top:20%;bottom:20%;width:3px;border-radius:3px;background:var(--c)}
.sb-foot{margin-top:auto;padding-top:1.2rem;font-size:.78rem;color:var(--muted)}
.sb-foot a{color:var(--accent)}
.mtop{display:none}
main{margin-left:272px;padding:0 clamp(1.2rem,4vw,3.5rem) 5rem;max-width:1180px}
.hero3{position:relative;padding:5rem 0 3.5rem;border-bottom:1px solid var(--line);overflow:hidden}
.hero3 .ring{position:absolute;right:-40px;top:10px;opacity:.16}
.eyebrow{font-size:.72rem;letter-spacing:.26em;text-transform:uppercase;color:var(--accent);font-weight:600}
.hero3 h1{font-size:clamp(2.8rem,6.4vw,5.4rem);font-weight:500;line-height:.98;margin:1rem 0 1.2rem;position:relative}
.hero3 h1 i{color:var(--accent)}
.hero3 p{font-size:1.12rem;color:var(--muted);max-width:50ch;position:relative}
.stats{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--line)}
.stats div{padding:1.6rem 0}.stats b{font-family:var(--font-head);font-size:2.6rem;font-weight:500;color:var(--accent);display:block;line-height:1}
.stats span{font-size:.8rem;color:var(--muted);letter-spacing:.06em}
.h3sec{font-family:var(--font-head);font-size:2rem;font-weight:500;margin:3.2rem 0 1.2rem;display:flex;align-items:center;gap:1rem}
.h3sec:after{content:"";flex:1;height:1px;background:linear-gradient(90deg,var(--line),transparent)}
.news3{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1rem}
.news3 a{background:var(--surface);border:1px solid var(--line);border-top:2px solid var(--c);border-radius:var(--radius);padding:1.3rem;text-decoration:none}
.news3 small{color:var(--c);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.news3 h3{font-size:1.45rem;margin:.4rem 0}.news3 p{color:var(--muted);font-size:.92rem;margin:0}
.topics3{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.topics3 a{background:var(--bg);padding:1.4rem;text-decoration:none;display:flex;gap:1rem;align-items:flex-start;transition:background .2s}
.topics3 a:hover{background:var(--surface)}
.topics3 .ico{color:var(--c);width:26px;height:26px;margin-top:.2rem}
.topics3 b{font-family:var(--font-head);font-size:1.4rem;font-weight:600;display:block}.topics3 span{color:var(--muted);font-size:.88rem}
.cal3{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}
.cal3 div{border:1px solid var(--line);border-radius:var(--radius);padding:1.2rem}
.cal3 b{font-family:var(--font-head);font-size:2.3rem;color:var(--accent);font-weight:500;line-height:1}.cal3 i{font-style:normal;color:var(--muted);margin-left:.4rem;text-transform:uppercase;font-size:.8rem;letter-spacing:.1em}
.cal3 p{margin:.5rem 0 0}.cal3 em{font-size:.75rem;color:var(--muted);font-style:normal}
.page:not(#hem){padding-top:4rem;max-width:880px}
.phead3 .eyebrow{color:var(--c);display:flex;align-items:center;gap:.6rem}
.phead3 h1{font-size:clamp(2.6rem,6vw,4.4rem);font-weight:500;margin:.6rem 0 .8rem;line-height:1}
.phead3 p{font-size:1.15rem;color:var(--muted);margin:0;max-width:56ch}
.phead3:after{content:"";display:block;width:64px;height:2px;background:var(--c);margin-top:1.8rem}
.content h2{font-size:1.9rem;font-weight:500}
.threads .chip{background:transparent;color:var(--ink);border:1px solid #3a3f45}
@media(max-width:900px){aside.sidebar{display:none}.mtop{display:flex;position:sticky;top:0;z-index:5;background:#0c0e10;border-bottom:1px solid var(--line);align-items:center;gap:.8rem;padding:.6rem 1rem;overflow-x:auto;scrollbar-width:none}
.mtop a{white-space:nowrap;text-decoration:none;font-size:.82rem;color:var(--muted);padding:.4rem .2rem;border-bottom:2px solid transparent}.mtop a.active{color:var(--ink);border-color:var(--c)}
main{margin-left:0}.stats,.cal3{grid-template-columns:1fr 1fr}}
"""

def t3_head(pid, name, lead, i, c):
    return f'<div class="phead3"><div class="eyebrow">{icon(pid,16)} Avsnitt {i:02d}</div><h1>{name}</h1><p>{lead}</p></div>'

def t3_home(colors, logo):
    news = news_items(colors, lambda w,t,x,p,c: f'<a href="#{p}" style="--c:{c}"><small>{w}</small><h3>{t}</h3><p>{x}</p></a>')
    tops = "".join(f'<a href="#{pid}" style="--c:{colors[pid]}">{icon(pid,26)}<div><b>{name}</b><span>{d}</span></div></a>' for pid,name,s,c,d in TOPICS)
    cal = "".join(f'<div><b>{a}</b><i>{b}</i><p>{t}</p><em>{n}</em></div>' for a,b,t,n in DATES)
    return f'''<div class="hero3"><div class="ring">{logo("#c9a45c","#c9a45c","#111315",460)}</div><div class="eyebrow">Anläggningssamfälligheten Väringen</div>
<h1>Välkommen hem<br>till <i>Väringen</i>.</h1><p>Föreningens samlade information för de 28 husen på Runslingan 1–11 i Täby kyrkby – uppdaterad, enkel och alltid till hands.</p></div>
<div class="stats"><div><b>28</b><span>radhus med lika andel</span></div><div><b>2</b><span>städdagar per år</span></div><div><b>1</b><span>lekpark och gemensamma ytor</span></div><div><b>1997</b><span>nuvarande stadgar</span></div></div>
<h2 class="h3sec">Aktuellt</h2><div class="news3">{news}</div>
<h2 class="h3sec">Kalender</h2><div class="cal3">{cal}</div>
<h2 class="h3sec">Föreningen</h2><div class="topics3">{tops}</div>'''

def t3_shell(pages, colors, logo):
    return f'''<aside class="sidebar"><a class="sb-brand" href="#hem">{logo("#c9a45c","#ece7dd","#0c0e10",86)}<b>VÄRINGEN</b><small>Runslingan 1–11 · Täby</small></a>
<nav aria-label="Huvudmeny">{nav_links(colors=colors, show_icon=True)}</nav>
<div class="sb-foot">Frågor? <a href="#kontakt">Kontakta styrelsen</a><br><a href="https://varinge.wordpress.com/">Gamla hemsidan →</a></div></aside>
<nav class="mtop" aria-label="Meny mobil">{nav_links(colors=colors, short=True)}</nav>
<main>{pages}</main>'''

# =====================================================================
# 4. FÖRENINGSPÄRMEN – pärm med färgade registerflikar
# =====================================================================
T4_CSS = r"""
:root{--bg:#d8d1c3;--surface:#fffefa;--ink:#1c1c1a;--muted:#67625a;--line:#e6e0d3;--radius:2px;--btn-r:3px;--accent:#1c1c1a;--font-head:'Archivo',system-ui,sans-serif;--font-body:'Archivo',system-ui,sans-serif;--mono:'IBM Plex Mono',ui-monospace,monospace;--head-w:800}
body{background:var(--bg) radial-gradient(circle at 20% 0,#e4ded2,transparent 60%)}
.binder{max-width:1160px;margin:2.2rem auto 4rem;display:grid;grid-template-columns:1fr 56px;padding:0 1rem}
.sheet{background:var(--surface);min-height:80vh;box-shadow:0 1px 0 #cfc7b6,0 24px 60px -30px rgba(40,30,10,.45);position:relative;padding:2.4rem clamp(1.3rem,4vw,3.6rem) 4rem clamp(3.4rem,6vw,5.2rem)}
.holes{position:absolute;left:1.3rem;top:0;bottom:0;display:flex;flex-direction:column;justify-content:space-around;padding:6rem 0}
.holes i{width:16px;height:16px;border-radius:50%;background:var(--bg);box-shadow:inset 0 2px 3px rgba(0,0,0,.25)}
.tabs{display:flex;flex-direction:column;gap:3px;padding-top:2.4rem;position:sticky;top:0;align-self:start;max-height:100vh;overflow-y:auto;scrollbar-width:none}
.tabs a{background:var(--c);color:var(--on-c,#fff);text-decoration:none;writing-mode:vertical-rl;font-size:.74rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:.6rem .45rem;border-radius:0 6px 6px 0;width:40px;transition:width .15s;font-family:var(--mono);white-space:nowrap}
.tabs a:hover{width:48px}.tabs a.active{width:56px;box-shadow:4px 0 0 rgba(0,0,0,.08)}
.tabs a[href="#hem"]{background:#1c1c1a}
.sheet-head{display:flex;align-items:center;gap:1rem;border-bottom:3px solid var(--ink);padding-bottom:1rem;margin-bottom:.4rem}
.sheet-head b{font-size:1.7rem;font-weight:900;letter-spacing:.01em;text-transform:uppercase;line-height:1}
.sheet-head .meta{font-family:var(--mono);font-size:.72rem;color:var(--muted);margin-left:auto;text-align:right;line-height:1.5}
.sub{font-family:var(--mono);font-size:.72rem;color:var(--muted);display:flex;justify-content:space-between;margin-bottom:2.4rem}
.ph4{display:grid;grid-template-columns:auto 1fr;gap:0 1.4rem;align-items:start}
.ph4 .no{font-family:var(--mono);font-size:.8rem;background:var(--c);color:var(--on-c,#fff);padding:.3rem .6rem;margin-top:.7rem}
.ph4 h1{font-size:clamp(2.4rem,6vw,4.3rem);letter-spacing:-.035em;line-height:.95}
.ph4 p{grid-column:2;font-size:1.15rem;color:var(--muted);max-width:56ch;margin:.9rem 0 0}
.page:not(#hem) .pdfbar{padding-left:0;border-bottom:1px solid var(--line);padding-bottom:1.5rem}
.content{max-width:820px}
.content h2{font-size:1.35rem;letter-spacing:-.01em;text-transform:none;display:flex;gap:.7rem;align-items:center}
.content h2:before{content:"";width:14px;height:14px;background:var(--c)}
.toc-head{display:grid;grid-template-columns:1.25fr .75fr;gap:2.5rem}
.intro h1{font-size:clamp(2.4rem,5.6vw,4.4rem);letter-spacing:-.04em;line-height:.95}
.intro p{font-size:1.12rem;color:var(--muted);max-width:50ch}
.lbl{font-family:var(--mono);font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:2.6rem 0 .8rem;display:flex;gap:.6rem;align-items:center}
.lbl:after{content:"";flex:1;border-top:1px dashed #cfc7b6}
.toc a{display:grid;grid-template-columns:3.4rem 1fr auto;gap:1rem;align-items:center;padding:.85rem 0;border-bottom:1px solid var(--line);text-decoration:none}
.toc .no{font-family:var(--mono);font-size:.78rem;background:var(--c);color:var(--on-c,#fff);text-align:center;padding:.3rem 0}
.toc b{font-size:1.15rem}.toc span{color:var(--muted);font-size:.9rem;display:block}
.toc .pg{font-family:var(--mono);font-size:.75rem;color:var(--muted)}
.toc a:hover b{text-decoration:underline;text-decoration-color:var(--c);text-decoration-thickness:3px;text-underline-offset:4px}
.board{background:#c8b28a url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='6' height='6'%3E%3Ccircle cx='1' cy='1' r='.6' fill='%23a38c63'/%3E%3C/svg%3E");padding:1.2rem;display:grid;gap:1rem;border:8px solid #8a6e45;border-radius:4px}
.note4{background:#fffdf3;padding:1rem 1.1rem 1.1rem;text-decoration:none;position:relative;box-shadow:0 6px 12px -6px rgba(0,0,0,.35);display:block}
.note4:nth-child(odd){transform:rotate(-.8deg)}.note4:nth-child(even){transform:rotate(.7deg)}
.note4:before{content:"";position:absolute;top:-8px;left:50%;width:56px;height:16px;margin-left:-28px;background:var(--c);opacity:.85}
.note4 small{font-family:var(--mono);font-size:.7rem;color:var(--muted)}.note4 b{display:block;font-size:1.05rem;margin:.15rem 0}.note4 p{margin:0;font-size:.88rem;color:var(--muted)}
.cal4{font-family:var(--mono);font-size:.88rem;border-top:2px solid var(--ink)}
.cal4 div{display:grid;grid-template-columns:7rem 1fr auto;padding:.7rem 0;border-bottom:1px dashed #d4ccbb}
.cal4 em{font-style:normal;color:var(--muted)}
.foot4{font-family:var(--mono);font-size:.72rem;color:var(--muted);margin-top:4rem;border-top:1px solid var(--line);padding-top:1rem;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.5rem}
@media(max-width:860px){.binder{grid-template-columns:1fr;margin-top:0;padding:0}
.tabs{flex-direction:row;overflow-x:auto;padding:0;position:sticky;top:0;z-index:5;order:-1;background:var(--bg);scrollbar-width:none;gap:2px}
.tabs a{writing-mode:horizontal-tb;width:auto!important;border-radius:6px 6px 0 0;white-space:nowrap;padding:.6rem .7rem}.tabs a.active{padding-top:.9rem}
.holes{display:none}.sheet{padding:1.6rem 1.1rem 3rem}.toc-head{grid-template-columns:1fr}.sheet-head .meta{display:none}.ph4{grid-template-columns:1fr}.ph4 p{grid-column:1}.ph4 .no{justify-self:start}}
"""

def t4_head(pid, name, lead, i, c):
    return f'<div class="ph4"><span class="no">FLIK {i:02d}</span><h1>{name}</h1><p>{lead}</p></div>'

def t4_home(colors, logo):
    toc = "".join(f'<a href="#{pid}" style="--c:{colors[pid]}"><span class="no">{i:02d}</span><div><b>{name}</b><span>{d}</span></div><span class="pg">→</span></a>' for i,(pid,name,s,c,d) in enumerate(TOPICS,1))
    notes = news_items(colors, lambda w,t,x,p,c: f'<a class="note4" href="#{p}" style="--c:{c}"><small>{w}</small><b>{t}</b><p>{x}</p></a>')
    cal = "".join(f'<div><span>{a} {b}</span><span>{t}</span><em>{n}</em></div>' for a,b,t,n in DATES)
    return f'''<div class="toc-head"><div class="intro"><h1>Föreningspärmen för Väringen.</h1><p>Det här är vår gemensamma pärm – på nätet. Bläddra med flikarna till höger eller välj i innehållsförteckningen nedan. Varje flik går att skriva ut eller ladda ned som PDF.</p>
<div class="lbl">Kalender</div><div class="cal4">{cal}</div></div>
<div><div class="lbl" style="margin-top:0">Anslagstavlan</div><div class="board">{notes}</div></div></div>
<div class="lbl">Innehåll</div><div class="toc">{toc}</div>'''

def t4_shell(pages, colors, logo):
    tabs = f'<a href="#hem" data-nav style="--c:#1c1c1a">Innehåll</a>' + "".join(f'<a href="#{pid}" data-nav style="--c:{colors[pid]}">{s}</a>' for pid,n,s,c,d in TOPICS)
    return f'''<div class="binder"><div class="sheet"><div class="holes"><i></i><i></i><i></i></div>
<header class="sheet-head"><a href="#hem" style="display:flex;align-items:center;gap:.9rem;text-decoration:none">{logo("#1c1c1a","#1c1c1a","#fffefa",54)}<b>Väringen</b></a><div class="meta">Anläggningssamfälligheten Väringen<br>Runslingan 1–11 · Täby</div></header>
<div class="sub"><span>Föreningspärm · verksamhetsåret 2026/27</span><span><a href="https://varinge.wordpress.com/">Gamla hemsidan ↗</a></span></div>
<main>{pages}</main>
<div class="foot4"><span>© Anläggningssamfälligheten Väringen</span><span><a href="#kontakt">Kontakta styrelsen</a></span></div></div>
<nav class="tabs" aria-label="Flikar">{tabs}</nav></div>'''

THEMES = [
 dict(slug="runsten", title="Förslag 1 · Runsten", accent="#8e3b2e", css=T1_CSS, page_head=t1_head, home=t1_home, shell=t1_shell,
      fonts="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,400&family=Inter:wght@400;500;600&display=swap"),
 dict(slug="fjall", title="Förslag 2 · Fjäll", accent="#101317", css=T2_CSS, page_head=t2_head, home=t2_home, shell=t2_shell,
      fonts="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"),
 dict(slug="nattvaring", title="Förslag 3 · Nattväring", accent="#c9a45c", css=T3_CSS, page_head=t3_head, home=t3_home, shell=t3_shell,
      colors=T3_COLORS, on_c=T3_ON,
      fonts="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=swap"),
 dict(slug="parmen", title="Förslag 4 · Föreningspärmen", accent="#1c1c1a", css=T4_CSS, page_head=t4_head, home=t4_home, shell=t4_shell,
      fonts="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;800;900&family=IBM+Plex+Mono:wght@400;500&display=swap"),
]

from theme_fjall import THEME as _FJALL
THEMES[1].update(folder="forslag-2a-fjall", title="Förslag 2A · Fjäll")
THEMES[0].update(folder="forslag-1-runsten")
THEMES[:] = [THEMES[1], _FJALL]
