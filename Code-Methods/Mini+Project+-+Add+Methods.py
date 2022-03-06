
'''
class MusicSchool:

	students = {"Gino": 	[15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": 	[28, "555-765-452", ["Cello"]],
                "Eric":   	[12, "583-356-223", ["Singing"]]}

	def __init__(self, working_hours, revenue):
		self.working_hours = working_hours
		self.revenue = revenue

	# Add your methods below this line
	def print_student_data(self, name):
		for key, value in  MusicSchool.students.items():
			print(f"{MusicSchool.students[key]}, who is {MusicSchool.students[key][0]} and is taking
			f"" \
			f"{MusicSchool.students[key][2]}")
'''


# Create the instance



# Call the methods


		class MusicSchool:

			students = {"Gino": 	[15, "653-235-345", ["Piano", "Guitar"]],
						"Talina": 	[28, "555-765-452", ["Cello"]],
						"Eric": 	[12, "583-356-223", ["Singing"]]}

			def __init__(self, working_hours, revenue):
				self.working_hours = working_hours
				self.revenue = revenue

			# Add your methods below this line

			def print_students_data(self):
				for name in MusicSchool.students:
					self.print_student(name)

			### The first method to create is this one since it will be used on the one above
			### The first step is to create a list object from the dictionary object
			### print the message using formating method
			### Since i will use it in print_student_data
			def print_student(self, name):
				'''
				The first step in implementing this method here is to create
				an object that can access the keys[lists] using the argument
				as an index of the list iterable.
				'''

				data = MusicSchool.students[name]
				print("Student: " + name + " who is " + str(data[0]) + " years old and is taking " + str(data[2]))

			def add_student(self, name, data):
				MusicSchool.students[name] = data

		headquarters = MusicSchool(8, 15000)

		headquarters.print_students_data()

		headquarters.print_student("Gino")

		headquarters.add_student("Jack", [60, "562-234-234", ["Piano"]])


