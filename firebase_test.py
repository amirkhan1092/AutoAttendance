'''
from firebase import firebase
firebase = firebase.FirebaseApplication('https://eons-2c748.firebaseio.com', None)


firebase.post('/user2/sk',{'abc':'hello'})

# result = firebase.get('/Attendance/M1', None)
# print (result)
# # {'1': 'John Doe', '2': 'Jane Doe'}

import json

# your variables are already assigned before this
data = {'url': 'abcdf', 'address': 'khirwa', 'name': 'patlu'}
sent = json.dumps(data)
result = firebase.post("/businesses", sent)
'''

from firebase import firebase
firebase = firebase.FirebaseApplication('https://eons-2c748.firebaseio.com', None)
new_user = '/Ozgur Vatansever'

result = firebase.post('/users/new_user',{'print': 'pretty','X_FANCY_HEADER': 'VERY FANCY'})
print (result)
# {u'name': u'-Io26123nDHkfybDIGl7'}

# result = firebase.post('/users', new_user, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})
# # print (result == None)
# # # True