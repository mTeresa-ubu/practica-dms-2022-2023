#!/bin/bash

TEMP_DIR="$(mktemp -d)"

## Comentado por alvar para permitir la modificacion en tuenoi real
# Install
# cp -R * "${TEMP_DIR}"
# pushd "${TEMP_DIR}"
pip3 install -e .
# popd

# rm -R "${TEMP_DIR}"
