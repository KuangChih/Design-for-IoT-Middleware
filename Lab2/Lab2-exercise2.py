void setup() {
    pinMode(11, OUTPUT); //pin 11 for the Led R on board
    pinMode(12, OUTPUT); //pin 12 for the Led G on board
    pinMode(13, OUTPUT); //pin 13 for the Led B on board
}
void loop() {
    int sensorValue=analogRead(A0);
    delay(1);
    if(sensorValue<0.25){
        digitalWrite(11, LOW);
        digitalWrite(12, LOW);
        digitalWrite(13, LOW);
    }else if(sensorValue<0.5){
        digitalWrite(11, HIGH);
        digitalWrite(12, LOW);
        digitalWrite(13, LOW);
    }else if(sensorValue<0.75){
        digitalWrite(11, HIGH);
        digitalWrite(12, HIGH);
        digitalWrite(13, LOW);
    }else if(sensorValue<1){
        digitalWrite(11, HIGH);
        digitalWrite(12, HIGH);
        digitalWrite(13, HIGH);
    }
}
