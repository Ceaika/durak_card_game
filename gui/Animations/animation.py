class Animation():

    def __init__(self, target, start_position):

        self.steps = 10
        self.target_x = target[0]
        self.target_y = target[1]
        self.dx = 0
        self.dy = 0

        if not self.target_x == start_position[0] and not self.target_y == start_position[1]:
            self.dx = self.optimal_delta(self.target_x - start_position[0])
            self.dy = self.optimal_delta(self.target_y - start_position[1])

        # if abs(self.dx) < 1 and self.dx != 0:
        #     self.dx = 0
        # elif abs(self.dy) < 1 and self.dy != 0:
        #     self.dy = 0


        # print("Start_x: ", start_position[0], "Start_y: ", start_position[1])
        # print("Targer x:", self.target_x, "Targer_y:", self.target_y)
        print("dx: ", self.dx, "dy: ", self.dy)

    def optimal_delta(self, diff):
        optimal = self.steps
        delta = 0
        while True:
            delta = diff / optimal
            if abs(delta) < 1 and delta != 0:
                optimal -= 1
            elif optimal <= 0:
                delta = 0
                break
            else:
                break
        return delta

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

        # print(x,sep=",")
        # print(animated_card.suit,animated_card.value)
        if abs(x - self.get_target_x()) < abs(4 * self.get_dx()):
            self.set_dx(0)

        elif abs(y - self.get_target_y()) < abs(3 * self.get_dy()):
            self.set_dy(0)

        if self.get_dx() == 0 and self.get_dy() == 0:
            area.add_new_card(animated_card)
            do_animation = False
            animated_card = None
            return do_animation, animated_card

        else:
            animated_card.position = x + self.get_dx(), y + self.get_dy()

        return do_animation, animated_card
