from models.projects import Users
from models.result import Users as Ub


print(Users(user_id=2, user_name='mbj2').save())
print(Ub(user_id=3, user_name='mbj3').save())

