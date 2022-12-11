
class Animation():

    def __init__(self, target, start_position):
        self.target_x = target[0]
        self.target_y = target[1]
        self.dx = (self.target_x - start_position[0] ) /20
        self.dy = (self.target_y - start_position[1]) / 20
        print(self.target_x)

    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy

    def set_dx(self, dx):
        self.dx = dx

    def set_dy(self, dy):
        self.dy = dy

    def get_target_x(self):
        return self.target_x

    def get_target_y(self):
        return self.target_y

    def do_animation(self, animated_card, area):
        do_animation = True
        x, y = animated_card.position

        if abs(x - self.get_target_x()) < abs(self.get_dx()):
            self.set_dx(0)

        elif abs(y - self.get_target_y()) < abs(self.get_dy()):
            self.set_dy(0)

        if self.get_dx() == 0 and self.get_dy() == 0:
            area.add_new_card(animated_card)
            do_animation = False
            animated_card = None
            return do_animation, animated_card

        else:
            animated_card.position = x + self.get_dx(), y + self.get_dy()

        return do_animation, animated_card
