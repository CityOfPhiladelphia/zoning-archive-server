from flask import Flask, jsonify
from flask.ext.cors import CORS
from json import dumps as json_dumps
import cx_Oracle
from config import DSN, DOCS_SELECT
# DEV
import sys
from pprint import pprint

app = Flask(__name__)
CORS(app)

db = cx_Oracle.connect(DSN)
c = db.cursor()
stmt = c.prepare(DOCS_SELECT)

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + "".join(x.title() for x in components[1:])

def get_rows_as_dicts():
    global c
    colnames = [i[0].lower() for i in c.description]
    return [dict(zip(colnames, row)) for row in c]

def get_documents_from_db(address):
    global c
    c.execute(None, address=address)
    return get_rows_as_dicts()

@app.route('/address/<address>/documents/')
def get_documents(address):
    docs = get_documents_from_db(address)
    docs = [{to_camel_case(key): value for key, value in doc.iteritems()} \
        for doc in docs]
    resp = {
        'inputAddress': address,
        'documents': docs,
    }
    return jsonify(resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
