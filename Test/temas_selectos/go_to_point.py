from manim import *


class GoToPointSimple(Scene):
    def construct(self):
        # Points
        p2 = Dot(point=UP*3 + RIGHT*3, color=WHITE)
        p1 = Dot(point=DOWN*2+LEFT*2)

        # Labels for each point
        p1_label = Tex("P1", font_size=20).move_to(p1.get_center()+RIGHT*0.3)
        p2_label = Tex("P2", font_size=20).move_to(p2.get_center()+LEFT*0.3)

        # Axes
        axis = Axes(
            x_range=[0, 1, 1],
            y_range=[0, 1, 1],
            x_length=0.5,
            y_length=0.5,
            tips=False
        ).move_to(LEFT*6 + DOWN * 3)

        # Line from P1 to P2
        path_line = Line(p1.get_center(), p2.get_center())

        # X-Line
        x_line = Line(p1.get_center(), p1.get_center() +
                      RIGHT*(p2.width - p1.width))
        y_line = Line(p2.get_center(), p2.get_center() -
                      DOWN*(p2.height - p1.height))

        # Robot
        robot_body = Rectangle(color=RED,
                               height=0.5,
                               width=1).move_to(p1.get_center()).rotate(-PI/6)

        self.play(Create(p1),
                  Create(p2),
                  Create(axis), run_time=1)

        self.play(Create(p1_label),
                  Create(p2_label),
                  Create(robot_body), run_time=1)

        self.play(Create(x_line),
                  Create(y_line), run_time=2)

        self.play(Create(path_line), run_time=1)
        self.wait(duration=2)
