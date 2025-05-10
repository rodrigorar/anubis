#!/bin/bash

set -euo pipefail

poetry build
version=$(cat pyproject.toml | grep version | tr -d 'version = "' | tr -d '"')
mkdir "olisipo-$version"

tar -xf "dist/olisipo-$version.tar.gz" -C "./olisipo-$version" --strip-components 1
cp dist/**any.whl "./olisipo-$version/olisipo/bin"
rm "olisipo-$version/olisipo/bin/package.sh"
rm "olisipo-$version/olisipo/bin/package_wrapper.py"

tar -cf "olisipo-$version.tar.gz" "olisipo-$version"