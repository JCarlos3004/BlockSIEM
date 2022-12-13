# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:44:21 2022

@author: Jean Carlos
"""

import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        self.chain = [] #Lista que va contener los bloques
        self.create_block(proof=1, previous_hash='0') 
    
    
    def create_block(self, proof, previous_hash):
        block = { 'index' : len(self.chain)+1,
                  'timestap' : str(datetime.datetime.now()),
                  'proof' : proof,
                  'previous_hash': previous_hash}
        #Llamamos a la cadena
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof +=1
            return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['prof']
            new_proof = block['proof']
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1 
            
        return True
    
    
#%% Paso 2 - Mirando el Blockchain


app = Flask(__name__)
blockchain = Blockchain()

#Minando un Nuevo bloque
@app.route('/mine_block', methods=['GET'])

def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message':'Felicidades, haz minado un bloque!',
                'index':block['index'],
                'timestap':block['timestap'],
                'proof':block['proof'],
                'previous_hash':block['previous_hash']}
    return jsonify(response), 200    


#%% Obteniendo Cadena completa
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

## Validando validez de cadena de bloques
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message':'Todo bien. El Blockchain es valido'}
    else:
        response = {'message':'Houston, tenemos un problema. El blockchain no es valido'}
    return jsonify(response), 200

#%% Corriendo el App
app.run(host='0.0.0.0', port='5000')