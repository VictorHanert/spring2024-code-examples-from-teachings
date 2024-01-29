def message(name):
    if name == 'Victor'.lower():
        print('Hi ' + str(name))
    elif type(name) == str:
        print('Hello ' + str(name))
    else:
        print('Not a name')

message('victor')
message('Bob')
message(1234)
message(1.2)
message(True)
