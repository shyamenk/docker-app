# Stage 1: Build
FROM node:19.4-bullseye AS build

WORKDIR /app

# Copy only package.json and package-lock.json to take advantage of Docker cache
COPY package*.json ./

RUN --mount=type=cache,target=/app/.npm \
  npm set cache /app/.npm && \
  npm install

# Stage 2: Development
FROM build as dev

# Copy the entire application code
COPY . .

# Set environment variables for development
ENV NODE_ENV=development
ENV PORT=3000

# Expose the port that your development server is running on
EXPOSE 3000

# Specify the command to run your development server
CMD ["npm", "run", "dev"]


# FROM nginxinc/nginx-unprivileged:1.23-alpine-perl

# COPY nginx.conf /etc/nginx/conf.d/default.conf

# COPY --from=dev /app/dist/ /usr/share/nginx/html
