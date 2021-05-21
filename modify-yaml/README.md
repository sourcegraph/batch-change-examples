# Modify YAML files with a Ruby script

This batch change demonstrates how to modify YAML files.

It uses a short Ruby script to read in the `docker-compose.yaml` files returned
by the Sourcegraph search, parse them, and add a new `entrypoint` argument to
existing `services` definitions.

It then uses a second container to install [prettier](https://prettier.io/) to
format the files that were rewritten by the previous step.
