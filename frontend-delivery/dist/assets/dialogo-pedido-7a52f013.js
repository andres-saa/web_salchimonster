import{_ as v,k as O,o as R,U as P,l as r,r as I,a as d,c as u,d as t,F as g,e as f,t as l,m as w,u as s,f as h,b as k,w as T,q as C,v as A,x as N,y as $,h as m,z as S,n as j,P as D,A as M,B as F,C as L}from"./index-8dadb416.js";function _(o){return new Intl.NumberFormat("es-CO",{style:"currency",currency:"COP",minimumFractionDigits:0,maximumFractionDigits:0}).format(o)}const B=1e6,U=_(B);console.log(U);function q(o){let n=0;for(let i=0;i<o.length;i++)n+=o[i].price;return n}function z(o){const n={};return o.forEach(e=>{const p=e.id;n[p]?n[p].quantity++:n[p]={product:e,quantity:1}}),Object.values(n).map(e=>e)}function E(o){if(o.price){const n=q(o.adiciones);return o.price+n}else return o.price||0}function x(o){let n=0;for(const i of o.order_products)n+=E(i);return n}const c=o=>(C("data-v-25029b94"),o=o(),A(),o),V={class:"col-12 p-0 m-0 xl:col-12 p-0 md:p-3 texto-negro",style:{width:"100%"}},H=c(()=>t("p",{class:"text-xl col-12 text-center",style:{"font-weight":"bold"}},"SALCHIMONSTER",-1)),G=c(()=>t("p",{class:"text-xl pl-4",style:{"font-weight":"bold",color:"white","background-color":"black"}},"ENTREGAR",-1)),J={class:"productos"},K={class:"producto",style:{display:"flex","justify-content":"space-between","align-items":"center","flex-direction":"column"}},Q={class:"col-12 p-0",style:{display:"flex","justify-content":"space-between","align-items":"center"}},W={class:"",style:{"font-weight":"bold","text-transform":"uppercase","min-width":"max-content",margin:"0",padding:"0.5rem 0"}},X={style:{"font-weight":"bold",height:""}},Y={key:0,class:"col-12 p-0 pl-2 mb-0",style:{"font-weight":"bold"}},Z={class:"col-12 p-0 pl-1",style:{display:"flex","justify-content":"space-between","align-items":"center"}},tt={class:"pl-2",style:{"text-transform":"uppercase","min-width":"",margin:"0",padding:"0.1rem 0",width:"100%"}},et={key:1,class:"col-12 p-0 pl-2 mb-0",style:{"font-weight":"bold"}},st={class:"col-12 p-0 pl-1",style:{display:"flex","justify-content":"space-between","align-items":"center"}},ot={class:"pl-2",style:{"text-transform":"uppercase","min-width":"",margin:"0",padding:"0.1rem 0",width:"100%"}},nt={style:{"font-weight":"",height:""}},at=c(()=>t("div",{style:{width:"100%","border-bottom":"0.1px solid","margin-top":"0rem"}},null,-1)),rt=c(()=>t("br",null,null,-1)),lt={class:"text-l",style:{width:"100%",display:"flex","justify-content":"space-between",margin:"1rem 0"}},it=c(()=>t("span",{style:{"font-weight":"bold"}}," SUBTOTAL ",-1)),dt={style:{"font-weight":"bold"}},ct={class:"text-l",style:{width:"100%",display:"flex","justify-content":"space-between",margin:"1rem 0"}},pt=c(()=>t("span",{style:{"font-weight":"bold"}}," DOMICILIO ",-1)),ut={style:{"font-weight":"bold"}},_t={class:"text-xl",style:{width:"100%",display:"flex","justify-content":"space-between",margin:"1rem 0"}},mt=c(()=>t("span",{style:{"font-weight":"bold"}}," TOTAL ",-1)),ht={style:{"font-weight":"bold"}},yt=c(()=>t("p",{class:"text-xl pl-4",style:{"font-weight":"bold",color:"white","background-color":"black"}},"NOTAS",-1)),bt=c(()=>t("div",{class:"text-l",style:{width:"100%",display:"flex","justify-content":"space-between",margin:"1rem 0"}},[t("p",{class:"text-xl pl-4 col-12 p-0",style:{"font-weight":"bold",color:"white","background-color":"black"}},"DATOS DE USUARIO")],-1)),gt={class:"text-l",style:{width:"100%",display:"flex","justify-content":"space-between",margin:"1rem 0"}},ft=c(()=>t("span",{style:{"font-weight":"bold"}}," NOMBRE ",-1)),wt={style:{"text-transform":"uppercase"}},xt={class:"text-l",style:{width:"100%",display:"flex","justify-content":"space-between",margin:"1rem 0"}},vt=c(()=>t("span",{style:{"font-weight":"bold"}}," TELEFONO ",-1)),It={style:{"text-transform":"uppercase"}},kt={class:"text-l",style:{width:"100%",display:"flex","justify-content":"space-between",margin:"1rem 0"}},Tt=c(()=>t("span",{style:{"font-weight":"bold"}}," DIRECCIÓN ",-1)),Ct={style:{"text-transform":"uppercase"}},At={class:"text-l",style:{width:"100%",display:"flex","justify-content":"space-between",margin:"1rem 0"}},Et=c(()=>t("span",{style:{"font-weight":"bold"}}," MÉTODO DE PAGO ",-1)),Ot={style:{"text-transform":"uppercase"}},Rt={__name:"factura",setup(o){const n=O({});return R(async()=>{const i=`${P}/user/${r.value.user_id}`;try{const e=await fetch(i);if(!e.ok)throw new Error(`Error en la solicitud: ${e.status}`);const p=await e.json();n.value=p}catch(e){console.error("Error en la solicitud:",e)}}),(i,e)=>{const p=I("P");return d(),u("div",V,[H,G,t("div",J,[(d(!0),u(g,null,f(s(z)(s(r).order_products),a=>(d(),u("div",K,[t("div",Q,[t("p",W,[t("span",null,l(a.quantity),1),w(),t("span",null,l(a.product.name),1)]),t("p",X,l(s(_)(a.quantity*s(E)(a.product))),1)]),a.product.salsas.length>0?(d(),u("p",Y,"SALSAS")):h("",!0),(d(!0),u(g,null,f(a.product.salsas,y=>(d(),u("div",Z,[t("p",tt,[t("span",null,l(y),1)])]))),256)),a.product.adiciones.length>0?(d(),u("p",et,"ADICIONES")):h("",!0),(d(!0),u(g,null,f(a.product.adiciones,y=>(d(),u("div",st,[t("p",ot,[t("span",null,l(y.name),1)]),t("p",nt,l(s(_)(y.price)),1)]))),256)),at]))),256)),rt]),t("div",lt,[it,t("span",dt,l(s(_)(s(x)(s(r)))),1)]),t("div",ct,[pt,t("span",ut,l(s(_)(s(r).delivery_price)),1)]),t("div",_t,[mt,t("span",ht,l(s(_)(s(x)(s(r))+s(r).delivery_price)),1)]),yt,k(p,null,{default:T(()=>[w(l(s(r).order_notes),1)]),_:1}),bt,t("div",gt,[ft,t("span",wt,l(n.value.user_name),1)]),t("div",xt,[vt,t("span",It,l(n.value.user_phone),1)]),t("div",kt,[Tt,t("span",Ct,l(n.value.user_address),1)]),t("div",At,[Et,t("span",Ot,l(s(r).payment_method),1)])])}}},Pt=v(Rt,[["__scopeId","data-v-25029b94"]]);const b=o=>(C("data-v-9536643d"),o=o(),A(),o),Nt={class:"btn_accion_dialogo",style:{position:"absolute",top:"90%",display:"flex",gap:"2rem"}},$t=b(()=>t("span",{class:"text-xl p-0",style:{border:"none","font-weight":"bold"}},"PREPARAR",-1)),St=[$t],jt=b(()=>t("span",{class:"text-xl p-0",style:{border:"none","font-weight":"bold"}},"ENVIAR",-1)),Dt=[jt],Mt=b(()=>t("span",{class:"text-xl",style:{border:"none","font-weight":"bold"}},"CANCELAR",-1)),Ft=[Mt],Lt=b(()=>t("span",{class:"text-xl",style:{border:"none","font-weight":"bold"}},"IMPRIMIR",-1)),Bt=[Lt],Ut={__name:"dialogo-pedido",setup(o){const n=()=>{const i=document.getElementById("factura").innerHTML,e=window.open("","_blank");e.document.write("<html><head><title>Factura</title>");const p=document.getElementsByTagName("style");for(let a=0;a<p.length;a++)e.document.write(p[a].outerHTML);e.document.write("</head><body>"),e.document.write(i),e.document.write("</body>   <style>  *{font-family: sans-serif; padding: 0 !IMPORTANT; margin: 0.1rem !IMPORTANT; font-size:0.8rem !IMPORTANT} </style>      </html> "),e.document.close(),e.print(),e.close()};return(i,e)=>{const p=I("Dialog");return d(),N(p,{class:"dialogo",style:$([{"padding-bottom":"7rem","border-radius":"1rem",overflow:"hidden","background-color":"rgb(255, 255, 255)",color:"black"},{width:"40rem"}]),visible:s(m),"onUpdate:visible":e[4]||(e[4]=a=>S(m)?m.value=a:null),modals:"",header:"name",breakpoints:{"1199px":"75vw","575px":"90vw"}},{default:T(()=>[t("button",{class:"btn_cerrar",onClick:e[0]||(e[0]=a=>m.value=!s(m)),style:{"z-index":"99","background-color":"var(--primary-color)",padding:"0.5rem 1rem",border:"none","border-radius":"0.5rem",color:"white",position:"absolute",right:"2rem"}},[t("i",{style:{color:"white","font-weight":"bold","border-radius":"1rem"},class:j(s(D).TIMES)},null,2)]),k(Pt,{class:"factura",id:"factura"}),t("div",Nt,[s(r).order_status.status=="generada"&&s(r).order_status.status!="enviada"?(d(),u("button",{key:0,onClick:e[1]||(e[1]=a=>s(M)(s(r))),style:{border:"none","box-shadow":"0 0 1rem rgba(0, 0, 0, 0.5)",padding:"0rem 2rem","border-radius":"0.5rem","background-color":"rgb(0, 255, 106)"}},St)):h("",!0),s(r).order_status.status=="en preparacion"&&s(r).order_status.status!="enviada"?(d(),u("button",{key:1,onClick:e[2]||(e[2]=a=>s(F)(s(r))),style:{border:"none","box-shadow":"0 0 1rem rgba(0, 0, 0, 0.5)",padding:"0rem 2rem","border-radius":"0.5rem","background-color":"rgb(0, 255, 0)"}},Dt)):h("",!0),s(r).order_status.status!="enviada"?(d(),u("button",{key:2,onClick:e[3]||(e[3]=a=>s(L)(s(r))),style:{border:"none","box-shadow":"0 0 1rem rgba(0, 0, 0, 0.5)",padding:"1rem 2rem","border-radius":"0.5rem","background-color":"rgb(255, 120, 120)"}},Ft)):h("",!0),t("button",{onClick:n,style:{border:"none","box-shadow":"0 0 1rem rgba(0, 0, 0, 0.5)",padding:"1rem 2rem","border-radius":"0.5rem","background-color":"rgb(255, 246, 120)"}},Bt)])]),_:1},8,["visible"])}}},zt=v(Ut,[["__scopeId","data-v-9536643d"]]);export{zt as D};