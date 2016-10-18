void setup() {
    pinMode(2, INPUT);
    pinMode(11, OUTPUT); //pin 11 for the Led R on board
    pinMode(12, OUTPUT); //pin 12 for the Led G on board
    pinMode(13, OUTPUT); //pin 13 for the Led B on board
}
void loop() {
    int touchPadState = digitalRead(2);
    if (touchPadState == HIGH) { //touched
        digitalWrite(11, HIGH);
        digitalWrite(12, LOW);
        digitalWrite(13, LOW);
    } else {
        digitalWrite(11, LOW);
        digitalWrite(12, HIGH);
        digitalWrite(13, HIGH);
    }
}
