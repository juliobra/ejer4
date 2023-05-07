class Ventana:
    def __init__(self, titulo='Ventana', x1=0, y1=0, x2=100, y2=100):
        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if x2 > 500:
            x2 = 500
        if y2 > 500:
            y2 = 500
        if x1 >= x2:
            x1, x2 = 0, 100
        if y1 >= y2:
            y1, y2 = 0, 100
        self.titulo = titulo
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    
        self.titulo = titulo
       
    def alto(self):
        return abs(self.y2 - self.y1)

    def ancho(self):
        return abs(self.x2 - self.x1)

    def mostrar(self):
        print('Título: {} - Coordenadas: ({}, {}) - Dimensiones: {}x{}'.format(self.titulo, self.x1, self.y1, self.ancho(), self.alto()))

    def moverDerecha(self, unidades=1):
        if self.x2 + unidades <= 500:
            self.x1 += unidades
            self.x2 += unidades

    
            self.x1 += unidades
    def moverIzquierda(self, unidades=1):
        if self.x1 - unidades >= 0:
            self.x1 -= unidades
            self.x2 -= unidades

    
            self.x1 -= unidades
            self.x2 -= unidades

   
    def bajar(self, unidades=1):
        if self.y2 + unidades <= 500:
            self.y1 += unidades
            self.y2 += unidades

    
            self.y1 += unidades
            self.y
    def subir(self, unidades=1):
        if self.y1 - unidades >= 0:
            self.y1 -= unidades
            self.y2 -= unidades

    def getTitulo(self):
        return self.titulo