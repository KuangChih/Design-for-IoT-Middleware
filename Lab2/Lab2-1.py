void setup() {
    Serial.begin(9600);
}
void loop() {
    if (Serial.available() > 0) {
        int c = Serial.read();
        Serial.print("I received: ");
        Serial.println(c);
    }
}
