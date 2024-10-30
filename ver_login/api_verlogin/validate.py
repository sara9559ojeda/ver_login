import jwt
import os
from flask import request, jsonify
from validate import encrypt, decrypt  

jwt_secret_key = os.getenv('AUTH_JW_SECRET_KEY')

def create_jwt(data):
    payload = {
        'id': data.get('id'),
        'user': data.get('user')
    }
    token = jwt.encode(payload, jwt_secret_key, algorithm="HS256")
    return token

def validate_jwt():
    
    encrypted_token = request.headers.get('Authorization')
    
    if not encrypted_token:
        return jsonify({'msn': 'Token invalido'}), 401

    try:
        
        token = decrypt(encrypted_token)
        token = token.replace('Bearer ', '')
        
        
        payload = jwt.decode(token, jwt_secret_key, algorithms=["HS256"])
        print(payload['id'], payload['user'])

    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return jsonify({'msn': 'Token invalido'}), 401

    return None  