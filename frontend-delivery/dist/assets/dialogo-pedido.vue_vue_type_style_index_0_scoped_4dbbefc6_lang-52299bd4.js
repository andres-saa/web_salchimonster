function c(o){return new Intl.NumberFormat("es-CO",{style:"currency",currency:"COP",minimumFractionDigits:0,maximumFractionDigits:0}).format(o)}const s=1e6,a=c(s);console.log(a);function i(o){let t=0;for(let e=0;e<o.length;e++)t+=o[e].price;return t}function d(o){const t={};return o.forEach(r=>{const n=r.id;t[n]?t[n].quantity++:t[n]={product:r,quantity:1}}),Object.values(t).map(r=>r)}function u(o){if(o.price){const t=i(o.adiciones);return o.price+t}else return o.price||0}function m(o){let t=0;for(const e of o.order_products)t+=u(e),console.log("precio producto",t);return t}const l=o=>{let t=0;for(const e of o.product.adiciones)t+=e.price*o.quantity;return o.quantity*o.product.price+t},f=o=>{let t=0;for(const e of o)t+=l(e);return t};export{d as a,l as b,m as c,c as f,f as s};