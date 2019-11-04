echo "Thank-you for testing my program"

if [ "`echo -n`" = "-n" ]; then
  n=""
  c="\c"
else
  n="-n"
  c=""
fi

echo $n For future refrence, what is your name? $c
read name
echo "Hello, $name"

echo "Installing termuxStartPython..."
echo "This may take a long time..."

apt-get install wget

echo "Installing control..."
wget https://raw.githubusercontent.com/TysonMcLaws/termuxStartPython/master/control.sh
chmod +x control.sh
echo "25% Done"

echo "Installing Lazymux..."
apt-get install python2
wget https://github.com/Gameye98/Lazymux.git
pip2 install os
pip2 install colorama
echo "50% Done"

echo $n Do you want to install Debian? $c

if [ "`echo -n`" = "-n" ]; then
  n=""
  c="\c"
else
  n="-n"
  c=""
fi

read name
echo "Hello, $name"
echo "Do you want to install a Debian Virtual Machine?" 
