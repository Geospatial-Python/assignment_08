from . import utils



class Point(object):
  
  def __init__(self, x, y, mark={}):
      self.x = x
      self.y = y
      self.mark = mark
  
  def point_check_coincident(self, test):
      return utils.check_coincident((self.x, self.y), test)
  
  def point_shift_point(self, x_shift, y_shift):
      test = utils.shift_point((self.x, self.y), x_shift, y_shift)
      self.x = utils.getx(test)
      self.y = utils.gety(test)
      
