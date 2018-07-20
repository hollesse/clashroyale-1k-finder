from pushbullet.pushbullet import Pushbullet
import logging


class Device:

    def __init__(self, pushbullet_api_key, pushbullet_device_name):
        self._pushbullet_api_key = pushbullet_api_key
        self._pushbullet_device_name = pushbullet_device_name
        self._pushbullet = Pushbullet(self._pushbullet_api_key)
        self._pushbullet_device = self.__get_pushbullet_device()

    def __get_pushbullet_device(self):
        all_possible_devices = self._pushbullet.devices
        for device in all_possible_devices:
            if device.nickname == self._pushbullet_device_name:
                logging.info('Found Pushbullet device: "%s"', device.nickname)
                return device
        logging.error('Did not found Pushbullet device! '
                      'These are all possible devices: "%s" '
                      'This is the device name specified in config: "%s"',
                      all_possible_devices,
                      self._pushbullet_device_name)
        exit(1)

    def send_notification(self, tournament):
        self._pushbullet.push_note('1K Tournament found!',
                                   'Name: ' + tournament['name'],
                                   device=self._pushbullet_device)
        logging.info('Pushbullet notification sent to "%s"! Tag: "%s" Name: "%s"',
                     self._pushbullet_device.nickname,
                     tournament['tag'],
                     tournament['name'])

    def pushbullet_device_name(self):
        return self._pushbullet_device_name

    def test_pushbullet(self):
        self._pushbullet.push_note('Test', 'Test', device=self._pushbullet_device)
        logging.info('Pushbullet test notification sent to "%s"!', self._pushbullet_device.nickname)

    def print_all_possible_pushbullet_devices(self):
        print(self._pushbullet.devices)
