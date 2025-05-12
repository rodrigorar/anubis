#!/bin/bash

set -euo pipefail

poetry build
version=$(cat pyproject.toml | grep version | tr -d 'version = "' | tr -d '"')
mkdir "anubis-$version"

tar -xf "dist/anubis-$version.tar.gz" -C "./anubis-$version" --strip-components 1
cp dist/**any.whl "./anubis-$version/anubis/bin"
rm "anubis-$version/anubis/bin/package.sh"
rm "anubis-$version/anubis/bin/package_wrapper.py"

tar -cf "anubis-$version.tar.gz" "anubis-$version"

rm -r "anubis-$version"