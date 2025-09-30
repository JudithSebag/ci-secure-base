from flask import Flask
app = Flask(_name_)


@app.route('/')
def hello():
    return "Hello from Flask!"


if _name_ == '_main_':
    app.run(host='0.0.0.0', port=3000)


# Version erreur

# import os
# from flask import Flask, request
# app = Flask(_name_)

# @app.route('/')
# def hello():
#     return "Hello from Flask!"

# @app.route('/ping')
# def ping():
#     # Vulnérabilité : Commande système basée sur l'entrée utilisateur
#     host = request.args.get('host', '127.0.0.1')
#     os.system(f"ping -c 1 {host}")  # Command injection possible
#     return f"Pinging {host}"

# if _name_ == '_main_':
#     app.run(host='0.0.0.0', port=3000)