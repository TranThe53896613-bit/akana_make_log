import datetime
import os

import actions


class AddLog:
    def __init__(self, file, action, obj, actor="ADMIN"):
        self.file = 'logs/' + file + '.log'
        self.actor = actor
        self.action = actions.get_action_name(action)
        self.obj = obj
        self.now = datetime.datetime.now()
        self.log = f"[on {self.now}]-[{self.actor}]: {self.action} {self.obj}\n"
        self.save_log()

    def save_log(self):
        if not os.path.exists('logs/'):
            os.system('mkdir logs')

        with open(self.file, 'a') as logs:
            logs.write(self.log)

    def __str__(self):
        return self.log


def main():
    log = AddLog('old_log', actions.DELETE, 'all files', "Huzaifa")
    print(log)


if __name__ == '__main__':
    main()
