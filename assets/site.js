/* Relicquary site shared behavior: nav toggle, copy buttons, reveal, year. */
(function(){
  'use strict';

  // year stamp
  var yrs=document.querySelectorAll('.yr');
  for(var i=0;i<yrs.length;i++){ yrs[i].textContent=String(new Date().getFullYear()); }

  // nav toggle
  var toggle=document.getElementById('navToggle');
  var links=document.getElementById('navlinks');
  if(toggle&&links){
    var closeNav=function(){ links.classList.remove('open'); toggle.setAttribute('aria-expanded','false'); };
    toggle.addEventListener('click',function(){
      var open=links.classList.toggle('open');
      toggle.setAttribute('aria-expanded',open?'true':'false');
    });
    var as=links.querySelectorAll('a');
    for(var j=0;j<as.length;j++){ as[j].addEventListener('click',closeNav); }
  }

  // copy buttons: any element with [data-copy] copies that text
  var copies=document.querySelectorAll('[data-copy]');
  for(var k=0;k<copies.length;k++){
    (function(btn){
      btn.addEventListener('click',function(){
        var text=btn.getAttribute('data-copy');
        var done=function(){ var t=btn.textContent; btn.textContent='copied'; setTimeout(function(){ btn.textContent=t; },1400); };
        if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(text).then(done,done); }
        else{ var ta=document.createElement('textarea'); ta.value=text; document.body.appendChild(ta); ta.select(); try{document.execCommand('copy');}catch(e){} document.body.removeChild(ta); done(); }
      });
    })(copies[k]);
  }

  // reveal system with guarded failsafe
  var revs=document.querySelectorAll('.reveal');
  var fired=false;
  var showAll=function(){ for(var m=0;m<revs.length;m++){ revs[m].classList.add('in'); } };
  if(!('IntersectionObserver' in window)){ showAll(); return; }
  var thr=parseFloat(document.body.getAttribute('data-reveal-threshold')||'0.1');
  var io=new IntersectionObserver(function(entries){
    fired=true;
    for(var n=0;n<entries.length;n++){
      if(entries[n].isIntersecting){ entries[n].target.classList.add('in'); io.unobserve(entries[n].target); }
    }
  },{threshold:thr,rootMargin:'0px 0px -8% 0px'});
  for(var p=0;p<revs.length;p++){ io.observe(revs[p]); }
  // quick failsafe if the observer never fired at all
  setTimeout(function(){ if(!fired) showAll(); },1600);
  // hard backstop: content must never stay hidden, whatever the environment does
  setTimeout(showAll,3500);
})();
