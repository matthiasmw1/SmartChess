/*Example sketch to control a stepper motor with A4988/DRV8825 stepper motor driver and Arduino without a library. More info: https://www.makerguides.com */

// Define stepper motor connections and steps per revolution:
#define dirPin 4
#define stepPin 3
#define stepsPerRevolution 500
#define tasterPin 11
//define m1
//#define m2
//#define m3

void setup() {
  // Declare pins as output:
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(tasterPin, INPUT);  
}

void loop() {
digitalWrite(dirPin, HIGH);

  for (int i = 0; i < 10000; i++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(500);
    if (digitalRead(tasterPin) == HIGH){
      digitalWrite(stepPin, LOW);
      break;
    }
  }
}
