try:
    from manimlib import *
    from manim import *
except ImportError:
    pass

class Prueba(Scene):
    def construct(self):
        box = Rectangle(stroke_color=GREEN_C, stroke_opacity=0.7,
        fill_color=RED_B, fill_opacity=0.5, height=1, width=1)
        self.add(box)
        self.play(box. animate.shift(RIGHT*2), run_time=2)
        self.play(box.animate.shift(UP*2), run_time=2)
        self.play(box.animate.shift(DOWN*5 + LEFT*5),run_time=2)
        self.play(box.animate.shift(UP*3 + RIGHT*3),run_time=1)

class Triangulo(Scene):
    def construct(self):
        tri = Triangle( color=BLACK, fill_opacity=0.9, stroke_color=BLUE_A, stoke_color=WHITE)
        self.add(tri)
        self.play(tri.animate.rotate(3.1416/2), run_time=2)
        self.play(tri.animate.rotate(3.1416/2), run_time=2) 