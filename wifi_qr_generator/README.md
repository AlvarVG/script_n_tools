# WiFi QR Code Generator

This script generates a QR code that allows users to connect to a WiFi network easily by scanning it with their smartphone. No need to manually enter the SSID and password.

Example: 

![Wifi qr code](wifi_qr.png)

## Repositories

This image is stored in both [docker](https://hub.docker.com/repository/docker/alvarvg/wifi_qr_generator/tags) and [quay.io](https://quay.io/repository/alvarvg/wifi_qr_generator) repositories, you can choose the one best fits for you. This image is also mutliarch and is being built for arm64 and amd64 architectures.

## Usage

There are two ways of running this script. The first one (and easiest one) is simply running the docker command:

```bash
docker run --rm -v $(pwd):/app wifi_qr_generator:1.0.0 -n "<your_wifi_name>" -p "<your_password>" 
```

The other one is directly using the script (useful if you want to tweak the resulting image):

```bash
python3 qr_generator -n "<your_wifi_name>" -p "<your_password>" 
```

By default, it assumes the password encryption is WPA2 you can also configure it to have, for example, the newly created WPA3:

```
usage: WIFI QR Generator [-h] -n NAME -p PASSWORD [-t {WEP,WPA,WPA2,WPA3}]

This scripts generates a wifi qr code to be used by your friends/clients

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Wifi name/SSID you are connecting to
  -p PASSWORD, --password PASSWORD
                        Wifi password you use to connect
  -t {WEP,WPA,WPA2,WPA3}, --password-enc {WEP,WPA,WPA2,WPA3}
                        Password encryption to be use. Default: WPA2
```                        
