FROM alpine:3.21.3

RUN apk add --no-cache imagemagick

COPY intensifier.sh /bin
WORKDIR /app

ENTRYPOINT ["sh", "/bin/intensifier.sh"]
