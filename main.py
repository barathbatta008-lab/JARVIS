from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime
import ast
import operator


# =========================
# SAFE CALCULATOR
# =========================

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}


def calculate(expression):
    try:
        tree = ast.parse(expression, mode="eval")

        def solve(node):

            if isinstance(node, ast.Expression):
                return solve(node.body)

            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                raise ValueError()

            if isinstance(node, ast.BinOp):

                operation = OPERATORS.get(type(node.op))

                if operation is None:
                    raise ValueError()

                left = solve(node.left)
                right = solve(node.right)

                # Safety limit for powers
                if isinstance(node.op, ast.Pow) and abs(right) > 10:
                    raise ValueError()

                return operation(left, right)

            if isinstance(node, ast.UnaryOp):

                value = solve(node.operand)

                if isinstance(node.op, ast.USub):
                    return -value

                if isinstance(node.op, ast.UAdd):
                    return value

            raise ValueError()

        result = solve(tree)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return str(result)

    except Exception:
        return "I could not calculate that."


# =========================
# JARVIS APP
# =========================

class JarvisApp(App):

    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        # TITLE
        title = Label(
            text="J.A.R.V.I.S",
            font_size=32,
            size_hint_y=None,
            height=60
        )

        layout.add_widget(title)

        # STATUS
        status = Label(
            text="SYSTEM ONLINE",
            font_size=18,
            size_hint_y=None,
            height=40
        )

        layout.add_widget(status)

        # RESPONSE AREA
        self.reply = Label(
            text=(
                "Hello. I am JARVIS.\n\n"
                "Your personal AI assistant is ready.\n\n"
                "Try:\n"
                "VLSI\n"
                "ECE\n"
                "CSE\n"
                "robotics\n"
                "drone\n"
                "coding\n"
                "time\n"
                "date\n"
                "calculate 25+25"
            ),
            font_size=17,
            halign="left",
            valign="top"
        )

        self.reply.bind(
            size=lambda obj, value:
            setattr(obj, "text_size", value)
        )

        layout.add_widget(self.reply)

        # COMMAND BOX
        self.command = TextInput(
            hint_text="Type a command...",
            multiline=False,
            size_hint_y=None,
            height=55,
            font_size=18
        )

        self.command.bind(
            on_text_validate=self.process_command
        )

        layout.add_widget(self.command)

        # SEND BUTTON
        button = Button(
            text="SEND",
            font_size=20,
            size_hint_y=None,
            height=55
        )

        button.bind(
            on_press=self.process_command
        )

        layout.add_widget(button)

        return layout

    # =========================
    # PROCESS COMMAND
    # =========================

    def process_command(self, instance):

        command = self.command.text.strip().lower()

        if not command:
            return

        response = self.get_response(command)

        self.reply.text = response

        self.command.text = ""

        self.speak(response)

    # =========================
    # JARVIS BRAIN
    # =========================

    def get_response(self, command):

        # -------------------------
        # GREETING
        # -------------------------

        if command in [
            "hi",
            "hello",
            "hey",
            "hi jarvis",
            "hello jarvis"
        ]:

            return (
                "Hello. JARVIS is online.\n"
                "How can I assist you?"
            )

        # -------------------------
        # IDENTITY
        # -------------------------

        if "who are you" in command:

            return (
                "I am JARVIS, your personal AI assistant."
            )

        # -------------------------
        # TIME
        # -------------------------

        if command == "time" or "what time" in command:

            current_time = datetime.now().strftime(
                "%I:%M %p"
            )

            return (
                "The current time is "
                + current_time
            )

        # -------------------------
        # DATE
        # -------------------------

        if command == "date" or "today" in command:

            current_date = datetime.now().strftime(
                "%d %B %Y"
            )

            return (
                "Today's date is "
                + current_date
            )

        # -------------------------
        # VLSI
        # -------------------------

        if "vlsi" in command:

            return (
                "VLSI Specialist activated.\n\n"
                "I can help with:\n"
                "• Digital logic\n"
                "• Boolean algebra\n"
                "• CMOS circuits\n"
                "• Semiconductor basics\n"
                "• Verilog\n"
                "• Logic gates\n"
                "• Flip-flops\n"
                "• Registers\n"
                "• Counters\n"
                "• VLSI calculations"
            )

        # -------------------------
        # ECE
        # -------------------------

        if command == "ece" or "electronics" in command:

            return (
                "ECE Specialist activated.\n\n"
                "I can help with:\n"
                "• Electronic circuits\n"
                "• Analog electronics\n"
                "• Digital electronics\n"
                "• Signals and systems\n"
                "• Communication systems\n"
                "• Microprocessors\n"
                "• Microcontrollers\n"
                "• Embedded systems"
            )

        # -------------------------
        # CSE
        # -------------------------

        if (
            command == "cse"
            or "computer science" in command
            or "computer science engineering" in command
        ):

            return (
                "CSE Specialist activated.\n\n"
                "I can help with:\n"
                "• Python programming\n"
                "• C programming\n"
                "• C++ programming\n"
                "• Java basics\n"
                "• Data structures\n"
                "• Algorithms\n"
                "• Object-oriented programming\n"
                "• Databases\n"
                "• Operating systems\n"
                "• Computer networks\n"
                "• Web development\n"
                "• AI and machine learning\n"
                "• Software engineering"
            )

        # -------------------------
        # ROBOTICS
        # -------------------------

        if (
            "robotics" in command
            or command == "robot"
            or "robot" in command
        ):

            return (
                "Robotics Specialist activated.\n\n"
                "Topics:\n"
                "• Sensors\n"
                "• Motors\n"
                "• Microcontrollers\n"
                "• Control systems\n"
                "• Embedded programming\n"
                "• Robot navigation"
            )

        # -------------------------
        # DRONE EDUCATION
        # -------------------------

        if "drone" in command:

            return (
                "Drone Education module activated.\n\n"
                "I can explain:\n"
                "• Drone components\n"
                "• Flight controllers\n"
                "• Sensors\n"
                "• Motors and propellers\n"
                "• ESC concepts\n"
                "• Battery basics\n"
                "• GPS concepts\n"
                "• Stabilization\n"
                "• Drone electronics\n"
                "• Flight-control theory\n\n"
                "Guidance is limited to safe "
                "educational and legal uses."
            )

        # -------------------------
        # CODING
        # -------------------------

        if (
            "coding" in command
            or "programming" in command
            or command == "python"
        ):

            return (
                "Coding Specialist activated.\n\n"
                "I can help with:\n"
                "• Python\n"
                "• Programming logic\n"
                "• Variables\n"
                "• Loops\n"
                "• Functions\n"
                "• Classes\n"
                "• Debugging\n"
                "• AI programming"
            )

        # -------------------------
        # CALCULATOR
        # -------------------------

        if command.startswith("calculate "):

            expression = command.replace(
                "calculate ",
                "",
                1
            ).strip()

            return (
                "Calculation result: "
                + calculate(expression)
            )

        # -------------------------
        # SIMPLE CALCULATION
        # -------------------------

        if all(
            character in "0123456789+-*/(). %"
            for character in command
        ):

            return (
                "Calculation result: "
                + calculate(command)
            )

        # -------------------------
        # HELP
        # -------------------------

        if (
            command == "help"
            or "what can you do" in command
        ):

            return (
                "JARVIS command center:\n\n"
                "VLSI\n"
                "ECE\n"
                "CSE\n"
                "robotics\n"
                "drone\n"
                "coding\n"
                "time\n"
                "date\n"
                "calculate 100+50\n"
                "hello"
            )

        # -------------------------
        # UNKNOWN COMMAND
        # -------------------------

        return (
            "I received your command:\n\n"
            + command
            + "\n\n"
            "Try VLSI, ECE, CSE, robotics, "
            "drone, coding, time, date or help."
        )

    # =========================
    # ANDROID VOICE
    # =========================

    def speak(self, text):

        try:

            from jnius import autoclass

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            TextToSpeech = autoclass(
                "android.speech.tts.TextToSpeech"
            )

            activity = PythonActivity.mActivity

            def on_init(status):

                if status == TextToSpeech.SUCCESS:

                    tts.speak(
                        text,
                        TextToSpeech.QUEUE_FLUSH,
                        None,
                        "JARVIS"
                    )

            tts = TextToSpeech(
                activity,
                on_init
            )

        except Exception:
            pass


# =========================
# START JARVIS
# =========================

if __name__ == "__main__":
    JarvisApp().run()
