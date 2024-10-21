
# FIXME: This should come from the pyproject.toml file
OLISIPO_VERSION="1.0.0"

help() {
  echo -e "\033[92m install\033[0m -> Install the Olisipo application"
  echo -e "\033[92m uninstall\033[0m -> Uninstall the Olisipo application"
  echo -e "\033[92m help\033[0m -> Shows this command"
}

install() {
  echo "Installing Olisipo $OLISIPO_VERSION"
  python3 -m pip install olisipo-$OLISIPO_VERSION-py3-none-any.whl --break-system-packages
  chmod +x olisipo.sh
  if [[ ! -d /usr/local/bin ]]; then sudo mkdir /usr/local/bin; fi
  sudo mv olisipo.sh /usr/local/bin
}

uninstall() {
  echo "Removing Olisipo $OLISIPO_VERSION"
  python3 -m pip uninstall olisipo-$OLISIPO_VERSION-py3-none-any.whl --break-system-packages
  rm -r $HOME/.olisipo
  sudo rm /usr/bin/olisipo.sh
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