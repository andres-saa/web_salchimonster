import{_ as w,x as k,d as c,k as h,o as d,c as u,l as b,q as $,a as o,v as j,t as m,E as f,u as l,U as p,C as E,z as I,n as T,P as U,F as z}from"./index-46e4bcc0.js";const D={key:0},F=["src"],N=["src"],P={class:"cont",style:{"background-color":"white"}},S={class:"imagen-cont",style:{position:""}},V=["src"],A={style:{height:"2rem",display:"flex","padding-top":"1rem"}},B={style:{"font-size":"1rem","font-weight":"bold"}},L={class:"info"},O={class:"text-xl",style:{"font-size":"2rem","font-weight":"bold"}},R={__name:"TarjetaMenuAdmin",props:{product:{type:Object,default:{}}},setup(y){const s=y;k();const a=c(!1),_=c(null),n=c(null),x=t=>{const e=t.target.files[0];e&&(_.value=e,n.value=URL.createObjectURL(e))},C=async()=>{try{const t=new FormData;t.append("file",_.value);const e=`${p}/upload-product-image/${s.product.id}`;console.log(e);const r=await(await fetch(e,{method:"POST",body:t})).json();console.log("Imagen subida exitosamente:",r),a.value=!a.value,location.reload()}catch(t){console.error("Error al subir la imagen:",t)}},g=t=>{t.target.src="https://salchimonster.com/images/logo.png"};return(t,e)=>{const v=h("Dialog"),r=h("Toast");return d(),u(z,null,[b(v,{visible:a.value,"onUpdate:visible":e[1]||(e[1]=i=>a.value=i),style:E([{width:"500px"},{"background-color":"rgb(255, 255, 255)",border:"none","border-radius":"1rem","padding-top":"2rem",color:"rgb(255, 7, 7)"}]),header:"Seleccion de sede",modal:!0,class:"p-fluid p-3"},{default:$(()=>[o("div",null,[j(m(s.product.id)+" ",1),o("input",{type:"file",onChange:x},null,32),n.value?(d(),u("div",D,[o("img",{src:n.value,style:{width:"100%",height:"30rem","object-fit":"contain"},alt:"Uploaded"},null,8,F)])):f("",!0),n.value?f("",!0):(d(),u("img",{key:1,class:"imagen",onError:g,src:`${l(p)}/read_product_image/300/${s.product.id}`,alt:""},null,40,N)),o("button",{onClick:e[0]||(e[0]=i=>C())},"Subir Imagen")])]),_:1},8,["visible"]),o("div",P,[o("div",S,[o("img",{class:"imagen",onError:g,src:`${l(p)}/read_product_image/300/${s.product.id}`,alt:""},null,40,V)]),o("div",A,[o("p",B,m(s.product.name),1)]),b(r,{style:{"box-shadow":"none"}}),o("div",L,[o("div",O,m(l(I)(s.product.price)),1),o("button",{onClick:e[2]||(e[2]=i=>a.value=!a.value),class:"add-cart-btn text-xl"},[o("i",{style:{color:"red","z-index":"99"},class:T(["icono text-5xl lg:text-6xl p-0 m-0",l(U).PENCIL])},null,2)])])])],64)}}},q=w(R,[["__scopeId","data-v-93c288d6"]]);export{q as t};