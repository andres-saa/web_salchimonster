import{_ as w,e as V,d as b,f as c,C as S,q as $,U as y,w as I,g as _,o as R,c as U,a as e,h as l,u as a,p as P,b as k,l as L,t as N}from"./index-e14d68eb.js";import{r as E}from"./resumen-9c00cf67.js";import{p as T}from"./pay.vue_vue_type_style_index_0_scoped_294f5d88_lang-b4604063.js";import{f as B}from"./fetchService-fad9e3cc.js";const d=p=>(P("data-v-3f16f27a"),p=p(),k(),p),D={class:"col-12 px-2 p-0",style:{}},j=d(()=>e("p",{class:"text-center text-2xl mb-8"},[e("b",null,"RESERVAR")],-1)),q={class:"grid mx-auto",style:{"max-width":"800px"}},z={class:"col-12 md:col-6 p-1 md:px-4",style:{display:"flex","flex-direction":"column",gap:"1rem"}},A={class:"flex flex-wrap align-items-center m-0 gap-2",style:{width:"100%"}},F=d(()=>e("h5",{class:"m-0"},"Fecha",-1)),H={class:"flex flex-wrap align-items-center m-0 gap-2",style:{width:"100%"}},G=d(()=>e("h5",{class:"m-0"},"Nombre",-1)),J={class:"flex flex-wrap align-items-center m-0 gap-2",style:{width:"100%"}},K=d(()=>e("h5",{class:"m-0"},"Sede",-1)),O={class:"flex flex-wrap align-items-center m-0 gap-2",style:{width:"100%"}},Q=d(()=>e("h5",{class:"m-0"},"Telefono",-1)),W={class:"flex flex-wrap align-items-center m-0 gap-2",style:{width:"100%"}},X=d(()=>e("h5",{class:"m-0"},"Metodo de pago",-1)),Y=d(()=>e("h5",{class:"m-0 p-0"},"Notas",-1)),Z={__name:"payReservas",setup(p){const i=V(),n=b();c(0);const s=S(),u=c([]),h=c([]);return $(async()=>{h.value=await T.getPaymentMethods(),n.setNeighborhoodPriceCero(),u.value=await B.get(`${y}/sites`)}),I(()=>s.user.payment_method_option,m=>{n.location.neigborhood.delivery_price=0}),(m,o)=>{var g,x;const v=_("Calendar"),r=_("InputText"),f=_("Dropdown"),C=_("InputMask"),M=_("Textarea");return R(),U("div",D,[j,e("div",q,[e("div",z,[e("div",A,[F,l(v,{style:{width:"100%"},id:"username",modelValue:a(s).user.name,"onUpdate:modelValue":o[0]||(o[0]=t=>a(s).user.name=t),invalid:""},null,8,["modelValue"])]),e("div",H,[G,l(r,{style:{width:"100%"},id:"username",modelValue:a(s).user.name,"onUpdate:modelValue":o[1]||(o[1]=t=>a(s).user.name=t),invalid:""},null,8,["modelValue"])]),e("div",J,[K,l(f,{modelValue:a(n).location.siteReservas,"onUpdate:modelValue":o[2]||(o[2]=t=>a(n).location.siteReservas=t),style:{width:"100%"},id:"username",invalid:"",options:(g=u.value)==null?void 0:g.filter(t=>t.show_on_web),optionLabel:"site_name"},null,8,["modelValue","options"])]),e("div",O,[Q,l(C,{modelValue:a(s).user.phone_number,"onUpdate:modelValue":o[3]||(o[3]=t=>a(s).user.phone_number=t),style:{width:"100%"},id:"basic",mask:"999 999 9999"},null,8,["modelValue"])]),e("div",W,[X,l(f,{modelValue:a(s).user.payment_method_option,"onUpdate:modelValue":o[4]||(o[4]=t=>a(s).user.payment_method_option=t),style:{width:"100%"},id:"username",invalid:"",options:(x=h.value)==null?void 0:x.filter(t=>t.id!=7),optionLabel:"name"},null,8,["modelValue","options"])]),Y,l(M,{modelValue:a(i).cart.order_notes,"onUpdate:modelValue":o[5]||(o[5]=t=>a(i).cart.order_notes=t),style:{height:"8rem",resize:"none"},placeholder:"Dimelo:",class:"m-0"},null,8,["modelValue"])]),l(E,{class:"md:col-6"})])])}}},ee=w(Z,[["__scopeId","data-v-3f16f27a"]]);const te={class:"col-12 px-2 my-8 p-0",style:{"margin-top":"6rem",display:"flex","justify-content":"center","flex-direction":"column","align-items":"center","max-width":"1280px",margin:"auto"}},oe={class:"grid mt-6",style:{"align-items":"start","border-radius":"1rem"}},se={class:"col-12 md:col-4 md:pr-0",style:{display:"flex","align-items":"center"}},ae=["src"],ne={class:"col-12 md:col-8 md:pl-0"},re={__name:"reservas",setup(p){const i=L(),n=V(),s=b();c(0);const u=S(),h=c([]),m=c({}),o=[...n.cart.products];$(async()=>{s.location.neigborhood.delivery_price=0,h.value=await T.getPaymentMethods(),s.setNeighborhoodPriceCero(),n.cart.products=[],m.value=await v(),n.addProductToCart(m.value)}),N(()=>{n.cart.products=o});const v=async()=>{i.setLoading(!0,"cargando productos");try{let r=await fetch(`${y}/products-active/category-id/25/site/1/1`);if(!r.ok)throw n.setLoading(!1,"cargando productos"),new Error(`HTTP error! status: ${r.status}`);return i.setLoading(!1,"cargando productos"),(await r.json())[0]}catch(r){i.setLoading(!1,"cargando productos"),console.error("Error fetching data: ",r)}};return I(()=>u.user.payment_method_option,r=>{s.location.neigborhood.delivery_price=0}),(r,f)=>(R(),U("div",te,[e("div",oe,[e("div",se,[e("img",{style:{width:"100%","border-radius":"1rem"},src:`${a(y)}/read-photo-product/${m.value.img_identifier}/600`,alt:""},null,8,ae)]),e("div",ne,[l(ee)])])]))}},pe=w(re,[["__scopeId","data-v-f376cb30"]]);export{pe as default};