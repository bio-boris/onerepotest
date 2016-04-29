#BEGIN_HEADER
import time
import os
from kbaseclients.GenericClient import GenericClient
#END_HEADER


class onerepotest:
    '''
    Module Name:
    onerepotest

    Module Description:
    A KBase module: onerepotest
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/kbaseIncubator/onerepotest"
    GIT_COMMIT_HASH = "8c95a02912fa9b287bece9d7509872f0988e3269"
    
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.deploy_config = config
        #END_CONSTRUCTOR
        pass
    

    def send_data(self, ctx, params):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN send_data
        user = ctx['user_id']
        returnVal = {'params': params, 'user': user}
        #END send_data

        # At some point might do deeper type checking...
        if not isinstance(returnVal, object):
            raise ValueError('Method send_data return value ' +
                             'returnVal is not type object as required.')
        # return the results
        return [returnVal]

    def print_lines(self, ctx, text):
        # ctx is the context object
        # return variables are: number_of_lines
        #BEGIN print_lines
        number_of_lines = 0
        for line in text.split("\n"):
            print("[" + line.rstrip() + "]")
            number_of_lines += 1
            time.sleep(5)
        #END print_lines

        # At some point might do deeper type checking...
        if not isinstance(number_of_lines, int):
            raise ValueError('Method print_lines return value ' +
                             'number_of_lines is not type int as required.')
        # return the results
        return [number_of_lines]

    def generate_error(self, ctx, error):
        # ctx is the context object
        #BEGIN generate_error
        print("Preparing to generate an error...")
        raise ValueError(error)
        #END generate_error
        pass

    def get_deploy_config(self, ctx):
        # ctx is the context object
        # return variables are: config
        #BEGIN get_deploy_config
        config = self.deploy_config
        #END get_deploy_config

        # At some point might do deeper type checking...
        if not isinstance(config, dict):
            raise ValueError('Method get_deploy_config return value ' +
                             'config is not type dict as required.')
        # return the results
        return [config]

    def list_ref_data(self, ctx, ref_data_path):
        # ctx is the context object
        # return variables are: files
        #BEGIN list_ref_data
        files = os.listdir(ref_data_path)
        #END list_ref_data

        # At some point might do deeper type checking...
        if not isinstance(files, list):
            raise ValueError('Method list_ref_data return value ' +
                             'files is not type list as required.')
        # return the results
        return [files]

    def local_sdk_callback(self, ctx, params):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN local_sdk_callback
        callback_url = os.environ['SDK_CALLBACK_URL']
        cl = GenericClient(callback_url, use_url_lookup=False)
        returnVal = cl.sync_call("kb_read_library_to_file.convert_read_library_to_file", [params],
                                 json_rpc_context = {"service_ver": "dev"})[0]
        #END local_sdk_callback

        # At some point might do deeper type checking...
        if not isinstance(returnVal, object):
            raise ValueError('Method local_sdk_callback return value ' +
                             'returnVal is not type object as required.')
        # return the results
        return [returnVal]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
