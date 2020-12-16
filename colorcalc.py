import kivy
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]
turq = [0,1,1,1]

class LayoutApp(App):
    def build(self):
        # creating top level layout
        main_layout = BoxLayout(orientation='vertical')
        self.solution = TextInput(readonly=True, multiline=False, size_hint_y=.5)

        # (multiline=False, readonly=True, fontsize=20, halign='left')
        colors = [red, green, purple, blue, turq]
        main_layout.add_widget(self.solution)

        # creating handy values
        self.last_btn = None
        self.last_was_operator = None

        # creating list of operators
        self.operators = ['/', '*', '-', '+']

        buttons = (
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '.', '+')
        
        # creating gridlayout for buttons, 4 columns, vertical size to 2 
        btn_grid = GridLayout(cols=4, size_hint_y=2)

        for i in buttons:
            # creating buttons for row. Binding them to an event handler then adding to layout (parent widget)
            # instantiating Button class
            btn = Button(
                text=i,
                pos_hint={'center_x': .5, 'center_y': .5},
                background_color = random.choice(colors)
            )
            # binding input, making sure when on_press occurs, function is called
            btn.bind(on_press=self.on_button_press)
            btn.bind(on_press=self.update_buttons)
            btn_grid.add_widget(btn)
        # adding to main layout
        main_layout.add_widget(btn_grid)

        equal_btn = Button(text='=', size_hint_y=.5, pos_hint={'center_x': .5, 'center_y': .5})
        # binding input 
        equal_btn.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_btn)

        return main_layout
    
    # changes color of buttons
    def update_buttons(self, btn):
        colors = [red, green, purple, blue, turq]
        btn.background_color=random.choice(colors)

    def on_button_press(self, instance):
        # store value of button press
        current = self.solution.text
        btn_text = instance.text

        # implementing clear button. If not clear, print text
        if btn_text == 'C':
            self.solution.text = ''
        else:
            # Making it so two operators cannot be input next to eachother
            if current and (self.last_was_operator and btn_text in self.operators):
                return
            # first character cannot be operator
            elif current == '' and btn_text in self.operators:
                return
            # if neither of above conditions are true, we can continue on to operation/ update solution
            else:
                new_text=current + btn_text
                self.solution.text = new_text

        # last_btn will be set to the button which was last pressed
        self.last_btn = btn_text
        # last_was_operator set to T or F depending on whether it was an op char or not
        self.last_was_operator = self.last_btn in self.operators

    def on_solution(self, instance):
        # using eval() to execute operation. grabbing current text from solution
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

    def resize_text(self, new_height):
        text = self.solution.text

        # event is named height
        text.font_size = .5*self.solution.height
        text.bind(height=resize_text)


if __name__=='__main__':
    app = LayoutApp()
    app.run()