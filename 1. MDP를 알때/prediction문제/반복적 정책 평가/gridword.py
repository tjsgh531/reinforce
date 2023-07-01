class GridWorld():
    def move(self, x, y):
        result = []

        x_prime, y_prime = self.move_right(x, y)
        result.append((x_prime, y_prime))

        x_prime, y_prime = self.move_left(x, y)
        result.append((x_prime, y_prime))

        x_prime, y_prime = self.move_up(x, y)
        result.append((x_prime, y_prime))

        x_prime, y_prime = self.move_down(x, y)
        result.append((x_prime, y_prime))

        return result

    def move_right(self, x, y):
        y += 1
        if y > 3:
            y = 3
        return x, y

    def move_left(self, x, y):
        y -= 1
        if y < 0:
            y = 0
        return x, y
    
    def move_up(self, x, y):
        x -= 1
        if x < 0:
            x = 0
        return x, y

    def move_down(self, x, y):
        x += 1
        if x > 3:
            x = 3
        return x, y
