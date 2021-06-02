#@ Uses a base python3.7.5 slim image as the base OS kernel
FROM python:3.7.9-slim

#@ Make an app folder
WORKDIR /app

#@ Copy all the files inside of the app folder
COPY . /app

#@ Install the requirements
RUN pip3 install -r requirements.txt

#@ Exposing 4000 port
EXPOSE 4000

#@ Command to use and open python shell
ENTRYPOINT  ["streamlit"]

#@ Execute `main.py` file with ENTRYPOINT during runtime 
CMD ["run", "main.py"] 