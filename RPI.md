# Raspberry PI Setup

## 1. Create Image with Raspberry Pi Imager
  
- hostname:   cocktail-machine.local  
- username:   toor  
- password:   otzberg  

Enable SSH with password authentication

## 2. Setup Raspberry Pi

```language
sudo apt update && apt upgrade  // Update RPI
sudo apt install sqlite3        // Install SQLite
sudo apt install pip            // Install pip for python
sudo apt install quart          // Install Quart for Webite with Async
```

## 3. Download Project

```
wget https://github.com/timsterber/cocktail-machine.git
```

## 4. Autostart Script

```
cd cocktail-machine     
chmod 755 launcher.sh   // make it executable
cd ..
mkdir logs              // create logs folder for crontab

sudo crontab -e         // Edit /bin/nano
```
add to the file:  
@reboot sh /home/toor/cocktail-machine/launcher.sh >/home/toor/logs/cronlog 2>&1

When you want to deactivate the autostart, you can just simply comment the line above.

## 5. Configure Access Point
Instructions similar to [Bcyber](https://www.youtube.com/watch?v=S4E35d91Xss&ab_channel=Bcyber)

1. You will need "Raspberry PI OS (Legacy, 64-Bit) Lite / Bullseys" for the access point to work with the following instructions.
```
sudo apt update && sudo apt upgrade

sudo raspi-config		// Config Country-Code in WIFI

sudo apt install hostapd		// Install the dependencies for the AP
sudo systemctl unmask hostapd
sudo systemctl enable hostapd

sudo apt install dnsmasq		// DNS & DHCP-Server
sudo DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent
```

2. Edit DHCP config
```
sudo nano /etc/dhcpcd.conf
```
Now add the following to the end of the file:
```
interface wlan0
static ip_address=192.168.1.1/24
nohook wpa_supplicant
```

3. Edit IP-Forwarding
```
sudo nano /etc/sysctl.d/routed-ap.conf
```
and add the following line to the file:
```
net.ipv4.ip_forward=1
```

4. IPtables Forwarding
```
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo netfilter-persistent save
``` 

5. Edit DNSmasq
```
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.old
sudo nano /etc/dnsmasq.conf
```
Then add the following lines:
```
interface=wlan0
dhcp-range=192.168.1.2,192.168.1.20,255.255.255.0,24h
domain=wlan
```

6. Unblock wifi if not already done
```
sudo rfkill unblock wlan
```

7. Edit WLAN Settings
```
sudo nano /etc/hostapd/hostapd.conf
```
Add the following lines:
```
interface=wlan0
country_code=DE
ssid=CocktailMachine
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=0
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=OtzbergJT
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
```

8. Reboot the RPI
```
sudo reboot
```

## 6. Configure DNS Server
dnsmasq with cocktail.app

edit /etc/dnsmasq.conf and add the following lines:
```
address=/cocktail.app/192.168.1.1
dhcp-option=6,192.168.1.1
```

Then execute the following commands, so that all DNS traffic is routed through the Raspberrys DNS Server:
```
sudo iptables -t nat -A PREROUTING -p udp --dport 53 -j DNAT --to-destination 192.168.1.1:53
sudo iptables -t nat -A PREROUTING -p tcp --dport 53 -j DNAT --to-destination 192.168.1.1:53
sudo sh -c "iptables-save > /etc/iptables.rules"

sudo modprobe iptable_nat
sudo modprobe nf_conntrack

iptables-restore < /etc/iptables.rules

```


## 7. DONE