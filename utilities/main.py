from kivy.app import App
from kivy.uix.label import Label
from kiwisolver import Solver, Variable

class HelloWorldApp(App):
    def build(self):
        # Create a solver instance
        solver = Solver()

        # Create a variable
        var = Variable('example')

        # Add a constraint (just a simple example)
        solver.addConstraint(var == 10)

        # Solve the constraints
        solver.updateVariables()

        # Check if the variable meets the constraint and set the label text accordingly
        if var.value() == 10:
            return Label(text="Hello, World!")
        else:
            return Label(text="Failed to solve constraints")

if __name__ == '__main__':
    HelloWorldApp().run()
