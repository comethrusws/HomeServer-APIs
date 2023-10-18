from flask import Flask, request, jsonify, send_file, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_extended_jwt import JWTManager, create_access_token, jwt_required, get_jwt_identity

app=Flask(__name__)
app.config.from_object('config.Config')
db= SQLAlchemy(app)
bcrypt= Bcrypt(app)
CORS(app)
jwt = JWTManager(app)

#nowsince we're done impirting stuff and laying a framework, imma define a user-model

#User Model
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(120), unique=True, nullable=False)
    password= db.Column(db.String(60), nullable=False)

#now, Moving on to user registration and other parts;

#Endpoint for User reg
@app.route('/register',methods=['POST'])
def register():
    data= request.get_json()
    hashed_password= bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user=User(username=data['username'],password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User Registered Succesfully'})

#Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data= request.get_json()
    user=User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token=create_access_token(identity=user.id)
    
    return jsonify({'message':'Invalid Login Details! Try Again...'}, 401)

#Endpoint for file upload
@app.route('/upload', methods=['POST'])
@jwt_required()
def upload_file(): 
    uploaded_file=request.files['file']
    if uploaded_file:
        file_path=os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)
        return jsonify({'message':'Files Uploaded Successfully!'})
    

#Endpoint for file download
@app.route('/download/<filename>', methods=['GET'])
@jwt_required()
def dowmload_file(filename):
    file_path=os.path.joint(app.config['UPLOAD_FOLDER'], filename)
    try:
        response= make_response(send_file(file_path))
        response.headers["Content-Disposition"]=f"attachment;filename=(filename)"
        return response
    except FileNotFoundError:
        return jsonify({'message':'File Not Found!'}, 404)


#initialising db schema based on the models i defined earlier   
if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=80)

#note:the host address makes this api accesibe from any interface on my homeserver(since its obvious u would want to transfer files from multiple external devices)


    

