import{_ as E,d as I,f as $,e as C,C as O,q as R,m as D,G as U,g as x,o as l,c as i,a as t,A as c,u as o,z as S,i as g,h as p,D as A,B as h,p as N,b as B}from"./index-c1bf18d6.js";const n=u=>(N("data-v-3aa82e5c"),u=u(),B(),u),L={class:"p-2 col-12 my-3",style:{height:"auto","min-height":"90vh",display:"flex","justify-content":"center","align-items":"center"}},P={class:"shadow-3 p-4",style:{"border-radius":"0.5rem","max-width":"500px"}},T={class:"text-4xl text-center mt-5",style:{"font-weight":"bold"}},M=n(()=>t("p",{class:"text-2xl text-center mb-5",style:{"font-weight":"bold"}},"🔥MUCHAS GRACIAS POR TU COMPRA!🔥",-1)),V={class:"text-4xl text-center my-5",style:{"font-weight":"bold","text-transform":"uppercase"}},j=n(()=>t("span",{class:"text-2xl"},"ID DEL PEDIDO",-1)),q=n(()=>t("br",null,null,-1)),G=n(()=>t("p",{class:"text-2xl text-center my-3 p-3",style:{"border-radius":".3rem","background-color":"var(--primary-color)",color:"white"}},"Hemos recibido tu pedido y en breve será despachado",-1)),H={id:"factura",style:{width:"100%","text-transform":"uppercase"}},z={class:"",style:{width:"auto",color:"black"}},F=n(()=>t("div",{class:"",style:{"font-weight":"bold",color:"white",margin:"0","background-color":"black","align-items":"center",display:"grid","grid-template-columns":"auto auto"}},null,-1)),Q={class:"",style:{display:"grid",color:"","margin-top":"0.5rem","grid-template-columns":"auto auto"}},Z=n(()=>t("div",{class:""},[t("span",{style:{"font-weight":"bold"}},[t("b",null,"Subtotal")])],-1)),J={class:""},K={style:{"text-align":"end","font-weight":"bold",color:"black"}},W={key:0,class:""},X=n(()=>t("span",{style:{"font-weight":"bold"}},[t("b",null,"Domicilio")],-1)),Y=[X],tt={key:1,class:""},et={style:{"text-align":"end","font-weight":"bold",color:"black"}},ot=n(()=>t("div",{class:""},[t("span",{style:{"font-weight":"bold",color:"black"}},[t("b",null,"Total")])],-1)),st={class:""},at={key:0,style:{"text-align":"end",color:"black","font-weight":"bold"}},nt={key:1,style:{"text-align":"end",color:"black","font-weight":"bold"}},rt=n(()=>t("div",{class:""},null,-1)),lt={style:{display:"flex","flex-direction":"column",gap:"1rem"}},it=["href"],ct={__name:"gracias",setup(u){const m=I(),r=$(""),s=C(),a=O();R(()=>{var d,_;r.value=`Hola soy *${a.user.name.toUpperCase()}* 🤗 acabo de hacer el siguiente pedido en la página web. El número de la orden es *#${s.last_order}*.


*Escribo para Realizar la Transferecia*

*🛒 PRODUCTOS*
${s.cart.products.map(e=>`*${e.quantity}* ${e.product.product_name}`).join(`
`)}

`,s.cart.additions.length>0&&(r.value+=`*➕ ADICIONES*
${s.cart.additions.filter(e=>e.group=="ADICIONES").map(e=>`*${e.quantity}* ${e.name}`).join(`
`)}

`),s.cart.additions.filter(e=>e.group=="CAMBIOS").length>0&&(r.value+=`*➕ CAMBIOS*
${s.cart.additions.filter(e=>e.group=="CAMBIOS").map(e=>`*${e.quantity}* ${e.name}`).join(`
`)}

`),s.cart.additions.filter(e=>e.group=="SALSAS").length>0&&(r.value+=`*➕ SALSAS*
${s.cart.additions.filter(e=>e.group=="SALSAS").map(e=>` ${e.name}`).join(`
`)}

`),r.value+=`*📍 DIRECCIÓN*
${a.user.address} BARRIO ${(_=(d=m.location)==null?void 0:d.neigborhood)==null?void 0:_.name}

*📞 TELEFONO*
${a.user.phone_number}

*📝 NOTAS*
${s.cart.order_notes||"Sin notas"}

*💰 METODO DE PAGO*
${a.user.payment_method_option.name}

*Muchas Gracias* 🙏`,console.log(r.value)});const k=D(()=>{const d="https://api.whatsapp.com/send",_=new URLSearchParams({phone:"573053447255",text:r.value});return`${d}?${_.toString()}`});return U(()=>{a.user={name:"",neigborhood:"",address:"",phone_number:"",payment_method_option:"",was_reserva:!1},s.cart={products:[],total_cost:0,additions:[]}}),(d,_)=>{var y,f,v,w;const e=x("Button"),b=x("router-link");return l(),i("div",L,[t("div",P,[t("p",T," 🤩"+c(o(a).user.name.toUpperCase())+"🤩",1),M,t("p",V,[j,S(),q,S(" #"+c(o(s).last_order),1)]),G,t("div",H,[t("div",z,[F,t("div",Q,[Z,t("div",J,[t("p",K,[t("b",null,c(o(h)(o(s).cart.total_cost)),1)])]),o(a).user.was_reserva?g("",!0):(l(),i("div",W,Y)),o(a).user.was_reserva?g("",!0):(l(),i("div",tt,[t("p",et,[t("b",null,c(o(h)((f=(y=o(m).location)==null?void 0:y.neigborhood)==null?void 0:f.delivery_price)),1)])])),ot,t("div",st,[o(a).user.was_reserva?(l(),i("p",at,[t("b",null,c(o(h)(o(s).cart.total_cost)),1)])):(l(),i("p",nt,[t("b",null,c(o(h)(((w=(v=o(m).location)==null?void 0:v.neigborhood)==null?void 0:w.delivery_price)+o(s).cart.total_cost)),1)]))]),rt])])]),t("div",lt,[p(b,{to:"/rastrear-pedido"},{default:A(()=>[p(e,{class:"mt-3",icon:"pi ",iconPos:"right",severity:"warning",style:{"font-weight":"bold",width:"100%"},label:"PUEDES RASTREARLO AQUI"})]),_:1}),o(a).user.payment_method_option.id==6?(l(),i("a",{key:0,href:k.value,target:"_blank"},[p(e,{icon:"pi pi-whatsapp",severity:"danger",class:"wsp",style:{"font-weight":"bold","background-color":"#00b66c",border:"none",width:"100%"},label:"REALIZAR TRANSFERENCIA"})],8,it)):g("",!0),p(b,{to:"/"},{default:A(()=>[p(e,{icon:"pi pi-arrow-left",severity:"danger",outlined:"",style:{"font-weight":"bold",border:"none",width:"100%"},label:"VOLVER AL MENU"})]),_:1})])])])}}},_t=E(ct,[["__scopeId","data-v-3aa82e5c"]]);export{_t as default};
