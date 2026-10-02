/* SIGEJ Service Worker — caché inteligente (stale-while-revalidate) para consultas básicas con conectividad limitada */
var CACHE='sigej-v1';
self.addEventListener('install',function(e){self.skipWaiting();});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(ks){return Promise.all(ks.filter(function(k){return k!==CACHE;}).map(function(k){return caches.delete(k);}));}).then(function(){return self.clients.claim();}));});
self.addEventListener('fetch',function(e){
  var req=e.request;if(req.method!=='GET')return;var url=new URL(req.url);if(url.origin!==location.origin)return;
  e.respondWith(caches.open(CACHE).then(function(cache){
    return cache.match(req).then(function(cached){
      var net=fetch(req).then(function(res){if(res&&res.status===200)cache.put(req,res.clone());return res;}).catch(function(){return cached||caches.match('SIGEJ_inicio.html');});
      return cached||net;
    });
  }));
});
