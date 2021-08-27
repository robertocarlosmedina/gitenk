
# gitenk dependencies
# Setup and dependencies installation
credentials = ""
if [ -z "$1"]
then
    echo -n "PASTE YOUR CREDENTIALS TOKEN HERE: "
    read credentials
else
    credentials = $1
fi

apt install figlet toilet
pip3 install pynput
sudo apt install lolcat
sudo cp ./gitenk.py /bin/
sudo cp ./gitenk /bin/
echo "$credentials" > credentials.txt   

clear

figlet -f slant -k -c  gitenk | lolcat -a -d 1
figlet -f term -k -c  Roberto Carlos Medina | lolcat -a -d 1
figlet -f term -k -c  robertocarlosmedina.dev@gmail.com | lolcat
figlet -f circle -k -c  2021 | lolcat
figlet -fterm -c Use 'gitenk help' to get start. | lolcat -a
