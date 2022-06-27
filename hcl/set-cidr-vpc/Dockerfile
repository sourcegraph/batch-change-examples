# If building on M1, build using --platform linux/amd64
FROM golang:1.18.3-alpine3.16
RUN apk --no-cache add make git bash
RUN git clone https://github.com/minamijoyo/hcledit; make install -C hcledit

FROM alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /work
COPY --from=0 /go/bin/hcledit /bin
ENTRYPOINT ["bin/sh"]
