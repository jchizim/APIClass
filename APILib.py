import requests
import logging
import robot.libraries.BuiltIn


class APILib(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, use_certs=False):
        self.session = requests.Session()
        self.session.verify = use_certs
        self.resp = ''

    def open_uri(self, uri, payload ,method = 'GET'):
        '''
        :param uri:
        :param payload:
        :param method:
        :return:
        '''
        logging.info("Payload = {0}".format(payload))
        if method == 'POST':
            try:
                r = self.session.post(uri, json=payload)
            except Exception as e:
                logging.error("{0} Failed".format(uri))
        logging.info("Response = {0}".format(r.json()))
        self.resp = r.json()
        return r.json(), r.status_code

    def validate(self, expecting_response):
        # logging.info(self.resp)
        if expecting_response:
            try:
                # response = str(self.resp['Error'])
                if str(expecting_response) in str(self.resp):
                    logging.info("Validation succeeded ")
                    return True
                else:
                    # logging.info(expecting_response)
                    # logging.info(self.resp['Error'])
                    logging.error("Validation failed")
                    return False
            except:
                logging.error("Failed")

    def update_headers(self, headers):
        # 'Accept-encoding': 'gzip'
        self.session.headers.update(headers)