# Container image that runs your code
FROM python:3.6-rc-alpine

RUN pip install requests

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY sync-issue.py /sync-issue.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
  ENTRYPOINT ["python","sync-issue.py"]
