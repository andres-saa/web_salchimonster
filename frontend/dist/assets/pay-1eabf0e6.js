import{r as N}from"./resumen-5dca72e6.js";import{l as V,J as O,U,j as C,e as I,f as _,g as h,o as x,y as $,D as b,a as d,h as r,u as o,c as S,K as B,i as D,L as g,M as y,N as M,O as w,_ as L,d as P,C as T,q as A,w as E,p as R,b as q}from"./index-57707c05.js";import{p as K}from"./pay.vue_vue_type_style_index_0_scoped_3775c0bb_lang-f5d4c636.js";import"./resumen.vue_vue_type_style_index_0_scoped_e0c03dc9_lang-98106281.js";const j={async validateOrder(c){const u=V();try{u.setLoading(!0,"cargando");const l=await O.post(`${U}/validate-order-code`,c);if(l.status===200)l.data.valid?(C.push("/gracias"),u.visible.show_validate=!1):alert("codigo incorrecto"),u.setLoading(!1,"validando tu orden");else return u.setLoading(!1,"validando tu orden"),alert("error, intentalo de nuevo"),null}catch(l){return u.setLoading(!1,"validando tu orden"),console.error("An error occurred while sending the order:",l),alert("error, intentalo de nuevo"),null}}},F={style:{display:"flex","flex-direction":"column",gap:"2rem",position:"relative"}},W={key:0,style:{position:"absolute","background-color":"#ffffff9f",left:"0",right:"0",width:"100%",height:"100%",display:"flex","align-items":"center","justify-content":"center"}},z=d("img",{src:M,alt:"",style:{width:"100%","max-width":"10rem"}},null,-1),G=d("p",{style:{"max-width":"100%",color:"black"}},"Hemos enviado un código de 3 dígitos a tu WhatsApp. Introdúcelo para validar tu pedido.",-1),H={style:{display:"flex",gap:"1rem",margin:"auto"}},J={__name:"validate",setup(c){const u=I(),l=V(),t=_({first:"",second:"",third:""}),m=(a,e)=>{const n=e.target.value;/^\d$/.test(n)?(t.value[a]=n,w(()=>i(a))):e.target.value=""},p=(a,e)=>{e.target.value===""&&w(()=>f(a))},i=a=>{a==="first"?(t.value.second="",document.querySelector("#secondInput").focus()):a==="second"&&(t.value.third="",document.querySelector("#thirdInput").focus())},f=a=>{a==="second"?(t.value.fist="",document.querySelector("#firstInput").focus()):a==="third"&&document.querySelector("#secondInput").focus()},v=async()=>{const a={order_id:u.last_order,order_code:t.value.first+t.value.second+t.value.third};await j.validateOrder(a)};return(a,e)=>{const n=h("Button"),k=h("Dialog");return x(),$(k,{modal:"",class:"mx-2",style:{width:"20rem",display:"flex","flex-direction":"column","background-color":"#fff"},visible:o(l).visible.show_validate,"onUpdate:visible":e[9]||(e[9]=s=>o(l).visible.show_validate=s)},{footer:b(()=>[d("div",null,[r(n,{disabled:o(l).loading.visible,onClick:v,style:{border:"none",width:"100%","font-weight":"bold"},label:"Validar mi pedido",severity:"help"},null,8,["disabled"])])]),default:b(()=>[d("div",F,[o(l).loading.visible?(x(),S("div",W,[r(o(B),{style:{width:"100px",height:"100px"},strokeWidth:"4",animationDuration:".1s","aria-label":"Custom ProgressSpinner"})])):D("",!0),z,G,d("div",H,[r(o(g),{modelValue:t.value.first,"onUpdate:modelValue":e[0]||(e[0]=s=>t.value.first=s),id:"firstInput",style:{width:"3rem",height:"2rem","text-align":"center"},maxlength:"1",onInput:e[1]||(e[1]=s=>m("first",s)),onKeydown:e[2]||(e[2]=y(s=>p("first",s),["backspace"]))},null,8,["modelValue"]),r(o(g),{modelValue:t.value.second,"onUpdate:modelValue":e[3]||(e[3]=s=>t.value.second=s),id:"secondInput",style:{width:"3rem",height:"2rem","text-align":"center"},maxlength:"1",onInput:e[4]||(e[4]=s=>m("second",s)),onKeydown:e[5]||(e[5]=y(s=>p("second",s),["backspace"]))},null,8,["modelValue"]),r(o(g),{modelValue:t.value.third,"onUpdate:modelValue":e[6]||(e[6]=s=>t.value.third=s),id:"thirdInput",style:{width:"3rem",height:"2rem","text-align":"center"},maxlength:"1",onInput:e[7]||(e[7]=s=>m("third",s)),onKeydown:e[8]||(e[8]=y(s=>p("third",s),["backspace"]))},null,8,["modelValue"])])])]),_:1},8,["visible"])}}},Z=c=>(R("data-v-3775c0bb"),c=c(),q(),c),Q={class:"col-12 px-2 my-8 p-0",style:{"margin-top":"6rem"}},X=Z(()=>d("p",{class:"text-center text-2xl my-8"},[d("b",null,"FINALIZAR COMPRA")],-1)),Y={class:"grid mx-auto",style:{"max-width":"800px"}},ee={class:"col-12 md:col-6 p-1 md:px-4",style:{display:"flex","flex-direction":"column",gap:"1rem"}},te={class:"flex flex-wrap align-items-center mb-2 gap-2",style:{width:"100%"}},oe={class:"flex flex-wrap align-items-center mb-2 gap-2",style:{width:"100%"}},se={class:"flex flex-wrap align-items-center mb-2 gap-2",style:{width:"100%"}},le={class:"flex flex-wrap align-items-center mb-2 gap-2",style:{width:"100%"}},ae={class:"flex flex-wrap align-items-center mb-2 gap-2",style:{width:"100%"}},ne={__name:"pay",setup(c){const u=I(),l=P();_(0);const t=T(),m=_([]);return A(async()=>{var p;m.value=await K.getPaymentMethods(),((p=t.user.payment_method_option)==null?void 0:p.id)!=7?l.setNeighborhoodPrice():l.setNeighborhoodPriceCero()}),E(()=>t.user.payment_method_option,p=>{p.id==7?(l.current_delivery=l.location.neigborhood.delivery_price,l.location.neigborhood.delivery_price=0):l.setNeighborhoodPrice()}),(p,i)=>{const f=h("InputText"),v=h("InputMask"),a=h("Dropdown"),e=h("Textarea");return x(),S("div",Q,[r(J),X,d("div",Y,[d("div",ee,[d("div",te,[r(f,{style:{width:"100%"},id:"username",placeholder:"NOMBRE",modelValue:o(t).user.name,"onUpdate:modelValue":i[0]||(i[0]=n=>o(t).user.name=n),invalid:""},null,8,["modelValue"])]),d("div",oe,[r(f,{onClick:i[1]||(i[1]=n=>o(l).setVisible("currentSite",!0)),modelValue:o(l).location.neigborhood.name,style:{width:"100%"},id:"username",placeholder:"Barrio",invalid:"",readonly:""},null,8,["modelValue"])]),d("div",se,[r(f,{modelValue:o(t).user.address,"onUpdate:modelValue":i[2]||(i[2]=n=>o(t).user.address=n),style:{width:"100%"},id:"username",placeholder:"DIRECCION",invalid:""},null,8,["modelValue"])]),d("div",le,[r(v,{modelValue:o(t).user.phone_number,"onUpdate:modelValue":i[3]||(i[3]=n=>o(t).user.phone_number=n),style:{width:"100%"},id:"basic",mask:"999 999 9999",placeholder:"TELEFONO"},null,8,["modelValue"])]),d("div",ae,[r(a,{modelValue:o(t).user.payment_method_option,"onUpdate:modelValue":i[4]||(i[4]=n=>o(t).user.payment_method_option=n),style:{width:"100%"},id:"username",placeholder:"METODO DE PAGO",invalid:"",options:m.value,optionLabel:"name"},null,8,["modelValue","options"])]),r(e,{modelValue:o(u).cart.order_notes,"onUpdate:modelValue":i[5]||(i[5]=n=>o(u).cart.order_notes=n),style:{height:"8rem",resize:"none"},placeholder:"NOTAS:"},null,8,["modelValue"])]),r(N,{class:"md:col-6"})])])}}},pe=L(ne,[["__scopeId","data-v-3775c0bb"]]);export{pe as default};