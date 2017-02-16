
class Robot(object):
    def fetch(self, tool):
        print "Physical Movement! Fetching"

    def move_forward(self, tool):
    	print "Physical Movement! Moving Forward"

    def move_backward(self, tool):
    	print "Physical Movement! Moving Backward"

    def replace(self, tool):
    	print "Physical Movement! Replacing"

class NotSuperRobot(Robot):
	def dry(self):
		pass

	def clean(self):
		print "I do dumb things"

class CleaningRobot(NotSuperRobot):
	def clean(self, tool, times=10):
		super(CleaningRobot, self).fetch(tool)
		for i in range(times):
			super(CleaningRobot, self).move_forward(tool)
			super(CleaningRobot, self).move_backward(tool)
		super(CleaningRobot, self).replace(tool)

if __name__ == '__main__':
	c = CleaningRobot()
	c.clean('broom')