import{_ as b,y as v,f as w,g as C,l as j,h as u,o as p,c as m,a as e,i,D as k,E as P,n as S,G as T,T as B,x as D,C as d,u as E,H as N}from"./index-5395ea26.js";/* empty css                                                                    */const V={class:"container shadow-3 col-12",style:{"border-radius":"0.5rem",height:"100%",position:"relative"}},$=["src"],I={key:0,style:{width:"100%",display:"flex","justify-content":"center","align-items":"center","aspect-ratio":"1 / 1","background-color":"rgb(255, 255, 255)","object-fit":"contain","border-radius":"0.5rem"}},L={class:"texto",style:{}},M={style:{display:"flex",gap:"1rem",height:"100%","flex-direction":"column","justify-content":"space-between"}},z={style:{display:"flex","justify-content":"space-between","align-items":"center"}},O={style:{"text-transform":"uppercase"}},q=["src"],A={style:{display:"flex","justify-content":"space-between","align-items":"c"}},G={style:{display:"flex","align-items":"center",gap:"1rem"}},H={class:"text-xl"},W={__name:"TarjetaMenu",props:{product:{type:Object,default:{}},index:{type:Number,default:12}},setup(_){const c=v(),h=s=>{c.addProductToCart(s)},a=w(!1),g=()=>{a.value=!0},y=s=>{c.setCurrentProduct(s),c.setVisible("currentProduct",!0)},o=_;C(()=>{const s=new IntersectionObserver(t=>{t.forEach(n=>{if(n.isIntersecting){const r=n.target;r.src=r.dataset.src,a.value[r.dataset.index]=!0,s.unobserve(r)}})},{threshold:.1});document.querySelectorAll("img.lazy").forEach((t,n)=>{t.dataset.index=n,s.observe(t)})});const f=j(()=>o.product.product_description.substring(0,100)+"...");return(s,t)=>{var l;const n=u("ProgressSpinner"),r=u("Button");return p(),m("div",V,[e("div",{class:"imagen",style:{display:"flex","align-items":"center"},onClick:t[0]||(t[0]=x=>y(o.product))},[i(B,{name:"fade"},{default:k(()=>[P(e("img",{onLoad:g,class:S(a.value?"cargado":"sin-cargar"),style:{width:"100%","aspect-ratio":"1 / 1","border-radius":"0.5rem","background-color":"rgb(255, 255, 255)","object-fit":"contain"},src:`https://backend.salchimonster.com/read-product-image/300/${o.product.product_name}`,alt:""},null,42,$),[[T,a.value]])]),_:1}),a.value?D("",!0):(p(),m("div",I,[i(n,{style:{width:"60px",height:"60px"},strokeWidth:"8",animationDuration:".2s","aria-label":"Custom ProgressSpinner"})]))]),e("div",L,[e("div",M,[e("div",z,[e("span",null,[e("b",O,d(o.product.product_name),1)]),e("img",{class:"character",style:{width:"4rem"},src:`/images/characters/${o.index}.png`,alt:""},null,8,q)]),e("span",null,d((l=f.value)==null?void 0:l.toLocaleLowerCase()),1),e("div",A,[i(r,{icon:"pi pi-heart text-2xl",text:"",rounded:"",style:{color:"red"}}),e("div",G,[e("span",H,[e("b",null,d(E(N)(o.product.price)),1)])])])])]),i(r,{style:{position:"absolute",right:"-1rem",top:"-1rem"},onClick:t[1]||(t[1]=x=>h(o.product)),severity:"danger",rounded:"",icon:"pi pi-plus text-xl fw-100"})])}}},K=b(W,[["__scopeId","data-v-ac4e479a"]]);export{K as T};