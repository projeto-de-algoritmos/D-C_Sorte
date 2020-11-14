import pygame
import random
import time

colors = (
    (0, 0, 0),  # Preto
    (255, 255, 255),  # Branco
    (0, 39, 118),  # Azul
    (255, 223, 0),  # Amarelo
    (0, 156, 59),  # Verde

    (255, 40, 0)  # Vermelho
)


class Sort:
    def __init__(self, resolution, display):
        self.resolution = resolution
        self.display = display

        self.running = True

        self.list = []
        self.orderedList = []
        self.unorderedList = []

        self.frameUnit = 20

        self.x_list = []
        self.x_1_list = []
        self.endY = 0

    def drawLine(self, color, initialPosition, endPosition):
        pygame.draw.line(self.display, color, initialPosition, endPosition)

    def merge(self, firstHalf, secondHalf, array):
        print("Realizando merge...")

        i, j, k = 0, 0, 0
        while i < len(firstHalf) and j < len(secondHalf):
            if firstHalf[i] < secondHalf[j]:
                array[k] = firstHalf[i]
                i += 1
            else:
                array[k] = secondHalf[j]
                j += 1
            k += 1

        while i < len(firstHalf):
            array[k] = firstHalf[i]
            i += 1
            k += 1

        while j < len(secondHalf):
            array[k] = secondHalf[j]
            j += 1
            k += 1

    def mergesort(self, array, startColumn=0):
        print("Aplicando mergesort...")

        if len(array) > 1:
            # sort_f = 1
            # Visualização de metade com mais de um componente
            self.populateFrames(1, array, startColumn)

            middleListId = int(len(array)/2)

            firstHalf = array[:middleListId]
            secondHalf = array[middleListId:]

            self.mergesort(firstHalf, startColumn)
            self.mergesort(secondHalf, startColumn+middleListId)

            startColumn_1 = startColumn + middleListId
            halfs = (firstHalf, secondHalf)

            # sort_f = 3
            # Visualização de metades que serão mergeadas
            self.populateFrames(3, halfs, startColumn, startColumn_1)

            self.merge(firstHalf, secondHalf, array)

            before = self.orderedList[:startColumn]
            after = self.orderedList[startColumn + len(array):]
            self.orderedList = before + array + after

            self.populateFrames(3, halfs, startColumn, startColumn_1)

            # sort_f = 4
            # Visualização merge de metades ordenado
            self.populateFrames(4)
        else:
            # sort_f = 2
            # Visualização de metade com um componente
            self.populateFrames(2, array, startColumn)

    def populateFrames(self, sort_f, array=[], startColumn=0, startColumn_1=0):
        print("Apresentando a lista nos quadros...")

        self.framesBuilder(sort_f if sort_f else sort_f + 1)

        i = 0
        for j in self.unorderedList:
            pygame.draw.rect(
                self.display, colors[2],
                (self.x_list[i] + 1, self.endY - j * 20 + 1, 19, (j * 20) - 1)
            )

            if not sort_f:
                time.sleep(0.25)
                pygame.display.update()

            i += 1

        i_1 = 0
        for j in self.orderedList:
            pygame.draw.rect(
                self.display, colors[2],
                (
                    self.x_1_list[i_1] + 1, self.endY - j * 20 + 1, 19,
                    (j * 20) - 1
                )
            )

            if not sort_f:
                time.sleep(0.13)
                pygame.display.update()

            i_1 += 1

        if sort_f and sort_f != 3:
            i = startColumn
            color = colors[3] if sort_f == 1 else colors[4]

            for j in array:
                pygame.draw.rect(
                    self.display, color,
                    (
                        self.x_list[i] + 1, self.endY - j * 20 + 1, 19,
                        (j * 20) - 1
                    )
                )

                i = i + 1

            pygame.display.update()
            time.sleep(0.5)

        if sort_f == 3:
            numberHalf = 0
            halfsStartColumns = [startColumn, startColumn_1]
            halfsColors = [colors[3], colors[4]]

            for half in array:
                i = halfsStartColumns[numberHalf]
                color = halfsColors[numberHalf]

                for j in half:
                    pygame.draw.rect(
                        self.display, color,
                        (
                            self.x_1_list[i] + 1, self.endY - j * 20 + 1,
                            19, (j * 20) - 1
                        )
                    )

                    i += 1

                numberHalf += 1

            pygame.display.update()
            time.sleep(1)

    def framesBuilder(self, sort_f):
        self.display.fill(colors[0])

        print("Construindo quadros...")

        y, w = 80, self.frameUnit

        limit_x = int((self.resolution[0] / 2) / self.frameUnit)
        limit_y = int((self.resolution[1] - 60) / self.frameUnit)

        for j in range(1, limit_y - 1):
            x, x_1 = 20, 560

            for i in range(1, limit_x - 1):
                # Linhas de Baixo
                self.drawLine(colors[1], (x, y + w), (x + w, y + w))
                self.drawLine(colors[1], (x_1, y + w), (x_1 + w, y + w))

                # Linhas da Direita
                self.drawLine(colors[1], (x + w, y), (x + w, y + w))
                self.drawLine(colors[1], (x_1 + w, y), (x_1 + w, y + w))

                if x == 20:
                    # Linhas da Esquerda
                    self.drawLine(colors[1], (x, y), (x, y + w))
                    self.drawLine(colors[1], (x_1, y), (x_1, y + w))

                if y == 80:
                    # Linhas do Topo
                    self.drawLine(colors[1], (x, y), (x + w, y))
                    self.drawLine(colors[1], (x_1, y), (x_1 + w, y))

                    self.x_list.append(x)
                    self.x_1_list.append(x_1)

                if not sort_f:
                    pygame.display.update()

                x = x + self.frameUnit
                x_1 = x_1 + self.frameUnit

            y = y + self.frameUnit

        self.endY = y

        if not sort_f:
            pygame.display.update()

    def sortPage(self):
        print("Criando lista de números aleatórios...")
        options = [i + 1 for i in range(25)]

        self.list = [random.choice(options) for i in range(25)]
        self.orderedList = self.list.copy()
        self.unorderedList = self.list.copy()

        print("Iniciando construção de quadros de dados...")

        # Primeira construção
        sort_f = 0
        self.framesBuilder(sort_f)

        print("Iniciando apresentações da lista...")
        self.populateFrames(sort_f)

        aux = 0
        started = False
        while not started:
            if not aux:
                textFont = pygame.font.Font(
                    './assets/fonts/Roboto-Bold.ttf', 17
                )
                numberStepsTitle = textFont.render(
                    'Clique na tela para iniciar a ordenação.', True, colors[1]
                )
                numberStepsTitleArea = numberStepsTitle.get_rect()
                numberStepsTitleArea.center = (
                    20+int(numberStepsTitle.get_width()/2),
                    20+int(numberStepsTitle.get_height()/2)
                )
                self.display.blit(numberStepsTitle, numberStepsTitleArea)
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    started = True

            aux += 1

        print("Iniciando mergesort...")
        self.mergesort(self.list)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def principal(self):

        while self.running:
            self.display.fill(colors[0])

            print("Acessando tela de ordenações...")
            self.sortPage()


def main():
    pygame.init()

    print("Iniciando aplicação...")

    resolution = (1080, 600)

    pygame.display.set_caption("Sorte")

    icon = pygame.image.load("./assets/media/icon.png")
    pygame.display.set_icon(icon)

    display = pygame.display.set_mode(resolution)
    newSort = Sort(resolution, display)
    newSort.principal()


if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
