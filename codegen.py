import uuid # from http://zesty.ca/python/uuid.html
import base64


def fetch_code():
    b64uid = '0000'


    uid = uuid.uuid4()
    b64uid = base64.b64encode(uid.bytes,'-_')

    code = b64uid[0:2]
    return "_" + code
