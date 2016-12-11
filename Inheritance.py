class office_furniture(object):
    def __init__(self, category, material, length, width, height, price, quantity):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price
        self.__quantity = quantity

    def set_category (self, category):
        self.__category = category

    def set_material (self, material):
        self.__material = material

    def set_length (self, length):
        self.__length = length

    def set_width (self, width):
        self.__width = width

    def set_height (self, height):
        self.__height = height

    def set_price (self, price):
        self.__price = price

    def set_quantity (self, quantity):
        self.__quantity = quantity

    def get_category (self):
        return self.__category

    def get_material (self):
        return self.__material

    def get_length (self):
        return self.__length

    def get_width (self):
        return self.__width

    def get_height (self):
        return self.__height

    def get_price (self):
        return self.__price

    def get_quantity (self):
        return self.__quantity

    def get_total (self):
        return self.__price * self.__quantity

    def __str__(self):
        line_item = "(" + str(self.__quantity) + ")" + "  " + self.__category + "  " + self.__material + "  " + str(self.__length) + " in. x " + str(self.__width) + " in. x " + str(self.__height) + " in.  at $" + str(self.__price) + " each  =  $" + str(self.get_total()) + "\n"
        return line_item

reception_desk = office_furniture("desk", "oak", 48, 25, 34, 350, 1)
bookcase = office_furniture("shelf", "pine", 65, 20, 48, 250, 4)
print reception_desk
print bookcase
print "\n"
