'''
import we come here
models is for Databases
'''

class User(db.Model):
	id = Colunm(db.Integer(),primary_key=True)
	name = Colunm(db.String(),nullable=False)


	def __repr__(self):

		return f"This user is {self.name}"

