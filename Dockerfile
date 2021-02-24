FROM python:3
EXPOSE 5555
WORKDIR /tests
CMD [ "python3", "/tests/tests.py" ]
