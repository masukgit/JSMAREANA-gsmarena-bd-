import json


my_dicts = {
"specifications": "{\"Technology\":\"GSM \\/ HSPA \\/ LTE\",\"2G bands\":\"GSM 850 \\/ 900 \\/ 1800 \\/ 1900 - SIM 1 & SIM 2\",\"3G bands\":\"HSDPA 850 \\/ 900 \\/ 2100 \",\"4G bands\":\"1, 3, 5, 7, 8, 20\",\"Speed\":\"HSPA 42.2\\/11.5 Mbps, LTE-A Cat7 300\\/150 Mbps\",\"Announced\":\"2020, November 12\",\"Status\":\"Available. Released 2020, November 12\",\"Dimensions\":\"156.1 x 73.7 x 9.7 mm (6.15 x 2.90 x 0.38 in)\",\"Weight\":\"177.5 g (6.28 oz)\",\"SIM\":\"Dual SIM\",\"Type\":\"Li-Ion 3500 mAh, non-removable\",\"Size\":\"6.1 inches, 92.3 cm2 (~80.2% screen-to-body ratio)\",\"Resolution\":\"600 x 1280 pixels (~232 ppi density)\",\"OS\":\"Android 10\",\"Chipset\":\"Mediatek MT6761 Helio A22 (12 nm)\",\"CPU\":\"Octa-core 2.0 GHz Cortex-A53\",\"GPU\":\"PowerVR GE8320\",\"Card slot\":\"microSDXC (dedicated slot)\",\"Internal\":\"16GB 2GB RAM\",\"&nbsp;\":\"eMMC 5.1\",\"Triple\":\"8 MP, f\\/2.0, (wide)\\r\\n  2 MP\\r\\n  2 MP\",\"Features\":\"LED flash\",\"Video\":\"\",\"Single\":\"5 MP, f\\/2.2\",\"Loudspeaker \":\"Yes\",\"3.5mm jack \":\"Yes\",\"WLAN\":\"Wi-Fi 802.11 a\\/b\\/g\\/n\\/ac, dual-band, hotspot\",\"Bluetooth\":\"5.0, A2DP, LE\",\"GPS\":\"Yes, with A-GPS, GLONASS\",\"NFC\":\"No\",\"Radio\":\"Stereo FM radio, RDS, recording\",\"USB\":\"microUSB 2.0\",\"Sensors\":\"Accelerometer, proximity\",\"Colors\":\"Twilight, Black, Midnight Green\",\"SAR\":\"0.67 W\\/kg (head) &nbsp; &nbsp; 0.59 W\\/kg (body) &nbsp; &nbsp; \"}"
}
data = my_dicts.get('specifications')
json_data = json.loads(data)
print(json_data)