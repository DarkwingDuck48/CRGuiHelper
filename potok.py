from threading import Thread
from time import sleep


class MyThread(Thread):

    def __init__(self, text):
        Thread.__init__(self)
        self.text = text

    def run(self):
        for i in range(20):
            print(self.text)
            sleep(0.222)

c = MyThread("Main")
b = MyThread("Daemon")
b.setDaemon(True)
c.start()
b.start()
c.join()  # дождаться завершения потока в основном потоке
print("finish")
