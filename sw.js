// Cripta d20: funciona sin conexión una vez instalada.
const VERSION='cripta-d20-v18';
const SHELL=['./','index.html','manifest.webmanifest','icon-192.png','icon-512.png','maskable-512.png','apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(VERSION).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==VERSION).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const req=e.request;if(req.method!=='GET')return;
  const url=new URL(req.url);
  // Fuentes de Google: se guardan la primera vez para usarlas sin conexión.
  if(url.hostname.includes('fonts.googleapis.com')||url.hostname.includes('fonts.gstatic.com')){
    e.respondWith(caches.open(VERSION).then(c=>c.match(req).then(hit=>hit||fetch(req).then(r=>{c.put(req,r.clone());return r}).catch(()=>hit))));return;
  }
  // El juego: primero la red (para recibir actualizaciones), si no hay conexión usa lo guardado.
  if(url.origin===location.origin){
    e.respondWith(fetch(req).then(r=>{const cp=r.clone();caches.open(VERSION).then(c=>c.put(req,cp));return r}).catch(()=>caches.match(req).then(h=>h||caches.match('index.html'))));
  }
});
