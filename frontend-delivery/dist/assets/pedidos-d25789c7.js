import{D as h}from"./DialogoPedido-860d8b65.js";import{O as r}from"./OrderItem-6aae5e05.js";import{_ as f,u,g as x,o,c as s,a as l,b as e,F as a,i,d as n,s as v,v as y,h as _}from"./index-af185e0c.js";import"./formatoPesos-2a38d2e7.js";import"./logo-c69ae777.js";const p=d=>(v("data-v-e75d658c"),d=d(),y(),d),g={class:"grid xl:mx-2 my-0 py-0"},b={class:"md:px-2 xl:pt-5 p-0 col-12 xl:col-4 top"},w={class:"shadow-4 contenedor pb-2",style:{overflow:"hidden","background-color":"#ffad53"}},m={style:{height:"100%",width:"100%"}},k=p(()=>e("p",{class:"col-12 text-center shadow-4",style:{"background-color":"#ffffff61"}},[e("span",{class:"text-center text-2xl",style:{color:"black","font-weight":"bold"}},[e("i",{class:"pi pi-envelope text-2xl"}),_(" RECIBIDOS")])],-1)),O={class:"lg:pb-8",style:{height:"100%","overflow-y":"auto"}},I={class:"px-3 py-2"},N={class:"md:px-2 xl:pt-5 p-0 col-12 xl:col-4 top"},S={class:"shadow-4 contenedor pb-2",style:{overflow:"hidden","background-color":"#8e3693"}},E={style:{height:"100%",width:"100%"}},T=p(()=>e("p",{class:"col-12 text-center shadow-4",style:{"background-color":"#ffffff61"}},[e("span",{class:"text-center text-2xl",style:{color:"black","font-weight":"bold"}},[e("i",{class:"pi pi-clock text-2xl"}),_(" EN PREPARACION")])],-1)),B={class:"lg:pb-8",style:{height:"100%","overflow-y":"auto"}},D={class:"px-3 py-2"},V={class:"md:px-2 xl:pt-5 p-0 col-12 xl:col-4 top"},A={class:"shadow-4 contenedor pb-2",style:{overflow:"hidden","background-color":"#00bf7a"}},P={class:"lg:pb-8",style:{height:"100%",width:"100%"}},R=p(()=>e("p",{class:"col-12 text-center shadow-4",style:{"background-color":"#ffffff61"}},[e("span",{class:"text-center text-2xl",style:{color:"black","font-weight":"bold"}},[e("i",{class:"pi pi-send text-2xl"}),_(" ENVIADOS")])],-1)),C={style:{height:"100%","overflow-y":"auto"}},F={class:"px-3 py-2"},L={__name:"pedidos",setup(d){const c=u();return x(()=>{c.getTodayOrders()}),(M,j)=>(o(),s("div",g,[l(h),e("div",b,[e("div",w,[e("div",m,[k,e("div",O,[(o(!0),s(a,null,i(n(c).TodayOrders.filter(t=>t.current_status=="generada"),t=>(o(),s("div",I,[l(r,{order:t},null,8,["order"])]))),256))])])])]),e("div",N,[e("div",S,[e("div",E,[T,e("div",B,[(o(!0),s(a,null,i(n(c).TodayOrders.filter(t=>t.current_status=="en preparacion"),t=>(o(),s("div",D,[l(r,{order:t},null,8,["order"])]))),256))])])])]),e("div",V,[e("div",A,[e("div",P,[R,e("div",C,[(o(!0),s(a,null,i(n(c).TodayOrders.filter(t=>t.current_status=="enviada"),t=>(o(),s("div",F,[l(r,{order:t},null,8,["order"])]))),256))])])])])]))}},K=f(L,[["__scopeId","data-v-e75d658c"]]);export{K as default};