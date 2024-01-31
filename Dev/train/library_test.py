import threading
import time

class MinhaThread(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        print(f"Tarefa {self.nome} iniciada")
        time.sleep(5)
        print(f"Tarefa {self.nome} concluída")

for i in range(10):
    thread = MinhaThread(f"T{i + 1}")
    thread.start()
thread.join()
