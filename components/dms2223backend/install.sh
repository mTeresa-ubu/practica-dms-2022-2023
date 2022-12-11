#!/bin/bash

TEMP_DIR="$(mktemp -d)"

# Install
cp -R * "${TEMP_DIR}"
pushd "${TEMP_DIR}"
pip3 install .
popd

rm -R "${TEMP_DIR}"

# Elimina la base de datos cuando se ejecuta
dms2223backend-crear-ejemplo