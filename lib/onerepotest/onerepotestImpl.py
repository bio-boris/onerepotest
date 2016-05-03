#BEGIN_HEADER
import time
import os
import shutil
import json
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
    GIT_COMMIT_HASH = "0888ef46787df9e8d0335be4265c29d65e38c1cb"
    
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

    def local_sdk_callback(self, ctx, input):
        # ctx is the context object
        # return variables are: output, state
        #BEGIN local_sdk_callback
        dir_path = "/kb/module/work/tmp/"
        input_fn = "input.txt"
        f = open(dir_path + input_fn, 'w')
        f.write(input)
        f.close()
        output_fn = "output.txt"
        callback_url = os.environ['SDK_CALLBACK_URL']
        cl = GenericClient(callback_url, use_url_lookup=False)
        state = cl.sync_call("onerepotest.copy_scratch_file", [input_fn, output_fn],
                             json_rpc_context = {"service_ver": "dev"})[0]
        f = open(dir_path + output_fn, 'r')
        output = f.read()
        f.close()
        #END local_sdk_callback

        # At some point might do deeper type checking...
        if not isinstance(output, basestring):
            raise ValueError('Method local_sdk_callback return value ' +
                             'output is not type basestring as required.')
        if not isinstance(state, basestring):
            raise ValueError('Method local_sdk_callback return value ' +
                             'state is not type basestring as required.')
        # return the results
        return [output, state]

    def copy_scratch_file(self, ctx, input_file_name, output_file_name):
        # ctx is the context object
        # return variables are: state
        #BEGIN copy_scratch_file
        dir_path = "/kb/module/work/tmp/"
        shutil.copy(dir_path + input_file_name, dir_path + output_file_name)
        state = "OK"
        #END copy_scratch_file

        # At some point might do deeper type checking...
        if not isinstance(state, basestring):
            raise ValueError('Method copy_scratch_file return value ' +
                             'state is not type basestring as required.')
        # return the results
        return [state]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
