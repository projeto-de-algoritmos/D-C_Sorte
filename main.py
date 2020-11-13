import pygame
import random

colors = (
    (0, 0, 0),  # Preto
    (255, 255, 255)  # Branco
)


class Sort:
    def __init__(self, resolution, display):
        self.resolution = resolution
        self.display = display

    def drawLine(self, color, initialPosition, endPosition):
        pygame.draw.line(self.display, color, initialPosition, endPosition)

    def framesGenerator(self, frameUnit):
        print("Construindo quadros...")

        x_list = []
        x_1_list = []

        y_list = []

        y, w = 80, frameUnit

        limit_x = int((self.resolution[0] / 2) / frameUnit)
        limit_y = int((self.resolution[1] - 60) / frameUnit)

        for j in range(1, limit_y - 1):
            x = 20
            x_1 = 560

            for i in range(1, limit_x - 1):
                # Linhas da Esquerda
                self.drawLine(colors[1], (x, y), (x, y + w))
                self.drawLine(colors[1], (x_1, y), (x_1, y + w))

                # Linhas do Topo
                self.drawLine(colors[1], (x, y), (x + w, y))
                self.drawLine(colors[1], (x_1, y), (x_1 + w, y))

                # Linhas de Baixo
                self.drawLine(colors[1], (x, y + w), (x + w, y + w))
                self.drawLine(colors[1], (x_1, y + w), (x_1 + w, y + w))

                # Linhas da Direita
                self.drawLine(colors[1], (x + w, y), (x + w, y + w))
                self.drawLine(colors[1], (x_1 + w, y), (x_1 + w, y + w))

                pygame.display.update()

                if y == 80:
                    x_list.append(x)
                    x_1_list.append(x_1)

                x = x + frameUnit
                x_1 = x_1 + frameUnit

            y_list.append(y)
            y = y + frameUnit

        pygame.display.update()

        options = [i + 1 for i in range(25)]
        array = [random.choice(options) for i in range(25)]

        j = 0
        for i in array:
            pygame.draw.rect(
                self.display, colors[1],
                (x_list[j], y-i*20, 20, i*20)
            )
            pygame.display.update()

            pygame.draw.rect(
                self.display, colors[1],
                (x_1_list[j], y-i*20, 20, i*20)
            )
            pygame.display.update()

            j = j + 1

    def principal(self):
        frameUnit = 20

        running = True
        showInitialPage = False
        while running:
            self.display.fill(colors[0])

            if showInitialPage:
                print("a")
                # self.initialPage()

            print("Iniciando construção de quadros de dados...")
            self.framesGenerator(frameUnit)


def main():
    pygame.init()

    print("Iniciando aplicação...")

    resolution = (1080, 600)

    pygame.display.set_caption("Sorte")

    # icon = pygame.image.load("./assets/media/icon.png")
    # pygame.display.set_icon(icon)

    display = pygame.display.set_mode(resolution)
    newSort = Sort(resolution, display)
    newSort.principal()


if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
