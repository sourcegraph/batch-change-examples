#! /usr/bin/env sh

# Copy files to container only disk location for to avoid file sync thrashing
cp -r /work /tmp/app
cd /tmp/app
yarn add --non-interactive --ignore-optional --ignore-engines --ignore-platform  rxjs@^6.5.4
rm -fr node_modules .git
cp -fr . /work
