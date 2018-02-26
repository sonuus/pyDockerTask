import boto3
import os
import sys
import json
from flask import request, Response,jsonify,Flask

# # Create the Flask app
#application = flask.Flask(__name__)
app = Flask(__name__)

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') if os.environ.get('AWS_ACCESS_KEY_ID') is not None else None
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') if os.environ.get('AWS_SECRET_ACCESS_KEY') is not None else None

@app.route('/')
def hello_world():    
    return "Helllllll ^&^&6767676767 changed code in branch 2"


@app.route('/xxx')
def get_s3_buckets():
    s3 = boto3.resource('s3')
    # Print out bucket names
    lst=[]
    for bucket in s3.buckets.all():
        print(bucket.name)
        lst.append(bucket.name + "  777777777")
    return jsonify({'buckets':lst})
    

@app.route('/api')
def rest_hello_world():
    return '{"id":1,"message":"Flask: Hello World from Docker"}'



# from boto3 import dynamodb
# from boto3.dynamodb.table import Table

# from boto3.dynamodb.items import Item
# from boto3.dynamodb.fields import HashKey
# from boto3.dynamodb.exceptions import ConditionalCheckFailedException
# from boto3.exceptions import JSONResponseError






# # Default config vals
# THEME = 'default' if os.environ.get('THEME') is None else os.environ.get('THEME')
# FLASK_DEBUG = 'false' if os.environ.get('FLASK_DEBUG') is None else os.environ.get('FLASK_DEBUG')


# # Load config values specified above
# application.config.from_object(__name__)

# # Load configuration vals from a file
# application.config.from_pyfile('application.config', silent=True)

# # Only enable Flask debugging if an env var is set to true
# application.debug = application.config['FLASK_DEBUG'] in ['true', 'True']

# # Connect to DynamoDB and get ref to Table
# ddb_conn = dynamodb2.connect_to_region(application.config['AWS_REGION'])
# ddb_table = Table(table_name=application.config['STARTUP_SIGNUP_TABLE'],
#                   connection=ddb_conn)

# @application.route('/')
# def welcome():
#     theme = application.config['THEME']
#     return flask.render_template('index.html', theme=theme, flask_debug=application.debug)


# @application.route('/signup', methods=['POST'])
# def signup():
#     signup_data = dict()
#     for item in request.form:
#         signup_data[item] = request.form[item]

#     try:
#         store_in_dynamo(signup_data)
#     except ConditionalCheckFailedException:
#         return Response("", status=409, mimetype='application/json')

#     return Response(json.dumps(signup_data), status=201, mimetype='application/json')


# def store_in_dynamo(signup_data):
#     signup_item = Item(ddb_table, data=signup_data)
#     signup_item.save()


# def create_table():
#     signups = Table.create(application.config['STARTUP_SIGNUP_TABLE'], 
#         schema=[
#             HashKey('email') # defaults to STRING data_type
#         ], 
#         throughput={
#             'read': 1,
#             'write': 1,
#         },
#         connection=ddb_conn
#     )


# def init_db():
#     try:
#         ddb_table.describe()
#     except JSONResponseError:
#         print ("DynamoDB table doesn't exist, creating...")
#         create_table()

if __name__ == '__main__':
    # init_db()
    app.run(debug=True, host='0.0.0.0',port=80)









