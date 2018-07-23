# clashroyale-1k-finder

This is a python script, which looks for 1k tournaments on clashroyale and sends you a notification over pushbullet if it found on. Get this script on your Raspberry Pi und run it via cronjob.

## Setup

1. Install [git](https://git-scm.com/) >2.12
2. Install [Python](https://www.python.org/) >=3.5.3 `apt-get install python3 && apt-get install python3-pip`
3. Verify that `python --version` shows a version equal to or higher then 3.5.3 Otherwise use [pyenv](https://github.com/pyenv/pyenv#installation) to install version 3.5.3
4. `pip3 install -r requirements.txt`
5. Copy `clashroyale.example.cfg` to `clashroyale.cfg` and adjust the config to your needs.
6. run `python3 main.py `



## Config

* Copy `clashroyale.example.cfg` to `clashroyale.cfg`.

* Then enter your ClashRoyale api key, which you can get here.

* ```
  [ClashRoyale]
  clashroyale_api_key = YourClashRoyaleApiKey
  ```

* Then add you Devices. You can add as many devices as you want. Therefore you have to give your device a number, starting from 1 and iterate until you have added all devices. For example the first device is introduced with `[Device_1]`, the second device is introduced with `[Device_2]`, and so on. 

* Then you have to configure the notification service which should be used. This service can be different for all you devices. You can choose from the following notification services: 

  * `Pushover` (Android & iOS)[more information](https://pushover.net/)
  * `Pushbullet` (Android & iOS) [more information](https://www.pushbullet.com/)
  *  `PushMe` (iOS) [more information](https://pushme.jagcesar.se/)

* After you specified your notification service, you have to configure them. Their options can be different. The following example shows a configfile with all three notification services configured:

* ```
  [ClashRoyale]
  clashroyale_api_key = YourClashRoyaleApiKey
  
  [Device_1]
  notification_service = Pushbullet
  api_key = YourPushbulletApiKey
  device_identifier = YourDeviceIdentifier
  
  [Device_2]
  notification_service = Pushover
  api_key = YourFriendsPushbulletApiKey
  device_identifier = YourFriendsDeviceIdentifier
  
  [Device_3]
  notification_service = PushMe
  device_identifier = YourDeviceIdentifier
  ```

  



 