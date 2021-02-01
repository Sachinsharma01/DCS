int R1 = 30000;
int R2 = 7500;
void setup() {
  pinMode(A0, INPUT);
  Serial.begin(9600);

}
void loop() {
  float readA = analogRead(A0);
  float Vout = (readA * 5) / 1024;
  Serial.print("Vout ");
  Serial.println(Vout);
  float Vin = Vout * R1 / (R1 + R2);
  Serial.print("Vin ");
  Serial.println(Vin);
  delay(1000);
}
