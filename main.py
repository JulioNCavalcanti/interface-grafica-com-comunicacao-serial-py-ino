import tkinter as tk
import serial
import time

def enviar_para_arduino():
    try:
        dado = entrada_texto.get()
        ser.write(dado.encode())
        print(f"Dado enviado para o Arduino: {dado}")

        # Aguarda a resposta do Arduino
        time.sleep(1)  # Aguarda 1 segundo para garantir que o Arduino teve tempo de processar
        resposta = ser.readline().decode().strip()
        print(f"Resposta do Arduino: {resposta}")

        # Exibe a resposta na interface gráfica
        label_resposta.config(text=f"Resposta do Arduino: {resposta}")

    except Exception as e:
        print(f"Erro ao comunicar com o Arduino: {e}")

# Configuração da comunicação serial
ser = serial.Serial('COM3', 9600, timeout=1)

# Cria a janela
root = tk.Tk()
root.title("Comunicação Python-Arduino")

# Configura para abrir em tela cheia
root.attributes('-fullscreen', True)

# Cria a entrada para o texto
entrada_texto = tk.Entry(root, width=100)
entrada_texto.pack(pady=10)

# Cria o botão para enviar
botao_enviar = tk.Button(root, text="Enviar para Arduino", command=enviar_para_arduino)
botao_enviar.pack()

# Cria uma etiqueta para mostrar a resposta do Arduino
label_resposta = tk.Label(root, text="")
label_resposta.pack(pady=10)

# Inicia o loop principal
root.mainloop()

# Fecha a porta serial ao encerrar o programa
ser.close()
