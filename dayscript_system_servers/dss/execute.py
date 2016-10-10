#libraries
import paramiko
import os
import json


#class
class execute:
    def __init__(self,service,command,dataConection):
        self.command = command
        self.service = service
        self.dataConection = dataConection
        self.response = Array()
        self.basepath = '/root/dss/'

    def create_conexion(self):
        self.conexion = paramiko.Transport((self.dataConection.ipv4_address, self.dataConection.port))
        self.conexion.connect(username = self.dataConection.root, password = self.dataConection.password)
        self.canal = self.conexion.open_session()
        return 'ok'

    def prepare_command(self):
        if self.command == 'initial':
            self.command = { 'service mysql status','service apache2 status' }
        if self.service == 'mysql':
            self.command = " cd "+self.basepath+' && sh mysqldump.sh '+'root root '+self.command
        if self.service == 'files':
            self.command = " cd "+self.basepath+' && sh files.sh'

    def excute_command(self):
        if type(self.command) == set:
            for a in self.command:
                self.create_conexion()
                self.canal.exec_command(a)
                self.response[a.replace(" ","")] = self.canal.makefile('rb', -1).readlines()
                self.conexion.close()
        else:
            self.create_conexion()
            self.canal.exec_command(self.command)
            self.response = self.canal.makefile('rb', -1).readlines()
            self.conexion.close()
        self.dataConection.response = self.response
        return self.dataConection




class Array(dict):

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
