import octoprint.plugin
import serial

class OnlinePrinter(octoprint.plugin.BlueprintPlugin, octoprint.plugin.StartupPlugin):
    ser = None

    def initPort(self):
        hasInitilized = False

        try:
            self.ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
            print("Initilized port /dev/ttyUSB0")
            hasInitilized = True
        except:
            try:
                self.ser = serial.Serial("/dev/ttyUSB1", 115200, timeout=1)
                print("Initilized port /dev/ttyUSB1")
                hasInitilized = True
            except:
                try:
                    self.ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
                    print("Initilized port /dev/ttyACM0")
                    hasInitilized = True
                except:
                    try:
                        self.ser = serial.Serial("/dev/ttyACM1", 115200, timeout=1)
                        print("Initilized port /dev/ttyACM1")
                        hasInitilized = True
                    except:
                        self.ser = None
                        hasInitilized = False
        
        if not hasInitilized:
            for i in range(12):
                try:
                    self.ser = serial.Serial("COM" + str(i), 115200, timeout=1)
                    print("Initilized port COM" + str(i))
                    hasInitilized = True
                    break
                except:
                    print("Failed to initilize port COM" + str(i))
        
        if not hasInitilized:
            raise IOError("Failed to initilize port")

    @octoprint.plugin.BlueprintPlugin.route("/ledon", methods=["GET"])
    def ledON(self):
        if self.ser:
            print("[OnlinePrinterPlugin] Turning LED on")
            self.ser.write(b'LED_ON')
            return "OK", 200
        else:
            return "Failed to initilize serial connection", 500
    
    @octoprint.plugin.BlueprintPlugin.route("/ledoff", methods=["GET"])
    def ledOFF(self):
        if self.ser:
            print("[OnlinePrinterPlugin] Turning LED off")
            self.ser.write(b'LED_OFF')
            return "OK", 200
        else:
            return "Failed to initilize serial connection", 500
    
    @octoprint.plugin.BlueprintPlugin.route("/unlock", methods=["GET"])
    def unlock(self):
        if self.ser:
            print("[OnlinePrinterPlugin] Unlocking")
            print(self.ser)
            self.ser.write(b'UNLOCK')
            return "OK", 200
        else:
            return "Failed to initilize serial connection", 500
    
    def on_startup(self, *args, **kwargs):
        print("[OnlinePrinterPlugin] Starting OnlinePrinterPlugin...")
        try:
            self.initPort()
        except Exception as e:
            raise IOError("[OnlinePrinterPlugin] Failed to initilize port")
        print("[OnlinePrinterPlugin] Successfully initilized COM port")
        print("[OnlinePrinterPlugin] OnlinePrinterPlugin has successfully started.")

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OnlinePrinter()