import{_ as h,a as e,c as o,d as s,F as a,e as _,u as l,b as m,n as r,U as y,f as i,t as p,p as v,h as c,s as f}from"./index-8dadb416.js";import{D as g}from"./dialogo-pedido-7a52f013.js";const b={style:{},class:"grid col-12 m-0 p-0"},x={class:"col p-0",style:{}},k={class:"col-12 mb-6 m-0 pb-0",style:{"border-radius":"1rem","box-shadow":"0px 0px 30px rgba(0, 0, 0, 0.3)",overflow:"hidden"}},w={class:"p-0 grid"},z=["onClick"],C={class:"col-12"},B={class:"grid p-2 pedido",style:{color:"white",cursor:"pointer"}},D={class:""},N=["src"],P={class:"col",style:{display:"flex","justify-content":"end","align-items":"center",gap:"1rem"}},V={key:0,class:"pi pi-spin pi-spinner p-3",style:{"font-size":"3rem",color:"var(--primary-color)","font-weight":"bold"}},$={key:1,class:"pi pi-check p-3",style:{"font-size":"3rem",color:"var(--primary-color)","font-weight":"bold"}},j={key:2,class:"pi pi-star-fill p-3",style:{"font-size":"3rem",color:"var(--primary-color)","font-weight":"bold"}},F={key:3,class:"pi pi-times p-3",style:{"font-size":"3rem",color:"var(--primary-color)","font-weight":"bold"}},I={style:{color:"black","font-weight":"bold","min-width":"max-content"}},U={__name:"historial-pedidos",setup(E){const u=d=>{f(d),c.value=!c.value};return(d,L)=>(e(),o(a,null,[s("div",b,[s("div",x,[s("div",k,[s("div",w,[(e(!0),o(a,null,_(l(v),t=>(e(),o("div",{class:r(["col-12 xl:col-6 p-0",t.order_status.status.split(" ")[0]]),style:{},onClick:n=>u(t)},[s("div",C,[s("div",B,[(e(!0),o(a,null,_(t.order_products,n=>(e(),o("div",D,[s("img",{class:"p-1",style:{width:"60px",height:"60px","object-fit":"contain"},src:`${l(y)}/read_product_image/96/${n.id}`,alt:""},null,8,N)]))),256)),s("div",P,[t.order_status.status=="en preparacion"?(e(),o("i",V)):i("",!0),t.order_status.status=="enviada"?(e(),o("i",$)):i("",!0),t.order_status.status=="generada"?(e(),o("i",j)):i("",!0),t.order_status.status=="cancelada"?(e(),o("i",F)):i("",!0),s("div",{class:r(["p-2",t.order_status.status.split(" ")[0]]),style:{"border-radius":"2rem",color:"black",width:"max-content"}},p(t.order_status.status),3),s("span",I,p(t.order_id),1)])])])],10,z))),256))])])])]),m(g),s("div",{class:r(l(c)?"before":"")},null,2)],64))}},q=h(U,[["__scopeId","data-v-970ee21e"]]);export{q as default};