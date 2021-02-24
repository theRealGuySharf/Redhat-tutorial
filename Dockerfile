FROM python:3
ADD tests.py test.py
ADD example example
ADD example2 example2
EXPOSE 5555
CMD [ "python", "./tests.py" ]
