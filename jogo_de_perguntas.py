import os
import time
import random
import threading

class JogoDePerguntas:
    def __init__(self, tempo_inicial=8, tempo_minimo=2):
        self.tempo_limite = tempo_inicial
        self.tempo_minimo = tempo_minimo
        self.perguntas = {
            "Qual é a capital da França?": "Paris",
            "Qual é a capital da Itália?": "Roma",
            "Qual é a capital da Espanha?": "Madri",
            "Qual é a capital da Alemanha?": "Berlim",
            "Qual é a capital do Brasil?": "Brasilia"
        }
        self.resposta = None

    def pegar_resposta(self, pergunta):
        print("Bem-vindo ao Jogo de Perguntas! Você tem {} segundos para responder cada pergunta.".format(self.tempo_limite))
        self.resposta = input(pergunta + " ")

    def jogar(self):
        perguntas = list(self.perguntas.keys())
        random.shuffle(perguntas)

        for pergunta in perguntas:
            self.resposta = None
            thread = threading.Thread(target=self.pegar_resposta, args=(pergunta,))
            thread.start()

            thread.join(self.tempo_limite)

            if thread.is_alive():
                print("\nTempo esgotado! Você perdeu.")
                return

            if self.resposta.strip().lower() == self.perguntas[pergunta].lower():
                print("Resposta correta!")
                time.sleep(1)
                # Limpa a tela para a próxima pergunta
                os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para a próxima pergunta

                # DIMINUI O TEMPO AQUI
                self.tempo_limite = max(self.tempo_minimo, self.tempo_limite - 1)
            else:
                print("Resposta incorreta! Fim de jogo.")
                return

            time.sleep(1)

        print("Parabéns! Você venceu o jogo!")

if __name__ == "__main__":
    jogo = JogoDePerguntas(tempo_inicial=30, tempo_minimo=10)
    jogo.jogar()