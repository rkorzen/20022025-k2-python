import sys

def check_module_name(name: str) -> bool:
    return name in sys.stdlib_module_names


print(check_module_name("random"))

# Jakis sposob na radzenie sobie z problemem nazwania biblioteki tak jak biblioteka z biblioteki standardowej
# badza zainstalowany modul
#
# print(sys.path)
#
# mypaths = sys.path[:1]
#
# for p in mypaths:
#     sys.path.remove(p)
#
# sys.path.extend(mypaths)
#
#
# print(sys.path)


# from config import Settings
# import config
# import random

from random import randint
from config import randint as myrandint, Settings

from mypackage import mymodule1
from mypackage import mymodule2

print(dir(mymodule1))

class MyApp:

    def __init__(self, config):
        self.config = config

    def run(self):
        print("Uruchamiam aplikację...")
        # print(random.randint(1, 100))
        # print(config.randint(1, 100))
        print(randint(400, 500))
app = MyApp(config=Settings())
app.run()