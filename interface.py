from modules import speech


class Interface:

    def __init__(self):
        self._s = speech.Speech("mirror mirror on the wall", "thank you mirror")
    
    def authenticate(self):
        while not self._s.check_launch_phrase():
            self._s.speak()
        print("You gained access")

    def decide_action(self):
        self._s.speak()
        print("decide action")


if __name__ == "__main__":
    interface = Interface()
    interface.start()
