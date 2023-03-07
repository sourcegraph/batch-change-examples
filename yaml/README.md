# Modify YAML files with a Ruby script

This batch change demonstrates how to modify YAML files.

It uses a short Ruby script to read in the `docker-compose.yaml` files returned
by the Sourcegraph search, parse them, and add a new `entrypoint` argument to
existing `services` definitions.

It then uses a second container to install [prettier](https://prettier.io/) to
format the files that were rewritten by the previous step.

There are three main ways to pass long scripts to a batch change:
- add the script in the spec using the `file` property, see [modify-yaml](modify-yaml.batch.yaml)
- from Sourcegraph 3.41, mount a local script on the container, see [modify-yaml-mount-file](modify-yaml-mount-file.batch.yaml)
- bake them inside the containerHello World
