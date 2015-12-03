#BEGIN_HEADER
import time
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
