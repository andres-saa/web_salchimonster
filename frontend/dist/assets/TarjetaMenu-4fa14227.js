import{_ as u,x as _,h as g,o as f,c as x,a as s,u as a,U as y,y as h,t as r,i as v,z as b,n as C,P as T,A as P}from"./index-406397d9.js";/* empty css                                                                     */const k={class:"cont",style:{"background-color":"white"}},w=["src"],z={style:{height:"2rem",display:"flex","padding-top":"1rem"}},I={style:{"font-size":"1rem","font-weight":"bold"}},$={class:"info"},j={class:"text-xl",style:{"font-size":"rem","font-weight":"bold"}},A={__name:"TarjetaMenu",props:{product:{type:Object,default:{}}},setup(n){const o=n,c=_(),i=t=>(t.adiciones=[],t.salsas=[],t),d=t=>{P.add(t),c.add({severity:"success",summary:"Agregado al carrito",detail:o.product.name,life:3e3})},l=t=>{t.target.src="https://novatocode.online/assets/logo-f2daca0e.png"};return(t,e)=>{const p=g("Toast");return f(),x("div",k,[s("div",{class:"imagen-cont",style:{position:""},onClick:e[0]||(e[0]=m=>a(h)(n.product))},[s("img",{class:"imagen",onError:l,src:`${a(y)}/read_product_image/300/${o.product.id}`,alt:""},null,40,w)]),s("div",z,[s("p",I,r(o.product.name),1)]),v(p,{style:{"box-shadow":"none"}}),s("div",$,[s("div",j,r(a(b)(o.product.price)),1),s("button",{onClick:e[1]||(e[1]=m=>d(i(o.product))),class:"add-cart-btn"},[s("i",{class:C(["icono text-xl lg:text-4xl p-2",a(T).SHOPPING_CART])},null,2)])])])}}},N=u(A,[["__scopeId","data-v-ed8f8177"]]);export{N as T};