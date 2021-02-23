FROM python:3
ADD tests.py
ADD example
ADD example2
EXPOSE 5555
CMD [ "python", "./tests.py" ]