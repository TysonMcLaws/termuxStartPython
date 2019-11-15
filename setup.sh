echo "Thank-you for testing my program"

echo -n "For future refrence, what is your name?"
read name
echo "Hello, $name"

echo "Installing termuxStartPython..."
echo "This may take a long time..."

apt-get install wget

echo "Installing control.sh..."
wget https://raw.githubusercontent.com/TysonMcLaws/termuxStartPython/master/control.sh
chmod +x control.sh
echo "25% Done"

echo -n "Do you want to install Lazymux? (Y/n) "
read lazymuxChoice
if [ lazymuxChoice = "Y" ]; then
  echo "Installing Lazymux..."
  apt-get install python2
  wget https://github.com/Gameye98/Lazymux.git
  pip2 install os
  pip2 install colorama
  echo "50% Done"
fi

echo -n "Do you want to install a Debian Virtual Machine? (Y/n) "
read debianChoice
if [ debianChoise = "Y" ]; then
  echo "Installing Debian Virtual Machine..."
  echo "This may take a long time..."
  pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh
  ./start-debian.sh
  echo "Now paste the text that was atomatically copied to your clip-board"
  echo "75% Done"
fi
