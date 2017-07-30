class first(object):
    def __init__(self,first,second):
      self.first_name=first
      self.second_name=second

    def fullname(self):
      return self.first_name + "@" + self.second_name 

    def address(self,city):
        self.city_name=city
        return self.city_name


    def address1(self,city):
        city_name=city
        return city_name



name=first('AJ','K')
print(name.first_name, name.second_name)
print(name.fullname())
print(name.address('Pune'))
print(name.address1('Mumbai'))
