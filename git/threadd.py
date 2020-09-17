from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):  # le mot clef Thread transforme le classe en processus
    def run(self):
        for i in range(5):
            print("hi!!!")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)  # on endors les le processeur pour empecher les colisions
t2.start()

t1.join()  # la methode {join()} empeche le "__main__" de s'executer eg: print("bye!!")
t2.join()  # t1 et t2 s'execute tous avant que bye s'affiche donc le main

print("bye!!!")


