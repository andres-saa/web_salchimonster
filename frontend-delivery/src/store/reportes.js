import { defineStore } from "pinia";
import { URI } from "../service/conection";





export const useReportesStore = defineStore('reportes', {
   
    persist: {
       
                key: 'reportes', // La clave bajo la cual se almacenará tu estado en el storage
                storage: localStorage,
                paths:[
                    'dateRange',
                    'salesReport',
                    'selectedSites',
                    'order_status', // Estado por defecto si no hay nada en localStorage
                    // 'ventasCharData',
                    'visibleNotifications']

        
    },
    state: () => {


        // const savedStartDate = localStorage.getItem('reportesStartDate');
        // const savedEndDate = localStorage.getItem('reportesEndDate');
        // const savedSites = localStorage.getItem('selectedSites');
        // const savedOrderStatus = localStorage.getItem('orderStatus');
        


        return {
            dateRange: {
                startDate: new Date(new Date().setDate(new Date().getDate() - 7)),
                endDate: new Date(),
            },
            salesReport:
            {
                "total_sales": {
                    "total_sales": 0,
                    "total_orders": 0,
                    "average_ticket": 0
                }
            },
            selectedSites: [],
            order_status: 'enviada', // Estado por defecto si no hay nada en localStorage
            ventasCharData:{},
            ordersCharData:{},
            ticketsCharData:{},
            loading:false,
            visibleNotifications:false,
            visibleOrder:{
                visible:false,
                order:{}
            },

            Loading:{
                visible:false,
                tittle:'Cargando'
            },
            sitesStatus:[]
            



        }
    },

    getters: {
        lastWeek: (state) => {
            const today = new Date();
            const pastDate = new Date();
            pastDate.setDate(today.getDate() - 7); // +1 para incluir el día de hoy en el rango
            return {
                startDate: pastDate,
                endDate: today
            }
        },
        lastMidMonth: (state) => {
            const today = new Date();
            const pastDate = new Date();
            pastDate.setDate(today.getDate() - 14); // +1 para incluir el día de hoy en el rango
            return {
                startDate: pastDate,
                endDate: today
            }
        },
        lastMonth: (state) => {
            const today = new Date();
            const pastDate = new Date();
            pastDate.setDate(today.getDate() - 28); // +1 para incluir el día de hoy en el rango
            return {
                startDate: pastDate,
                endDate: today
            }
        },

        dateRangeDifference(state) {
            // Obtiene la fecha actual y elimina las horas, minutos y segundos
            const today = new Date();
            today.setHours(0, 0, 0, 0);
        
            const tomorrow = new Date(today);
            tomorrow.setDate(tomorrow.getDate() + 1);
        
            const yesterday = new Date(today);
            yesterday.setDate(yesterday.getDate() - 1);
        
            // Obtiene las fechas de inicio y fin del estado y elimina las horas, minutos y segundos
            const start_date = new Date(state.dateRange.startDate);
            start_date.setHours(0, 0, 0, 0);
        
            const end_date = new Date(state.dateRange.endDate);
            end_date.setHours(0, 0, 0, 0);
        
            // Calcula la diferencia en días
            const diffTime = Math.abs(end_date - start_date);
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        
            // Determina el nombre del rango basado en la diferencia de días
            let rangeName = '';
            if (start_date.getTime() === today.getTime() && end_date.getTime() === tomorrow.getTime()) {
                rangeName = 'Hoy';
            } else if (start_date.getTime() === yesterday.getTime() && end_date.getTime() === today.getTime()) {
                rangeName = 'Ayer';
            } else {
                switch (diffDays) {
                    case 2:
                        rangeName = 'Últimos 2 días';
                        break;
                    case 8:
                        rangeName = 'Últimos 7 días';
                        break;
                    case 15:
                        rangeName = 'Últimos 14 días';
                        break;
                    case 29:
                        rangeName = 'Últimos 28 días';
                        break;
                    default:
                        // No coincide con ningún rango predefinido
                        rangeName = null;
                }
            }
        
            return {
                diffDays,
                rangeName
            };
        }
        
        
        
        
    },

    // actions y el resto de tu configuración...

   

    actions: {

        async fetchSalesReport() {

             
            const formattedStartDate = this.formatDate(this.dateRange.startDate);
            const formattedEndDate = this.formatDate(this.dateRange.endDate);
            const siteIds = this.selectedSites.map(site => site.site_id).join(',');


            const queryParams = new URLSearchParams({
                site_ids: siteIds,
                status: this.order_status,
                start_date: formattedStartDate,
                end_date: formattedEndDate
            });

            const url = `${URI}/sales_report?${queryParams.toString()}`;

            try {
                this.setLoading(true, 'cargando reporte')
                const response = await fetch(url, {
                    method: 'GET', // Método GET especificado aquí
                    headers: {
                        'Content-Type': 'application/json',
                        // Agrega aquí otros encabezados si son necesarios
                    }
                });

                if (!response.ok) {
                    this.setLoading(false, 'cargando reporte')
                    throw new Error(`HTTP error! status: ${response.status}`);
                    
                }

                const data = await response.json();
                this.salesReport = data
                this.fetchDilyReport()
                this.fetchDilyOrdersReport()
                this.fetchTicketsReport()


                // Maneja la respuesta
                console.log(data);
                this.setLoading(false, 'cargando reporte')
            } catch (error) {
                console.error('Fetch error:', error);
                this.setLoading(false, 'cargando reporte')
            }
        },


        formatDate(dated) {
            const date = new Date(dated)
            const year = date.getFullYear();
            const month = (date.getMonth() + 1).toString().padStart(2, '0');
            const day = date.getDate().toString().padStart(2, '0');
            return `${year}-${month}-${day}`;
        },

        setDateRange(startDate, endDate) {
            // Actualizar el estado
            this.dateRange.startDate = new Date(startDate);
            this.dateRange.endDate = new Date(endDate);

            
        },



        async fetchDilyReport() {
              const formattedStartDate = this.formatDate(this.dateRange.startDate)
              const formattedEndDate = this.formatDate(this.dateRange.endDate)
              const siteIds = this.selectedSites.map(site => site.site_id).join(',');
        
            // Construir la URL con parámetros de consulta
            const queryParams = new URLSearchParams({
                site_ids: siteIds,
                status: this.order_status,
                start_date: formattedStartDate,
                end_date: formattedEndDate
            });
        
            const url = `${URI}/daily_sales?${queryParams.toString()}`;
        
            try {
                const response = await fetch(url, {
                    method: 'GET', // Método GET especificado aquí
                    headers: {
                        'Content-Type': 'application/json',
                        // Agrega aquí otros encabezados si son necesarios
                    }
                });
        
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
        
                const data = await response.json();
                // salesReport.value = data

                this.setChartData(data)
                return (data)
        
        
                // Maneja la respuesta
                console.log(data);
            } catch (error) {
                console.error('Fetch error:', error);
            }
        },
        async fetchDilyOrdersReport() {
            const formattedStartDate = this.formatDate(this.dateRange.startDate)
            const formattedEndDate = this.formatDate(this.dateRange.endDate)
            const siteIds = this.selectedSites.map(site => site.site_id).join(',');
      
          // Construir la URL con parámetros de consulta
          const queryParams = new URLSearchParams({
              site_ids: siteIds,
              status: this.order_status,
              start_date: formattedStartDate,
              end_date: formattedEndDate
          });
      
          const url = `${URI}/daily_orders?${queryParams.toString()}`;
      
          try {
              const response = await fetch(url, {
                  method: 'GET', // Método GET especificado aquí
                  headers: {
                      'Content-Type': 'application/json',
                      // Agrega aquí otros encabezados si son necesarios
                  }
              });
      
              if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
              }
      
              const data = await response.json();
              // salesReport.value = data

              this.setCharOrdersData(data)
              return (data)
      
      
              // Maneja la respuesta
              console.log(data);
          } catch (error) {
              console.error('Fetch error:', error);
          }
      },
      async fetchTicketsReport() {
        const formattedStartDate = this.formatDate(this.dateRange.startDate)
        const formattedEndDate = this.formatDate(this.dateRange.endDate)
        const siteIds = this.selectedSites.map(site => site.site_id).join(',');
  
      // Construir la URL con parámetros de consulta
      const queryParams = new URLSearchParams({
          site_ids: siteIds,
          status: this.order_status,
          start_date: formattedStartDate,
          end_date: formattedEndDate
      });
  
      const url = `${URI}/daily_average_ticket?${queryParams.toString()}`;
  
      try {
          const response = await fetch(url, {
              method: 'GET', // Método GET especificado aquí
              headers: {
                  'Content-Type': 'application/json',
                  // Agrega aquí otros encabezados si son necesarios
              }
          });
  
          if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
          }
  
          const data = await response.json();
          // salesReport.value = data

          this.setCharTicketsData(data)
          return (data)
  
  
          // Maneja la respuesta
          console.log(data);
      } catch (error) {
          console.error('Fetch error:', error);
      }
  },

        setChartData (data) {
                const keys = [];
                const values = [];
                data.forEach(obj => {
                    Object.keys(obj).forEach(key => {
                        if (!keys.includes(key)) {
                            keys.push(key);
                        }
                    });
        
                    Object.values(obj).forEach(value => {
                        values.push(value); // Si quieres valores únicos, debes verificar antes de añadir
                    });
                });
        
                this.ventasCharData = {
                    labels: keys,
                datasets: [
                    {
                        label: 'Venta',
                        data: values,
                        fill: true,
                        tension: 0.4,
                        backgroundColor: this.order_status == 'enviada'? '#d0e1fd' : 'rgba(255, 99, 132, 0.2)', // Color de fondo
                        borderColor:this.order_status == 'enviada'? '#3b82f6' :  'rgba(255, 99, 132, 1)', // Color del borde
                        borderWidth: 1.8,
                    },
        
                ]
                }
        
        
        
        
            const documentStyle = getComputedStyle(document.documentElement);
        
           
        },

        setCharOrdersData (data) {
            const keys = [];
            const values = [];
            data.forEach(obj => {
                Object.keys(obj).forEach(key => {
                    if (!keys.includes(key)) {
                        keys.push(key);
                    }
                });
    
                Object.values(obj).forEach(value => {
                    values.push(value); // Si quieres valores únicos, debes verificar antes de añadir
                });
            });
    
            this.ordersCharData = {
                labels: keys,
            datasets: [
                {
                    label: 'Venta',
                    data: values,
                    fill: true,
                    tension: 0.4,
                    backgroundColor: this.order_status == 'enviada'? '#d0e1fd' : 'rgba(255, 99, 132, 0.2)', // Color de fondo
                    borderColor:this.order_status == 'enviada'? '#3b82f6' :  'rgba(255, 99, 132, 1)', // Color del borde
                    borderWidth: 1.8,
                },
    
            ]
            }
    
    
    
    
        const documentStyle = getComputedStyle(document.documentElement);
    
       
    },
    setCharTicketsData (data) {
        const keys = [];
        const values = [];
        data.forEach(obj => {
            Object.keys(obj).forEach(key => {
                if (!keys.includes(key)) {
                    keys.push(key);
                }
            });

            Object.values(obj).forEach(value => {
                values.push(value); // Si quieres valores únicos, debes verificar antes de añadir
            });
        });

        this.ticketsCharData = {
            labels: keys,
        datasets: [
            {
                label: 'Venta',
                data: values,
                fill: true,
                tension: 0.4,
                backgroundColor: this.order_status == 'enviada'? '#d0e1fd' : 'rgba(255, 99, 132, 0.2)', // Color de fondo
                borderColor:this.order_status == 'enviada'? '#3b82f6' :  'rgba(255, 99, 132, 1)', // Color del borde
                borderWidth: 1.8,
            },

        ]
        }




    const documentStyle = getComputedStyle(document.documentElement);

   
},
        setSelectedSites(sites) {
            this.selectedSites = sites;
            localStorage.setItem('selectedSites', JSON.stringify(sites));
          },

        setOrderStatus(status) {
            this.order_status = status;
            localStorage.setItem('orderStatus', status);
          },
          toogleVisibleNotifications(status) {
            this.visibleNotifications = !this.visibleNotifications
          },
          
          setLoading(visibleValue,tittleValue='cargando') {
            // if(this.loading.visible  && visibleValue ){
            //     return
            // }

            if(this.loading?.visible == true && visibleValue == true) {
                return
            }

            if(!visibleValue){
                setTimeout(() => {
                    this.loading = {
                        visible:visibleValue,
                        tittle: visibleValue == false? 'cargando' : tittleValue
                        }
                }, 0);
            }else
            this.loading = {
            visible:visibleValue,
            tittle: visibleValue == false? 'cargando' : tittleValue
            }
          },

          setVisibleOrder(visible, order={}){
            if(!visible){
                this.visibleOrder.order = {}
            }

            this.visibleOrder = {
                visible:visible,
                order:order
            }

          },
        
        
          async setSitesStatus() {
            
            try {
                const response = await fetch(`${URI}/sites/online-status`)

                if(!response.ok){
                    throw 'paila'
                }

                this.sitesStatus = await response.json()
            } catch (error) {
                
            }
          },

          startSitesStatusUpdate() {
            this.setSitesStatus(); // Llama inmediatamente al inicio para obtener el estado actual
            setInterval(async () => {
                await this.setSitesStatus(); // Llama a la acción cada 30 segundos
            }, 3000); // 30000 milisegundos = 30 segundos
        },


    },


})


