import eel

eel.init('web')
print('1')
@eel.expose
def rec_data(login, password):
    print('2')
    return print(login, password)

eel.start('index.html', size=(500, 500))

