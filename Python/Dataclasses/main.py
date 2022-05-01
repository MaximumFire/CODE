import inspect
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Student:
	gpa: float
	name: str
	age: int


def main():
	student1 = Student(4.0, "Connor", 15)
	print(student1)


if __name__ == "__main__":
	main()