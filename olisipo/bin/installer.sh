
# FIXME: This should come from the pyproject.toml file
OLISIPO_VERSION="1.0.0"

help() {
  echo "Not implemented"
}

install() {
  echo "Installing Olisipo $OLISIPO_VERSION"
  python3 -m pip install olisipo-$OLISIPO_VERSION-py3-none-any.whl --break-system-packages
  chmod +x olisipo.sh
  sudo mv olisipo.sh /usr/bin
  # TODO Set the script such that we can call olisipo only and not olisipo.sh
}

uninstall() {
  echo "Removing Olisipo $OLISIPO_VERSION"
  python3 -m pip uninstall olisipo-$OLISIPO_VERSION-py3-none-any.whl --break-system-packages
  sudo rm /usr/bin/olisipo.sh
  # TODO Remove the config to run olisipo.sh as olisipo
}

if [[ "$1" == "install" ]];
then
  install
elif [[ "$1" == "remove" ]];
then
  uninstall
else
  help
fi