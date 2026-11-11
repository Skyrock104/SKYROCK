
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
from kivy.metrics import dp
from math import sin, cos, pi
from plyer import tts

class Reactor(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        Clock.schedule_interval(self.animate, 1 / 30)

    def animate(self, dt):
        self.angle += 1.5
        self.draw_reactor()

    def on_size(self, *args):
        self.draw_reactor()

    def on_pos(self, *args):
        self.draw_reactor()

    def draw_reactor(self):
        self.canvas.clear()

        cx = self.center_x
        cy = self.center_y
        r = min(self.width, self.height) * 0.34

        with self.canvas:
            Color(0, 0.6, 1, 0.12)
            Ellipse(pos=(cx-r*1.2, cy-r*1.2),
                    size=(r*2.4, r*2.4))

            Color(0, 0.75, 1, 0.9)
            Line(circle=(cx, cy, r), width=dp(2))

            Color(0, 0.4, 0.9, 0.8)
            Line(circle=(cx, cy, r*0.82), width=dp(1.5))

            Color(0, 0.85, 1, 1)
            Line(circle=(cx, cy, r*0.55), width=dp(2))

            for i in range(36):
                a = (i * 10 + self.angle) * pi / 180

                x1 = cx + cos(a) * r * 0.88
                y1 = cy + sin(a) * r * 0.88

                x2 = cx + cos(a) * r
                y2 = cy + sin(a) * r

                Line(points=[x1, y1, x2, y2], width=dp(1))

            Color(0.1, 0.8, 1, 0.2)
            Ellipse(pos=(cx-r*0.42, cy-r*0.42),
                    size=(r*0.84, r*0.84))

            Color(0.1, 0.85, 1, 1)
            Ellipse(pos=(cx-r*0.23, cy-r*0.23),
                    size=(r*0.46, r*0.46))


class SkyrockApp(App):

    def build(self):
        self.root_layout = FloatLayout()

        with self.root_layout.canvas.before:
            Color(0.008, 0.018, 0.045, 1)
            self.bg = Ellipse(pos=(0, 0), size=(0, 0))

        self.root_layout.bind(
            size=self.update_bg,
            pos=self.update_bg
        )

        title = Label(
            text="S K Y R O C K",
            font_size=dp(30),
            bold=True,
            color=(0.1, 0.8, 1, 1),
            size_hint=(1, 0.1),
            pos_hint={"x": 0, "top": 0.95}
        )

        self.root_layout.add_widget(title)

        subtitle = Label(
            text="PERSONAL ARTIFICIAL INTELLIGENCE",
            font_size=dp(10),
            color=(0.3, 0.65, 0.85, 1),
            size_hint=(1, 0.05),
            pos_hint={"x": 0, "top": 0.84}
        )

        self.root_layout.add_widget(subtitle)

        reactor = Reactor(
            size_hint=(0.9, 0.48),
            pos_hint={"center_x": 0.5, "center_y": 0.54}
        )

        self.root_layout.add_widget(reactor)

        self.status = Label(
            text="SYSTEME EN ATTENTE",
            font_size=dp(14),
            color=(0.2, 0.85, 1, 1),
            size_hint=(1, 0.08),
            pos_hint={"center_x": 0.5, "center_y": 0.23}
        )

        self.root_layout.add_widget(self.status)

        button = Button(
            text="ACTIVER SKYROCK",
            font_size=dp(15),
            bold=True,
            color=(1, 1, 1, 1),
            background_normal="",
            background_color=(0, 0.35, 0.65, 1),
            size_hint=(0.72, 0.075),
            pos_hint={"center_x": 0.5, "center_y": 0.12}
        )

        button.bind(on_release=self.activate)

        self.root_layout.add_widget(button)

        return self.root_layout

    def update_bg(self, *args):
        self.bg.pos = (0, 0)
        self.bg.size = self.root_layout.size

    def activate(self, instance):
        self.status.text = "SKYROCK EST ACTIF"
        instance.text = "SKYROCK ACTIVE"

        try:
            tts.speak(
                "Bonjour Monsieur. "
                "Skyrock est opérationnel. "
                "Je suis à votre service."
            )
        except Exception as e:
            self.status.text = "ERREUR VOCALE"
            print("Erreur vocale :", e)


if __name__ == "__main__":
    SkyrockApp().run()
