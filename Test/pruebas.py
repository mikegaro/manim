from manim import *


class CuboConTex(Scene):
    def construct(self):
        newton_first = MathTex(r"\vec{F} = m\vec{a}")
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
        texto = MathTex("\\frac{3}{4} = 0.75").set_color_by_gradient(GREEN,
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
        circulo = Circle(radius=0.5,
                         stroke_color=BLUE,
                         stroke_width=5).move_to(DOWN*1)
        rectangulo = RoundedRectangle(stoke_color=WHITE,
                                      fill_color=BLUE,
                                      width=3.5,
                                      height=1.2)
        texto = MathTex(
            "F = G\\frac{m_{1}m_{2}}{r^{2}}").scale(scale_factor=0.7)

        texto.move_to(rectangulo.get_center())
        texto.add_updater(lambda x: x.move_to(rectangulo.get_center()))
        self.play(Create(rectangulo))
        self.play(Write(texto))
        self.play(rectangulo.animate.shift(UP*2.5),
                  runtime=0.7)
        self.play(DrawBorderThenFill(circulo),
                  runtime=0.5)
        circulo_dos = Circle(radius=0.5,
                             stroke_color=BLUE,
                             stroke_width=5).move_to(DOWN*1)
        self.add(circulo_dos)

        flecha_uno = Arrow(buff=1,
                           start=circulo.get_center(),
                           end=circulo.get_center()+RIGHT*1)
        dot_uno = Dot(point=circulo.get_center())

        flecha_uno.add_updater(lambda x: x.move_to(
            circulo.get_center()+RIGHT*0.5))
        dot_uno.add_updater(lambda x: x.move_to(circulo.get_center()))

        flecha_dos = Arrow(buff=1.5,
                           start=circulo_dos.get_center(),
                           end=circulo_dos.get_center()+LEFT*1)
        dot_dos = Dot(point=circulo_dos.get_center())
        flecha_dos.add_updater(lambda x: x.move_to(
            circulo_dos.get_center()+LEFT*0.5))
        dot_dos.add_updater(lambda x: x.move_to(circulo_dos.get_center()))
        self.play(Create(dot_uno),
                  Create(dot_dos),
                  run_time=0.5)
        self.play(Create(flecha_uno),
                  Create(flecha_dos),
                  circulo.animate.shift(LEFT*1.4),
                  circulo_dos.animate.shift(RIGHT*1.4),
                  run_time=2)
        self.play(Rotate(circulo,
                         about_point=ORIGIN+DOWN,
                         angle=2*PI),
                  Rotate(circulo_dos,
                         about_point=ORIGIN+DOWN,
                         angle=2*PI),
                  Rotate(
                      flecha_dos, about_point=circulo_dos.get_center(), angle=2*PI),
                  Rotate(flecha_uno, about_point=circulo.get_center(), angle=2*PI),
                  run_time=15)
        self.wait(duration=3)


class RotandoEnCirculo(Scene):
    def construct(self):
        punto = Dot()
        circulo = Circle(radius=1)
        punto.move_to(circulo.get_center() + circulo.radius*RIGHT)
        self.play(Create(punto), Create(circulo))
        self.play(Rotate(punto,
                         about_point=circulo.get_center(),
                         angle=PI),
                  run_time=3)
        self.wait(duration=3)


class TitleExample(Scene):
    def construct(self):
        banner = ManimBanner()
        title = Title(f"Manim version {manim.__version__}")
        self.add(banner, title)


class DecimalMatrixExample(Scene):
    def construct(self):
        m0 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket="\{",
            right_bracket="\}")
        self.play(Create(m0))
        self.wait()


class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(
            r"$x^2 + y^2 = z^2$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=144,
        )
        self.play(Create(tex),
                  run_time=3)


class RespuestaTransitoria(Scene):
    def construct(self):
        texto = MarkupText('Hola')
        self.play(Create(texto), run_time=3)


class Example1Text(Scene):
    def construct(self):
        text = MarkupText('Hello world').scale(3)
        self.add(text)


class LogScalingExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x ** 2,
                        x_range=[0.001, 10], use_smoothing=False)
        self.play(Create(ax), Create(graph))
