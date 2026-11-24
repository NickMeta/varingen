# -*- coding: utf-8 -*-
# Förslag 2 · Fjäll – version C: grupperade flikar, ljusgrå husfärg, sökfunktion
import json, re, html as H
from content import TOPICS, NEWS, DATES, PAGES, icon

GROUPS = [
 ("vardag", "Vardag", "#1f5fa8", ["sophantering","parkering","laddstolpar","grasklippning","tv-bredband"]),
 ("gemenskap", "Gemenskap", "#3f7a3c", ["stadning","forum","projekt"]),
 ("foreningen", "Föreningen", "#7a6a48", ["dokument","kontakt","historik"]),
 ("ny", "Ny & mäklare", "#b7801a", ["ny-har","maklare"]),
]
KEYWORDS = {
 "sophantering":"sopor soptunna sopkärl kärl avfall återvinning matavfall restavfall verdis tömning sophämtning tömningsdag grovsopor",
 "parkering":"parkera bil p-plats parkeringsplats gäst besök snöskottning snö skotta datumparkering garage skyltning",
 "laddstolpar":"elbil laddning laddbox ladda laddplats laddstolpe hybrid el",
 "grasklippning":"gräsklipparschema gräsklippningsschema klippschema gräsklippare gräs klippa brandgata brandgator brandväg schema",
 "tv-bredband":"tv telia kanaler kanalutbud internet wifi fiber bredband box",
 "stadning":"städdag städdagar grändvärd grändvärdar container grill grillning vårstäddag höststäddag snöröjning gemenskap",
 "forum":"diskussion grannar chatt fråga tråd",
 "projekt":"garage garageprojekt garageprojektet kallförråd förråd verktyg redskap vattenmätare träd häck arborist",
 "dokument":"stadgar protokoll årsstämma stämma motion motioner kallelse underhållsplan pdf regler",
 "kontakt":"styrelse styrelsen mejl mail e-post epost ordförande felanmälan kassör sekreterare",
 "historik":"runsten runstenar viking vikingar väring väringar historia runriket",
 "ny-har":"inflyttning inflyttad ny nyinflyttad avgift årsavgift kostnad faktura välkommen medlem",
 "maklare":"mäklare försäljning sälja köpa ägarbyte organisationsnummer underhållsfond",
}

def search_index():
    idx = []
    for pid, name, short, c, d in TOPICS:
        p = PAGES[pid]
        txt = re.sub(r"<[^>]+>", " ", p["lead"] + " " + p["body"])
        txt = re.sub(r"\{[^}]*\}", " ", txt)
        txt = re.sub(r"\s+", " ", H.unescape(txt)).strip()
        idx.append(dict(id=pid, t=name, c=c, k=KEYWORDS.get(pid, ""), x=txt))
    return json.dumps(idx, ensure_ascii=False)

CSS = r"""
:root{--bg:#f1f2f4;--house:#101317;--house-2:#2a3038;--surface:#fff;--ink:#1b2127;--muted:#58616b;--line:#dde1e5;--radius:16px;--accent:#58616b;--font-head:'Plus Jakarta Sans',system-ui,sans-serif;--font-body:'Plus Jakarta Sans',system-ui,sans-serif;--head-w:700}
h1,h2,h3{letter-spacing:-.025em}
body{background:var(--bg)}
.hdr{background:var(--house);border-bottom:1px solid var(--house-2)}
.hdr .in{max-width:1240px;margin:0 auto;padding:.9rem 1.25rem 0;display:flex;align-items:flex-end;gap:2rem}
.brand{color:#fff;display:flex;align-items:center;gap:.65rem;text-decoration:none;font-weight:800;font-size:1.2rem;letter-spacing:-.02em;padding-bottom:.85rem;flex:none}
.brand svg{flex:none}.brand small{display:block;font-weight:500;font-size:.72rem;color:#9aa3ad;letter-spacing:0}
.gtabs{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}
.gtab{font:inherit;cursor:pointer;border:0;background:#1d2329;color:#cfd5dc;font-weight:700;font-size:.98rem;padding:.75rem 1.25rem .8rem;border-radius:12px 12px 0 0;border-top:4px solid var(--g);white-space:nowrap}
.gtab:hover{background:#2a3038;color:#fff}.gtab.on{background:#fff;color:var(--ink)}
.hsearch{margin-left:auto;padding-bottom:.75rem;position:relative;flex:0 1 300px}
.sub{background:#fff;border-bottom:1px solid var(--line)}
.sub .in{max-width:1240px;margin:0 auto;padding:.65rem 1.25rem;display:flex;gap:.5rem;overflow-x:auto;scrollbar-width:none}
.sub .grp{display:none;gap:.5rem}.sub .grp.on{display:flex}
.sub a{display:flex;align-items:center;gap:.45rem;padding:.5rem .95rem;border-radius:99px;font-size:.88rem;font-weight:700;text-decoration:none;white-space:nowrap;background:color-mix(in srgb,var(--c) 12%,#fff);color:color-mix(in srgb,var(--c) 82%,#000)}
.sub a .ico{width:16px;height:16px}.sub a:hover{background:color-mix(in srgb,var(--c) 22%,#fff)}
.sub a.active{background:var(--c);color:var(--on-c,#fff)}
/* sök */
.search{position:relative}
.search input{width:100%;font:inherit;font-size:.92rem;padding:.6rem .9rem .6rem 2.3rem;border-radius:99px;border:1px solid var(--house-2);background:#fff;color:var(--ink);outline:none}
.search input:focus{border-color:#8f98a2;box-shadow:0 0 0 3px rgba(88,97,107,.18)}
.search .ico{position:absolute;left:.8rem;top:50%;transform:translateY(-50%);color:var(--muted);width:16px;height:16px}
.results{position:absolute;left:0;right:0;top:calc(100% + 6px);background:#fff;border:1px solid var(--line);border-radius:14px;box-shadow:0 18px 40px -18px rgba(20,30,40,.35);z-index:30;overflow:hidden;display:none}
.results.open{display:block}
.results a{display:grid;grid-template-columns:10px 1fr;gap:.2rem .7rem;padding:.7rem .9rem;text-decoration:none;border-top:1px solid var(--line)}
.results a:first-child{border-top:0}.results a:hover,.results a.sel{background:#f3f4f6}
.results i{grid-row:1/3;width:10px;height:10px;border-radius:50%;background:var(--c);margin-top:.35rem}
.results b{font-size:.92rem}.results span{font-size:.8rem;color:var(--muted);line-height:1.35}
.results mark{background:#fff1bf;color:inherit;padding:0 .1em;border-radius:3px}
.results .none{padding:.8rem .9rem;font-size:.88rem;color:var(--muted)}
main{max-width:1240px;margin:0 auto;padding:1.4rem 1.25rem 5rem}
/* start */
.hero2{background:var(--house);color:#fff;border:0;border-radius:26px;padding:clamp(1.6rem,4.5vw,3rem);display:grid;grid-template-columns:1.25fr .75fr;gap:2rem;align-items:center}
.hero2 h1{font-size:clamp(2rem,4.6vw,3.3rem);line-height:1.04;font-weight:800}
.hero2 p{color:#b9c0c9;font-size:1.08rem;max-width:46ch;margin:.7rem 0 1.3rem}
.hero2 .search{max-width:460px}.hero2 .search input{padding:.85rem 1rem .85rem 2.6rem;font-size:1rem;border-color:transparent}.hero2 .results{color:var(--ink)}
.hero2 .q{display:flex;flex-direction:column;gap:.5rem}
.hero2 .q a{background:rgba(255,255,255,.08);color:#fff;border-radius:14px;padding:.8rem 1rem;text-decoration:none;display:flex;justify-content:space-between;font-weight:600;border:1px solid rgba(255,255,255,.12)}
.hero2 .q a:hover{background:rgba(255,255,255,.14)}.hero2 .q small{color:#b9c0c9;font-weight:500}
.groups{margin-top:1.6rem;display:grid;gap:.9rem}
.grow{display:grid;grid-template-columns:130px 1fr;gap:1rem;align-items:center}
.grow h3{font-size:.75rem;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);font-weight:700;display:flex;align-items:center;gap:.5rem;font-family:var(--font-body)}
.grow h3:before{content:"";width:10px;height:10px;border-radius:3px;background:var(--g)}
.tl{display:grid;grid-template-columns:repeat(5,1fr);gap:.65rem}
.tc{background:#fff;border:1px solid var(--line);border-radius:14px;padding:.75rem .85rem;display:flex;gap:.7rem;align-items:center;text-decoration:none;box-shadow:inset 4px 0 0 var(--c);transition:transform .15s,box-shadow .15s}
.tc:hover{transform:translateY(-2px);box-shadow:inset 4px 0 0 var(--c),0 10px 22px -16px rgba(0,0,0,.5)}
.tc .i{width:34px;height:34px;border-radius:10px;background:var(--c);color:var(--on-c,#fff);display:grid;place-items:center;flex:none}
.tc b{display:block;font-size:.93rem;line-height:1.25}.tc span{font-size:.8rem;color:var(--muted);line-height:1.3;display:block}
.row2{display:grid;grid-template-columns:1.6fr 1fr;gap:1rem;margin-top:1.6rem}
.panel{background:var(--surface);border-radius:20px;padding:1.4rem 1.5rem;border:1px solid var(--line)}
.panel h2{font-size:1.2rem;margin-bottom:.8rem}
.newsl a{display:grid;grid-template-columns:auto 1fr;gap:.9rem;padding:.8rem 0;border-top:1px solid var(--line);text-decoration:none;align-items:start}
.newsl .ic{width:38px;height:38px;border-radius:11px;background:var(--c);color:var(--on-c,#fff);display:grid;place-items:center}
.newsl small{color:var(--muted);font-weight:600;font-size:.74rem}.newsl b{display:block}.newsl p{margin:.1rem 0 0;color:var(--muted);font-size:.9rem}
.cal2 div{display:grid;grid-template-columns:56px 1fr;gap:.9rem;align-items:center;padding:.55rem 0}
.cal2 .d{background:var(--bg);border-radius:14px;text-align:center;padding:.4rem 0;line-height:1.1}
.cal2 .d b{display:block;font-size:1.2rem}.cal2 .d i{font-style:normal;font-size:.68rem;text-transform:uppercase;color:var(--muted);font-weight:700}
.cal2 em{font-style:normal;font-size:.75rem;color:var(--muted)}
/* undersidor */
.phead2{background:var(--c);color:var(--on-c,#fff);border-radius:26px;padding:clamp(1.6rem,4.5vw,2.8rem) clamp(1.4rem,4.5vw,2.8rem) 4.6rem;position:relative;overflow:hidden}
.phead2 .crumb{font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;opacity:.8;display:flex;align-items:center;gap:.5rem;margin-bottom:.9rem}
.phead2 .ic{width:50px;height:50px;border-radius:15px;background:rgba(255,255,255,.17);display:grid;place-items:center;margin-bottom:.9rem}
.phead2 .ic .ico{width:26px;height:26px}
.phead2 h1{font-size:clamp(2rem,4.6vw,3.1rem);font-weight:800}.phead2 p{font-size:1.1rem;opacity:.9;max-width:56ch;margin:.55rem 0 0}
.page:not(#hem) .pdfbar{margin:-3.9rem clamp(1.4rem,4.5vw,2.8rem) 0;position:relative}
.page:not(#hem) .btn-pdf{background:#fff;color:#1b2127}.page:not(#hem) .btn-ghost{border-color:rgba(255,255,255,.45);color:var(--on-c,#fff)}
.page:not(#hem) .content{background:var(--surface);border-radius:22px;padding:clamp(1.3rem,4vw,2.5rem);margin-top:2rem;border:1px solid var(--line)}
.content>*:first-child{margin-top:0}
footer{background:var(--house);border-top:0}footer a{color:#fff}
footer .in{max-width:1240px;margin:0 auto;padding:1.6rem 1.25rem 2.2rem;color:#b9c0c9;font-size:.86rem;display:flex;justify-content:space-between;flex-wrap:wrap;gap:1rem}
@media(max-width:1080px){.tl{grid-template-columns:repeat(3,1fr)}}
@media(max-width:900px){.hero2,.row2{grid-template-columns:1fr}.hdr .in{flex-wrap:wrap;gap:.6rem 1rem}.hsearch{order:2;flex:1 1 100%;margin:0;padding-bottom:.2rem}.gtabs{order:3;width:100%}.grow{grid-template-columns:1fr;gap:.45rem}}
@media(max-width:560px){.tl{grid-template-columns:1fr 1fr}.tc>span>span{display:none}.brand small{display:none}.gtab{padding:.6rem .9rem;font-size:.88rem}}
@media print{.hdr,.sub{display:none!important}}
"""

def group_of(pid):
    for gid, n, c, ps in GROUPS:
        if pid in ps: return gid, n
    return None, None

def page_head(pid, name, lead, i, c):
    gid, gname = group_of(pid)
    return (f'<div class="phead2"><div class="crumb">{gname}</div><div class="ic">{icon(pid,26)}</div>'
            f'<h1>{name}</h1><p>{lead}</p></div>')

SEARCH_ICON = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>'

def searchbox(sid, ph):
    return (f'<div class="search" role="search">{SEARCH_ICON}<input id="{sid}" type="search" placeholder="{ph}" '
            f'autocomplete="off" aria-label="Sök på sidan"><div class="results" role="listbox"></div></div>')

def home(colors, logo):
    D = {t[0]: t for t in TOPICS}
    rows = ""
    for gid, gname, gc, ps in GROUPS:
        cards = "".join(f'<a class="tc" href="#{p}" style="--c:{colors[p]}"><span class="i">{icon(p,18)}</span><span><b>{D[p][1]}</b><span>{D[p][4]}</span></span></a>' for p in ps)
        rows += f'<div class="grow" style="--g:{gc}"><h3>{gname}</h3><div class="tl">{cards}</div></div>'
    news = "".join(f'<a href="#{p}" style="--c:{colors[p]}"><span class="ic">{icon(p,19)}</span><div><small>{w}</small><b>{t}</b><p>{x}</p></div></a>' for w,t,x,p in NEWS)
    cal = "".join(f'<div><span class="d"><b>{a}</b><i>{b}</i></span><span>{t}<br><em>{n or "&nbsp;"}</em></span></div>' for a,b,t,n in DATES)
    return f'''<div class="hero2"><div><h1>Välkommen till Väringen</h1>
<p>Här hittar du allt som rör oss 28 hushåll på Runslingan 1–11, från sopor och gräsklippning till städdagar och årsstämman.</p>
{searchbox("q-hero","Sök, t.ex. gräsklippning eller städdag")}</div>
<div class="q"><a href="#ny-har">Ny i området? <span>→</span></a><a href="#dokument">Stadgar &amp; protokoll <span>→</span></a><a href="mailto:varingen@proton.me">Mejla styrelsen <small>varingen@proton.me</small></a></div></div>
<div class="groups">{rows}</div>
<div class="row2"><div class="panel"><h2>Aktuellt</h2><div class="newsl">{news}</div></div><div class="panel"><h2>Kalender</h2><div class="cal2">{cal}</div></div></div>'''

def shell(pages, colors, logo):
    D = {t[0]: t for t in TOPICS}
    gt = "".join(f'<button class="gtab" type="button" data-g="{gid}" style="--g:{gc}">{gn}</button>' for gid,gn,gc,ps in GROUPS)
    sub = "".join(f'<div class="grp" data-grp="{gid}">' + "".join(f'<a href="#{p}" data-nav style="--c:{colors[p]}">{icon(p,16)}{D[p][1]}</a>' for p in ps) + '</div>' for gid,gn,gc,ps in GROUPS)
    pg2grp = json.dumps({p: gid for gid,gn,gc,ps in GROUPS for p in ps})
    js = """<script>
(function(){
 var P2G=%s, IDX=%s;
 function setGroup(g){[].forEach.call(document.querySelectorAll('.gtab'),function(b){b.classList.toggle('on',b.dataset.g===g)});
  [].forEach.call(document.querySelectorAll('.sub .grp'),function(d){d.classList.toggle('on',d.dataset.grp===g)});}
 function sync(){var h=(location.hash||'#hem').slice(1);setGroup(P2G[h]||'vardag');}
 [].forEach.call(document.querySelectorAll('.gtab'),function(b){b.addEventListener('click',function(){setGroup(b.dataset.g)})});
 window.addEventListener('hashchange',sync);sync();
 /* sök */
 function norm(s){return (s||'').toLowerCase()}
 function esc(s){return s.replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
 function find(q){
  var words=norm(q).split(/[^a-zåäöé0-9-]+/).filter(function(w){return w.length>1});
  if(!words.length) return [];
  var res=[];
  IDX.forEach(function(p){
   var T=norm(p.t),K=norm(p.k),X=norm(p.x),score=0,hit=null;
   words.forEach(function(w){
    for(var L=w.length;L>=Math.min(4,w.length);L--){
     var s=w.slice(0,L),q=L/w.length;
     if(T.indexOf(s)>-1){score+=10*q;hit=hit||s;break}
     if(K.indexOf(s)>-1){score+=6*q;hit=hit||s;break}
     if(X.indexOf(s)>-1){score+=2*q;hit=hit||s;break}
    }
   });
   if(score>0) res.push({p:p,score:score,hit:hit});
  });
  res.sort(function(a,b){return b.score-a.score});
  return res.slice(0,6);
 }
 function snippet(p,hit){
  var X=p.x,i=norm(X).indexOf(hit);
  if(i<0) return esc(X.slice(0,90))+'…';
  var a=Math.max(0,i-40),s=X.slice(a,i+70);
  var j=norm(s).indexOf(hit);
  return (a>0?'…':'')+esc(s.slice(0,j))+'<mark>'+esc(s.slice(j,j+hit.length))+'</mark>'+esc(s.slice(j+hit.length))+'…';
 }
 [].forEach.call(document.querySelectorAll('.search'),function(box){
  var inp=box.querySelector('input'),out=box.querySelector('.results'),sel=0,cur=[];
  function render(){
   var q=inp.value.trim(); if(!q){out.classList.remove('open');return}
   cur=find(q); sel=0;
   out.innerHTML=cur.length?cur.map(function(r,i){return '<a href="#'+r.p.id+'" style="--c:'+r.p.c+'" class="'+(i===0?'sel':'')+'"><i></i><b>'+esc(r.p.t)+'</b><span>'+snippet(r.p,r.hit)+'</span></a>'}).join('')
     :'<div class="none">Inga träffar på ”'+esc(q)+'”. Prova ett annat ord, eller mejla styrelsen på varingen@proton.me.</div>';
   out.classList.add('open');
  }
  inp.addEventListener('input',render);
  inp.addEventListener('focus',render);
  inp.addEventListener('keydown',function(e){
   var as=out.querySelectorAll('a');
   if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();if(!as.length)return;sel=(sel+(e.key==='ArrowDown'?1:-1)+as.length)%%as.length;[].forEach.call(as,function(a,i){a.classList.toggle('sel',i===sel)})}
   else if(e.key==='Enter'){e.preventDefault();if(cur[sel]){location.hash=cur[sel].p.id;close()}}
   else if(e.key==='Escape'){close()}
  });
  out.addEventListener('click',function(){close()});
  function close(){out.classList.remove('open');inp.value='';inp.blur()}
  document.addEventListener('click',function(e){if(!box.contains(e.target))out.classList.remove('open')});
 });
})();
</script>""" % (pg2grp, search_index())
    return f'''<header class="hdr"><div class="in"><a class="brand" href="#hem">{logo("#ffffff","#ffffff","#101317",42)}<span>VÄRINGEN<small>Anläggningssamfälligheten</small></span></a>
<nav class="gtabs" aria-label="Huvudmeny">{gt}</nav>
<div class="hsearch">{searchbox("q-top","Sök…")}</div></div></header>
<nav class="sub" aria-label="Undermeny"><div class="in">{sub}</div></nav>
<main>{pages}</main>
<footer><div class="in"><span>© Anläggningssamfälligheten Väringen · Runslingan 1–11, Täby</span><span>Styrelsen: <a href="mailto:varingen@proton.me">varingen@proton.me</a> · <a href="#kontakt">Kontakt</a> · <a href="https://varinge.wordpress.com/">Gamla hemsidan</a></span></div></footer>{js}'''

THEME = dict(slug="fjall-flikar", folder="forslag-2b-fjall-flikar", title="Förslag 2B · Fjäll med flikar", accent="#101317", css=CSS, page_head=page_head, home=home, shell=shell,
             colors={"laddstolpar":"#1b2127"},
             fonts="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap")
