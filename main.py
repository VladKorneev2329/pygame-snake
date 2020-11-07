import sys
import random
import pygame as pg


class App:
    """Класс окна приложения"""

    def __init__(self, WIDTH: int = 800, HEIGHT: int = 800):
        """Инициализирует настройки приложения"""

        # Инициализирует настроки экрана
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.PIXEL = 20
        self.FPS = 5
        self._clock = pg.time.Clock()

        # Инициализирует библеотеку pygame и вызывает главное окно
        pg.init()
        self.ICON = pg.image.load('images/icon.png')
        pg.display.set_icon(self.ICON)
        self.DISPLAY = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Змейка')

        # Создание экзепляра Змейки
        self.snake = Snake(self.PIXEL)

        # Создание экземпляра Еды
        self.food = Food(self.DISPLAY, self.PIXEL, self.snake)

    def run(self):
        """Главный цикл приложения"""
        while True:
            self.check_event()
            self.draw()

            pg.display.flip()
            self._clock.tick(self.FPS)

    def check_event(self):
        [sys.exit() for event in pg.event.get() if event.type == pg.QUIT]

        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.snake.get_direction('up')
        elif keys[pg.K_DOWN]:
            self.snake.get_direction('down')
        elif keys[pg.K_LEFT]:
            self.snake.get_direction('left')
        elif keys[pg.K_RIGHT]:
            self.snake.get_direction('right')

    def draw(self):
        """Отображает на экране объекте"""

        # Фон
        self.DISPLAY.fill((55, 55, 55))
        for pos_x in range(0, self.HEIGHT, self.PIXEL):
            pg.draw.line(self.DISPLAY, (22, 22, 22), (pos_x, 0), (pos_x, self.HEIGHT))

        for pos_y in range(0, self.WIDTH, self.PIXEL):
            pg.draw.line(self.DISPLAY, (22, 22, 22), (0, pos_y), (self.WIDTH, pos_y))

        # Проверка на пересечении координат еды и змейки
        self.food.is_collision()
        # Отрисовка еды
        self.food.draw()

        # Отрисовка змейки
        self.snake.draw(self.DISPLAY)


class Snake:
    """Объект змейки"""

    def __init__(self, PIXEL):
        """Инициализирует главные характеристики змейки"""
        self.SIZE = PIXEL
        self.COLOR = (0, 230, 118)

        # Координаты змейки
        self.pos_x = 0
        self.pos_y = 0

        # Направление змейки
        self.direction = 'down'

    def move(self):

        if self.direction == 'up':
            self.pos_y -= self.SIZE
        elif self.direction == 'down':
            self.pos_y += self.SIZE
        elif self.direction == 'left':
            self.pos_x -= self.SIZE
        elif self.direction == 'right':
            self.pos_x += self.SIZE

        # Проверка на пересечении с стенами,
        # в случае если змейка врезается в стенку, она телепортируется к противоположной стенке
        if pg.display.get_window_size()[0] < self.pos_x + self.SIZE:
            self.pos_x = 0
        elif 0 > self.pos_x:
            self.pos_x = pg.display.get_window_size()[0] - self.SIZE
        elif pg.display.get_window_size()[1] < self.pos_y + self.SIZE:
            self.pos_y = 0
        elif 0 > self.pos_y:
            self.pos_y = pg.display.get_window_size()[1] - self.SIZE

    def draw(self, DISPLAY):
        self.move()
        pg.draw.rect(DISPLAY, self.COLOR, (self.pos_x, self.pos_y, self.SIZE, self.SIZE))

    def get_direction(self, direction):
        self.direction = direction


class Food:
    """Класс Еды"""

    def __init__(self, DISPLAY, PIXEL, snake):
        self.DISPLAY = DISPLAY
        self.PIXEL = PIXEL
        self.snake = snake

        self.icons = [
            pg.image.load('images/apple.png'),
            pg.image.load('images/orange.png')
        ]
        # Создание переменных
        self.pos_x = self.pos_y = self.icon = None

        self.random_icon()
        self.random_pos()


    def draw(self):
        """Отрисовка еды в координатах self.pos_x, self.pos_y"""
        self.DISPLAY.blit(self.icon, (self.pos_x, self.pos_y))

    def random_icon(self):
        """Выбор рандомной иконки еды"""
        self.icon = random.choice(self.icons)

    def random_pos(self):
        """Генерация рандомных координат self.pos_x, self.pos_y"""
        self.pos_x = random.randrange(0, pg.display.get_window_size()[0], self.PIXEL)
        self.pos_y = random.randrange(0, pg.display.get_window_size()[1], self.PIXEL)

    def is_collision(self):
        """Проверка на пересечении головы змейки и еды"""
        if self.snake.pos_x == self.pos_x and \
                self.snake.pos_y == self.pos_y:
            self.random_pos()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
