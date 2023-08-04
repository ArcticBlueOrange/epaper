import time
import spidev
import RPi.GPIO as GPIO
import logging

logger = logging.getLogger(__name__)

class Epaper:
    def __init__(self,
                 x=128,
                 y=250,
                 max_speed_hz=500000):
        self.x = x
        self.y = y

        self.RESET_PIN = 17
        self.DC_PIN = 25
        self.BUSY_PIN = 24

        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = max_speed_hz

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.RESET_PIN, GPIO.OUT)
        GPIO.setup(self.DC_PIN, GPIO.OUT)
        GPIO.setup(self.BUSY_PIN, GPIO.IN)

        time.sleep(0.1)
        GPIO.output(self.RESET_PIN, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.RESET_PIN, GPIO.HIGH)
        time.sleep(0.1)
        self.wait()
        self.command(0x12)
        self.wait()
        logger.debug("Epaper object created")

    def wait(self):
        while True:
            logger.debug("Waiting for free pin")
            if GPIO.input(self.BUSY_PIN) == GPIO.LOW:
                break
            else:
                time.sleep(0.1)

    def command(self, cmd):
        GPIO.output(self.DC_PIN, GPIO.LOW)
        self.spi.xfer([cmd])

    def data(self, data):
        GPIO.output(self.DC_PIN, GPIO.HIGH)
        self.spi.xfer([data])

    def update(self):
        self.command(0x20)
        self.wait()
        self.command(0x10)
        self.data(0x01)
        time.sleep(0.1)

    def flash_red(self,
                  on=True,
                  buf=None):
        logger.debug("Flashing RED")
        self.wait()
        self.command(0x26)
        if buf is None:
            if on:
                for i in range(int((self.x * self.y) / 8)):
                    self.data(0xFF)
            else:
                for i in range(int((self.x * self.y) / 8)):
                    self.data(0x00)
        else:
            for i in range(int((self.x * self.y) / 8)):
                self.data(buf[i])

    def flash_black(self,
                    on=True,
                    buf=None):
        logger.debug("Flashing BLACK")
        self.wait()
        self.command(0x24)
        if buf is None:
            if on:
                for i in range(int((self.x * self.y) / 8)):
                    self.data(0x00)
            else:
                for i in range(int((self.x * self.y) / 8)):
                    self.data(0xFF)
        else:
            for i in range(int((self.x * self.y) / 8)):
                self.data(buf[i])
