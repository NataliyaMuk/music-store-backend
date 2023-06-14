FROM python:3.10

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/back_proj

RUN mkdir -p ${PROJ_DIR}
COPY ./musicbackend ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install -r requirements.txt

<<<<<<< HEAD
CMD ["celery", "-A", "musicbackend", "beat", "-l", "INFO"]
=======
CMD ["celery", "-A", "musicbackend", "beat", "-l", "INFO"]
>>>>>>> c2ad37208c2820a4d6fdf491f4b614aa1605bc72
