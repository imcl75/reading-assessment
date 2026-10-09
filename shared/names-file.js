/* Loads the shared "Show names" helper on STAFF tools only (this repo is public static hosting, so the helper is
   fetched from the wfa-shared CDN copy rather than bundled). Inlined by each tool's build.py. Screens show pupil
   initials; elements marked data-pupil-id="<pupil code>" are swapped for the full name only while a teacher has
   loaded their own names file (kept in page memory, never uploaded or stored). If the CDN is unreachable the
   tool simply carries on showing initials. */
(function(){
  try {
    const s = document.createElement('script');
    s.src = 'https://cdn.jsdelivr.net/gh/wallscourtfarm/wfa-shared@main/web/names-file.js?v=2';
    s.async = true;
    s.onload = function(){
      try {
        if (window.WFANames && WFANames.screen) {
          WFANames.screen.init();
          const st = document.createElement('style'); st.textContent = '@media print{body>button[style*="z-index:99997"],body>div[style*="z-index:99998"]{display:none!important}}';
          document.head.appendChild(st);
        }
      } catch(e) {}
    };
    document.head.appendChild(s);
  } catch(e) {}
})();
