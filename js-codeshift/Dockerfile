# Container image that runs your code
FROM node:14

RUN npm install -g jscodeshift

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY warn-to-log.ts /warn-to-log.ts

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["jscodeshift", "-t", "./warn-to-log.ts", "./work"]