## akana_make_log
it used to generate and save log automatically

## usage 
1. add your actions buy following the same syntax as given in actions
2. from akana_ml import AddLog
3. then give params to AddLog in following way to generate logs
4. you can see an example in test.py

## Class AddLog
AddLog([str][main_folder], [str][file], [int][action_code], [str][object of the action], [str][actor])

* :param1 = main_folder (main folder for your logs)
* :param1 = file (file name for your logs, all are saved in logs/)
* :param2 = actions code, import actions then tap p.e: actions.CREATE
* :param3 : object of the action p.e : "USER Jahid"
* :param4 : actor of the action p.e : "Jabir"
* :return : str

with those args AddLog will generate :
* *[datetime for now] - [Jabir] : CREATE USER Jahid*
