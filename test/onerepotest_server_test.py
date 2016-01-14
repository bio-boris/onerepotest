import unittest
import os
import json
import time

from os import environ
from ConfigParser import ConfigParser
from pprint import pprint

import biokbase.nexus
from biokbase.workspace.client import Workspace as workspaceService
from onerepotest.onerepotestImpl import onerepotest


class onerepotestTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        auth_client = biokbase.nexus.Client(config={'server': 'nexus.api.globusonline.org',
                'verify_ssl': True, 'client': None, 'client_secret': None})
        user, _, _ = auth_client.validate_token(token)
        cls.ctx = {'token': token, 'authenticated': 1, 'user_id': user}
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('onerepotest'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = onerepotest(cls.cfg)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_onerepotest_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def test_send_data(self):
        ret = self.getImpl().send_data(self.getContext(), {"genomeA": "myws.mygenome1", "genomeB": "myws.mygenome2"})
        self.assertEqual(len(ret[0]['params'].items()), 2)
        self.assertEqual(ret[0]['params']["genomeA"], "myws.mygenome1")

    def test_print_lines(self):
        ret = self.getImpl().print_lines(self.getContext(), "l1\nl2\nl3")
        self.assertEqual(ret[0], 3)

    def test_generate_error(self):
        with self.assertRaises(ValueError) as context:
            self.getImpl().generate_error(self.getContext(), "Super!")
        self.assertTrue("Super!" in context.exception)

    def test_get_deploy_config(self):
        ret = self.getImpl().get_deploy_config(self.getContext())
        self.assertTrue(type(ret[0]) is dict)
        self.assertTrue(ret[0]["kbase-endpoint"].startswith("http"))

    def test_list_ref_data(self):
        ret = self.getImpl().list_ref_data(self.getContext(), "/kb")
        self.assertTrue("dev_container" in ret[0])
