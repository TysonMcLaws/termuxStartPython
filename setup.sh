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
wget 
