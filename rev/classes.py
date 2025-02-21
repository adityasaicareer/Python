class sup:

	def __init__(self):
		self.one=1
		self.two=2


class sub(sup):

	def __init__(self):

		super().__init__()

		self.val=self.one**2+self.two**2


ex=sub()
print(ex.val)