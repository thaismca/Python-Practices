
# ROAD RUNNER CALCULATOR

This app implements a calculator that makes conversions from miles to kilomenters and vice-versa. It works for pace, speed and distance.

Implemented as part of the day 27 of the course *100 days of Python*.
Goal of the project was to practice with Tkinter to create GUI Programs.

## Key differences from course solution

This implementation was inspired by the project proposed in the course, but it has way more features.

**Course project scope:** create program that simply converts miles to kilometers. It has one input where the value to be converted can be entered, and a calculate button. Displays a label with the result when the button is clicked.

**This project scope:** program that converts units for a value based on user selection. It works to convert distance, speed and pace, and can do both mile -> kilometer and the opposite.

## How this app works

1. User can choose either one of the conversion types (radio button selector): distance, speed or pace. Distance is selected by default when the application starts.

2. The base unit selector (dropdown menu) changes options based on the conversion type selection:
- Distance: mi (miles) or km (kilometers)
- Speed: mph or kph
- Pace: min/mi or min/km

3. For all conversion types, user can choose to convert from miles to kilometers, or the opposite.

4. User can input the value to be converted in the entry input. Note that the entry expects a specific type and format, depending on the conversion type that was selected. Failing to enter data in the expected format will display an error message when clicking the 'calculate' button.
- Distance and Speed: expect a numeric value, with or without decimals
- Pace: expects numeric values for minutes and seconds, in the format minutes:seconds

5. When the user enters a valid input and clicks the 'calculate' button, a conversion formula will be applied and a label with the result will be displayed. This label change sat every new calculation.

6. Distance and Speed results will always be displayed with two decimal places.
## Implementation notes

Implemented using a class Runner_Conversion_Calculator that handles all the components creation and the respective changes that are applied to these components, based on the user interaction with the application.

**Conversion options**
  - dictionary containing conversion types and the respective units supported by this application
  - conversion types -> dictionary keys: Distance, Speed, Pace
  - units -> values associated with each key

**Conversion type**
  - conversion_type options -> serie of radio buttons selectors, for the conversion type
  - options are based on the keys of the conversion options dictionary (distance, speed, pace)
  - conversion_type_state -> variable to hold on to the selected state of conversion type
  - changes applied to conversion_type_state are traced and, whenever they happen (when a new option is selected) that impacts the options in the base_unit_options dropdown, the placeholder in the user_input entry, and the formula applied to the calculate_button command

**Base unit**  
  - base_unit_options -> base unit dropdown selector
  - options in this dropdown will change based on the conversion type that is currently selected, and will be comprised of the values for the key in the conversion_options dictionary that match this conversion type selection 
  - base_unit_state -> variable to hold on to the selected state of base unit
  - changes applied to the base_unit_state are traced and, whenever they happen (when a new option is selected) that impacts the current result_target_unit, which will be the other option taht is not currently selected as base unit

**User input**
  - user_input -> entry where the user can input a value to be converted
  - expects a specific type and format, depending on the conversion type that was selected, and failing to enter data in the expected format will display an error message when clicking the 'calculate' button
  - placeholder was added to help the user understand the expected format, and it changes based on the conversion type selection
  - placeholder is deleted whe user focus in the entry, and it is added back if the user leaves the input without entering some value
  - Distance and Speed: expect a numeric value, with or without decimals
  - Pace: expects numeric values for minutes and seconds, in the format minutes:seconds

**Calculate button**
  - calculate_button: button that will apply a conversion formula, based on the conversion type selected, and change the text for the result_label

**Result**
  - result -> variable that holds the latest result string containing the calculation result that can come either from pace_converter() or distance_speed_converter()
  - result_target_unit -> variable that hold the current target unit, based on whatever that is selected as base unit
  - result_label -> label that is used to output a string containing the conversion result

-----
**METHODS**

*create_screen_elements():*
- It's called in the __init__ method of the Runner_Conversion_Calculator class
- Creates all elements present in the screen for the application


*update_unit_option():*
- Method that applies changes to the base unit dropdown selector, and its called when there are changes in the conversion type that is currently selected.
- Base unit dropdown selector options will be comprised of the values for the key in the conversion_options dictionary that match this conversion type selection
- The first value in the base unit options will be selected as base unit by default, and the second one will be set as target unit.


*set_target_unit():*
- Method that applies changes to the result_target_unit, and its called when there are changes in the base unit that is currently selected.
- It sets taget unit as the other option in the dropdown which is not the one that is currently selected


*update_input_placeholder():*
- Method that applies changes to user_input placeholder, and its called when there are changes in the conversion type that is currently selected, or when user takes focus out of the input without entering some value
- The placeholder has the format expected for the user input, depending on the conversion typw that is currently selected


*focus_in_input():*
- Method that is called when user focuses in the user_input
- Removes the placeholder text
- Won't remove text that was entered by the user, since it will first check if the current value matches the placeholder value


*focus_out_input():*
- Method that is called when user focuses out of the user_input
- Addes the placeholder text back, if the user leaves the entry without entering some value


*define_button_command():*
- Method that applies changes to the calculate_button, and its called when there are changes in the conversion type that is currently selected
- Defines calculation to be performed when button is clicked


*display_result():*
- Puts together a string with the result and sets it as text attribute for the result_label
- Called after the calculations in either one of the conversion formulas is done and there is a new result to be displayed


*distance_speed_converter():*
- Converts inputted distance or speed from base unit selected in the dropdown menu to its target pair
- Command applied to the calculate_button when the conversion type selected is either Distance or Speed
- Expects a numeric value
- Distance and Speed results will always be displayed with two decimal places
- If value is not valid, it changes the result_label to output an error string


*pace_converter():*
- Converts inputted pace from base unit selected in the dropdown menu to its target pair
- Command applied to the calculate_button when the conversion type selected is Pace
- Expects input in the format minutes:seconds, where both minutes and seconds are both numeric
- If value is not valid, it changes the result_label to output an error string