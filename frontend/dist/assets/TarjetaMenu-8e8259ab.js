import{_ as b,z as x,f as w,g as C,l as j,h as _,o as l,c as d,a as e,i,D as k,E as P,n as S,G as T,T as z,y as B,t as u,F as D,r as E,u as L,H as N}from"./index-20b484e8.js";/* empty css                                                                    */const V={class:"container shadow-3 col-12",style:{"border-radius":"0.5rem",height:"100%",position:"relative"}},$=["src"],I={key:0,style:{width:"100%",display:"flex","justify-content":"center","align-items":"center","aspect-ratio":"1 / 1","background-color":"rgb(255, 255, 255)","object-fit":"contain","border-radius":"0.5rem"}},M={class:"texto",style:{}},F={style:{display:"flex",gap:"1rem",height:"100%","flex-direction":"column","justify-content":"space-between"}},O={style:{display:"flex","justify-content":"space-between","align-items":"center"}},q={style:{"text-transform":"uppercase"}},A=["v-lazy"],G={style:{display:"flex","justify-content":"space-between","align-items":"c"}},H={style:{display:"flex","align-items":"center",gap:"1rem"}},W={class:"text-xl"},J={__name:"TarjetaMenu",props:{product:{type:Object,default:{}},index:{type:Number,default:12}},setup(h){const o=h,c=x(),g=s=>{c.addProductToCart(s)},n=w(!1),y=()=>{n.value=!0},f=s=>{c.setCurrentProduct(s),c.setVisible("currentProduct",!0)};C(()=>{const s=new IntersectionObserver(t=>{t.forEach(a=>{if(a.isIntersecting){const r=a.target;r.src=r.dataset.src,n.value[r.dataset.index]=!0,s.unobserve(r)}})},{threshold:.1});document.querySelectorAll("img.lazy").forEach((t,a)=>{t.dataset.index=a,s.observe(t)})});const v=j(()=>o.product.product_description.substring(0,100)+"...");return(s,t)=>{var p;const a=_("ProgressSpinner"),r=_("Button");return l(),d("div",V,[e("div",{class:"imagen",style:{display:"flex","align-items":"center"},onClick:t[0]||(t[0]=m=>f(o.product))},[i(z,{name:"fade"},{default:k(()=>[P(e("img",{onLoad:y,class:S(n.value?"cargado":"sin-cargar"),style:{width:"100%","aspect-ratio":"1 / 1","border-radius":"0.5rem","background-color":"rgb(255, 255, 255)","object-fit":"contain"},src:`https://backend.salchimonster.com/read-product-image/300/${o.product.product_name}`,alt:""},null,42,$),[[T,n.value]])]),_:1}),n.value?B("",!0):(l(),d("div",I,[i(a,{style:{width:"60px",height:"60px"},strokeWidth:"8",animationDuration:".2s","aria-label":"Custom ProgressSpinner"})]))]),e("div",M,[e("div",F,[e("div",O,[e("span",null,[e("b",q,u(o.product.product_name),1)]),(l(),d(D,null,E([1],m=>e("img",{class:"character",style:{width:"6rem"},"v-lazy":`/images/characters/${o.index}.png`,alt:""},null,8,A)),64))]),e("span",null,u((p=v.value)==null?void 0:p.toLocaleLowerCase()),1),e("div",G,[i(r,{icon:"pi pi-heart text-2xl",text:"",rounded:"",style:{color:"red"}}),e("div",H,[e("span",W,[e("b",null,u(L(N)(o.product.price)),1)])])])])]),i(r,{style:{position:"absolute",right:"-1rem",top:"-1rem"},onClick:t[1]||(t[1]=m=>g(o.product)),severity:"danger",rounded:"",icon:"pi pi-plus text-xl fw-100"})])}}},R=b(J,[["__scopeId","data-v-cf446e37"]]);export{R as T};