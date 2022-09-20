FROM ubuntu:latest
RUN apt-get update && apt-get install -y curl && mkdir -p /code/convert
WORKDIR /code/convert
ADD convert-supplier.sh ./convert-supplier.sh

RUN ./convert-supplier.sh

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]
