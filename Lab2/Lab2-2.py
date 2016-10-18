void setup() {
    pinMode(2, INPUT);
    pinMode(13, OUTPUT); //pin 13 for the Led on board
}
void loop() {
    int touchPadState = digitalRead(2);
    if (touchPadState == HIGH) { //touched
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }
}
