
OLISIPO_VERSION="1.1.0"
OLISIPO_EXEC_LOCATION="/usr/local/bin"
OLISIPO_EXEC="olisipo.sh"

help() {
  echo "\033[92m install\033[0m -> Install the Olisipo application"
  echo "\033[92m uninstall\033[0m -> Uninstall the Olisipo application"
  echo "\033[92m help\033[0m -> Shows this command"
}

install() {
  echo "Installing Olisipo $OLISIPO_VERSION"
  python3 -m pip install olisipo-$OLISIPO_VERSION-py3-none-any.whl --break-system-packages
  chmod +x olisipo.sh
  if [[ ! -d /usr/local/bin ]]; then sudo mkdir /usr/local/bin; fi
  sudo cp $OLISIPO_EXEC $OLISIPO_EXEC_LOCATION
}

uninstall() {
  echo "Removing Olisipo $OLISIPO_VERSION"
  python3 -m pip uninstall olisipo-$OLISIPO_VERSION-py3-none-any.whl --break-system-packages
  rm -r $HOME/.olisipo
  sudo rm $OLISIPO_EXEC_LOCATION/$OLISIPO_EXEC
}

if [[ "$1" == "install" ]];
then
  install
elif [[ "$1" == "uninstall" ]];
then
  uninstall
else
  help
fi