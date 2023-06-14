FROM python:3.10

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/back_proj

RUN mkdir -p ${PROJ_DIR}
COPY ./musicbackend ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install -r requirements.txt


COPY ./compose/django/entry.sh /entry.sh
RUN chmod +x /entry.sh
<<<<<<< HEAD
ENTRYPOINT [ "/entry.sh" ]
=======
ENTRYPOINT ["sh", "/entry.sh" ]

# CMD ["celery", "-A", "musicbackend", "worker", "-l", "INFO"]
>>>>>>> c2ad37208c2820a4d6fdf491f4b614aa1605bc72
