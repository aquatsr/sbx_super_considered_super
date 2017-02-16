from robot import Robot, CleaningRobot, NotSuperRobot

class MockBot(Robot):
	def __init__(self):
		self.tasks = []

	def fetch(self, tool):
		self.tasks.append('fetching %s' % tool)

	def move_forward(self, tool):
		self.tasks.append('forward %s' % tool)

	def move_backward(self, tool):
		self.tasks.append('backward %s' % tool)

	def replace(self, tool):
		self.tasks.append('replace %s' % tool)

class MockedCleaningRobot(CleaningRobot, MockBot):
	pass

class TestCleaningRobot():
	def test_clean(self):
		t = MockedCleaningRobot()
		t.clean('mop')
		expected = ['fetching mop'] + ['forward mop', 'backward mop'] * 10 + ['replace mop']
		assert t.tasks == expected


if __name__ == '__main__':
	import pytest
	pytest.main(['mockcleaningrobot.py'])