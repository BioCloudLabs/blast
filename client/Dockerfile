FROM node:20-alpine
WORKDIR /app
COPY client/package.json client/
RUN npm install
COPY . /app
RUN npm run build
EXPOSE 5173
CMD ["npm", "run", "preview"]