FROM python:3.9

COPY . /local
WORKDIR /local
RUN apt-get update && apt-get install apt-utils -y 
RUN cat requirements.system | xargs apt-get install -y

RUN pip install --no-cache -r requirements.txt
RUN ansible-galaxy collection install -r requirements.yml
CMD /bin/bash