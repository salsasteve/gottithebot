FROM node:lts-alpine3.16

# update and install dependency
RUN apk update && apk upgrade
RUN apk add --no-cache python3 g++ make git
RUN apk --no-cache --virtual build-dependencies add \
    python3 \
    make \
    g++

# create destination directory
RUN mkdir -p /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app

# copy the app, note .dockerignore
COPY /app /usr/src/nuxt-app/
RUN yarn install
RUN yarn build

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

CMD [ "yarn", "dev", "-o"]



