import{r as z,_ as D}from"./empty-cart-1de83224.js";import{_ as J,d as i,i as L,g as I,J as M,k as R,j as U,N as x,B as C,q as T,o as s,c as o,u as a,a as e,F as r,r as d,s as O,n as y,O as V,U as F,t as l,x as c,D as m,Q as u,E as p,P as g,p as G,b as Q,R as A,I as q}from"./index-d8b1f75b.js";/* empty css                                                                        *//* empty css                                                                */const P=_=>(G("data-v-f351525f"),_=_(),Q(),_),H={class:"col-12 p-4 p-0 m-0"},K={key:0,sty:"",class:"contenedor-principal p- md:p-3 grid md:col-10 md:m-auto xl:col-8 xl:ml-auto xl:mr-auto clase",style:{"margin-bottom":"5rem",overflow:"hidden",height:"100%"}},X={class:"col-12 xl:col-7 xl:p-5",style:{}},Y={class:"cont-products grid p-2",style:{position:"inherit"}},Z={class:"m-0 grid mb-5 md:pr-5 pb-6 col-12",style:{"box-shadow":"0 0 10px rgba(0, 0, 0, 0.3)",height:"min-content","border-radius":"1rem",overflow:"hidden",position:"relative","background-color":"white"}},tt=["onClick","src"],et={class:"col-10 grid m-0 pl-5",style:{}},st={class:"col text-left text-md p-0",style:{"font-weight":"bold",display:"flex",gap:"0.5rem"}},ot={class:"name-product",style:{width:"auto"}},nt={class:"col-4 text-right text-md p-0",style:{"font-weight":"bold"}},at={class:"col-12 text-left descripcion p-0",style:{"text-transform":"lowercase"}},lt={key:0,class:"col-12 pl-0 mb-0 pb-0",style:{"font-weight":"bold"}},ct={style:{"max-width":"max-content"}},it={class:"col text-left text-md descripcion p-0",style:{"min-width":"max-content","text-transform":"lowercase"}},rt={style:{"font-weight":"bold"}},dt={key:1,class:"col-12 pl-0 mb-0 pb-0",style:{"font-weight":"bold"}},mt={style:{"max-width":"max-content"}},pt={class:"col text-left text-md descripcion p-0",style:{"min-width":"max-content","text-transform":"lowercase"}},_t={style:{"font-weight":"bold"}},ht={key:2,class:"col-12 pl-0 mb-0 pb-0",style:{"font-weight":"bold"}},ut={style:{"max-width":"max-content"}},xt={class:"col text-left text-md descripcion p-0",style:{"min-width":"max-content","text-transform":"lowercase"}},yt={style:{"font-weight":"bold"}},gt={key:3,class:"col-12 pl-0 mb-0 pb-0",style:{"font-weight":"bold"}},ft={style:{"max-width":"max-content"}},bt={class:"col text-left text-md descripcion p-0",style:{"min-width":"max-content","text-transform":"lowercase"}},wt={style:{"font-weight":"bold"}},vt={key:4,class:"col-12 pl-0 mb-0 pb-0",style:{"font-weight":"bold"}},St={style:{"max-width":"max-content"}},kt={class:"col md:col text-left text-md descripcion p-0",style:{"text-transform":"lowercase"}},Nt={class:"contador col text-reignt"},It=["onClick"],Ct=["value"],Ot=["onClick"],At={key:1,class:"col-12 m-auto d-flex w-100 my-8 p-0 m-0",style:{display:"flex","flex-direction":"column","justify-content":"center","text-align":"center","min-height":"80vh","align-items":"center"}},qt=P(()=>e("img",{style:{width:"100%","max-width":"640px","margin-bottom":"5rem"},src:D,alt:""},null,-1)),Pt=P(()=>e("p",{class:"text-2xl"},"Metele unas Salchis",-1)),jt={__name:"cart",setup(_){i(!1),i(),i([]),i([]);const f=i(window.innerWidth);L(()=>f.value<580);const b=()=>{f.value=window.innerWidth};I(()=>{window.addEventListener("resize",b),M.value=JSON.parse(localStorage.getItem("currentNeigborhood")).currenNeigborhood}),R(()=>{window.removeEventListener("resize",b),U()});const j=h=>{A.add(h),q()},B=h=>{A.remove(h),q()},E=i();I(()=>{x.value=C(JSON.parse(localStorage.getItem("cart")).products),E.value=JSON.parse(localStorage.getItem("cart")).total});const W=C(JSON.parse(localStorage.getItem("cart")).products);return console.log(W),(h,Bt)=>{const $=T("Sesion_main");return s(),o("div",H,[a(x).length>0?(s(),o("div",K,[e("div",X,[e("div",Y,[(s(!0),o(r,null,d(a(x),t=>{var w,v,S,k,N;return s(),o("div",Z,[e("img",{onClick:n=>a(V)(t.product),class:"col-2 p-1",style:{"object-fit":"contain"},src:`${a(F)}/read-product-image/96/${t.product.name}`,alt:""},null,8,tt),e("div",et,[e("div",st,[e("p",null,l(`${t.quantity}  `),1),c(),e("p",ot,l(t.product.name),1)]),e("div",nt,l(a(m)(t.quantity*t.product.price+t.quantity*a(u)(t.product.adiciones)+t.quantity*a(u)(t.product.toppings)+t.quantity*a(u)(t.product.cambios)+t.quantity*a(u)(t.product.acompanantes))),1),e("div",at,l(t.product.description),1),((w=t.product.adiciones)==null?void 0:w.length)>0?(s(),o("p",lt,"ADICIONES")):p("",!0),e("div",ct,[(s(!0),o(r,null,d(t.product.adiciones,n=>(s(),o("span",it,[c(l(n.name)+" + ",1),e("span",rt,l(a(m)(n.price)),1),c(" , ")]))),256))]),((v=t.product.adiciones)==null?void 0:v.length)>0?(s(),o("p",dt,"CAMBIOS")):p("",!0),e("div",mt,[(s(!0),o(r,null,d(t.product.cambios,n=>(s(),o("span",pt,[c(l(n.name)+" + ",1),e("span",_t,l(a(m)(n.price)),1),c(" , ")]))),256))]),((S=t.product.toppings)==null?void 0:S.length)>0?(s(),o("p",ht,"TOPPINGS")):p("",!0),e("div",ut,[(s(!0),o(r,null,d(t.product.toppings,n=>(s(),o("span",xt,[c(l(n.name)+" + ",1),e("span",yt,l(a(m)(n.price)),1),c(" , ")]))),256))]),((k=t.product.acompanantes)==null?void 0:k.length)>0?(s(),o("p",gt,"ACOMPANANTES")):p("",!0),e("div",ft,[(s(!0),o(r,null,d(t.product.acompanantes,n=>(s(),o("span",bt,[c(l(n.name)+" + ",1),e("span",wt,l(a(m)(n.price)),1),c(" , ")]))),256))]),((N=t.product.salsas)==null?void 0:N.length)>0?(s(),o("p",vt,"SALSAS")):p("",!0),e("div",St,[(s(!0),o(r,null,d(t.product.salsas,n=>(s(),o("span",kt,l(n)+", ",1))),256))])]),e("div",Nt,[e("button",{style:{display:"flex","align-items":"center","justify-content":"center",border:"none","background-color":"transparent"},onClick:n=>B(t.product)},[e("i",{class:y(a(g).MINUS)},null,2)],8,It),e("input",{class:"cantidad",style:{"font-size":"1.5rem","text-align":"center",width:"30px",border:"1px none"},readonly:"",type:"text",value:t.quantity},null,8,Ct),e("button",{style:{display:"flex","align-items":"center","justify-content":"center",border:"none","font-weight":"bold","font-size":"3vh","background-color":"transparent"},onClick:n=>j(t.product)},[e("i",{class:y(a(g).PLUS)},null,2)],8,Ot)])])}),256))])]),O(z)])):(s(),o("div",At,[qt,Pt,e("i",{class:y(["text-5xl",a(g).ARROW_DOWN]),style:{margin:"5rem"}},null,2),O($)]))])}}},Dt=J(jt,[["__scopeId","data-v-f351525f"]]);export{Dt as default};