"""
그림과 관련된 함수와 클래스를 제공하는 figure 모듈
line 클래스와 area_square(), area_circle(), area_regular_triangle() 메소드 제공
"""
import math
class line:
	"""
	line 클래스는 선의 길이를 저장
	외부에서 접근 불가능한 필드 __length가 있음
	line클래스의 필드는 외부에서 접근 불가능한 필드 __length가 있으며, 초기 값은 0
	해당 필드에 접근하기 위한 메소드 set_length(), get_length() 존재
	"""
	__length = 0
	def __init__(self, length):
		""" 생성자, line instance 생성 시 설정될 __length 값을 설정
		Args:
			length (int or float): 초기 선의 길이
		"""
		self.__length = length

	def set_length(self, length):
		""" __length의 setter
		Args:
			length (int or float): 변경될 선의 길이
		"""
		self.__length = length

	def get_length(self):
		""" __length의 getter
		Returns:
			int or float: 선의 길이 (__length) 값
		"""
		return self.__length

def area_square(length):
	""" 각 변이 length 길이인 정사각형의 넓이를 구함
	Args:
		length (int or float): 정사각형의 변의 길이
	Returns:
		int or float: 주어진 길이의 변을 가진 정사각형의 넓이
	"""
	return length*length

def area_circle(length):
	""" 반지름이 length인 원의 넓이를 구함
	Args:
		length (int or float): 원의 반지름의 길이
	Returns:
		int or float: 주어진 길이의 반지름을 가진 원의 넓이
	"""
	return math.pi * length * length #pi * r^2

def area_regular_triangle(length):
	""" 각 변의 길이가 length인 정삼각형의 길이를 구함
	Args:
		length (int or float): 정삼각형의 변의 길이
	Returns:
		int or float: 주어진 길이의 변을 가진 정삼각형의 넓이
	"""
	return length*length*math.sqrt(3)/4

