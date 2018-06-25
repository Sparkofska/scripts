This python script retrieves the current local IP address of the host and sends it to the specified Email receiver. Can be quite handy for a headless local server without static ip.

In order to run the script automatically on ubuntu startup paste the following line
```
python /path/to/ip_mailer.py
```
into the following file
```
/etc/rc.local
```
