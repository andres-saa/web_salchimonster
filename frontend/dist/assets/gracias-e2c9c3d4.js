import{_ as f,d as S,f as y,z as x,g as b,q as A,h as p,o as v,c as O,a as o,t as u,u as _,C as m,i as r,E as h,p as I,b as $}from"./index-bc41fba6.js";import{u as E}from"./user-5f37e4e0.js";const i=a=>(I("data-v-7916e776"),a=a(),$(),a),C={class:"p-2 col-12 my-3",style:{height:"auto","min-height":"90vh",display:"flex","justify-content":"center","align-items":"center"}},w={class:"shadow-3 p-4",style:{"border-radius":"0.5rem","max-width":"500px"}},D={class:"text-4xl text-center mt-5",style:{"font-weight":"bold"}},R=i(()=>o("p",{class:"text-2xl text-center mb-5",style:{"font-weight":"bold"}},"🔥MUCHAS GRACIAS POR TU COMPRA!🔥",-1)),B={class:"text-4xl text-center my-5",style:{"font-weight":"bold","text-transform":"uppercase"}},U=i(()=>o("span",{class:"text-2xl"},"ID DEL PEDIDO",-1)),M=i(()=>o("br",null,null,-1)),N=i(()=>o("p",{class:"text-2xl text-center my-3 p-3",style:{"border-radius":".3rem","background-color":"var(--primary-color)",color:"white"}},"Hemos recibido tu pedido y en breve será despachado",-1)),L={style:{display:"flex","flex-direction":"column",gap:"1rem"}},k={__name:"gracias",setup(a){const g=S(),n=y(""),t=x(),s=E();return b(()=>{var c,l;n.value=`Hola soy *${s.user.name.toUpperCase()}* 🤗 acabo de hacer el siguiente pedido en la página web. El número de la orden es *#${t.last_order}*.

*🛒 PRODUCTOS*
${t.cart.products.map(e=>`*${e.quantity}* ${e.product.product_name}`).join(`
`)}

`,t.cart.additions.length>0&&(n.value+=`*➕ ADICIONES*
${t.cart.additions.filter(e=>e.group=="ADICIONES").map(e=>`*${e.quantity}* ${e.name}`).join(`
`)}

`),t.cart.additions.filter(e=>e.group=="CAMBIOS").length>0&&(n.value+=`*➕ CAMBIOS*
${t.cart.additions.filter(e=>e.group=="CAMBIOS").map(e=>`*${e.quantity}* ${e.name}`).join(`
`)}

`),t.cart.additions.filter(e=>e.group=="SALSAS").length>0&&(n.value+=`*➕ SALSAS*
${t.cart.additions.filter(e=>e.group=="SALSAS").map(e=>` ${e.name}`).join(`
`)}

`),n.value+=`*📍 DIRECCIÓN*
${s.user.address} BARRIO ${(l=(c=g.location)==null?void 0:c.neigborhood)==null?void 0:l.name}

*📞 TELEFONO*
${s.user.phone_number}

*📝 NOTAS*
${t.cart.order_notes||"Sin notas"}

*💰 METODO DE PAGO*
${s.user.payment_method_option.name}

*Muchas Gracias* 🙏`,console.log(n.value)}),A(()=>{s.user={name:"",neigborhood:"",address:"",phone_number:"",payment_method_option:""},t.cart={products:[],total_cost:0,additions:[]}}),(c,l)=>{const e=p("Button"),d=p("router-link");return v(),O("div",C,[o("div",w,[o("p",D," 🤩"+u(_(s).user.name.toUpperCase())+"🤩",1),R,o("p",B,[U,m(),M,m(" #"+u(_(t).last_order),1)]),N,o("div",L,[r(d,{to:"/"},{default:h(()=>[r(e,{icon:"pi ",iconPos:"right",severity:"help",style:{"font-weight":"bold","background-color":"black",width:"100%"},label:"PUEDES RASTREARLO AQUI"})]),_:1}),r(d,{to:"/"},{default:h(()=>[r(e,{icon:"pi pi-arrow-left",severity:"danger",outlined:"",style:{"font-weight":"bold",border:"none",width:"100%"},label:"VOLVER AL MENU"})]),_:1})])])])}}},j=f(k,[["__scopeId","data-v-7916e776"]]);export{j as default};
