
OLISIPO_VERSION="1.0.0"

install() {
  echo "Installing Olisipo $OLISIPO_VERSION"
  python3 -m pip install olisipo-$OLISIPO_VERSION-py3-none-any.whl --break-system-packages
  mv olisipo.sh /usr/bin
}

uninstall() {
  echo "Removing Olisipo $OLISIPO_VERSION"
  python3 -m pip uninstall olisipo-$OLISIPO_VERSION-py3-none-any.whl --break-system-packages
  rm /usr/bin/olisipo.sh
}

if [[ "$1" == "install" ]];
then
  install
elif [[ "$1" == "remove" ]];
then
  uninstall
else
  echo "Unknown command, please try again"
fi