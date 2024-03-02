
#define USE_ARDUINO_INTERRUPTS true    
#include <PulseSensorPlayground.h>       


const int PulseWire = 36;       
const int LED13 = 2;          
int Threshold = 2000;           

                               
PulseSensorPlayground pulseSensor;  


void setup() {   

  Serial.begin(9600);         

  
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       
  pulseSensor.setThreshold(Threshold);   

   
   if (pulseSensor.begin()) {
    Serial.println("Pulse sensor ready!");  
  }
}



void loop() {

 int myBPM = pulseSensor.getBeatsPerMinute();  


if (pulseSensor.sawStartOfBeat()) {            
 Serial.println("Current pulse: "); 
 Serial.print("BPM: ");                       
 Serial.println(myBPM);          

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