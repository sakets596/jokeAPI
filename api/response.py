import json
from flask import Flask, jsonify, request
# import connexion
from random import randint

# app = Flask(__name__)

# app = connexion.App(__name__, specification_dir='./api/')
# app.add_api('/Users/s0s0myx/python-projects/joke-api/api/swagger.yaml')


jokes = [{'id': 1, 'joke': "Tasty hai ki taste thik hai."},
         {'id': 2, 'joke': "he he ho ho ha ha"},
         {'id': 3, 'joke': "kujugga"},]

# @app.route('/api/alljoke', methods=['GET'])
def alljoke():
    #joke = {"joke1":"Hello, This is a joke."} #to jsonify the data need to be a dictiobary/list of dictionaries. As json also has key and value pair
    #return jsonify(jokes) #note json also has key and value so it will always jsonify dict(it has key and value)
    #return jsonify({'data': data}) # you can do somethink like this also
    return jsonify(jokes)

# @app.route('/api/randomjoke', methods=['GET'])
def randomjoke():
    len_jokes = len(jokes)
    rand_joke_index = randint(0, len_jokes-1)
    joke = jokes[rand_joke_index]
    return jsonify(joke)

# @app.route('/api/joke/<int:joke_id>', methods=['GET'])
def joke(joke_id):
    len_jokes = len(jokes)
    for i in jokes:
        if i['id'] == joke_id:
            joke = i
            return jsonify(joke)

def post_joke(joke):
    joke_count = len(jokes)
    id = joke_count + 1
    jokes.append({'id': id, 'joke': joke})
    return jsonify(jokes), 201


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=9000)

# print(post_joke("This is joke 4."))