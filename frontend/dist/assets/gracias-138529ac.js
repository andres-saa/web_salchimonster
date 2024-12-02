import{_ as R,d as D,f as L,y as N,E as U,g as T,m as B,I as M,h as O,o as a,c as l,a as t,C as n,u as o,B as C,F as y,r as v,j as f,i as h,G as E,D as _,p as P,b as j}from"./index-35a35cf6.js";const c=g=>(P("data-v-5b3a9d63"),g=g(),j(),g),q={class:"p-2 col-12 my-3",style:{height:"auto","min-height":"90vh",display:"flex","justify-content":"center","align-items":"center"}},V={class:"shadow-3 p-4",style:{"border-radius":"0.5rem","max-width":"500px"}},F={class:"text-4xl text-center mt-5",style:{"font-weight":"bold"}},G=c(()=>t("p",{class:"text-2xl text-center mb-5",style:{"font-weight":"bold"}},"🔥MUCHAS GRACIAS POR TU COMPRA!🔥",-1)),H={class:"text-4xl text-center my-5",style:{"font-weight":"bold","text-transform":"uppercase"}},z=c(()=>t("span",{class:"text-2xl"},"ID DEL PEDIDO",-1)),Q=c(()=>t("br",null,null,-1)),Z=c(()=>t("p",{class:"text-2xl text-center my-3 p-3",style:{"border-radius":".3rem","background-color":"var(--primary-color)",color:"white"}},"Hemos recibido tu pedido y en breve será despachado",-1)),J={id:"factura",style:{width:"100%","text-transform":"uppercase"}},K={class:"",style:{width:"auto",color:"black"}},W=c(()=>t("div",{class:"",style:{"font-weight":"bold",color:"white",margin:"0","background-color":"black","align-items":"center",display:"grid","grid-template-columns":"auto auto"}},[t("div",{style:{width:"100%"},class:"p-1"},[t("b",null," PRODUCTOS")]),t("div",{class:"p-1"},[t("p",{style:{"text-align":"end","font-weight":"bold"}},[t("b",null," TOTAL ")])])],-1)),X={style:{display:"grid","grid-template-columns":"auto auto"}},Y={class:"p-0 m-0"},tt={style:{"text-align":"end",color:"black"}},et=c(()=>t("div",{style:{"background-color":"rgba(0, 0, 0, 0.286)",height:"1px"}},null,-1)),ot={class:"p-1",style:{"background-color":"black","font-weight":"bold",color:"white",width:"100%",margin:"0"}},st={style:{display:"grid","grid-template-columns":"auto 20%","align-items":"center"}},nt={style:{"text-align":"end",color:"black"}},at={class:"",style:{display:"grid",color:"","margin-top":"0.5rem","grid-template-columns":"auto auto"}},lt=c(()=>t("div",{class:""},[t("span",{style:{"font-weight":"bold"}},[t("b",null,"Subtotal")])],-1)),it={class:""},rt={style:{"text-align":"end","font-weight":"bold",color:"black"}},ct={key:0,class:""},dt=c(()=>t("span",{style:{"font-weight":"bold"}},[t("b",null,"Domicilio")],-1)),_t=[dt],ut={key:1,class:""},pt={style:{"text-align":"end","font-weight":"bold",color:"black"}},ht=c(()=>t("div",{class:""},[t("span",{style:{"font-weight":"bold",color:"black"}},[t("b",null,"Total")])],-1)),gt={class:""},mt={key:0,style:{"text-align":"end",color:"black","font-weight":"bold"}},bt={key:1,style:{"text-align":"end",color:"black","font-weight":"bold"}},yt=c(()=>t("div",{class:""},null,-1)),vt={style:{display:"flex","flex-direction":"column",gap:"1rem"}},ft=["href"],St={__name:"gracias",setup(g){const b=D(),d=L(""),s=N(),r=U();T(()=>{var u,p;d.value=`Hola soy *${r.user.name.toUpperCase()}* 🤗 acabo de hacer el siguiente pedido en la página web. El número de la orden es *#${s.last_order}*.


*Escribo para Realizar la Transferecia*

*🛒 PRODUCTOS*
${s.cart.products.map(e=>`*${e.quantity}* ${e.product.product_name}`).join(`
`)}

`,s.cart.additions.length>0&&(d.value+=`*➕ ADICIONES*
${s.cart.additions.filter(e=>e.group=="ADICIONES").map(e=>`*${e.quantity}* ${e.name}`).join(`
`)}

`),s.cart.additions.filter(e=>e.group=="CAMBIOS").length>0&&(d.value+=`*➕ CAMBIOS*
${s.cart.additions.filter(e=>e.group=="CAMBIOS").map(e=>`*${e.quantity}* ${e.name}`).join(`
`)}

`),s.cart.additions.filter(e=>e.group=="SALSAS").length>0&&(d.value+=`*➕ SALSAS*
${s.cart.additions.filter(e=>e.group=="SALSAS").map(e=>` ${e.name}`).join(`
`)}

`),d.value+=`*📍 DIRECCIÓN*
${r.user.address} BARRIO ${(p=(u=b.location)==null?void 0:u.neigborhood)==null?void 0:p.name}

*📞 TELEFONO*
${r.user.phone_number}

*📝 NOTAS*
${s.cart.order_notes||"Sin notas"}

*💰 METODO DE PAGO*
${r.user.payment_method_option.name}

*Muchas Gracias* 🙏`,console.log(d.value)});const $=B(()=>{const u="https://api.whatsapp.com/send",p=new URLSearchParams({phone:"573053447255",text:d.value});return`${u}?${p.toString()}`});return M(()=>{r.user={name:"",neigborhood:"",address:"",phone_number:"",payment_method_option:"",was_reserva:!1},s.cart={products:[],total_cost:0,additions:[]}}),(u,p)=>{var w,x,A,I;const e=O("Button"),S=O("router-link");return a(),l("div",q,[t("div",V,[t("p",F," 🤩"+n(o(r).user.name.toUpperCase())+"🤩",1),G,t("p",H,[z,C(),Q,C(" #"+n(o(s).last_order),1)]),Z,t("div",J,[t("div",K,[W,(a(!0),l(y,null,v(o(s).cart.products,i=>(a(),l("div",null,[t("div",X,[t("p",Y,n(i.quantity)+" "+n(i.product.product_name),1),t("div",null,[t("p",tt,n(o(_)(i.total_cost)),1)])]),et]))),256)),(a(!0),l(y,null,v({ADICIONES:o(s).cart.additions.filter(i=>i.group=="ADICIONES"),SALSAS:o(s).cart.additions.filter(i=>i.group=="SALSAS"),CAMBIOS:o(s).cart.additions.filter(i=>i.group=="CAMBIOS")},(i,k)=>(a(),l("div",{key:k,style:{position:"relative","margin-top":"0.5rem"}},[t("p",ot,[t("b",null,n(k),1)]),(a(!0),l(y,null,v(i,m=>(a(),l("div",null,[t("div",st,[t("div",null,[t("p",null,n(m.quantity)+" "+n(m.name),1)]),t("div",null,[t("p",nt,n(o(_)(m.price*m.quantity)),1)])])]))),256))]))),128)),t("div",at,[lt,t("div",it,[t("p",rt,[t("b",null,n(o(_)(o(s).cart.total_cost)),1)])]),o(r).user.was_reserva?f("",!0):(a(),l("div",ct,_t)),o(r).user.was_reserva?f("",!0):(a(),l("div",ut,[t("p",pt,[t("b",null,n(o(_)((x=(w=o(b).location)==null?void 0:w.neigborhood)==null?void 0:x.delivery_price)),1)])])),ht,t("div",gt,[o(r).user.was_reserva?(a(),l("p",mt,[t("b",null,n(o(_)(o(s).cart.total_cost)),1)])):(a(),l("p",bt,[t("b",null,n(o(_)(((I=(A=o(b).location)==null?void 0:A.neigborhood)==null?void 0:I.delivery_price)+o(s).cart.total_cost)),1)]))]),yt])])]),t("div",vt,[h(S,{to:"/rastrear-pedido"},{default:E(()=>[h(e,{class:"mt-3",icon:"pi ",iconPos:"right",severity:"warning",style:{"font-weight":"bold",width:"100%"},label:"PUEDES RASTREARLO AQUI"})]),_:1}),o(r).user.payment_method_option.id==6?(a(),l("a",{key:0,href:$.value,target:"_blank"},[h(e,{icon:"pi pi-whatsapp",severity:"danger",class:"wsp",style:{"font-weight":"bold","background-color":"#00b66c",border:"none",width:"100%"},label:"REALIZAR TRANSFERENCIA"})],8,ft)):f("",!0),h(S,{to:"/"},{default:E(()=>[h(e,{icon:"pi pi-arrow-left",severity:"danger",outlined:"",style:{"font-weight":"bold",border:"none",width:"100%"},label:"VOLVER AL MENU"})]),_:1})])])])}}},xt=R(St,[["__scopeId","data-v-5b3a9d63"]]);export{xt as default};
