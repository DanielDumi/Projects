#include "BluetoothSerial.h"
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

#define RXp2 16
#define TXp2 17
void setup() {
 
  Serial.begin(115200);
  Serial2.begin(9600, SERIAL_8N1, RXp2, TXp2);

 SerialBT.begin("ESP32_Dev_Module"); 
 Serial.println("The device started, now you can pair it with bluetooth!");

}
void loop() {
    
    Serial.println(Serial2.readString());
     if (Serial.available()) {
 SerialBT.write(Serial.read());
 }
 if (SerialBT.available()) {
 Serial.write(SerialBT.read());
 }
 delay(20);
}
