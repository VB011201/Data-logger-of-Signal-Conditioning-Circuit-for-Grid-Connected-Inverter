int led_pin=13;
void setup() {
pinMode(led_pin,OUTPUT);
Serial.begin(115200);
}
void loop()
{
digitalWrite(led_pin,HIGH);
Serial.println("Signal 200");
delay(500);
digitalWrite(led_pin,LOW);
Serial.println("Signal 100");
delay(500);
}
