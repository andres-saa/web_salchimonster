import{T as m}from"./TarjetaMenu-eb4f228f.js";import{_ as i,e as u,d,g as p,w as _,o as a,c as o,F as g,r as f,U as h,s as y,v}from"./index-841331f2.js";/* empty css                                                               *//* empty css                                                                    */const w={class:"grid xl:col-10 xl:m-auto p-2 m-auto",style:{"border-radius":"2rem","margin-bottom":"5rem","max-width":"1024px"}},x={__name:"sesion",setup(k){const s=u([]),c=d(),n=async r=>{try{let e=await fetch(`${h}/products/category/name/${r}/site/${l.value.currenSiteId}`);if(!e.ok)throw new Error(`HTTP error! status: ${e.status}`);let t=await e.json();s.value=t}catch(e){console.error("Error fetching data: ",e)}};p(async()=>{n(c.params.menu_name)}),_(()=>c.params.menu_name,r=>{n(r)});const l=u(JSON.parse(localStorage.getItem("currentNeigborhood")));return(r,e)=>(a(),o("div",w,[(a(!0),o(g,null,f(s.value,t=>(a(),o("div",{key:t.id,class:"xl:col-3 lg:col-4 md:p-3 col-6 p-3"},[t.state=="active"?(a(),y(m,{key:0,style:{width:"100%"},product:t},null,8,["product"])):v("",!0)]))),128))]))}},B=i(x,[["__scopeId","data-v-bef12022"]]);export{B as default};