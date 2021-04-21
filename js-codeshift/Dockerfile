# Container image that runs your code
FROM node:14

RUN npm install -g jscodeshift

# As an alternative to defining steps.files in the batch spec, Transform files could be copied into the container.
# COPY warn-to-log.ts /warn-to-log.ts

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["bin/sh"]
