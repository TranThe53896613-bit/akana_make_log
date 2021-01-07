"""
Author : kalculata

by default logs all saved in the folder logs/, but you can change it in the code

"""
import datetime
import os

import actions


class AddLog:
    """create log and save logs
    :param [main_folder] : the main folder for you logs
    :param [file]   : name of your file for logs
    :param [action] : action
    :param [actor]  : who did the action
    :param [object] : object of the action
    :return log
    """

    def __init__(self, **kwargs):
        try:
            self.main_folder = kwargs['main_folder']
            self.file = self.main_folder + '/' + kwargs['file'] + '.log'
            self.actor = kwargs['actor']
            self.action = actions.get_action_name(kwargs['action'])
            self.object = kwargs['object']
            self.now = datetime.datetime.now()
            self.log = f"[on {self.now}]-[{self.actor}]: {self.action} {self.object}\n"
            self.save_log()

        except KeyError:
            self.log = ""
            print('Please, specify all required args: file, action, object, actor')

    def save_log(self):
        """To save log in logs/+file+.log"""

        # make sure if folder named logs exists
        if not os.path.exists(self.main_folder):
            os.system(f'mkdir {self.main_folder}')

        with open(self.file, 'a') as logs:
            logs.write(self.log)
            return self.log

    def __str__(self):
        return self.log
