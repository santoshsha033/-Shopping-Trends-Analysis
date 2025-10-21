const int trigPin = 2;
const int echoPin = 3;
long duration;
int distance;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //pinMode(pin, output/input): specify pin to behave either as an input/output
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //digitalWrite(pinNo., high/low ):will enable(high) or disable(low) on pin 
  digitalWrite(trigPin, LOW);
  //digitalMicroseconds(int): pauses the program for the amount of time in (microseconds) specified by a parameter
  digitalMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  digitalMicroseconds(10);
  digitalWrite(trigPin, LOW);
  //pulseIn(pinNo., high/low): inbuilt function read a pulse on a pin high/low 
  duration = pulseIn(echoPin, HIGH);
  //calculating distance
  distance = duration * 0.034 / 2;
  //print the data to serial port
  Serial.print("distance:" + distance + "cm");
  delay(10);
}
