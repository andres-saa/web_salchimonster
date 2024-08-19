// Función para formatear un número como pesos colombianos
function formatoPesosColombianos(numero) {
    return new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', minimumFractionDigits: 0, maximumFractionDigits: 0 }).format(numero);
  }
  
  // Ejemplo de uso
  const numero = 1000000; // Este es el valor en memoria
  const numeroFormateado = formatoPesosColombianos(numero); // Formatear el número
  console.log(numeroFormateado); // Esto mostrará "COP 1.000.000" en la consola
  

  export {formatoPesosColombianos}