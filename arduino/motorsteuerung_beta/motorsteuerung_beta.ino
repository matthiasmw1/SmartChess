#include <AccelStepper.h>

#define X_STEP_PIN 2
#define X_DIR_PIN 5
#define Y_STEP_PIN 3
#define Y_DIR_PIN 6
#define X_TASTER_PIN 9
#define Y_TASTER_PIN 10
#define Z_TASTER_PIN 11

AccelStepper stepperX(AccelStepper::DRIVER, X_STEP_PIN, X_DIR_PIN);
AccelStepper stepperY(AccelStepper::DRIVER, Y_STEP_PIN, Y_DIR_PIN);

void setup() {
  Serial.begin(9600);
  pinMode(9, INPUT_PULLUP);
  stepperX.setMaxSpeed(1000);
  stepperX.setAcceleration(5000);
  stepperX.setSpeed(500);

  stepperY.setMaxSpeed(1000);
  stepperY.setAcceleration(4000);
  stepperY.setSpeed(500);
}

void loop() {

  delay(1000);
  if(9 == true){
    Serial.print("Taste gedrückt!");
  }
  else if (9 == false){
    Serial.print("Taster nicht gedrückt!");
  }
/*
  if(X_TASTER_PIN == HIGH){
      int targetX = 300;
//  int targetY = 500;

  // Move both motors to their respective target positions
  stepperX.moveTo(targetX);
//  stepperY.moveTo(targetY);

  // Run both motors until they reach their targets
  while (stepperX.isRunning() || stepperY.isRunning()) {
    stepperX.run();
//    stepperY.run();
  }
  
  delay(1000);
  
  targetX = -200;
//  targetY = -500;

  // Move both motors to their respective target positions
  stepperX.moveTo(targetX);
//  stepperY.moveTo(targetY);

  // Run both motors until they reach their targets
  while (stepperX.isRunning() || stepperY.isRunning()) {
    stepperX.run();
//    stepperY.run();
  }
  
  }*/
}
