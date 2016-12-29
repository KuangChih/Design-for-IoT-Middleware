#Z-Wave Lab
##Outline
* [Objective](#objective)

* [Software](#software)
  * udpdevice_light_actuator.py
* [Hardware](#hardware)
  * WuDevice
  * Z-Wave Dongle
* [Implementation](#implementation)

##Objective
 * The goal is to build an IoT network that communicate between <b>zwave device</b></font> and <b>udp device</b>.
 * The message between the devices in different gateway will be <b>transmitted by their gateways</b>.
 * Use two gateways with different radio let two devices with different radio can communicate with each other.

<img src="./img/Lab6.gif" ><br/>

###Wukong Topologic
<img src="./img/WuKong Topologic.png" width="500"><br/>

###Communicate Between Different Radio
<img src="./img/Communicate Between Different Radio.png" width="500"><br/>

###WuDiagram
<img src="./img/WuDiagram.png" width="500"><br/>

##Software
###Wuclasses for Z-wave Device
```
cd <wkroot>/src/config/wunode
vim enabled_wuclasses.xml
```
```xml
<WuKong>
	<WuClass name="Binary_Sensor" appCanCreateInstances="false">
		<CreateInstance />
	</WuClass>
</WuKong>
```
###udpdevice_light_actuator.py

##Hardware

###WuDevice
<img src="./img/WuDevice.jpg" width="380" height="220">

###Z-Wave Dongle

##Implementation

