from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime
import ast
import operator


# -----------------------------
# Safe Calculator
# -----------------------------

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


# -----------------------------
# JARVIS
# -----------------------------

class JarvisApp(App):

    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        # Title
        title = Label(
            text="J.A.R.V.I.S",
            font_size=32,
            size_hint_y=None,
            height=60
        )

        layout.add_widget(title)

        # Status
        self.status = Label(
            text="SYSTEM ONLINE",
            font_size=18,
            size_hint_y=None,
            height=40
        )

        layout.add_widget(self.status)

        # Reply
        self.reply = Label(
            text=(
                "Hello. I am JARVIS.\n\n"
                "Your personal AI assistant is ready.\n\n"
                "Try:\n"
                "VLSI\n"
                "ECE\n"
                "CSE\n"
                "robotics\n"
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

        # Command box
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

        # Send button
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

    # -----------------------------
    # Process command
    # -----------------------------

    def process_command(self, instance):

        command = self.command.text.strip().lower()

        if not command:
            return

        response = self.get_response(command)

        self.reply.text = response

        self.command.text = ""

    # -----------------------------
    # JARVIS brain
    # -----------------------------

    def get_response(self, command):

        # Greeting
        if command in [
            "hi",
            "hello",
            "hey",
            "hi jarvis",
            "hello jarvis"
        ]:

            return (
                "Hello. JARVIS is online.\n\n"
                "How can I assist you?"
            )

        # Identity
        if "who are you" in command:

            return (
                "I am JARVIS, your personal AI assistant."
            )

        # Time
        if (
            command == "time"
            or "what time" in command
        ):

            current_time = datetime.now().strftime(
                "%I:%M %p"
            )

            return (
                "The current time is "
                + current_time
            )

        # Date
        if (
            command == "date"
            or "what date" in command
            or command == "today"
        ):

            current_date = datetime.now().strftime(
                "%d %B %Y"
            )

            return (
                "Today's date is "
                + current_date
            )

        # VLSI
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
                "• Counters"
            )

        # ECE
        if (
            command == "ece"
            or "electronics" in command
        ):

            return (
                "ECE Specialist activated.\n\n"
                "I can help with:\n"
                "• Analog electronics\n"
                "• Digital electronics\n"
                "• Signals and systems\n"
                "• Communication systems\n"
                "• Microprocessors\n"
                "• Microcontrollers\n"
                "• Embedded systems"
            )

        # CSE
        if (
            command == "cse"
            or "computer science" in command
        ):

            return (
                "CSE Specialist activated.\n\n"
                "I can help with:\n"
                "• Python\n"
                "• C\n"
                "• C++\n"
                "• Java\n"
                "• Data structures\n"
                "• Algorithms\n"
                "• Databases\n"
                "• Operating systems\n"
                "• Computer networks\n"
                "• AI and machine learning"
            )

        # Robotics
        if (
            "robotics" in command
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

        # Drone
        if "drone" in command:

            return (
                "Drone Education module activated.\n\n"
                "I can explain:\n"
                "• Drone components\n"
                "• Flight controllers\n"
                "• Sensors\n"
                "• Motors\n"
                "• ESC concepts\n"
                "• GPS concepts\n"
                "• Stabilization\n"
                "• Drone electronics\n"
                "• Flight-control theory"
            )

        # Coding
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
                "• Debugging"
            )

        # Transistor
        if (
            "what is transistor" in command
            or "what is a transistor" in command
            or command == "transistor"
        ):

            return (
                "A transistor is a semiconductor device "
                "used for switching and amplification.\n\n"
                "Common types are BJT and MOSFET.\n\n"
                "MOSFETs are fundamental components "
                "of modern CMOS VLSI circuits."
            )

        # Logic gates
        if "logic gate" in command:

            return (
                "Logic gates are digital circuits "
                "that perform Boolean operations.\n\n"
                "AND\n"
                "OR\n"
                "NOT\n"
                "NAND\n"
                "NOR\n"
                "XOR\n"
                "XNOR"
            )

        # Calculator
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

        # Direct calculation
        if all(
            character in "0123456789+-*/(). %"
            for character in command
        ):

            return (
                "Calculation result: "
                + calculate(command)
            )

        # Help
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
                "transistor\n"
                "logic gate\n"
                "time\n"
                "date\n"
                "calculate 100+50"
            )

        # Unknown
        return (
            "I received your command:\n\n"
            + command
            + "\n\n"
            "Try VLSI, ECE, CSE, robotics, "
            "drone, coding, time, date or help."
        )


# -----------------------------
# Start JARVIS
# -----------------------------

if __name__ == "__main__":
    JarvisApp().run()
    
