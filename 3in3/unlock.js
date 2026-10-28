/* 3 in 3 daily unlock - shared by home, login and index pages.
   A teacher shows today's code as a QR on the staff-only unlock page. Scanning it opens home.html#u=<code>;
   the code is checked, then kept on this iPad until midnight. The part after # is never sent to a server.
   Nothing secret lives here: without a valid code the API gives no pupil list and saves nothing. */
(function () {
  var API = 'https://api.wallscourt-farm-academy.co.uk/planning/readassess-db';
  var KEY = 'ra_unlock';
  var TOKEN = '2013';                         // the public light token, as on every pupil page

  function today() {
    var d = new Date();
    return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
  }
  function code() {
    try {
      var u = JSON.parse(localStorage.getItem(KEY) || '{}');
      return u && u.day === today() ? String(u.code || '') : '';
    } catch (e) { return ''; }
  }
  function store(c) { try { localStorage.setItem(KEY, JSON.stringify({ code: c, day: today() })); } catch (e) {} }
  function clear() { try { localStorage.removeItem(KEY); } catch (e) {} }
  function digits(s) { return String(s || '').replace(/[^0-9]/g, ''); }

  function check(c) {                          // resolves true / false (false on any trouble)
    return new Promise(function (resolve) {
      var cb = 'cbu_' + Date.now() + '_' + Math.random().toString(36).slice(2);
      var s = document.createElement('script');
      var done = function (v) { clearTimeout(t); delete window[cb]; if (s.parentNode) s.parentNode.removeChild(s); resolve(v); };
      var t = setTimeout(function () { done(false); }, 12000);
      window[cb] = function (d) { done(!!(d && d.ok)); };
      s.onerror = function () { done(false); };
      s.src = API + '?action=checkunlock&unlock=' + encodeURIComponent(digits(c)) + '&token=' + TOKEN + '&callback=' + cb;
      document.body.appendChild(s);
    });
  }

  // Reads #u=<code> from the address (a scanned QR), removes it from the address bar, checks and stores it.
  // Resolves 'ok', 'bad' or 'none'.
  function absorbHash() {
    var m = /[#&?]u=([0-9 %-]+)/.exec(location.hash);
    if (!m) return Promise.resolve('none');
    var c = digits(decodeURIComponent(m[1]));
    try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
    return check(c).then(function (ok) { if (ok) { store(c); return 'ok'; } return 'bad'; });
  }

  // Full-screen prompt: scan today's code, or type the 8 numbers. Resolves once a valid code is stored.
  function ask(why) {
    return new Promise(function (resolve) {
      var o = document.createElement('div');
      o.style.cssText = 'position:fixed;inset:0;z-index:99999;background:rgba(10,30,50,.82);display:flex;align-items:center;justify-content:center;padding:20px;font-family:Nunito,system-ui,sans-serif';
      o.innerHTML =
        '<div style="background:#fff;border-radius:18px;max-width:420px;width:100%;padding:26px 22px;text-align:center;box-shadow:0 10px 40px rgba(0,0,0,.35)">' +
        '<div style="font-size:2.4rem">&#128274;</div>' +
        '<h2 style="margin:6px 0 8px;color:#0a6fa8;font-size:1.35rem">This iPad needs unlocking</h2>' +
        '<p style="color:#444;font-size:.98rem;line-height:1.45;margin:0 0 14px">' + (why || 'Ask your teacher to show you today’s code.') +
        ' Scan the QR code with the iPad camera, or type the 8 numbers below.</p>' +
        '<input id="wfa-unlock-in" inputmode="numeric" autocomplete="off" maxlength="12" placeholder="0000 0000" ' +
        'style="width:100%;font-size:1.6rem;letter-spacing:.12em;text-align:center;padding:10px;border:2px solid #b3dff5;border-radius:12px;font-family:inherit">' +
        '<div id="wfa-unlock-msg" style="min-height:22px;color:#b42318;font-size:.9rem;margin:8px 0"></div>' +
        '<button id="wfa-unlock-go" style="font-family:inherit;font-weight:800;font-size:1.05rem;background:#1798d3;color:#fff;border:0;border-radius:12px;padding:12px 26px;cursor:pointer">Unlock</button>' +
        '</div>';
      document.body.appendChild(o);
      var inp = o.querySelector('#wfa-unlock-in'), msg = o.querySelector('#wfa-unlock-msg'), go = o.querySelector('#wfa-unlock-go');
      var busy = false;
      function submit() {
        if (busy) return;
        var c = digits(inp.value);
        if (c.length !== 8) { msg.textContent = 'The code has 8 numbers.'; return; }
        busy = true; go.textContent = 'Checking…'; msg.textContent = '';
        check(c).then(function (ok) {
          busy = false; go.textContent = 'Unlock';
          if (ok) { store(c); o.parentNode.removeChild(o); resolve(); }
          else { msg.textContent = 'That code did not work. Ask your teacher.'; }
        });
      }
      go.onclick = submit;
      inp.onkeydown = function (e) { if (e.key === 'Enter') submit(); };
      setTimeout(function () { try { inp.focus(); } catch (e) {} }, 50);
    });
  }

  window.WFAUnlock = { code: code, store: store, clear: clear, check: check, absorbHash: absorbHash, ask: ask };
})();
