int pinTemp = A1;  

void setup() {
  pinMode.begin(AO,O);
  Serial.begin(9600);     
}
void loop() {
  int temp = analogRead(pinTemp);   
  temp = temp * 0.48828125; 
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println("C");  
  delay(1000);  
}

void setup() {
  
}
