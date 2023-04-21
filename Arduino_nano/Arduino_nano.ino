int led_pin=13;
void setup() {
pinMode(led_pin,OUTPUT);
Serial.begin(9600);
}
void loop()
{
digitalWrite(led_pin,HIGH);
Serial.println("V200");
delay(500);
digitalWrite(led_pin,LOW);
Serial.println("V100");
delay(500);
}
