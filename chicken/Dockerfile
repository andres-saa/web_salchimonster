# Etapa de construcción
FROM node:14 as build-stage
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build

# Etapa de producción
FROM nginx:alpine
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]