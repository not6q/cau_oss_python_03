"""
그림과 관련된 함수와 클래스를 제공하는 figure 모듈
line 클래스와 area_rectangle(), area_ellipse(), area_right_triangle() 메소드 제공
"""
import math
class line:
	"""
	line 클래스는 선의 길이를 저장
	외부에서 접근 불가능한 필드 __width, __height가 있음
	line클래스의 필드는 외부에서 접근 불가능한 필드 __width, __height가 있으며, 초기 값은 0
	해당 필드들에 접근하기 위한 setter/getter가 존재
	"""
	__width = 0
	__height = 0
	def __init__(self, width, height):
		""" 생성자, line instance 생성 시 설정될 __width, __height 값을 설정
		Args:
			width (int or float): 초기 width의 길이
			height (int or float): 초기 height의 길이
		"""
		self.__width = width
		self.__height = height

	def set_length(self, width, height):
		""" __width와 __height의 setter
		Args:
			width (int or float): 설정될 width의 길이
			height (int or float): 설정될 height의 길이
		"""
		self.__width = width
		self.__height = height

	def get_length(self):
		""" __width와 __height의 getter
		Returns:
			int or float: 선의 길이 값들
		"""
		return self.__width, self.__height

def area_rectangle(width, height):
	""" 변 2개의 길이(너비, 길이)를 받아 해당 속성을 가진 직사각형의 넓이를 구함
	Args:
		width (int or float): 직사각형의 너비
		height (int or float): 직사각형의 높이
	Returns:
		int or float: 주어진 길이의 변을 가진 직사각형의 넓이
	Raises:
		ValueError: 길이가 0 이하인 경우
	"""
	if width <= 0 or height <= 0:
		raise ValueError
	return width * height

def area_ellipse(width, height):
	""" 반지름의 길이 2개를 받아 타원의 넓이를 구함
	Args:
		width (int or float): 타원의 짧은 쪽 반지름의 길이
		height (int or float): 타원의 긴 쪽 반지름의 길이
	Returns:
		int or float: 주어진 속성을 가진 타원의 넓이
	Raises:
		ValueError: 길이가 0 이하인 경우
	"""
	if width <= 0 or height <= 0:
		raise ValueError
	return math.pi * width * height

def area_right_triangle(width, height):
	""" 각 변의 길이가 width, height인 직삼각형의 길이를 구함
	Args:
		width (int or float): 직삼각형의 너비
		height (int or float): 직삼각형의 높이
	Returns:
		int or float: 주어진 길이의 변을 가진 직삼각형의 넓이
	Raises:
		ValueError: 길이가 0 이하인 경우
	"""
	if width <= 0 or height <= 0:
		raise ValueError
	return width * height/2