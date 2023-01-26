FROM node:16-alpine as base

ENV HOST=0.0.0.0
ENV PORT=5000

WORKDIR /var/www/

FROM base as dev

COPY package.json yarn.lock ./

RUN yarn install && \
    yarn cache clean

COPY . ./

EXPOSE 5000

CMD ["yarn", "dev", "--", "-o"]