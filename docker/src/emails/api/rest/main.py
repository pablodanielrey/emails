import logging
logging.getLogger().setLevel(logging.INFO)
import sys
from flask import Flask, abort, make_response, jsonify, url_for, request, json, send_from_directory
from emails.model import EMailsModel
from flask_jsontools import jsonapi

from rest_utils import register_encoder

app = Flask(__name__)
register_encoder(app)

@app.route('/emails/api/v1.0/correos/', methods=['OPTIONS'])
@app.route('/emails/api/v1.0/correos/<mid>', methods=['OPTIONS'])
@app.route('/emails/api/v1.0/enviar_correo', methods=['OPTIONS'])
@app.route('/emails/api/v1.0/enviar_pendientes', methods=['OPTIONS'])
def options(mid=None):
    '''
        para autorizar el CORS
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
    '''
    print(request.headers)
    o = request.headers.get('Origin')
    rm = request.headers.get('Access-Control-Request-Method')
    rh = request.headers.get('Access-Control-Request-Headers')

    r = make_response()
    r.headers[''] = 'PUT,POST,GET,HEAD,DELETE'
    r.headers['Access-Control-Allow-Methods'] = 'PUT,POST,GET,HEAD,DELETE'
    r.headers['Access-Control-Allow-Origin'] = '*'
    r.headers['Access-Control-Allow-Headers'] = rh
    r.headers['Access-Control-Max-Age'] = 1
    return r

@app.route('/emails/api/v1.0/correos/', methods=['GET'], defaults={'mid':None})
@app.route('/emails/api/v1.0/correos/<mid>', methods=['GET'])
@jsonapi
def correos(mid):
    offset = request.args.get('offset',None,int)
    limit = request.args.get('limit',None,int)
    solo_pendientes = request.args.get('p',False,bool)
    if not mid:
        return EMailsModel.correos(solo_pendientes=solo_pendientes, offset=offset, limit=limit)
    else:
        ms = EMailsModel.correos(mid=mid, solo_pendientes=False)
        return None if len(ms) == 0 else ms[0]

@app.route('/emails/api/v1.0/enviar_correo', methods=['PUT','POST'])
@jsonapi
def enviar_correo():
    print(request.data)
    datos = json.loads(request.data)
    print(datos)
    de = datos['de']
    assert de is not None
    para = datos['para']
    assert para is not None
    asunto = datos['asunto']
    assert asunto is not None
    cuerpo = datos['cuerpo']
    assert cuerpo is not None
    EMailsModel.enviar_correo(de, para, asunto, cuerpo)


@app.route('/emails/api/v1.0/enviar_pendientes', methods=['GET'])
@jsonapi
def enviar_pendientes():
    r = EMailsModel.enviar_correos_pendientes()
    print(r)
    return r

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'

    r.headers['Access-Control-Allow-Origin'] = '*'
    return r

def main():
    app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == '__main__':
    main()
