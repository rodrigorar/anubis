
ANUBIS_VERSION="1.1.0"
ANUBIS_EXEC_LOCATION="/usr/local/bin"
ANUBIS_EXEC="anubis.sh"

help() {
  echo "\033[92m install\033[0m -> Install the Anubis application"
  echo "\033[92m uninstall\033[0m -> Uninstall the Anubis application"
  echo "\033[92m help\033[0m -> Shows this command"
}

install() {
  echo "Installing Anubis $ANUBIS_VERSION"
  python3 -m pip install anubis-$ANUBIS_VERSION-py3-none-any.whl --break-system-packages
  chmod +x anubis.sh
  if [[ ! -d /usr/local/bin ]]; then sudo mkdir /usr/local/bin; fi
  sudo cp $ANUBIS_EXEC $ANUBIS_EXEC_LOCATION
}

uninstall() {
  echo "Removing Anubis $ANUBIS_VERSION"
  python3 -m pip uninstall anubis-$ANUBIS_VERSION-py3-none-any.whl --break-system-packages
  rm -r $HOME/.anubis
  sudo rm $ANUBIS_EXEC_LOCATION/$ANUBIS_EXEC
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