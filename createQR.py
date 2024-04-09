import segno
from segno import helpers

ssid = "SSID"
password = "passphrase"
security = "WPA"  # or "nopass" for open networks

qrcode = helpers.make_wifi(ssid=ssid, password=password, security=security)

qrcode.save("WiFi.png", scale=10)

qrcode.designator

print("WiFi QR code generated successfully!")
