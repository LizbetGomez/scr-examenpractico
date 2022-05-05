int boton = 13;
int activado = 1;
int desactivado = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
pinMode(boton,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
if(activado = digitalRead(boton))
  {
    Serial.println("1");//escribe 1 que es la entrada leida (5v)
  }
else if(desactivado == digitalRead(boton))
  {
    Serial.println("0");
  }
  delay(100);
}
