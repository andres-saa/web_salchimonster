import{_ as v,f as m,g as u,U as i,o as c,c as l,F as k,r as I,a as t,u as n,n as g,P as f,C as y,t as r,p as S,b as R}from"./index-b786d416.js";const A=a=>(S("data-v-8aae72ee"),a=a(),R(),a),P={class:"grid col-12 lg:col-10 m-auto p-3 m-0 mb-8",style:{"max-width":"1024px"}},j={style:{"border-radius":"0.5rem",overflow:"hidden"},class:"col-12 lg:col-6 p-0 mb-3 lg:p-3 m-0"},M={class:"col-12 p-0 m-0 shadow-3",style:{position:"relative",overflow:"hidden",height:"min-content","box-shadow":"0 0 10px black","border-radius":"0.5rem"}},$=["src"],B={class:"xl:pl-4 pl-2",style:{width:"100%",height:"40%",background:"linear-gradient(to top, black, transparent)",position:"absolute",display:"flex","flex-direction":"column","justify-content":"end",left:"0",bottom:"0","border-radius":"0 0 0.5rem 0.5rem"}},C={class:"xl:text-xl text-l m-0",style:{"font-weight":"bold",color:"var(--primary-color)"}},E={class:"pr-4",style:{"text-transform":"uppercase"}},F={style:{"font-weight":"normal","padding-left":"1rem",color:"white"}},N={style:{color:"white"}},T={class:"xl:text-xl text-l",style:{"font-weight":"normal",color:"white"}},U={class:"pr-4"},D={style:{position:"absolute",right:"0rem",width:"5rem",height:"5rem",bottom:"0","background-color":"transparent",display:"flex",padding:"1rem"}},H=["href"],L=A(()=>t("img",{style:{width:"100%",height:"100%","background-color":"rebeccapurple","border-radius":"0.5rem"},src:"https://th.bing.com/th/id/R.68201495ac2d0c4d1cd3cbf6d25f6755?rik=l%2bilUrRDF30tdw&pid=ImgRaw&r=0"},null,-1)),V=[L],z={__name:"sedes",setup(a){const d=m([]),_=m([]);u(()=>b().then(s=>d.value=s)),u(()=>w().then(s=>_.value=s));const b=async s=>{try{const o=await fetch(`${i}/sites`);if(o.ok)return await o.json()}catch{}},w=async()=>{try{const s=await fetch(`${i}/cities`);if(s.ok)return await s.json()}catch{}};return(s,o)=>(c(),l("div",P,[(c(!0),l(k,null,I(d.value.filter(e=>e.city_id&&e.show_on_web),e=>{var h,p;return c(),l("div",j,[t("div",M,[t("img",{style:{"object-fit":"cover","border-radius":"0.5rem",width:"100%",height:"30rem"},src:`${n(i)}/read-product-image/600/site-${e.site_id}`,alt:""},null,8,$),t("div",B,[t("p",C,[t("span",E,[t("i",{class:g(n(f).MAP_MARKER),style:{color:"var(--primary-color)","font-weight":"bold"}},null,2)]),y(" "+r((p=(h=_.value)==null?void 0:h.filter(x=>e.city_id==x.city_id)[0])==null?void 0:p.city_name)+" ",1),t("span",F,r(e.site_address),1),t("p",N,"SALCHIMONSTER "+r(e.site_name),1)]),t("p",T,[t("span",U,[t("i",{class:g(["text-l p-0",n(f).WHATSAPP]),style:{"font-weight":"bold",color:"rgb(58, 255, 58)"}},null,2)]),y(" "+r(e.site_phone),1)]),t("div",D,[t("a",{href:e.maps,style:{position:"relative"}},V,8,H)])])])])}),256))]))}},O=v(z,[["__scopeId","data-v-8aae72ee"]]);export{O as default};