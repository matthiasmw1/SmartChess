#define dirPin 4
#define stepPin 3
#define stepsPerRevolution 500 //Herausfinden wofür dieses ist
#define tasterPin 11
//#define m1
//#define m2
//#define m3

void setup() {
    pinMode(dirPin, OUTPUT);
    pinMode(stepPin, OUTPUT);
    pinMode(tasterPin, INPUT);

}

void loop(){
    digitalWrite(dirPin, HIGH);

    digitalWrite(stepPin, HIGH);
    delayMicroseconds(500);
    if (digitalRead(tasterPin) == HIGH){
        digitalRead(stepPin, LOW);
        break;
    }
}