/* Comentarios: 
    1- La sentencia (#Include) hace referencia a una libreria del lenguaje C.
    2- Esta libreria ofrece o permite el manejo de variedad de objetos o dispositivos a nivel de software y hardware.
    3- Las librerias de C, son documentos electronicos formados por codigos y scrips de programacion. */
/* Notacion:
    1- Led Verde-----> 1 = Pin digital (2) 
    2- Led Verde-----> 2 = Pin digital (5)
    3- Led Amarillo--> 1 = Pin digital (3)
    4- Led Amarillo--> 2 = Pin digital (6)
    5- Led Rojo------> 1 = Pin digital (4)
    6- Led Rojo------> 2 = Pin digital (7) */
// Variables
    int Valor_Infrared1 = 0;    // Estado por defecto o inicial del sensor (En espera)
    int Valor_Infrared2 = 0;
    bool Activo1        = true; // Indica si el semáforo 1 está activo, de lo contrario será el semáforo 2
    int TiempoCambio    = 2000; // Tiempo de espera entre transición de LEDs
    int TiempoEspera    = 5;    // Tiempo de espera hasta comenzar transición
    int Pausa           = 500;  // Tiempo de encendido de los semaforos segun su logica de actividad
    int Delay_Trigger   = 10;   // Tiempo de accion ciclo de disparador (Envio y Espera de señal al sensor) 10 mic/s.  
    int Tiempo;                 // Tiempo de traslacion del disparo o la onda de sonido.

// Leds y Pin 
    #define LEDVERDE1    2
    #define LEDAMARILLO1 3
    #define LEDROJO1     4
    #define LEDVERDE2    5
    #define LEDAMARILLO2 6
    #define LEDROJO2     7
// Motores
    #include <Servo.h> 
    Servo myservo;    // create servo object to control a servo
// Objetos_Alarmas y Pin
    #define trig   12 // Emisor de pulso o señal
    #define echo   11 // Receptor "del eco" del pulso o señal
    #define buzzer 13 // Zumbador
// Sensores y Pin
    #define INFRARED1 A0
// Pulsadores
    #define PULSADOR1 8
    #define PULSADOR2 9

void setup() { // Aqui definimos entradas y salidas. Sólo se activa una vez al iniciarse el programa.

  // Sensores

      //----- Modo entrada ----> Salida de los Leds Ultrasonido 1: ---------//
        pinMode(trig,   OUTPUT);   //Emisor 12
        pinMode(echo,    INPUT);   //Receptor 11
        pinMode(buzzer, OUTPUT);   //Emisor 13
      //----- Modo entrada ----> Salida de los Leds Infrarojo   1: ---------//
        pinMode(INFRARED1, INPUT); //Receptor

  // Puerto_Serial
      Serial.begin (9600);  // Iniciamos el monitor serie

  // Servo_Motor
      myservo.attach (10); // attaches the servo on pin 9 to the servo object

  // Modo entrada / salida de los Leds
      pinMode(LEDVERDE1,    OUTPUT);
      pinMode(LEDAMARILLO1, OUTPUT);
      pinMode(LEDROJO1,     OUTPUT);
      pinMode(LEDVERDE2,    OUTPUT);
      pinMode(LEDAMARILLO2, OUTPUT);
      pinMode(LEDROJO2,     OUTPUT);
      pinMode(PULSADOR1,  INPUT);
      pinMode(PULSADOR2,  INPUT);
  
  // Apagamos todos los LEDs
      digitalWrite(LEDVERDE1,    LOW);
      digitalWrite(LEDAMARILLO1, LOW);
      digitalWrite(LEDROJO1,  LOW);
      digitalWrite(LEDVERDE2, LOW);
      digitalWrite(LEDAMARILLO2, LOW);
      digitalWrite(LEDROJO2,     LOW);
  
  // Estado inicial: semáforo 1 abierto, semáforo 2 cerrado
      digitalWrite(LEDVERDE1,    HIGH);
      digitalWrite(LEDROJO2,     HIGH);
}
void loop() 
  { 
     delayMicroseconds(10);          // Tiempo de accion ciclo de disparador (Envio y Espera de señal al sensor) 10 mic/s.
     Serial.begin (9600);            // Habilita el puerto serial de la PC al ejecutar el programa.
     long Duration, Distance;        // Establecemos duration y distance como variables numéricas extensas
     digitalWrite(trig, LOW);        // Para tener un pulso limpio empezamos con 2 microsegundos en apagado
     delay(2);                       // Espera en Microsegundos
     digitalWrite(trig, HIGH);       // Mandamos un pulso de 5 microsegundos
     delay(10);                      // Espera en Microsegundos
     digitalWrite(trig, LOW);        // Apagamos el Trigger
     Duration = pulseIn(echo, HIGH); // Medimos el tiempo que la señal tarda en volver al sensor en microsegundos
     Distance = (Duration/59);     // La distancia es el tiempo por la velocidad del sonido (343 m/s = 0.0343 cm/microseg)
     
     Serial.println(analogRead(A0)); //Sensor
     delay(1000);                               //
     Valor_Infrared1 = digitalRead (INFRARED1); //*/

  // Dependiendo del semáforo que tengamos activo
  if  (Activo1)
    //if (Distance >=500 || Distance <=0){
    // Está encendido el semáforo 1, comprobamos el pulsador 2
  {  
    /*int valor2 = digitalRead(PULSADOR2); <----- OJO ESTE CODIGO  ES EL ORIGINAL creado inicialmente para boton o pulsador*/ 

    int Valor_Infrared1 = digitalRead (INFRARED1); 
    if (Valor_Infrared1 == LOW)        /*OJO ESTE CODIGO ES NUEVO DE PRUEBA SENSOR*/

    // Si hay un coche esperando, pulsador pulsado
    //if (Valor_Infrared2 == HIGH)
    }
    else
    {  
      // Encender semáforo 2
      ecenderSemaforo2();
      myservo.write(0);
      delay(Pausa);
      myservo.write(0);
      // Semáforo 2 activo
      Activo1 = false;
    }
    //if (Distance <= 10 && Distance >=1){
    // Está encendido el semáforo 1, comprobamos el pulsador 1
    //int valor1 = digitalRead(PULSADOR1);

    int Valor_Infrared1 = digitalRead (INFRARED1); 
    if (Valor_Infrared1 == LOW)        /*OJO ESTE CODIGO ES NUEVO DE PRUEBA SENSOR*/

    // Si hay un coche esperando, pulsador pulsado
    if (valor1 == HIGH)
    {
      // Encender semáforo 1
       ecenderSemaforo1();
       myservo.write(90);
       delay(Pausa);
       myservo.write(90);
      // Semáforo 1 activo*/
      Activo1 = true;
    }
  }
}
void ecenderSemaforo2()
{
  // Apagamos semáforo 1
  // Esperamos
   delay(TiempoEspera);
   noTone(buzzer);//no suena

  // Pasamos a luz amarilla
  digitalWrite(LEDVERDE1, LOW);
  digitalWrite(LEDAMARILLO1, HIGH);
  digitalWrite(LEDAMARILLO2, HIGH);
  
  // Esperamos
    delay(TiempoCambio);

  // Pasamos a luz roja
  digitalWrite(LEDAMARILLO1, LOW);
  digitalWrite(LEDAMARILLO2, LOW);

  tone (buzzer, 1000); //Suena el zumbador con una frecuencia de 1000Hz
  digitalWrite(LEDROJO1, HIGH);
  
  
  // Encendemos semáforo 2
  // Esperamos
  delay(TiempoCambio);
 
  // Pasamos a luz amarilla
  digitalWrite(LEDROJO2, LOW);
  digitalWrite(LEDAMARILLO2, HIGH);
  digitalWrite(LEDAMARILLO1, HIGH);
  
  // Esperamos
    delay(TiempoCambio);
    digitalWrite(LEDAMARILLO2, LOW);
    digitalWrite(LEDAMARILLO1, LOW);

  // Pasamos a luz roja
  digitalWrite(LEDVERDE2, HIGH);
}

void ecenderSemaforo1()
{
  // Apagamos semáforo 2
  // Esperamos
    delay(TiempoEspera);
    noTone(buzzer);//no suena

  // Pasamos a luz amarilla
  digitalWrite(LEDVERDE2, LOW);
  digitalWrite(LEDAMARILLO2, HIGH);
  digitalWrite(LEDAMARILLO1, HIGH);
 
  // Esperamos
    delay(TiempoCambio);

  // Pasamos a luz roja
  digitalWrite(LEDAMARILLO2, LOW);
  digitalWrite(LEDAMARILLO1, LOW);
  //tone (buzzer, 1000); //Suena el zumbador con una frecuencia de 1000Hz
  digitalWrite(LEDROJO2, HIGH);
 
  // Encendemos semáforo 1
  // Esperamos
     delay(TiempoCambio);

  digitalWrite(LEDAMARILLO2, HIGH); 
  digitalWrite(LEDAMARILLO1, HIGH); 

  // Pasamos a luz amarilla
  digitalWrite(LEDROJO1, LOW);

  digitalWrite(LEDAMARILLO2, LOW); 
  digitalWrite(LEDAMARILLO1, LOW); 

  digitalWrite(LEDVERDE1, HIGH);
}
