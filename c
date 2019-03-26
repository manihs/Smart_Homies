sudo chmod 777 c
sudo chmod 777 ngrok
lxterminal --command="./ngrok http 5000"
lxterminal --command="python post_random_url.py"
lxterminal --command="sudo python control.py"