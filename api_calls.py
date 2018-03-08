from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, world'


@app.route('/name', methods=['GET'])
def my_name(name='Gabriel'):
    return jsonify({'name': name})


@app.route('/hello/<name>', methods=['GET'])
def say_hello(name='Gabriel'):
    output = 'Hello there, {0}'.format(name)
    return jsonify({'message': output})


@app.route('/distance', methods=['POST'])
def distance():
    from math import sqrt
    r = request.get_json()
    print(r)
    print(type(r))
    sum_dist = 0
    for n, value in enumerate(r['a']):
        sum_dist += (r['a'][n] - r['b'][n])**2
    dist = sqrt(sum_dist)

    return jsonify({'distance': dist, 'a': r['a'], 'b': r['b']})
