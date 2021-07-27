# Smart Garden Using Raspberry PI
An 'IOT system' to monitor sensors like soil moisture, luminosity, Water Level ,Temperature and Humidity for plants.

### Feature Overview
* List of all Sensor values on a LCD screen & webpage hosted locally.
* Water Flow and Light Switch Control on webpage.
* Real-time video feedback and Motion Detection.

### Hardware Needed
* Raspberry PI 3B/3B+/zero WH
* Esp32 Camera Module
* DHT 11/22
* Soil Moisture Sensor
* Water Level Sensor
* TSL2561
* 2 x 5v Optocoupler Relay
* MCP3008/MCP3208 ADC
* 3.5 inch LCD Display (HDMI).

***Note: A PC will be needed to edit the Node-Red flow or at least a mouse, keyboard & monitor if you wish to do it on raspberry pi itself***

***Note: The LCD with HDMI  is preferred as the GPIO headed one will not work since the TSL2561 sensor shares the same pins SDA & SCL.*** 

## Installation

**Step 1:** Connect and open a terminal in Raspberry pi over VNC or Ignore this step if you are using Raspberry PI directly over monitor.

***Note: If you Don't know how to enable VNC over ssh  follow the steps [here](https://www.raspberrypi.org/documentation/remote-access/vnc/)*** 

**Step 2:** Update your Raspberry PI.
```
sudo apt-get update && sudo apt-get upgrade
```
**Step 3:** 
Make sure you have latest Node-Red Installed on your Raspberry pi.
```bash
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```
***Step 4:*** Clone Repository.
```
git clone https://github.com/sphod/Smart-Garden-Using-Raspberry-PI
```
***Step 5:*** Copy Files around (You can also copy these files in vnc without using terminal).
```
cp /home/pi/Smart-Garden-Using-Raspberry-PI/tsl.py /home/pi/Desktop
```
_Copying Luminosity sensor script to desktop._
```
cp /home/pi/Smart-Garden-Using-Raspberry-PI/flows.json /home/pi/.node-red/lib/flows
```
_Copying JSON file (Node-Red Flow) to its appropriate folder._
```
cp /home/pi/Smart-Garden-Using-Raspberry-PI/Custom_script.py /home/pi
```
_Copying custom **.py** Script to home directory._

***Step 6:*** Run the **.py** script
```python
sudo python Custom_script.py
```
_process description_ 

**Step 7:** Start Node-Red
```
node-red-start
```
**Step 8:** 
Once Node-RED is running open the editor in a browser.

If you are using the browser on the Pi desktop, you can open the address: 
***http://localhost:1880***

When browsing from another machine you should use the hostname or IP-address of the Pi: ***http://<hostname>:1880*** You can find the IP address by running ***hostname -I*** on the Pi.

**Step 9:** Import Flow by going into menu (top right 3 dashes) **Import>Local>Flows>Flow**

**Step 10:** Install the list of nodes given below by going into menu (top right 3 dashes) 
**Manage palette>palette>install>search**

* node-red-contrib-dht-sensor
* node-red-contrib-google-sheets
* node-red-contrib-fs
* node-red-contrib-pythonshell
* node-red-dashboard
* node-red-node-pi-mcp3008

**Step 11** Click on Deploy & Visit address: ***http://localhost:1880/ui*** for Dashboard.

**Step 12** Make changes to **range node** according to your preference for luminosity, water-level and soil-moisture sensors.

***Note: For ease add a 'debug node' at the end of each 'range nodes' one by one.***

**Step 13:** Make your final changes and Deploy again.

---
