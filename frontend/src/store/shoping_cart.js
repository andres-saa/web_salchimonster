    import { defineStore } from "pinia";
    import { URI } from "../service/conection";


    export const usecartStore = defineStore('cart', {
        persist: {
            key: 'cart', 
            storage: localStorage,
            paths: ['cart','last_order','menu']
        },
        state: () => ({
            currentProduct: {},
            visibles: {
                currentProduct: false,
                addAdditionToCart: false,
                last_order:''
            },
            cart: {
                products: [],
                total_cost: 0,
                additions: []  // Nueva propiedad para manejar las adiciones a nivel del carrito
            },
            last_order:'',
            sending_order:false,
            was_reserva:false,
            menu:{
                    "tipo": "1",
                    "data": [
                        {
                            "productogeneral_id": "59",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "1/4 CHICKEN MONSTER",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "27",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/22428b7d-57e1-4f94-ac44-d4ecbe36d4a4.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "62",
                                    "producto_presentacion": "",
                                    "producto_precio": "22000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/618ddc6c-6716-4ee4-98a8-e8b4a6955006.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "POLLO"
                        },
                        {
                            "productogeneral_id": "147",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "2X1 BURGER MONSTER + 2 PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "25",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/9a405418-5bd2-4871-81c7-791a46629ba7.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "150",
                            "productogeneral_precio": "40000.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "109",
                                    "producto_descripcion": "Burger Monster",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "2.000",
                                    "productocombo_precio": "26900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/8fb70cd1-2133-4140-a9ce-e9642dadb58b.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS"
                        },
                        {
                            "productogeneral_id": "96",
                            "productogeneral_descripcionweb": "BURGERMONSTER 2 X 1",
                            "productogeneral_descripcion": "2X1 BURGERMONSTER + PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "10",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/36e91489-7763-40a8-afd0-752153efc518.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "98",
                            "productogeneral_precio": "45000.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "28",
                                    "producto_descripcion": "Burgermonster",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "2.000",
                                    "productocombo_precio": "26900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "141",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/0d0f12b6-a4fd-4e6d-9f30-355269d7ef22.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [],
                            "categoria_descripcion": "COMBOS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "146",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "2X1 MONSTER BACON + 2 PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "25",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/5565993c-d958-4999-aa01-d13b3d3542fd.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "149",
                            "productogeneral_precio": "37900.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "108",
                                    "producto_descripcion": "Monster Bacon",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "24900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/990cd9d3-e106-49fe-aa1a-698b636c28a3.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS"
                        },
                        {
                            "productogeneral_id": "145",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "2X1 MONSTER CHEESE + 2 PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "25",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/e51fc412-00c9-4576-8ab7-dc28ac668544.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "148",
                            "productogeneral_precio": "33500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "107",
                                    "producto_descripcion": "Monster Cheese",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "2.000",
                                    "productocombo_precio": "21900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/650b5748-902c-43ee-9013-2249ab26b785.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS"
                        },
                        {
                            "productogeneral_id": "143",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "2X1 MONSTER CHICKEN + 2 PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "25",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/0188eea0-3167-45fa-815a-5e4cba8e52e2.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "146",
                            "productogeneral_precio": "30900.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "105",
                                    "producto_descripcion": "Monster Chicken",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "2.000",
                                    "productocombo_precio": "19900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/8d354549-2cdc-4764-a381-215c74bf3ca9.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS"
                        },
                        {
                            "productogeneral_id": "148",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "2X1 MONSTER DOBLE CARNE + 2 PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "25",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/116ce362-2d4f-4b18-a0a8-55f8c4387e01.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "151",
                            "productogeneral_precio": "38900.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "110",
                                    "producto_descripcion": "Monster Doble Carne",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "2.000",
                                    "productocombo_precio": "29900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/e7ccdb25-8e78-4084-8966-3c646af45cbe.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS"
                        },
                        {
                            "productogeneral_id": "144",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "2X1 MONSTER GHETTO + 2 PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "25",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/5362ca80-e2cb-4b52-a9c9-1eaf8447a476.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "147",
                            "productogeneral_precio": "32500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "106",
                                    "producto_descripcion": "Monster Ghetto",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "2.000",
                                    "productocombo_precio": "20900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/ac372c64-b08c-4f95-83be-1e5be4222c41.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS"
                        },
                        {
                            "productogeneral_id": "150",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "2X1 MONSTER REALEZA + 2 PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "25",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/0837b6f5-1db7-4beb-9c23-a7058bcd9dc4.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "153",
                            "productogeneral_precio": "51500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "112",
                                    "producto_descripcion": "Monster Realeza",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "2.000",
                                    "productocombo_precio": "35900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/4c1b5afb-c8ee-4773-b0c6-dff9ac67fb0f.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS"
                        },
                        {
                            "productogeneral_id": "142",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "2X1 MONSTER SENCILLA + 2 PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "25",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/3fb36964-8115-4a14-93bc-ae897f2cb1db.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "145",
                            "productogeneral_precio": "30900.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "104",
                                    "producto_descripcion": "Monster Sencilla",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "2.000",
                                    "productocombo_precio": "19900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/5cb87b86-5611-4f72-80f0-485ae4c30857.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS"
                        },
                        {
                            "productogeneral_id": "149",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "2X1 OIGA, MIRE, VEA + 2 PAPAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "25",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/16715f23-678d-4d5d-bb4b-b92abe842ef9.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "152",
                            "productogeneral_precio": "46500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "111",
                                    "producto_descripcion": "Oiga, Mire, Vea",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "2.000",
                                    "productocombo_precio": "31900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/6bf52f0f-4041-48b3-b212-3c67df44a29f.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "139",
                                    "producto_descripcion": "Papa Criolla Para Burger (150G)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "138",
                                            "producto_descripcion": "Papa Francesa Para Burger (150Gr) - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "71",
                                            "producto_descripcion": "Adicion Papa Amarilla - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "6600.0000000",
                                            "alternativacombo_costoadicional": "2600.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/99a6281a-6323-4078-845a-2e5b4ae2c81a.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS"
                        },
                        {
                            "productogeneral_id": "61",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION BACON PREMIUM",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/bc94d869-b775-4bdb-81ea-1e1e267bab32.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "63",
                                    "producto_presentacion": "",
                                    "producto_precio": "8800.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/f53c8dde-0a95-4d9c-9267-9d6d37e94ffe.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "78",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION CARNE DE RES",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "16",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/da400c65-b2f0-4c40-ad44-5cd0df8374fd.jpeg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "80",
                                    "producto_presentacion": "",
                                    "producto_precio": "8000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/0fe38797-458b-43aa-81da-1702a73e5676.jpeg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES HAMBURGUESA"
                        },
                        {
                            "productogeneral_id": "62",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION CARNE PREMIUM (DESMECHADA)",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/c5aacf9e-e121-48e9-898c-c09895a204ca.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "64",
                                    "producto_presentacion": "",
                                    "producto_precio": "16500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/2bf5d5fa-d197-4d9e-a54c-73b0f036d16f.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "63",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION CHICHARRON",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/63f78b5e-cb26-4970-81bd-2486b44261ca.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "65",
                                    "producto_presentacion": "",
                                    "producto_precio": "19500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/6e364326-85df-4627-a2e8-f6b11a63369e.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "64",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION CHORIZO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/d1250b95-9f04-4567-83a7-6757620d3f42.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "66",
                                    "producto_presentacion": "",
                                    "producto_precio": "14000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/4a6e9906-1617-4b21-b3d6-5c53645427b3.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "65",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION COSTILLA AHUMADA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/bfe96ec1-e183-4986-ab17-cc31e1be4c4f.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "67",
                                    "producto_presentacion": "",
                                    "producto_precio": "17900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/3c4d272c-7d5c-4367-a94d-560ef4d35324.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "66",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION GUACAMOLE",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/ef53a4b8-750a-439f-bddf-0323e15558a5.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "68",
                                    "producto_presentacion": "",
                                    "producto_precio": "6600.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/9f878f96-cb47-4e3a-876f-4e7f8fbb9942.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "67",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION MADURO GUAYABO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/a840d3b4-b837-4e86-bf92-9261fc4072c2.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "69",
                                    "producto_presentacion": "",
                                    "producto_precio": "5500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/d79382ea-97ff-437a-9c08-ca43864a8d4c.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "68",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION MAIZ",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/fc84cb83-7767-4539-911b-91f42110d9e4.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "70",
                                    "producto_presentacion": "",
                                    "producto_precio": "5500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/0aaf6de8-e639-4798-ba86-5b29bfb98cf7.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "69",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION PAPA AMARILLA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/b7bc9d2c-8409-4f70-b5ea-ad949d5d619a.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "71",
                                    "producto_presentacion": "",
                                    "producto_precio": "6600.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/99a6281a-6323-4078-845a-2e5b4ae2c81a.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "70",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION PAPA FRANCESA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/5d0bc4f4-350f-44a3-87fe-a7b9d81ec562.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "72",
                                    "producto_presentacion": "",
                                    "producto_precio": "7700.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/96cd9a59-e9ee-4ad7-af0e-e2e58350d5fa.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "71",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION PICO E GALLO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/d61198ae-bc27-4c5f-92e6-8279fb6cff7d.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "73",
                                    "producto_presentacion": "",
                                    "producto_precio": "3500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/ca6d805f-a6fb-4768-96a3-eb445e248edf.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "72",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION POLLO APANADO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/d0a2531b-7bd1-4c47-888e-5808e7f9749a.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "74",
                                    "producto_presentacion": "",
                                    "producto_precio": "15500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/e223a46f-bb79-47bd-b252-8145d1b76678.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "73",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION POLLO DESMECHADO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/a1047f79-eede-48f7-ae91-0c44181121f4.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "75",
                                    "producto_presentacion": "",
                                    "producto_precio": "16500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/6bdc17db-97b5-49d9-9f34-b8753472007e.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "74",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION QUESO MOZARELLA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/057fc89a-1811-459c-93e3-04b0e1eaad63.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "76",
                                    "producto_presentacion": "",
                                    "producto_precio": "6600.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/a2c8991b-c6d0-440e-a298-87e47db811e1.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "79",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION QUESO MOZARELLA 2 LONCHAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "16",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/ec87e8e5-435b-4aa4-ac73-d8306c1e68b0.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "81",
                                    "producto_presentacion": "",
                                    "producto_precio": "6000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/95875539-d1f4-446a-a44f-1dd5076d31e0.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES HAMBURGUESA"
                        },
                        {
                            "productogeneral_id": "75",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION RIPIO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/5e98f787-0ca0-4c3d-8b89-1d872a76153a.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "77",
                                    "producto_presentacion": "",
                                    "producto_precio": "3500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/260ec543-1ac8-40f4-9693-f425707897d7.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "76",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION SALCHICHA PREMIUM",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/338018fb-c063-4f38-bb27-ed48de2bfe10.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "78",
                                    "producto_presentacion": "",
                                    "producto_precio": "8900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/cc8b7af8-9ec1-4e72-896f-2ac4f4280ccc.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "77",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "ADICION SALCHICHA RANCHERA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "14",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/4e626a07-ae9a-4618-85f6-db996947dd19.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "79",
                                    "producto_presentacion": "",
                                    "producto_precio": "20000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/06293c9d-77f9-4011-ad7a-908d2e4b0785.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS"
                        },
                        {
                            "productogeneral_id": "9",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "AGUA BRISA 600 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/bc4e98ad-d833-441a-98b7-ff7627a8e648.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "11",
                                    "producto_presentacion": "Agua 600",
                                    "producto_precio": "4000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/1d5f9ba8-cb77-4392-99f9-76a969883f19.webp",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "120",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "27",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "BACONMONSTER 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/c960fa39-026f-4683-9278-d2e12fe3c1fe.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "29",
                                    "producto_presentacion": "",
                                    "producto_precio": "40500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/d7b48589-46f4-4e88-a2eb-24fe98c307dc.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "143",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "41",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "BACONMONSTER PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/c6a03e04-aaa9-4516-a2a5-6e438bc5fac8.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "43",
                                    "producto_presentacion": "",
                                    "producto_precio": "28500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/61841d74-062e-4a6f-a781-f5ea353d51e4.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "157",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "80",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "BAÑO DE QUESO BURGER 6 LONCHAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "16",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/f1bb94e9-602d-4e46-86f6-acf6117a6370",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "82",
                                    "producto_presentacion": "",
                                    "producto_precio": "10000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/2c84afb0-4c4d-40e3-8282-53824a481f3d",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES HAMBURGUESA"
                        },
                        {
                            "productogeneral_id": "107",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "BURGER MONSTER",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "18",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/a795aaa8-a309-4312-88db-1e41245bb408.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "109",
                                    "producto_presentacion": "",
                                    "producto_precio": "26900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/8fb70cd1-2133-4140-a9ce-e9642dadb58b.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "HAMBURGUESAS"
                        },
                        {
                            "productogeneral_id": "26",
                            "productogeneral_descripcionweb": "",
                            "productogeneral_descripcion": "BURGERMONSTER",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "13",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/c4f2f1b6-57ca-4de8-842d-283ec9d01d8a.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "28",
                                    "producto_presentacion": "",
                                    "producto_precio": "26900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/0d0f12b6-a4fd-4e6d-9f30-355269d7ef22.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "141",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "PRODUCTO NUEVO"
                        },
                        {
                            "productogeneral_id": "23",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "CERVEZA BUDWEISER LATA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "5",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/4752807d-c2c4-4d15-ab58-f010e9d14259.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "25",
                                    "producto_presentacion": "",
                                    "producto_precio": "8500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/06ec99ef-d2f6-4157-9da9-b60330520874.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "134",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Cervezas"
                        },
                        {
                            "productogeneral_id": "24",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "CERVEZA CORONA BOT. 355ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "5",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/72a0447d-8d53-48c0-b063-123fdfb41e1c.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "26",
                                    "producto_presentacion": "",
                                    "producto_precio": "9900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/f19ad6a5-aa68-4ed7-bac2-18adc3c44ff4.jpeg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "135",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "20",
                                    "modificador_nombre": "MICHELADO",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "51",
                                            "modificadorseleccion_nombre": "MICHELADO",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "2000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "Cervezas"
                        },
                        {
                            "productogeneral_id": "33",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "CHICHAMONSTER",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/60322090-a45b-4e85-9c6b-898d042e3fd5.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "35",
                                    "producto_presentacion": "",
                                    "producto_precio": "48000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/19f8aa13-45a5-4613-8caf-67c4fd6bd2ee.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "149",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "28",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "CLASICMONSTER 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/45c8cde1-9839-4721-bc0f-033b0f944c5a.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "30",
                                    "producto_presentacion": "",
                                    "producto_precio": "30900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/dae2cb82-97ca-49f1-897f-f9734e238147.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "144",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "42",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "CLASICMONSTER PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/b87b7db7-3630-4b18-8ed3-c17ad0fe29e3.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "44",
                                    "producto_presentacion": "",
                                    "producto_precio": "22900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/64b3edf0-69bd-48c2-8b85-4f1ca204aa46.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "158",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "10",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COCA COLA SABOR ORIGINAL 1.5 LT",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/be37c1f8-9e6c-41c4-b059-b39300a22338.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "12",
                                    "producto_presentacion": "",
                                    "producto_precio": "8900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/ba2a099b-73c8-4814-8cb7-ad4336f30d3d.webp",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "121",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "11",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COCA COLA SABOR ORIGINAL 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/491ad643-359d-4bbb-9834-68aa1d432339.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "13",
                                    "producto_presentacion": "",
                                    "producto_precio": "5900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "12",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COCA COLA ZERO 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/4f2da33b-720e-4364-848c-7df6998ee8a1.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "14",
                                    "producto_presentacion": "",
                                    "producto_precio": "5900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "123",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "157",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COCACOLA ZERO 1.5L",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/b86180e9-dc37-4dec-9c0f-7aa9ac9687e2.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "161",
                                    "producto_presentacion": "",
                                    "producto_precio": "8900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/39df6606-8926-4cdb-bf1b-38a92d6370e2.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "152",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO BACONMONSTER 2P + 2 BEBIDAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "1",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "10",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/019ab3e5-8703-4fce-b4e5-7d0218f71ebf.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "155",
                            "productogeneral_precio": "41900.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "29",
                                    "producto_descripcion": "Baconmonster 2 Personas",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "40500.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "143",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/d7b48589-46f4-4e88-a2eb-24fe98c307dc.png",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "23",
                                    "producto_descripcion": "Quatro 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "132",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "13",
                                            "producto_descripcion": "Coca Cola Sabor Original 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "122"
                                        },
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "98",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO BACONMONSTER PERSONAL + BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "26",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/9cdb1a6b-35e0-4bed-b362-ce5d294cb082.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "100",
                            "productogeneral_precio": "27500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "43",
                                    "producto_descripcion": "Baconmonster Personal",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "28500.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "157",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/61841d74-062e-4a6f-a781-f5ea353d51e4.png",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS PERSONALES"
                        },
                        {
                            "productogeneral_id": "132",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO BURGER MONSTER  +PAPAS+BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "22",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/f71280d1-9050-43cd-960d-5c5fb23d29a7.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "134",
                            "productogeneral_precio": "31500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "109",
                                    "producto_descripcion": "Burger Monster",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "26900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/8fb70cd1-2133-4140-a9ce-e9642dadb58b.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "130",
                                    "producto_descripcion": "Papas Francesa Para Burger (No)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7e80da5d-be85-4eeb-a3a9-74efb3643bd0.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER"
                        },
                        {
                            "productogeneral_id": "101",
                            "productogeneral_descripcionweb": "COMBO BURGERMONSTER + PAPAS + BEBIDA",
                            "productogeneral_descripcion": "COMBO BURGERMONSTER + PAPAS + BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "26",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/8a13a3a8-9ce4-4c2c-a1f1-87bdd2cf8ea8.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "103",
                            "productogeneral_precio": "29500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "28",
                                    "producto_descripcion": "Burgermonster",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "26900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "141",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/0d0f12b6-a4fd-4e6d-9f30-355269d7ef22.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS PERSONALES"
                        },
                        {
                            "productogeneral_id": "153",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO CLASICMONSTER 2P +  2 BEBIDAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "10",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/8702119d-3a3f-4901-9dca-7a4584104854.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "156",
                            "productogeneral_precio": "34500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "30",
                                    "producto_descripcion": "Clasicmonster 2 Personas",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "30900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "144",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/dae2cb82-97ca-49f1-897f-f9734e238147.png",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "23",
                                    "producto_descripcion": "Quatro 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "132",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "13",
                                            "producto_descripcion": "Coca Cola Sabor Original 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "122"
                                        },
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "100",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO CLASICMONSTER PERSONAL + BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "26",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/16dac6bc-01a2-460d-937a-6b2133eb79da.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "102",
                            "productogeneral_precio": "23000.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "44",
                                    "producto_descripcion": "Clasicmonster Personal",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "22900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "158",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/64b3edf0-69bd-48c2-8b85-4f1ca204aa46.png",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS PERSONALES"
                        },
                        {
                            "productogeneral_id": "154",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO COSTIMONSTER 2P  +  2 BEBIDAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "10",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/69c37407-e6b7-453b-a54b-61feba89cbc7.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "157",
                            "productogeneral_precio": "50500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "14",
                                    "producto_descripcion": "Coca Cola Zero 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "123",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "13",
                                            "producto_descripcion": "Coca Cola Sabor Original 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "122"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "31",
                                    "producto_descripcion": "Costimonster 2 Personas",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "50900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "145",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/d6d266cf-09c2-49b0-a6b1-b70579f28691.png",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "99",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO COSTIMONSTER PERSONAL + BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "26",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/b2489c8c-67d3-4b3b-a1ce-deb520491996.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "101",
                            "productogeneral_precio": "33000.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "45",
                                    "producto_descripcion": "Costimonster Personal",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "35500.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "159",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/a2ebc6f7-f02d-49ed-a305-c76335b4adb2.png",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS PERSONALES"
                        },
                        {
                            "productogeneral_id": "155",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO LA DE SIEMPRE 2P + 2 BEBIDAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "10",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/1f974112-bcb7-4caa-8b24-b016acb881f7.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "158",
                            "productogeneral_precio": "57500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "14",
                                    "producto_descripcion": "Coca Cola Zero 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "123",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "13",
                                            "producto_descripcion": "Coca Cola Sabor Original 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "122"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "36",
                                    "producto_descripcion": "La De Siempre 2 Personas",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "59900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "150",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/ad39edaf-7a6d-47ce-85a0-ca53a397ae7c.png",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "92",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO LA MATAHAMBRE 2P + 2 BEBIDAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "10",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/febcc2cf-9ba1-4e63-9156-2e3055c82c56.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "94",
                            "productogeneral_precio": "52500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "39",
                                    "producto_descripcion": "Mata Hambre 2 Personas",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "53900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "153",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/53faa098-0902-4486-bf27-fa4c56d07cac.png",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "22",
                                    "producto_descripcion": "Premio 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "131",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "13",
                                            "producto_descripcion": "Coca Cola Sabor Original 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "122"
                                        },
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "53",
                            "productogeneral_descripcionweb": "LA MIXTICA + 2 GASEOSAS 400 ML",
                            "productogeneral_descripcion": "COMBO LA MIXTICA 2P + 2 BEBIDAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "10",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/31dad2a0-200b-4ccc-9f46-66425a0e0fb1",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "55",
                            "productogeneral_precio": "64500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "37",
                                    "producto_descripcion": "La Mixtica 2 Personas",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "66900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "151",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7aa802dc-158d-4c97-817a-b46f9a3b490a.png",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "22",
                                    "producto_descripcion": "Premio 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "131",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "13",
                                            "producto_descripcion": "Coca Cola Sabor Original 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "122"
                                        },
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "131",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO MONSTER BACON +PAPAS+BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "22",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/670ed8c3-d698-4703-8798-76ea36ec04a2.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "133",
                            "productogeneral_precio": "29900.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "108",
                                    "producto_descripcion": "Monster Bacon",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "24900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/990cd9d3-e106-49fe-aa1a-698b636c28a3.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "138",
                                    "producto_descripcion": "Papa Francesa Para Burger (150Gr)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER"
                        },
                        {
                            "productogeneral_id": "130",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO MONSTER CHEESE +PAPAS+BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "22",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/add66382-8359-435f-a5a4-d93970702b9f.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "132",
                            "productogeneral_precio": "26500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "107",
                                    "producto_descripcion": "Monster Cheese",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "21900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/650b5748-902c-43ee-9013-2249ab26b785.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "130",
                                    "producto_descripcion": "Papas Francesa Para Burger (No)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7e80da5d-be85-4eeb-a3a9-74efb3643bd0.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER"
                        },
                        {
                            "productogeneral_id": "126",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO MONSTER CHICKEN +PAPAS+BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "22",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/79e5bd88-c029-4568-b066-d7d275681783.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "128",
                            "productogeneral_precio": "24500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "105",
                                    "producto_descripcion": "Monster Chicken",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "19900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/8d354549-2cdc-4764-a381-215c74bf3ca9.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "130",
                                    "producto_descripcion": "Papas Francesa Para Burger (No)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7e80da5d-be85-4eeb-a3a9-74efb3643bd0.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER"
                        },
                        {
                            "productogeneral_id": "133",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO MONSTER DOBLE CARNE  +PAPAS+BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "22",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/e9da2971-5333-4f87-8564-7583f731f380.jpeg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "135",
                            "productogeneral_precio": "34500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "110",
                                    "producto_descripcion": "Monster Doble Carne",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "29900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/e7ccdb25-8e78-4084-8966-3c646af45cbe.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "130",
                                    "producto_descripcion": "Papas Francesa Para Burger (No)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7e80da5d-be85-4eeb-a3a9-74efb3643bd0.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER"
                        },
                        {
                            "productogeneral_id": "129",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO MONSTER GHETTO +PAPAS+BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "22",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/c6a4ca47-49c6-41d3-859b-6eeeffb483b7.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "131",
                            "productogeneral_precio": "25500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "106",
                                    "producto_descripcion": "Monster Ghetto",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "20900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/ac372c64-b08c-4f95-83be-1e5be4222c41.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "130",
                                    "producto_descripcion": "Papas Francesa Para Burger (No)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7e80da5d-be85-4eeb-a3a9-74efb3643bd0.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER"
                        },
                        {
                            "productogeneral_id": "135",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO MONSTER REALEZA +PAPAS+BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "22",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/0909829a-7e07-4598-b2b4-c79e5abd371a.jpeg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "137",
                            "productogeneral_precio": "40500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "112",
                                    "producto_descripcion": "Monster Realeza",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "35900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/4c1b5afb-c8ee-4773-b0c6-dff9ac67fb0f.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "130",
                                    "producto_descripcion": "Papas Francesa Para Burger (No)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7e80da5d-be85-4eeb-a3a9-74efb3643bd0.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER"
                        },
                        {
                            "productogeneral_id": "125",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO MONSTER SENCILLA+PAPAS+BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "22",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/2c67c69b-ec8f-446b-9e31-75fbb9539d95.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "127",
                            "productogeneral_precio": "24500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "104",
                                    "producto_descripcion": "Monster Sencilla",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "19900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/5cb87b86-5611-4f72-80f0-485ae4c30857.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "130",
                                    "producto_descripcion": "Papas Francesa Para Burger (No)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7e80da5d-be85-4eeb-a3a9-74efb3643bd0.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER"
                        },
                        {
                            "productogeneral_id": "91",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO NACHIMONSTER 2P + 2 BEBIDAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "10",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/ad69e9d0-c7af-4614-9e48-87bb6fb7f8ad.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "93",
                            "productogeneral_precio": "52500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "33",
                                    "producto_descripcion": "Nachimonster 2 Personas",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "53900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "147",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/cbf69f36-6420-4cbf-a83f-60fd63d9e9ce.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "24",
                                    "producto_descripcion": "Sprite 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "133",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "13",
                                            "producto_descripcion": "Coca Cola Sabor Original 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "122"
                                        },
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "134",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COMBO OIGA, MIRE, VEA +PAPAS+BEBIDA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "22",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/716862d7-9d91-48f0-a5d8-960857459e9c.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "136",
                            "productogeneral_precio": "36500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "76",
                                            "producto_descripcion": "Adicion Queso Mozarella - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "6600.0000000",
                                            "alternativacombo_costoadicional": "700.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/a2c8991b-c6d0-440e-a298-87e47db811e1.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        },
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "111",
                                    "producto_descripcion": "Oiga, Mire, Vea",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "31900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/6bf52f0f-4041-48b3-b212-3c67df44a29f.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "130",
                                    "producto_descripcion": "Papas Francesa Para Burger (No)",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "4000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7e80da5d-be85-4eeb-a3a9-74efb3643bd0.jpg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "139",
                                            "producto_descripcion": "Papa Criolla Para Burger (150G) - .",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "4000.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": null
                                        }
                                    ]
                                }
                            ],
                            "lista_productoadicional": [
                                {
                                    "producto_id": "96",
                                    "producto_descripcion": "Postre Chocomonster - ",
                                    "producto_precio": "10000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null
                                }
                            ],
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER"
                        },
                        {
                            "productogeneral_id": "29",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COSTIMONSTER 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/cdc9be25-5241-4afd-aaeb-a1a0cc8acfca.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "31",
                                    "producto_presentacion": "",
                                    "producto_precio": "50900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/d6d266cf-09c2-49b0-a6b1-b70579f28691.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "145",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "43",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "COSTIMONSTER PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/a028e74e-2d2c-432c-af3d-8d8a022766b1.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "45",
                                    "producto_presentacion": "",
                                    "producto_precio": "35500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/a2ebc6f7-f02d-49ed-a305-c76335b4adb2.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "159",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "141",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "DETODITO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "13",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/316b0bbf-3a25-40bb-98b5-3fd42bc45495.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "143",
                                    "producto_presentacion": "DETODITO",
                                    "producto_precio": "35900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/57190689-99ac-4aa3-b76c-aeda5085cefa.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "PRODUCTO NUEVO"
                        },
                        {
                            "productogeneral_id": "14",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "JUGO DE LULO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/fb1d8699-5a91-4283-9a92-67584d5e1003.jpeg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "16",
                                    "producto_presentacion": "",
                                    "producto_precio": "8900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fd02f656-6e78-4d67-98d9-e58c2ea2341c.jpeg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "125",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "16",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "JUGO DE MANGO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/6b700b83-9743-4822-b8c0-60474d15887c.jpeg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "18",
                                    "producto_presentacion": "",
                                    "producto_precio": "8900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/c99ad4b0-e0f2-46ef-8270-6b4560bcfe3d.jpeg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "127",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "17",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "JUGO DE MARACUYA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/6a2a031c-8651-4d3f-9c10-a6c641534a68.jpeg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "19",
                                    "producto_presentacion": "",
                                    "producto_precio": "8900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/3ff59649-55ed-412d-9730-db90454932fe.jpeg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "128",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "138",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "KIT #1 CUMPLEAÑOS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "12",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/fb6b8855-57b4-4161-ba53-6f8ac6940028.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "140",
                            "productogeneral_precio": "299900.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "12",
                                    "producto_descripcion": "Coca Cola Sabor Original 1.5 Lt",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "8900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "121",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/ba2a099b-73c8-4814-8cb7-ad4336f30d3d.webp",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "12",
                                    "producto_descripcion": "Coca Cola Sabor Original 1.5 Lt",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "8900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "121",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/ba2a099b-73c8-4814-8cb7-ad4336f30d3d.webp",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "42",
                                    "producto_descripcion": "Salchimonster Para 6 Personas",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "125900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "156",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7c39dc25-cb1a-461b-b95a-c9e2295888a2.png",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "59",
                                    "producto_descripcion": "Show Chicharron",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "35000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/979cedee-d41d-4a62-bc7f-5ce2ed9d1f14.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "59",
                                    "producto_descripcion": "Show Chicharron",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "35000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/979cedee-d41d-4a62-bc7f-5ce2ed9d1f14.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "58",
                                    "producto_descripcion": "Show Queso",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "19500.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/25bbfe2d-b11f-422c-9267-891da85e5b1c.jpg",
                                    "lista_productoCambio": []
                                },
                                {
                                    "producto_id": "58",
                                    "producto_descripcion": "Show Queso",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "19500.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/25bbfe2d-b11f-422c-9267-891da85e5b1c.jpg",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [],
                            "categoria_descripcion": "Combo CumpleaÑos"
                        },
                        {
                            "productogeneral_id": "34",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "LA DE SIEMPRE 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/ead92109-a287-4d30-bce5-957ae4425453.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "36",
                                    "producto_presentacion": "",
                                    "producto_precio": "59900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/ad39edaf-7a6d-47ce-85a0-ca53a397ae7c.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "150",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "44",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "LA DE SIEMPRE PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/b970a201-a8d2-4e64-8983-b83e3728eb97.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "46",
                                    "producto_presentacion": "",
                                    "producto_precio": "41900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/aa53e399-4454-4374-99c2-59e19ab4c24a.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "160",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "35",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "LA MIXTICA 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/b497d55f-53ac-45eb-a37c-27c727be6cbc.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "37",
                                    "producto_presentacion": "",
                                    "producto_precio": "68900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7aa802dc-158d-4c97-817a-b46f9a3b490a.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "151",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "45",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "LA MIXTICA PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/5f89b48f-bbf5-4ec7-8541-901794278582.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "47",
                                    "producto_presentacion": "",
                                    "producto_precio": "47500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/2b4cb87d-05ca-4169-b97d-8c432fd54e01.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "161",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "36",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "LA NEA 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/b8f67f35-fbc0-480a-98cc-3d747172fcd3.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "38",
                                    "producto_presentacion": "",
                                    "producto_precio": "67000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/8849b81a-5db2-440c-9351-3d343407bb9e.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "152",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "30",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MADURIMONSTER 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/ed72ee34-adc3-43e8-9644-55403a690590.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "32",
                                    "producto_presentacion": "",
                                    "producto_precio": "39500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/d925099e-4209-43de-b96b-94b31d6ade6d.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "146",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "46",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MADURIMONSTER PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/5c2449d8-2802-4065-8231-04593f3d6bec.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "48",
                                    "producto_presentacion": "",
                                    "producto_precio": "27500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/d3faff50-3713-4414-a0d7-8b3d7bd716f8.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "162",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "37",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MATA HAMBRE 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/5bd7b2c4-4acc-4f28-a436-a7d8468ccca5.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "39",
                                    "producto_presentacion": "",
                                    "producto_precio": "53900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/53faa098-0902-4486-bf27-fa4c56d07cac.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "153",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "47",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MATA HAMBRE PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/7cea0ba3-5e87-46fa-b2b8-63c83c82eac4.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "49",
                                    "producto_presentacion": "",
                                    "producto_precio": "38900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/5cfeeb7d-c175-4ae4-ab26-109b09be8bc6.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "163",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "106",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MONSTER BACON",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "18",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/8c0a31ac-6135-4de4-84c5-c5747fe78fd3.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "108",
                                    "producto_presentacion": "MONSTER BACON",
                                    "producto_precio": "24900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/990cd9d3-e106-49fe-aa1a-698b636c28a3.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "HAMBURGUESAS"
                        },
                        {
                            "productogeneral_id": "105",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MONSTER CHEESE",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "18",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/9bce5e0b-c50a-4e46-839e-4f34890f8aa3.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "107",
                                    "producto_presentacion": "",
                                    "producto_precio": "21900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/650b5748-902c-43ee-9013-2249ab26b785.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "HAMBURGUESAS"
                        },
                        {
                            "productogeneral_id": "103",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MONSTER CHICKEN",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "18",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/dec64853-c700-46a5-bb7c-31442fda3312.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "105",
                                    "producto_presentacion": "",
                                    "producto_precio": "19900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/8d354549-2cdc-4764-a381-215c74bf3ca9.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "HAMBURGUESAS"
                        },
                        {
                            "productogeneral_id": "108",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MONSTER DOBLE CARNE",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "18",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/7ecc6722-a49c-4807-b72f-cd601f6c954e.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "110",
                                    "producto_presentacion": "",
                                    "producto_precio": "29900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/e7ccdb25-8e78-4084-8966-3c646af45cbe.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "HAMBURGUESAS"
                        },
                        {
                            "productogeneral_id": "104",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MONSTER GHETTO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "18",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/8a3fa60c-149b-4317-922b-eb07d4f51e85.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "106",
                                    "producto_presentacion": "",
                                    "producto_precio": "20900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/ac372c64-b08c-4f95-83be-1e5be4222c41.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "HAMBURGUESAS"
                        },
                        {
                            "productogeneral_id": "110",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MONSTER REALEZA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "18",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/ad3fb92c-37fe-476c-af20-837d90903016.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "112",
                                    "producto_presentacion": "",
                                    "producto_precio": "35900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/4c1b5afb-c8ee-4773-b0c6-dff9ac67fb0f.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "HAMBURGUESAS"
                        },
                        {
                            "productogeneral_id": "102",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "MONSTER SENCILLA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "18",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/643d43c4-6c26-4d49-908b-47809b0066b5.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "104",
                                    "producto_presentacion": "",
                                    "producto_precio": "19900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/5cb87b86-5611-4f72-80f0-485ae4c30857.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "HAMBURGUESAS"
                        },
                        {
                            "productogeneral_id": "31",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "NACHIMONSTER 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/70ea6534-11d8-48bb-b31e-321c86d1ab2f.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "33",
                                    "producto_presentacion": "",
                                    "producto_precio": "53900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/cbf69f36-6420-4cbf-a83f-60fd63d9e9ce.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "147",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "48",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "NACHIMONSTER PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/07939a1f-35fc-46e5-8a7c-f78c182e9421.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "50",
                                    "producto_presentacion": "",
                                    "producto_precio": "37900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/e7af754e-0a07-4000-92a1-6be519a939e5.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "164",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "109",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "OIGA, MIRE, VEA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "18",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/d7a6b7b6-8486-42f0-8b65-ca49a0b6ae83.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "111",
                                    "producto_presentacion": "",
                                    "producto_precio": "31900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/6bf52f0f-4041-48b3-b212-3c67df44a29f.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "17",
                                    "modificador_nombre": "ADICIONES BURGER",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "41",
                                            "modificadorseleccion_nombre": "ADICION CARNE DE RES",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "42",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA 2 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "43",
                                            "modificadorseleccion_nombre": "BAÑO DE QUESO BURGER 6 LONCHAS",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "10000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "44",
                                            "modificadorseleccion_nombre": "PAPA CRIOLLA PARA BURGER (150G)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "45",
                                            "modificadorseleccion_nombre": "PAPA FRANCESA PARA BURGER (150GR)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "10",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "HAMBURGUESAS"
                        },
                        {
                            "productogeneral_id": "137",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPA CRIOLLA PARA BURGER (150G)",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "16",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/f9dc7f25-8874-493d-9567-dbae46b2ff52.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "139",
                                    "producto_presentacion": ".",
                                    "producto_precio": "4000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/fe110217-b1cc-4a50-940a-36d68db42f10.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES HAMBURGUESA"
                        },
                        {
                            "productogeneral_id": "136",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPA FRANCESA PARA BURGER (150GR)",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "16",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/828d89fe-6cc9-48a7-808a-4a0ac3f953e3.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "138",
                                    "producto_presentacion": "",
                                    "producto_precio": "4000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/003ee755-8b34-4aef-a259-42d57a8f5d5f.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "ADICIONES HAMBURGUESA"
                        },
                        {
                            "productogeneral_id": "139",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS BACON",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "13",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/769a842b-6361-42d1-9ba0-4e3b2583a599.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "141",
                                    "producto_presentacion": "PAPAS BACON",
                                    "producto_precio": "19900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/507d9b7d-be99-490d-8870-e71c79e3fac8.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "PRODUCTO NUEVO"
                        },
                        {
                            "productogeneral_id": "113",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS CARNE",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "19",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/858a0b66-23d2-4888-b012-d756cd4edc22.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "117",
                                    "producto_presentacion": "",
                                    "producto_precio": "15900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/8e4e8a71-7452-457c-8e32-25ff9709aa67.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "PAPAS MONSTER PERSONALES"
                        },
                        {
                            "productogeneral_id": "120",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS CARNE + GASEOSA 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "24",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/28b7d8ea-4bc9-4bd5-b29b-bfe162ca92b1.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "122",
                            "productogeneral_precio": "20500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "117",
                                    "producto_descripcion": "Papas Carne",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "14800.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/8e4e8a71-7452-457c-8e32-25ff9709aa67.jpg",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [],
                            "categoria_descripcion": "COMBOS PAPAS MONSTER"
                        },
                        {
                            "productogeneral_id": "116",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS CERDO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "19",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/c2fc79e1-304d-47c1-a955-bb79feae7607.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "114",
                                    "producto_presentacion": "",
                                    "producto_precio": "23900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/725a7db4-80ad-45b6-83e1-d6d7ab1affe9.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "PAPAS MONSTER PERSONALES"
                        },
                        {
                            "productogeneral_id": "123",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS CERDO + GASEOSA 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "24",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/33c23382-e034-4db7-98b8-bfe5cdb59f27.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "125",
                            "productogeneral_precio": "28500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "114",
                                    "producto_descripcion": "Papas Cerdo",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "22200.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/725a7db4-80ad-45b6-83e1-d6d7ab1affe9.jpg",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [],
                            "categoria_descripcion": "COMBOS PAPAS MONSTER"
                        },
                        {
                            "productogeneral_id": "115",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS CHICHA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "19",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/cc2a0e13-fd40-4d26-8a1a-c7c5a1f9c988.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "115",
                                    "producto_presentacion": "",
                                    "producto_precio": "20900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/208ddfc2-6262-43d9-b831-15cb6a13ed3e.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "PAPAS MONSTER PERSONALES"
                        },
                        {
                            "productogeneral_id": "122",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS CHICHA + GASEOSA 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "24",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/5957a1b1-920f-4bb8-93ec-9912161bb15b.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "124",
                            "productogeneral_precio": "25500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "115",
                                    "producto_descripcion": "Papas Chicha",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "19400.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/208ddfc2-6262-43d9-b831-15cb6a13ed3e.jpg",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [],
                            "categoria_descripcion": "COMBOS PAPAS MONSTER"
                        },
                        {
                            "productogeneral_id": "112",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS HAWAINA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "19",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/511131a6-be31-4091-ac11-7fdef408c644.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "118",
                                    "producto_presentacion": "",
                                    "producto_precio": "13900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/12c7e63b-ac14-49b8-b5fd-7d7000957182.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "PAPAS MONSTER PERSONALES"
                        },
                        {
                            "productogeneral_id": "119",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS HAWAINA + GASEOSA 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "24",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/38a3ee04-2e38-47b4-9460-a37f410904fe.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "121",
                            "productogeneral_precio": "18500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "118",
                                    "producto_descripcion": "Papas Hawaina",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "12900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/12c7e63b-ac14-49b8-b5fd-7d7000957182.jpg",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [],
                            "categoria_descripcion": "COMBOS PAPAS MONSTER"
                        },
                        {
                            "productogeneral_id": "114",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS MIXTA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "19",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/e733c537-7fba-4156-8eb1-d2cc3926d950.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "116",
                                    "producto_presentacion": "",
                                    "producto_precio": "19900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/c11e93cc-ab3c-402b-94ea-15ef89bc57d1.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "PAPAS MONSTER PERSONALES"
                        },
                        {
                            "productogeneral_id": "121",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS MIXTAS + GASEOSA 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "24",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/6f1cb13a-2af2-4f86-818f-6005a61b8653.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "123",
                            "productogeneral_precio": "24500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "116",
                                    "producto_descripcion": "Papas Mixta",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "18500.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/c11e93cc-ab3c-402b-94ea-15ef89bc57d1.jpg",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [],
                            "categoria_descripcion": "COMBOS PAPAS MONSTER"
                        },
                        {
                            "productogeneral_id": "117",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS MONSTER",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "19",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/d7e68e86-f4f6-4227-992d-3c9507f13456.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "113",
                                    "producto_presentacion": "",
                                    "producto_precio": "29900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/ac093bfc-4464-46dd-a8da-f85afe15927e.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "PAPAS MONSTER PERSONALES"
                        },
                        {
                            "productogeneral_id": "124",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS MONSTER + GASEOSA 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "24",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/cda1a890-0eab-44b7-9514-04356b4c6a87.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "126",
                            "productogeneral_precio": "34500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "113",
                                    "producto_descripcion": "Papas Monster",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "27700.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/ac093bfc-4464-46dd-a8da-f85afe15927e.jpg",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [],
                            "categoria_descripcion": "COMBOS PAPAS MONSTER"
                        },
                        {
                            "productogeneral_id": "111",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS SAMBA",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "19",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/74e0320d-c54b-4608-8c3f-2da3057f1c22.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "119",
                                    "producto_presentacion": "",
                                    "producto_precio": "13900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/e98d3a84-f52f-458e-bd35-cfc78170ed15.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "PAPAS MONSTER PERSONALES"
                        },
                        {
                            "productogeneral_id": "118",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PAPAS SAMBA + GASEOSA 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "24",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/abfd1d5e-67e2-4e45-aa17-069756c1dda1.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "120",
                            "productogeneral_precio": "18500.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "13",
                                    "producto_descripcion": "Coca Cola Sabor Original 400 Ml",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "5900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "122",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/d4a326f0-5caf-4715-91a0-6571765d654e.jpeg",
                                    "lista_productoCambio": [
                                        {
                                            "producto_id": "14",
                                            "producto_descripcion": "Coca Cola Zero 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/9c57119e-2a95-4816-bc7f-3d9b423d184b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "123"
                                        },
                                        {
                                            "producto_id": "22",
                                            "producto_descripcion": "Premio 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "131"
                                        },
                                        {
                                            "producto_id": "23",
                                            "producto_descripcion": "Quatro 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "132"
                                        },
                                        {
                                            "producto_id": "24",
                                            "producto_descripcion": "Sprite 400 Ml - ",
                                            "alternativacombo_cantidad": "1.000",
                                            "alternativacombo_precio": "5900.0000000",
                                            "alternativacombo_costoadicional": "0.00",
                                            "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                            "producto_codigo": "",
                                            "producto_codigointerno": "133"
                                        }
                                    ]
                                },
                                {
                                    "producto_id": "119",
                                    "producto_descripcion": "Papas Samba",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "1.000",
                                    "productocombo_precio": "12900.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/e98d3a84-f52f-458e-bd35-cfc78170ed15.jpg",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": [],
                            "categoria_descripcion": "COMBOS PAPAS MONSTER"
                        },
                        {
                            "productogeneral_id": "204",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PECERA 14 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "100",
                            "productogeneral_urlimagen": null,
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "209",
                            "productogeneral_precio": "0.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "167",
                                    "producto_descripcion": "Q'chimba.",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "14.000",
                                    "productocombo_precio": "17000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "",
                                    "producto_urlimagen": "",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": []
                        },
                        {
                            "productogeneral_id": "212",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PECERA 14 PERSONAS UP",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "1",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "37",
                            "productogeneral_urlimagen": null,
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "producto_id": "218",
                            "productogeneral_precio": "0.00",
                            "lista_productobase": [
                                {
                                    "producto_id": "217",
                                    "producto_descripcion": "Hang Over",
                                    "productocombo_sepuedecambiar": "1",
                                    "productocombo_sepuedeeliminar": "0",
                                    "productocombo_cantidad": "14.000",
                                    "productocombo_precio": "17000.0000000",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_urlimagen": "",
                                    "lista_productoCambio": []
                                }
                            ],
                            "lista_productoadicional": []
                        },
                        {
                            "productogeneral_id": "140",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PICADA PA 3 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "13",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/d0da976c-dc8c-4365-98c3-d138234688fb.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "142",
                                    "producto_presentacion": "",
                                    "producto_precio": "99900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/eb9739cb-097f-4514-8e26-32d46457413a.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "PRODUCTO NUEVO"
                        },
                        {
                            "productogeneral_id": "32",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "POLLIMONSTER 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/231af275-5aa1-43ff-ac23-00a42df834ce.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "34",
                                    "producto_presentacion": "",
                                    "producto_precio": "46500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/1d3266ba-571e-4217-a165-6f6e219e1f72.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "148",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "49",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "POLLIMONSTER PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/57248341-8d26-4798-82f0-4d531b24d0f0.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "51",
                                    "producto_presentacion": "",
                                    "producto_precio": "32900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/1944ada2-8e01-41c4-a2bb-3139b3b4e17d.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "165",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "38",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PORKYMONSTER 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/f7b2a4e3-a2a7-40f4-90f8-7a6f41edc2d1.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "40",
                                    "producto_presentacion": "",
                                    "producto_precio": "51500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/f2b690c6-fc70-4a19-962b-57871c286ec9.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "154",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "10",
                                    "modificador_nombre": "TIPO DE SALCHICHA 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "13",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "14",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "50",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PORKYMONSTER PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/84133fbb-e157-4b5b-9770-dff41687d5c5.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "52",
                                    "producto_presentacion": "",
                                    "producto_precio": "35500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/46d19ade-a524-45cf-9599-79c5b1ae4d26.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "166",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "11",
                                    "modificador_nombre": "TIPO DE SALCHICHA PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "15",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SM PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "16",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "12000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "94",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "POSTRE CHOCOMONSTER",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "13",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/2dee98c7-ed09-4653-92be-4c838a369dfc.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "96",
                                    "producto_presentacion": "",
                                    "producto_precio": "10000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/bd5c4409-c027-433c-b0b6-d830e6c8d712.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "PRODUCTO NUEVO"
                        },
                        {
                            "productogeneral_id": "159",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PREMIO 1.5 L",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/19e18b89-a32f-4ae6-9cab-57a258f3bbb7.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "159",
                                    "producto_presentacion": "",
                                    "producto_precio": "8900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/01fa6084-c47f-4550-91c5-323a8b7767ba.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "20",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "PREMIO 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/43288d8e-908a-4060-826d-6722da8583f0.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "22",
                                    "producto_presentacion": "",
                                    "producto_precio": "5900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/c05f91b7-9c05-4182-9196-b421a992e05b.jpeg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "131",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "158",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "QUATRO 1.5 L",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/dc9ce64a-e442-4706-9c0b-2d5d821d4041.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "160",
                                    "producto_presentacion": "",
                                    "producto_precio": "8900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/25045594-45a2-4324-8f6a-d2e7f82ecc6a.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "21",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "QUATRO 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/87d77808-036d-4e73-b9fb-50e3fd78a526.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "23",
                                    "producto_presentacion": "",
                                    "producto_precio": "5900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/30454723-c01f-4adf-8627-034c3a4e38e4.webp",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "132",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "39",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "RANCHIMONSTER 2 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/719fe7e5-6843-4179-b9df-e6dd9c43fb2c.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "41",
                                    "producto_presentacion": "",
                                    "producto_precio": "48900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/9a02fec0-22ac-4e30-a824-3f694989dbb8.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "155",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "9",
                                    "modificador_nombre": "TIPO DE PAPAS 2 PERSONAS",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "11",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "12",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "51",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "RANCHIMONSTER PERSONAL",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "9",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/4e3baae6-c6d2-4962-ae36-f9b34a33cc32.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "53",
                                    "producto_presentacion": "",
                                    "producto_precio": "34500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7696cef4-830d-4438-be8a-76ab336fccea.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "167",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "12",
                                    "modificador_nombre": "TIPO DE PAPAS PERSONAL",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "17",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA 2 PERSONAS",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "4000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "18",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA PERSONAL",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES"
                        },
                        {
                            "productogeneral_id": "40",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "SALCHIMONSTER PARA 6 PERSONAS",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "8",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/580aae1e-84e8-47fa-8c09-b9cefb852b7e.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "42",
                                    "producto_presentacion": "",
                                    "producto_precio": "125900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7c39dc25-cb1a-461b-b95a-c9e2295888a2.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "156",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [
                                {
                                    "modificador_id": "14",
                                    "modificador_nombre": "TIPO DE SALCHICHA SALCHIMONSTER",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "22",
                                            "modificadorseleccion_nombre": "CAMBIO RANCHERA SALCHIMONSTER",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "24000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "23",
                                            "modificadorseleccion_nombre": "CON SALCHICHA PREMIUM SALCHIMONSTER",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "15",
                                    "modificador_nombre": "TIPO DE PAPAS  SALCHIMONSTER",
                                    "modificador_esmultiple": "0",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "20",
                                            "modificadorseleccion_nombre": "CAMBIO FRANCESA EN SALCHIMONSTER",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "8000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "21",
                                            "modificadorseleccion_nombre": "CON PAPA CRIOLLA SALCHIMONSTER",
                                            "modificadorseleccion_tipo": "0",
                                            "modificadorseleccion_precio": "0.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "1",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                },
                                {
                                    "modificador_id": "16",
                                    "modificador_nombre": "ADICIONES DE SALCHIPAPAS",
                                    "modificador_esmultiple": "1",
                                    "modificador_cantidadminima": "0",
                                    "listaModificadores": [
                                        {
                                            "modificadorseleccion_id": "24",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA RANCHERA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "20000.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/7384ceab-7b29-4d50-95ad-93e08e067fed.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "25",
                                            "modificadorseleccion_nombre": "ADICION SALCHICHA PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8900.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/306e75c5-03b3-46be-b7fe-3d337e90b1e2.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "26",
                                            "modificadorseleccion_nombre": "ADICION RIPIO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/08d357c0-68b4-4163-88f2-8317a2333eac.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "27",
                                            "modificadorseleccion_nombre": "ADICION QUESO MOZARELLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/5d42062d-8447-4f13-a214-179bba158829.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "28",
                                            "modificadorseleccion_nombre": "ADICION POLLO DESMECHADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": "salchimonsterrestaurantpe/seleccion/57ea1dbc-4d2b-4295-b08e-ab542bcb45b7.jpg",
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "29",
                                            "modificadorseleccion_nombre": "ADICION POLLO APANADO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "15500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "30",
                                            "modificadorseleccion_nombre": "ADICION PICO E GALLO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "3500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "31",
                                            "modificadorseleccion_nombre": "ADICION PAPA FRANCESA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "7700.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "32",
                                            "modificadorseleccion_nombre": "ADICION PAPA AMARILLA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "33",
                                            "modificadorseleccion_nombre": "ADICION MAIZ",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "34",
                                            "modificadorseleccion_nombre": "ADICION MADURO GUAYABO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "5500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "35",
                                            "modificadorseleccion_nombre": "ADICION GUACAMOLE",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "6600.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "36",
                                            "modificadorseleccion_nombre": "ADICION COSTILLA AHUMADA",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "17900.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "37",
                                            "modificadorseleccion_nombre": "ADICION CHORIZO",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "14000.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "38",
                                            "modificadorseleccion_nombre": "ADICION CHICHARRON",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "19500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "39",
                                            "modificadorseleccion_nombre": "ADICION CARNE PREMIUM (DESMECHADA)",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "16500.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        },
                                        {
                                            "modificadorseleccion_id": "40",
                                            "modificadorseleccion_nombre": "ADICION BACON PREMIUM",
                                            "modificadorseleccion_tipo": "1",
                                            "modificadorseleccion_precio": "8800.00",
                                            "modificadorseleccion_urlimagen": null,
                                            "productogeneralmodificador_cantidadmaxima": "17",
                                            "productogeneralmodificador_orden": "1"
                                        }
                                    ]
                                }
                            ],
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS"
                        },
                        {
                            "productogeneral_id": "57",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "SHOW CHICHARRON",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "11",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/c3cfa1d0-2711-4603-9034-1f31bcffb4c0.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "59",
                                    "producto_presentacion": "",
                                    "producto_precio": "35000.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/979cedee-d41d-4a62-bc7f-5ce2ed9d1f14.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "SHOW´S"
                        },
                        {
                            "productogeneral_id": "56",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "SHOW QUESO",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "11",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/8c43321b-9852-42b9-bef2-bb37c0129e93.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "58",
                                    "producto_presentacion": "",
                                    "producto_precio": "19500.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/25bbfe2d-b11f-422c-9267-891da85e5b1c.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "SHOW´S"
                        },
                        {
                            "productogeneral_id": "156",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "SPRITE 1.5 L",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/7587b7f9-786d-4435-a269-f489789d0152.png",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "162",
                                    "producto_presentacion": "",
                                    "producto_precio": "8900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/0a1ce738-55da-4811-9191-35fa69bb5672.png",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "22",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "SPRITE 400 ML",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "4",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productos/68768441-5e8f-4a8d-8c68-dddf782faba4.webp",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "24",
                                    "producto_presentacion": "",
                                    "producto_precio": "5900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/products/01922c6b-bdda-447c-ba15-5e55c9be817f.jpeg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": "133",
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "Bebidas"
                        },
                        {
                            "productogeneral_id": "60",
                            "productogeneral_descripcionweb": null,
                            "productogeneral_descripcion": "STRIPS MONSTER",
                            "productogeneral_marca": "",
                            "productogeneral_escombo": "0",
                            "productogeneral_preciofijo": "1",
                            "productogeneral_noalteratotalcambio": "0",
                            "productogeneral_totalpreciomayor": "0",
                            "productogeneral_leysunat": "0",
                            "categoria_id": "27",
                            "productogeneral_urlimagen": "salchimonsterrestaurantpe/productogeneral/f2e90cab-33f1-4897-bfa8-2a1642d5794a.jpg",
                            "productogeneral_estado": "Activo",
                            "notas": [],
                            "lista_presentacion": [
                                {
                                    "producto_id": "61",
                                    "producto_presentacion": "",
                                    "producto_precio": "25900.00",
                                    "producto_delivery": "1",
                                    "producto_urlimagen": "salchimonsterrestaurantpe/productos/7c544662-6f95-4556-9334-671457450dbb.jpg",
                                    "producto_codigo": "",
                                    "producto_codigointerno": null,
                                    "producto_estado": "Activo"
                                }
                            ],
                            "lista_agrupadores": [],
                            "categoria_descripcion": "POLLO"
                        }
                    ],
                    "listaInsumos": [],
                    "listaCategorias": [
                        {
                            "categoria_id": "16",
                            "local_id": "11",
                            "categoria_descripcion": "ADICIONES HAMBURGUESA",
                            "categoria_estado": "1",
                            "categoria_padreid": "20",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "14",
                            "local_id": "11",
                            "categoria_descripcion": "ADICIONES SALCHIPAPAS",
                            "categoria_estado": "1",
                            "categoria_padreid": "20",
                            "categoria_color": "#f9845b",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "4",
                            "local_id": "1",
                            "categoria_descripcion": "Bebidas",
                            "categoria_estado": "1",
                            "categoria_padreid": "0",
                            "categoria_color": "#637a91",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "21",
                            "local_id": "1",
                            "categoria_descripcion": "Burgermonster",
                            "categoria_estado": "1",
                            "categoria_padreid": "0",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "5",
                            "local_id": "1",
                            "categoria_descripcion": "Cervezas",
                            "categoria_estado": "1",
                            "categoria_padreid": "0",
                            "categoria_color": "#b7c0c7",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "12",
                            "local_id": "9",
                            "categoria_descripcion": "Combo CumpleaÑos",
                            "categoria_estado": "1",
                            "categoria_padreid": "0",
                            "categoria_color": "#c25975",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "10",
                            "local_id": "1",
                            "categoria_descripcion": "COMBOS 2 PERSONAS",
                            "categoria_estado": "1",
                            "categoria_padreid": "20",
                            "categoria_color": "#53bbb4",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "25",
                            "local_id": "3",
                            "categoria_descripcion": "COMBOS 2X1 BURGER + PAPAS",
                            "categoria_estado": "1",
                            "categoria_padreid": "21",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "22",
                            "local_id": "1",
                            "categoria_descripcion": "COMBOS DE BURGERMONSTER",
                            "categoria_estado": "1",
                            "categoria_padreid": "21",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "24",
                            "local_id": "3",
                            "categoria_descripcion": "COMBOS PAPAS MONSTER",
                            "categoria_estado": "1",
                            "categoria_padreid": "23",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "26",
                            "local_id": "3",
                            "categoria_descripcion": "COMBOS PERSONALES",
                            "categoria_estado": "1",
                            "categoria_padreid": "20",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "28",
                            "local_id": "3",
                            "categoria_descripcion": "DOMIICLIOS",
                            "categoria_estado": "1",
                            "categoria_padreid": "0",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "18",
                            "local_id": "3",
                            "categoria_descripcion": "HAMBURGUESAS",
                            "categoria_estado": "1",
                            "categoria_padreid": "21",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "19",
                            "local_id": "12",
                            "categoria_descripcion": "PAPAS MONSTER PERSONALES",
                            "categoria_estado": "1",
                            "categoria_padreid": "23",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "23",
                            "local_id": "3",
                            "categoria_descripcion": "Papasmonster",
                            "categoria_estado": "1",
                            "categoria_padreid": "0",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "27",
                            "local_id": "1",
                            "categoria_descripcion": "POLLO",
                            "categoria_estado": "1",
                            "categoria_padreid": "13",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "13",
                            "local_id": "1",
                            "categoria_descripcion": "PRODUCTO NUEVO",
                            "categoria_estado": "1",
                            "categoria_padreid": "20",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "20",
                            "local_id": "1",
                            "categoria_descripcion": "Salchimonster",
                            "categoria_estado": "1",
                            "categoria_padreid": "0",
                            "categoria_color": "#e74c3c",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "8",
                            "local_id": "1",
                            "categoria_descripcion": "SALCHIPAPAS 2 PERSONAS",
                            "categoria_estado": "1",
                            "categoria_padreid": "20",
                            "categoria_color": "#51b46d",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "9",
                            "local_id": "1",
                            "categoria_descripcion": "SALCHIPAPAS PERSONALES",
                            "categoria_estado": "1",
                            "categoria_padreid": "20",
                            "categoria_color": "#f092b0",
                            "categoria_delivery": "1"
                        },
                        {
                            "categoria_id": "11",
                            "local_id": "9",
                            "categoria_descripcion": "SHOW´S",
                            "categoria_estado": "1",
                            "categoria_padreid": "20",
                            "categoria_color": "#3079ab",
                            "categoria_delivery": "1"
                        }
                    ],
                    "totalregistros": 128
                },
               
        }),
       
            getters: {
                totalItems: (state) => {
                    return state.cart.products.reduce((total, product) => total + product.quantity, 0);
                },
                totalAdditions: (state) => {
                    return state.cart.additions.reduce((total, addition) => total + (addition.price  * addition.quantity), 0);
                },
                isProductInCart: (state) => (productId) => {
                    return state.cart.products.some(product => product.product.productogeneral_id === productId);
                }
            },
       
        actions: {

            incrementAdditionQuantity(additionId) {
                const addition = this.cart.additions.find(a => a.id === additionId);
                if (addition) {
                    addition.quantity += 1;
                    this.calculateCartTotal();
                }
            },
            removeAdditionCompletelyFromCart(additionId) {
                const additionIndex = this.cart.additions.findIndex(a => a.id === additionId);
                if (additionIndex > -1) {
                    this.cart.additions.splice(additionIndex, 1);
                    this.calculateCartTotal();
                }
            },
    
            decrementAdditionQuantity(additionId) {
                const addition = this.cart.additions.find(a => a.id === additionId);
                if (addition && addition.quantity > 1) {
                    addition.quantity -= 1;
                    this.calculateCartTotal();
                }
            },


            setCurrentProduct(product){
                this.currentProduct=product
            },

            setVisible(item,status){
                this.visibles[item]=status
            },
            getProductId(product) {
                if (product.producto_id) {
                  return product.producto_id;
                } else if (
                  product.lista_presentacion &&
                  product.lista_presentacion.length > 0 &&
                  product.lista_presentacion[0].producto_id
                ) {
                  return product.lista_presentacion[0].producto_id;
                } else {
                  console.error('No valid product ID found for product:', product);
                  return null; // Or throw an error if appropriate
                }
              },
              
              addProductToCart(product, quantity = 1, additionalItems = []) {
                const productId = this.getProductId(product);
              
                if (!productId) {
                  console.error('Cannot add product to cart: Invalid product ID');
                  return;
                }
              
                const cartProduct = this.cart.products.find(
                  (p) => this.getProductId(p.product) === productId
                );
              
                const price = this.getProductPrice(product);
              
                if (cartProduct) {
                  cartProduct.quantity += quantity;
                  cartProduct.total_cost += price * quantity;
                } else {
                  const productWithId = { ...product, producto_id: productId };
                    console.log(productWithId)
                  this.cart.products.push({
                    product: productWithId,
                    quantity,
                    additionalItems: this.groupAdditionalItems(additionalItems),
                    total_cost: this.calculateProductTotal(
                      productWithId,
                      quantity,
                      additionalItems
                    ),
                  });
                }
                this.calculateCartTotal();
              },
              

            removeProductFromCart(productId) {
                this.cart.products = this.cart.products.filter(product => product.product.productogeneral_id !== productId);
                this.calculateCartTotal();
            },

            getProductPrice(product) {
                const generalPrice = product.productogeneral_precio;
                const presentationPrice = product.lista_presentacion?.[0]?.producto_precio;
                return generalPrice !== undefined ? generalPrice : presentationPrice || 0;
              },

            addAdditionalItem(productId, additionalItem) {
                const product = this.cart.products.find(
                  (product) => product.product.productogeneral_id === productId
                );
                if (product) {
                  product.additionalItems.push(additionalItem);
                  const price = this.getProductPrice(additionalItem);
                  product.total_cost += price * additionalItem.quantity;
                  this.calculateCartTotal();
                }
              },
              removeAdditionalItem(productId, additionalItemId) {
                const product = this.cart.products.find(
                  (product) => product.product.productogeneral_id === productId
                );
                if (product) {
                  const itemIndex = product.additionalItems.findIndex(
                    (item) => item.productogeneral_id === additionalItemId
                  );
                  if (itemIndex > -1) {
                    const removedItem = product.additionalItems[itemIndex];
                    const price = this.getProductPrice(removedItem);
                    product.total_cost -= price * removedItem.quantity;
                    product.additionalItems.splice(itemIndex, 1);
                    this.calculateCartTotal();
                  }
                }
              },
            groupAdditionalItems(additionalItems) {
                return additionalItems.reduce((acc, item) => {
                    (acc[item.type] = acc[item.type] || []).push(item);
                    return acc;
                }, {});
            },
            calculateProductTotal(product, quantity, additionalItems) {
                const basePrice = this.getProductPrice(product) * quantity;
                const additionalPrice = additionalItems.reduce(
                  (sum, item) => sum + this.getProductPrice(item) * item.quantity,
                  0
                );
                return basePrice + additionalPrice;
              },
            removeProductInstance(productId) {
                const cartProduct = this.cart.products.find(p => p.product.productogeneral_id === productId);
            
                if (cartProduct && cartProduct.quantity > 1) {
                    cartProduct.quantity -= 1;
                    cartProduct.total_cost -= cartProduct.product.productogeneral_precio || cartProduct.product.lista_presentacion[0].producto_precio;
                    this.calculateCartTotal();
                } else if (cartProduct && cartProduct.quantity === 1) {
                    this.removeProductFromCart(productId);
                }
            },
            calculateCartTotal() {
                const productsTotal = this.cart.products.reduce((total, product) => total + product.total_cost, 0);
                const additionsTotal = this.totalAdditions;
                this.cart.total_cost = productsTotal + additionsTotal;
            },

            addAdditionToCart(addition) {
                const existingAddition = this.cart.additions.find(a => a.id === addition.id);
                if (existingAddition) {
                    existingAddition.quantity += addition.quantity;
                } else {
                    this.cart.additions.push({ ...addition});
                }
                this.calculateCartTotal();
            },
            removeAdditionFromCart(additionId) {
                const additionIndex = this.cart.additions.findIndex(a => a.id === additionId);
                if (additionIndex > -1) {
                    if (this.cart.additions[additionIndex].quantity > 1) {
                        this.cart.additions[additionIndex].quantity -= 1;
                    } else {
                        this.cart.additions.splice(additionIndex, 1);
                    }
                    this.calculateCartTotal();
                }
            },
        }
    });
