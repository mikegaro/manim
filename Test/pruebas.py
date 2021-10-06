try:
    from manim import *  # Para manimCE
except:
    from manimlib import *  # Para manim_gl


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


class Updaters(Scene):
    def construct(self):
        rectangulo = RoundedRectangle(stroke_width=8,
                                      stoke_color=WHITE,
                                      fill_color=BLUE_D,
                                      width=4.5,
                                      height=2).shift(UP*3+LEFT*4)
        texto = Tex("\\frac{3}{4} = 0.75").set_color_by_gradient(GREEN,
                                                                 PINK).set_height(1.5)
        texto.move_to(rectangulo.get_center())
        texto.add_updater(lambda x: x.move_to(rectangulo.get_center()))

        self.play(FadeIn(rectangulo))
        self.play(Write(texto))
        self.play(rectangulo.animate.shift(RIGHT*1.5 + DOWN*5), run_time=3)
        self.wait()
        texto.clear_updaters()
        self.play(rectangulo.animate.shift(LEFT*2 + UP*1), run_time=3)


# LAMENTABLEMENTE ESTA SOLO CORRE EN manimCE por el tema del .next_to()
class AlgoMasComplejo(Scene):
    def construct(self):
        r = ValueTracker(0.5)
        circulo = always_redraw(lambda: Circle(radius=r.get_value(),
                                               stroke_color=YELLOW,
                                               stroke_width=5))

        line_radius = always_redraw(lambda: Line(start=circulo.get_center(),
                                                 end=circulo.get_bottom(),
                                                 stroke_color=RED_B,
                                                 stroke_width=10)
                                    )
        linea_circunferencia = always_redraw(lambda: Line(stroke_color=YELLOW,
                                                          stroke_width=5).set_length(2*r.get_value()*PI).next_to(circulo,
                                                                                                                 DOWN,
                                                                                                                 buff=0.2))

        triangulo = always_redraw(lambda: Polygon(circulo.get_top(),
                                                  circulo.get_left(),
                                                  circulo.get_right(),
                                                  fill_color=GREEN))

        self.play(LaggedStart(Create(circulo),
                              DrawBorderThenFill(line_radius),
                              DrawBorderThenFill(triangulo),
                              run_time=4,
                              lag_ratio=0.75))
        self.play(ReplacementTransform(circulo.copy(),
                                       linea_circunferencia),
                  runtime=2)
        self.play(r.animate.set_value(2),
                  runtime=5)


class LeydeLaGravitacion(Scene):
    def construct(self):
        circulo = Circle(radius=1, stroke_color=YELLOW,
                         stroke_width=5)
        rectangulo = RoundedRectangle(stoke_color=WHITE,
                                      fill_color=BLUE,
                                      width=4,
                                      height=1.4)
        texto = MathTex(
            "\\int_{0}^{\\infty} F = G\\frac{m_{1}m_{2}}{r^{2}}").scale(scale_factor=0.8)

        texto.move_to(rectangulo.get_center())
        texto.add_updater(lambda x: x.move_to(rectangulo.get_center()))
        self.play(Create(rectangulo))
        self.play(Write(texto))
        self.play(rectangulo.animate.shift(UP*2.5), runtime=0.7)
        self.play(DrawBorderThenFill(circulo), runtime=0.5)
        flecha_uno = Arrow(buff=1.5, start=circulo.get_center(),
                           end=RIGHT*2)
        dot_uno = Dot(point=circulo.get_center())

        flecha_uno.add_updater(lambda x: x.move_to(
            circulo.get_center()+RIGHT))
        dot_uno.add_updater(lambda x: x.move_to(circulo.get_center()))
        self.play(Create(flecha_uno), Create(dot_uno),
                  circulo.animate.shift(LEFT*3), run_time=1)
        self.wait(duration=5)
