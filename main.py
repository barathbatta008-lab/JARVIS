from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class JarvisApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="J.A.R.V.I.S",
            font_size=32
        )

        status = Label(
            text="SYSTEM ONLINE",
            font_size=20
        )

        self.command = TextInput(
            hint_text="Type a command...",
            multiline=False
        )

        button = Button(
            text="SEND",
            size_hint_y=None,
            height=60
        )

        self.reply = Label(
            text="Hello. I am JARVIS.",
            font_size=18
        )

        button.bind(on_press=self.process_command)

        layout.add_widget(title)
        layout.add_widget(status)
        layout.add_widget(self.command)
        layout.add_widget(button)
        layout.add_widget(self.reply)

        return layout

    def process_command(self, instance):
        command = self.command.text.lower().strip()

        if command == "vlsi":
            self.reply.text = "VLSI Specialist: Ready for chip design questions."

        elif command == "ece":
            self.reply.text = "ECE Specialist: Ready for electronics questions."

        elif command == "robotics":
            self.reply.text = "Robotics Specialist: Ready for robotics questions."

        elif command == "drone":
            self.reply.text = "Drone Specialist: Ready for safe hobby drone questions."

        elif command == "coding":
            self.reply.text = "Coding Specialist: Ready for programming questions."

        elif command in ["hi", "hello", "hey"]:
            self.reply.text = "Hello. JARVIS is online."

        else:
            self.reply.text = "I received: " + command


if __name__ == "__main__":
    JarvisApp().run()
