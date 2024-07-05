# Usa la imagen base de Node.js con Alpine
FROM node:18-alpine

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia el archivo package.json y package-lock.json al directorio de trabajo
COPY package*.json ./

# Instala las dependencias de Node.js
RUN npm install

# Copia el resto del código de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que la aplicación estará disponible
EXPOSE 5173

# Comando predeterminado para ejecutar al iniciar el contenedor
CMD ["npm", "run", "dev", "--", "--host"]
