from manimlib.imports import *

set_custom_quality(800,20)

class QualityTest(Scene):
    def construct(self):
        t=Text("Hola mundo")
        self.Oldplay(Escribe(t))
        self.wait()