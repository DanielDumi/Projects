
#define USE_ARDUINO_INTERRUPTS true    
#include <PulseSensorPlayground.h>       //library

const int PulseWire = 0;       //Analog pin A0
const int LED13 = 13;          //Arduino led, blinks when heartbeat happens
int Threshold = 550;           //Standard threshold value, Arduino ADC values (0 - 1023)

                               
PulseSensorPlayground pulseSensor;  //instance of pulsesensor object


void setup() {   

  Serial.begin(9600);         

  
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       //for blinking the led when hartbeat happens
  pulseSensor.setThreshold(Threshold);   

   
   if (pulseSensor.begin()) {
    Serial.println("Pulse sensor ready!");  
  }
}



void loop() {

 int myBPM = pulseSensor.getBeatsPerMinute();  //function that returns BPM as 'int'


if (pulseSensor.sawStartOfBeat()) {  //tests if hartbeat happens          
 Serial.println("Current pulse: "); 
 Serial.print("BPM: ");                       
 Serial.println(myBPM);          //print BPM as 'int'hh

 if((myBPM>=60)&&(myBPM<=70))
 Serial.println("Your pulse is in normal parameters");

 else
 if((myBPM > 70)&&(myBPM <=95))
 Serial.println("You are in sportive mode");

 else
 if((myBPM >95)&&(myBPM<=110))
 Serial.println("You are stressed, you should calm down");

 else
 if(myBPM >110)
 Serial.println("Your pulse in not ok, your pulse is too high");

 else
 Serial.println("Your pulse is too low");       

 delay(1000);      
}                   

}
