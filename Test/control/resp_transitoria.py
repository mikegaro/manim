from manim import *
import math


class SistemaSubGraph(Scene):
    def construct(self):
        texto = MarkupText('Sistema Subamortiguado').scale(0.7)
        self.play(Write(texto), run_time=4)
        self.play(texto.animate.shift(UP*3), run_time=1)
        axis = Axes(
            x_range=[0, 10, 0.5],
            y_range=[0, 1.4, 0.5],
            tips=False,
            axis_config={"include_numbers": True}
        )
        graph = axis.plot(lambda x: 1-math.e**(-x)*(math.cos(math.sqrt(8*x))
                                                    + math.sqrt(8)/8*math.sin(math.sqrt(8*x))),
                          x_range=[0, 10], use_smoothing=False)
        self.play(Create(axis), Create(graph), run_time=3)
        self.wait()


class
