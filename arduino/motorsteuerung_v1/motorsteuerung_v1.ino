#include <AccelStepper.h>

AccelStepper xStepper(AccelStepper::DRIVER, 2, 3);  // X-Achse
AccelStepper yStepper(AccelStepper::DRIVER, 4, 5);  // Y-Achse

void setup() {
  xStepper.setMaxSpeed(2000.0);  // Max. Geschwindigkeit in Schritten pro Sekunde
  xStepper.setAcceleration(1000.0);  // Beschleunigung in Schritten pro Sekunde^2

  yStepper.setMaxSpeed(2000.0);
  yStepper.setAcceleration(1000.0);
}

void loop() {
  // Beispiel: Gehe zu den Koordinaten (100, 200)
  xStepper.moveTo(100);
  yStepper.moveTo(200);

  // Bewegung starten
  xStepper.run();
  yStepper.run();

  // Prüfen, ob die Bewegung abgeschlossen ist
  if (xStepper.distanceToGo() == 0 && yStepper.distanceToGo() == 0) {
    // Die Bewegung ist abgeschlossen
    // Fügen Sie hier Ihren Code für den nächsten Schachzug ein
  }
}
