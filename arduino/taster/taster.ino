#define tasterPin 7


void setup() {
  // put your setup code here, to run once:
  pinMode(tasterPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(tasterPin) == HIGH){
    Serial.print("taster is high!!!");
    delay(1000);
  }
}
