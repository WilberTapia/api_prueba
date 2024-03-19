from flask import Flask, request, jsonify, make_response
import jwt
from datetime import datetime, timedelta
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Entrevista'


@app.route('/login', methods =['POST'])
def login():
    auth = request.form
  
    if not auth or not auth.get('usuario') or not auth.get('password'):
        return make_response(
            'Favor de enviar toda la informacion',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    # user = User.query\
    #     .filter_by(email = auth.get('email'))\
    #     .first()

  
    if validdar_pass('1234', auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            # 'public_id': user.public_id,
            'public_id': auth.get('usuario'),
            'exp' : datetime.utcnow() + timedelta(minutes = 100)
        }, app.config['SECRET_KEY'])
  
        return jsonify({'token' : token})
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )

# # decorator for verifying the JWT
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#         # jwt is passed in the request header
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']
#         # return 401 if token is not passed
#         if not token:
#             return jsonify({'message' : 'No estas autorizado'}), 401
  
#         try:
#             # decoding the payload to fetch the stored details
#             data = jwt.decode(token, app.config['SECRET_KEY'])
#             current_user = 'UserW'
            
#             # User.query\
#             #     .filter_by(public_id = data['public_id'])\
#             #     .first()
#         except:
#             return jsonify({
#                 'message' : 'Token is invalid !!'
#             }), 401
#         # returns the current logged in users context to the routes
#         return  f(current_user, *args, **kwargs)
  
#     return decorated

def validdar_pass(pass1, pass2):
    if(pass1 == pass2):
        return True
    

products_data = [ { 'id':1, 'name':1, 'categoria':1, 'stock': 1, 'precio': 10 },
                 { 'id':2, 'name':2, 'categoria':2, 'stock': 1, 'precio': 107 },
                  { 'id':2, 'name':2, 'categoria':3, 'stock': 0, 'precio': 1034 },
                   { 'id':2, 'name':2, 'categoria':1, 'stock': 0, 'precio': 10543 } ]

@app.route('/product', methods =['POST'])
# @token_required
def productos_filtrados():
    data = request.get_json()
    categoria = data.get('categoria')    
    preciominimo = data.get('preciominimo')

    if categoria is None:
        producto_filtrado = [products_data for _product in 
                             producto_filtrado if _product.get('categoria') == categoria]
        
    if preciominimo is None:    
        producto_filtrado = [products_data for _product in 
                        producto_filtrado if _product.get('precio') == preciominimo]
        
    producto_filtrado = [products_data for _product in 
                producto_filtrado if _product.get('precio') == preciominimo]
        
    return jsonify({'producto_filtrado': producto_filtrado})


@app.route('/entrada', methods =['POST'])
# @token_required
def another():
        another = request.form
        
        if not another or not another.get('name') or not another.get('categoria') or not another.get('stock') or not another.get('precio'):
            return make_response('Favor de enviar toda la informacion', 401)

        if not isinstance(another.get('categoria'), str):
            return make_response('Categoria no puede contener numeros', 401)

        if not isinstance(another.get('stock'), int) or not isinstance(another.get('precio'), int):
            return make_response('stock y precio no puede contener texto', 401)
        
        return make_response('Se inserto correctamente', 200)
        # Insert en base de datos









        




    
