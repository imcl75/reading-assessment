/* Child reading view (shared by fluency and phonics; inlined by each tool's build.py). Fills the screen
   with just the title, the text and any pictures, so a child can read from the iPad instead of a printed
   pupil copy. No marks, no 100-word marker, no buttons except a small "Done" for the adult.
   Sits above everything else on the page, including the staff "Show names" button.
   The text is sized to fill the screen without scrolling (it re-fits when the iPad is turned round). */
const ChildReader = (function(){
  const css = '#childReader{position:fixed;inset:0;z-index:2147483000;background:#fff;color:#0a0101;display:flex;flex-direction:column;'+
    'padding:max(18px,env(safe-area-inset-top)) max(22px,env(safe-area-inset-right)) max(18px,env(safe-area-inset-bottom)) max(22px,env(safe-area-inset-left));'+
    'font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;-webkit-user-select:none;user-select:none}'+
    '#childReader[hidden]{display:none}'+
    '#childReader .cr-done{position:absolute;top:max(10px,env(safe-area-inset-top));right:max(12px,env(safe-area-inset-right));font-size:16px;padding:8px 14px;border-radius:10px;border:2px solid #cfe3ee;background:#fff;color:#567;font-weight:700;cursor:pointer}'+
    '#childReader .cr-body{flex:1;min-height:0;overflow-y:auto;-webkit-overflow-scrolling:touch;display:flex;flex-direction:column;align-items:center}'+
    '#childReader .cr-inner{width:100%;max-width:1100px;margin:auto 0}'+
    '#childReader h1{margin:0 90px .5em;text-align:center;font-size:1.15em;line-height:1.25}'+
    '#childReader .cr-pics{display:flex;gap:16px;justify-content:center;margin:0 0 .6em}'+
    '#childReader .cr-pics img{min-width:0;max-width:48%;max-height:var(--cr-pic,34vh);object-fit:contain;border-radius:12px;border:2px solid #cfe3ee}'+
    '#childReader .cr-pics img:only-child{max-width:70%}'+
    '#childReader .cr-text{margin:0;line-height:1.7;white-space:pre-line}'+
    'body.cr-open{overflow:hidden}';
  let el, inner, opts;
  function build(){
    const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    el = document.createElement('div'); el.id = 'childReader'; el.hidden = true;
    el.innerHTML = '<button class="cr-done" type="button">Done</button><div class="cr-body"><div class="cr-inner"></div></div>';
    document.body.appendChild(el);
    inner = el.querySelector('.cr-inner');
    el.querySelector('.cr-done').onclick = close;
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !el.hidden) close(); });
    window.addEventListener('resize', () => { if (!el.hidden) fit(); });
  }
  // Largest font size (between min and max) at which everything fits on screen with no scrolling.
  function fit(){
    const body = el.querySelector('.cr-body');
    let lo = opts.min || 22, hi = opts.max || 48;
    inner.style.fontSize = hi + 'px';
    if (body.scrollHeight <= body.clientHeight) return;
    while (hi - lo > 1) {
      const mid = (lo + hi) >> 1;
      inner.style.fontSize = mid + 'px';
      if (body.scrollHeight <= body.clientHeight) lo = mid; else hi = mid;
    }
    inner.style.fontSize = lo + 'px';
  }
  // o = {title, text, images:[src...], min, max} (min/max = font size range in px)
  function open(o){
    if (!el) build();
    opts = o;
    const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
    const imgs = o.images || [];
    inner.innerHTML = (o.title ? '<h1>'+esc(o.title)+'</h1>' : '') +
      (imgs.length ? '<div class="cr-pics">'+imgs.map(s=>'<img src="'+esc(s)+'" alt="">').join('')+'</div>' : '') +
      '<p class="cr-text">'+esc(o.text.trim())+'</p>';
    el.hidden = false; document.body.classList.add('cr-open');
    fit();
    inner.querySelectorAll('img').forEach(i => { if (!i.complete) i.addEventListener('load', fit, {once:true}); });
    const fs = el.requestFullscreen || el.webkitRequestFullscreen;   // iPad Safari: hides the address bar; ignored where not allowed
    if (fs) { try { const p = fs.call(el); if (p && p.catch) p.catch(()=>{}); } catch(e) {} }
  }
  function close(){
    el.hidden = true; document.body.classList.remove('cr-open');
    const fe = document.fullscreenElement || document.webkitFullscreenElement;
    if (fe) { const x = document.exitFullscreen || document.webkitExitFullscreen; try { const p = x.call(document); if (p && p.catch) p.catch(()=>{}); } catch(e) {} }
  }
  return {open, close};
})();
