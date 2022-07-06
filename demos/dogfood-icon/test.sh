if [[ $(pwd) = "/work" ]]; then
        echo "This is the root workspace, skipping"
      else
        yarn --cwd / transform --write -t 'packages/transforms/src/mdiIconToMdiPath/mdiIconToMdiPath.ts' "${PWD}/**/*.tsx"
      fi
