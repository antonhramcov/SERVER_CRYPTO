from flask import Flask
from models import calc_characteristics

app = Flask(__name__)

# Получение инфорамции об отслеживаемых криптовалютных парах
# http://127.0.0.1:5000/symbols/list
@app.route('/symbols/list', methods = ['GET'])
def get_list_symbols():
    with open("symbols.txt", "r") as f:
        symbols = list(map(lambda x: x.rstrip(), f.readlines()))
    return symbols

# Добавление новой криптовалютной пары
# http://127.0.0.1:5000/symbols/add=<symbol>
@app.route('/symbols/add=<symbol>', methods = ['GET'])
def add_symbol(symbol):
    with open("symbols.txt", "r") as f:
        symbols = list(map(lambda x: x.rstrip(), f.readlines()))
    if symbol.upper()+'/USDT' not in symbols:
        with open("symbols.txt", "a") as f:
            f.write(symbol.upper()+'/USDT'+'\n')
        with open("symbols.txt", "r") as f:
            symbols = list(map(lambda x: x.rstrip(), f.readlines()))
        return symbols
    else:
        return f'{symbol.upper()} has already'

# Удаление криптовалютной пары
# http://127.0.0.1:5000/symbols/del=<symbol>
@app.route('/symbols/del=<symbol>', methods = ['GET'])
def del_symbol(symbol):
    with open("symbols.txt", "r") as f:
        symbols = list(map(lambda x: x.rstrip(), f.readlines()))
    if symbol.upper()+'/USDT' in symbols:
        symbols.remove(symbol.upper()+'/USDT')
        with open("symbols.txt", "w") as f:
            for s in symbols:
                f.writelines(s+'\n')
        return 'Succes'
    else:
        return f'{symbol.upper()} not found'

# Получение информации обо всех отслеживаемых валютных парах
# http://127.0.0.1:5000/info
@app.route('/info', methods = ['GET'])
def info():
    return calc_characteristics()

app.run(debug=True)
