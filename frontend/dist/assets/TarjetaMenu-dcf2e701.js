import{_ as h,f as i,k as v,e as b,q as x,m as j,g as w,o as C,c as $,a as o,A as d,h as l,u as k,B,j as P}from"./index-e14d68eb.js";/* empty css                                                                    */const T={class:"container shadow-3 col-12",style:{"border-radius":"0.5rem",height:"100%",position:"relative"}},I=["src"],N={class:"texto",style:{}},E={style:{display:"flex",gap:"1rem",height:"100%","flex-direction":"column","justify-content":"space-between"}},M={style:{display:"flex","justify-content":"space-between","align-items":"center"}},R={style:{"text-transform":"uppercase"}},S={style:{display:"flex","justify-content":"space-between","align-items":"center"}},V={style:{display:"flex","align-items":"center",gap:"1rem"}},q={cal:"",class:"text-xl p-0 m-0"},z={__name:"TarjetaMenu",props:{product:{type:Object,default:{}},index:{type:Number,default:12}},setup(p){const u=i({});i({});const a=v(),c=b(),m=t=>{c.addProductToCart(t)},_=i(!1),g=t=>{if(c.setCurrentProduct(t),c.setVisible("currentProduct",!0),a.path!="/"){const e=a.params.menu_name,s=a.params.category_id,r=encodeURIComponent(t.productogeneral_descripcion),y=`/${e}/${s}/${r}/${t.productogeneral_id}/`;P.push(y)}},n=p;x(()=>{u.value={};const t=new IntersectionObserver(e=>{e.forEach(s=>{if(s.isIntersecting){const r=s.target;r.src=r.dataset.src,_.value[r.dataset.index]=!0,t.unobserve(r)}})},{threshold:.1});document.querySelectorAll("img.lazy").forEach((e,s)=>{e.dataset.index=s,t.observe(e)})});const f=j(()=>{var e;const t=((e=n.product)==null?void 0:e.productogeneral_descripcionweb)||"";return t.length>100?t.substring(0,100)+"...":t||"..."});return(t,e)=>{const s=w("Button");return C(),$("div",T,[o("div",{class:"imagen",style:{display:"flex","align-items":"center"},onClick:e[0]||(e[0]=r=>g(n.product))},[o("img",{style:{width:"100%","aspect-ratio":"1 / 1","border-radius":"0.5rem","background-color":"rgb(255, 255, 255)","object-fit":"cover"},src:`https://img.restpe.com/${n.product.productogeneral_urlimagen}`,alt:""},null,8,I)]),o("div",N,[o("div",E,[o("div",M,[o("span",null,[o("b",R,d(n.product.productogeneral_descripcion),1)])]),o("span",null,d(f.value),1),o("div",S,[l(s,{icon:"pi pi-heart text-xl p-0 m-0",text:"",rounded:"",style:{color:"red"}}),o("div",null,[o("div",V,[o("h5",q,[o("b",null,d(k(B)(n.product.productogeneral_precio||n.product.lista_presentacion[0].producto_precio)),1)])])])])])]),l(s,{style:{position:"absolute",right:"-1rem",top:"-1rem"},onClick:e[1]||(e[1]=r=>m(n.product)),severity:"danger",rounded:"",icon:"pi pi-plus text-xl fw-100"})])}}},O=h(z,[["__scopeId","data-v-8ef93e28"]]);export{O as T};