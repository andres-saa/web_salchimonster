import{T as m}from"./TarjetaMenu-f35e2ad5.js";import{A as f,d as h,B as y,f as l,k as w,g as x,C as u,w as k,U as S,o as r,c,a as i,D as v,t as T,u as b,F as L,r as N,i as $}from"./index-1e89a5bc.js";/* empty css                                                                    */const B={class:"grid p-1 pb-8",style:{"max-width":"1024px",margin:"auto"}},j={class:"text-center text-3xl col-12",style:{"font-weight":"bold",display:"flex",gap:"1rem","align-items":"center"}},E=i("div",{style:{width:"100%",height:"5px","background-color":"#ff6200"}},null,-1),R=i("div",{style:{width:"100%",height:"5px","background-color":"#ff6200"}},null,-1),M={__name:"sesion",setup(V){f();const g=h(),a=y(),n=l([]),o=w();x(async()=>{d(),await u()}),k(()=>o.params.category_id,async()=>{o.params.category_id&&(d(),await u())},{deep:!0});const d=async p=>{const s=g.location.site.site_id,e=o.params.category_id;if(e&&s){a.setLoading(!0,"cargando productos");try{let t=await fetch(`${S}/products-active/category-id/${e}/site/${s}`);if(!t.ok)throw a.setLoading(!1,"cargando productos"),new Error(`HTTP error! status: ${t.status}`);a.setLoading(!1,"cargando productos");let _=await t.json();n.value=_}catch(t){a.setLoading(!1,"cargando productos"),console.error("Error fetching data: ",t)}}};return l(JSON.parse(localStorage.getItem("currentNeigborhood"))),(p,s)=>(r(),c("div",B,[i("p",j,[E,v(" "+T(b(o).params.menu_name)+" ",1),R]),(r(!0),c(L,null,N(n.value,(e,t)=>(r(),c("div",{key:e.id,class:"col-12 md:col-4 lg:col-3 sm:col-6"},[$(m,{style:{width:"100%"},id:`tarjeta-${t}`,product:e},null,8,["id","product"])]))),128))]))}};export{M as default};