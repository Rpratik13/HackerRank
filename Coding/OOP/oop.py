#Object Oriented Programming

class Employee:
	raiseAmount = 1.05
	empNum = 0

	def __init__(self, first: str, last: str, pay: float) -> None:
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@company.com'
		self.pay = pay
		Employee.empNum += 1


	def getFullName(self) -> None:
		return self.first + ' ' + self.last


	@classmethod
	def setRaiseAmount(cls, amount: float) -> None:
		cls.raiseAmount = amount



if __name__ == '__main__':
	emp1 = Employee('Pratik', 'Rajbhandari', 50000)
	emp2 = Employee('Test', 'User', 12345)

	Employee.setRaiseAmount(1.15)
	print(Employee.raiseAmount)
	print(emp1.raiseAmount)
	print(emp2.raiseAmount)