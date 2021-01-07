from akana_ml import AddLog
import actions

data = {
    'actors':
        ['Jabir', 'Jahid', 'Nickel', 'Bruce', 'Blaise', 'Nathan', 'Marcellin', 'Husnan', 'Eddy',
         'Denis', 'Gretta', 'Zoé', 'Amandine', 'Cloé'],
    'actions': [actions.CREATE, actions.MODIFY, actions.DELETE]
}
for i in range(1000):
    for actor in data['actors']:
        for action in data['actions']:
            print(AddLog(main_folder='logs', file='test', actor=actor,
                         object=f"a file named {actor}.text", action=action))
