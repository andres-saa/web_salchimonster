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
                    'order_status', 
                    'visibleNotifications']

        
    },
    state: () => {

        return {
            dateRange: {
                startDate: new Date(new Date().setDate(new Date().getDate() - 7)),
                endDate: new Date(),
            },
           

            loading:{
                visible:false,
                tittle:'Cargando'
            },

            visible:{
                show_validate:false,
                show_new_product:true
            }

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
            // Calcula la diferencia en días
            const start_date =  new Date(state.dateRange.endDate)
            const end_date = new Date(state.dateRange.startDate)
            const diffTime = Math.abs(start_date - end_date);
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

            console.log(diffDays,'dif')
            // Determina el nombre del rango basado en la diferencia de días
            let rangeName = '';
            switch(diffDays) {
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

            return {
                diffDays,
                rangeName
            };
        },
    },

    // actions y el resto de tu configuración...

   

    actions: {

        async fetchSalesReport() {

            if(this.selectedSites.length<1){
                alert('Selecciones las sedes pare el reporte, gracias.')
                return
            }
            const formattedStartDate = this.formatDate(this.dateRange.startDate);
            const formattedEndDate = this.formatDate(this.dateRange.endDate);
            const siteIds = this.selectedSites.map(site => site.site_id).join(',');

            // Construir la URL con parámetros de consulta
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
          
          setLoading(visibleValue, titleValue = 'cargando') {

            // Si visibleValue es true, actualiza inmediatamente
           
              this.loading = {
                visible: visibleValue,
                tittle: titleValue
              };

            
          },
          

          setVisibleOrder(visible, order={}){
            if(!visible){
                this.visibleOrder.order = {}
            }

            this.visibleOrder = {
                visible:visible,
                order:order
            }

          }
        
        


    },


})


