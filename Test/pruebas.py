try:
    from manim import *
except:
    from manimlib import *


class CuboConTex(Scene):
    def construct(self):
        newton_first = Tex(r"\vec{F} = m\vec{a}")
        self.add(newton_first)
        self.play(newton_first.animate.shift(UP*2),
                  run_time=1)
        box = Rectangle(stroke_color=GREEN_C,
                        stroke_opacity=0.7,
                        fill_color=RED_B,
                        fill_opacity=0.5,
                        height=1,
                        width=1)
        self.add(box)
        self.play(box.animate.shift(RIGHT*2),
                  run_time=2)
        self.play(box.animate.shift(UP*2),
                  run_time=2)
        self.play(box.animate.shift(DOWN*5 + LEFT*5),
                  run_time=2)
        self.play(box.animate.shift(UP*3 + RIGHT*3),
                  run_time=1)
        self.play(Rotate(box, PI*2),
                  runtime=1)


class Triangulo(Scene):
    def construct(self):
        tri = Triangle(color=BLACK,
                       fill_opacity=0.9,
                       stroke_color=BLUE_A)
        self.add(tri)
        self.play(Rotate(tri, PI*2),
                  run_time=4)


class MuchosObjetos(Scene):
    def construct(self):
        eje = Axes(x_range=[-3, 3, 0.5],
                   y_range=[-2, 2, 0.5],
                   x_lenght=6,
                   y_length=6)
        eje.to_edge(LEFT, buff=0.5)

        circulo = Circle(stroke_width=6,
                         stroke_color=YELLOW,
                         fill_color=RED,
                         fill_opacity=0.8)
        circulo.set_width(2).to_edge(DR, buff=1)
        triangulo = Triangle(stroke_color=ORANGE,
                             stroke_width=10,
                             fill_color=RED).set_height(2).shift(DOWN*2+RIGHT*2)

        self.play(Write(eje))
        self.play(DrawBorderThenFill(circulo))
        self.play(circulo.animate.set_width(1))
        self.play(Transform(circulo, triangulo), run_time=2)
