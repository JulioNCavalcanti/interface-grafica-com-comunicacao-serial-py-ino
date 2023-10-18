void setup() {
  Serial.begin(9600); // Inicia a comunicação serial
}

void loop() {
  if (Serial.available() > 0) {
    char dado = Serial.read(); // Lê um caractere da porta serial

    if (dado == 'A') {
      Serial.println("Executar algoritmo na mão para a letra A");
    } else if (dado == 'B') {
      Serial.println("Executar algoritmo na mão para a letra C");
    } else if (dado == 'D') {
      Serial.println("Executar algoritmo na mão para a letra D");
    }
  }
}
