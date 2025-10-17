def forward():
    print("Робот едет вперед")

def backward():
    print("Робот едет назад")

def turn_left():
    print("Робот поворачивает налево")

def turn_right():
    print("Робот поворачивает направо")

def stop():
    print("Робот остановился")

def  smoothly():
    print("Робот едет плавно")
	
print("Управление:")
print("w-вперёд")
print("s-назад")
print("a-налево")
print("d-направо")
print("q-стоп")
print("e-робот едет плавно")
while True:
    command = input("Введите команду: ")

    if command == "w":
        forward()
    elif command == "s":
        backward()
    elif command == "a":
        turn_left()
    elif command == "d":
        turn_right()
    elif command == "q":
        stop()
    elif comand == "e":
	    smoothly()
