FROM node:alpine

RUN apk --no-cache add curl

WORKDIR /chatbot

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

CMD ["npm", "start"]