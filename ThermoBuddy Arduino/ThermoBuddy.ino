const int sensorPin = A0;  // Temperature sensor pin
const int ledPins[] = {2, 3, 4};  // Example LED pins

void setup() {
  Serial.begin(9600);  
  // Initialize LED pins
  for (int i = 0; i < 3; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  // Read raw sensor data
  int sensorVal = analogRead(sensorPin);  
  
 
  Serial.println(sensorVal);  

 
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');  
    Serial.print("Received command from ROS2: ");
    Serial.println(command);  
    processCommand(command);  
  }

  delay(1000);  // Wait for 1000ms before sending the next value
}

// Function to handle LED control based on ROS2 commands
void processCommand(String command) {
  Serial.print("Received command: ");
  Serial.println(command);  

  if (command == "COLD") {
    Serial.println("LEDs are OFF");
    // Turn off all LEDs
    digitalWrite(ledPins[0], HIGH);
    digitalWrite(ledPins[1], LOW);
    digitalWrite(ledPins[2], LOW);
    
  } else if (command == "WARM") {
    Serial.println("LEDs are LOW");
    // Turn on one LED (LOW state)
    //digitalWrite(ledPins[0], HIGH);  // First LED on
     digitalWrite(ledPins[0], LOW);
    digitalWrite(ledPins[1], HIGH);
    digitalWrite(ledPins[2], LOW);
    //digitalWrite(ledPins[2], LOW);
  } else if (command == "HOT") {
    Serial.println("LEDs are HIGH");
    // Turn on all LEDs (HIGH state)

    digitalWrite(ledPins[0], LOW);
    digitalWrite(ledPins[1], LOW);
    digitalWrite(ledPins[2], HIGH);
    
  } else {
    Serial.println("Unrecognized command");
  }
}
