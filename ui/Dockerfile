FROM node:20.9.0-slim AS builder

WORKDIR /ui

# Install dependencies
COPY package*.json ./
RUN npm install

# Build application
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]