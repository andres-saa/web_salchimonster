export default {
    init() {
      // Inicialización del código de Facebook Pixel
      !function(f, b, e, v, n, t, s) {
        if (f.fbq) return;
        n = f.fbq = function() {
          n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
        };
        if (!f._fbq) f._fbq = n;
        n.push = n;
        n.loaded = !0;
        n.version = '2.0';
        n.queue = [];
        t = b.createElement(e);
        t.async = !0;
        t.src = v;
        s = b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t, s);
      }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', '9692941457447887'); // Asegúrate de reemplazar este ID con tu propio ID de Pixel
  
      // Código de Google Tag Manager
      const script = document.createElement('script');
      script.async = true;
      script.src = 'https://www.googletagmanager.com/gtag/js?id=G-HGS98CQWJN'; // Reemplaza con tu propio ID de Google Analytics
      script.onload = () => {
        window.dataLayer = window.dataLayer || [];
        window.gtag = function() { dataLayer.push(arguments); };
        gtag('js', new Date());
        gtag('config', 'G-HGS98CQWJN');
      };
      document.head.appendChild(script);
    },
    sendTrackingEvent(eventName, eventParams = {}) {
        if (window.fbq) {
          if (eventName === 'Purchase') {
            fbq('track', 'Purchase', {
              value: eventParams.value,
              currency: 'COP',  // Asegúrate de ajustar esto si decides convertir a otra moneda
              content_type: 'product',
              content_ids: eventParams.items.map(item => item.id)
            });
          } else {
            fbq('track', eventName);
          }
        }
        if (window.gtag) {
          gtag('event', eventName, {
            // Asegúrate de mapear todos los parámetros necesarios también para Google Analytics
            value: eventParams.total,
            currency: 'COP',
            items: eventParams.items
          });
        }
      }
      
  };