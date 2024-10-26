CATEGORY_CHOICE_PROMPT = "<category_choice_prompt>Enter the Category (Leave Empty to Exit):</category_choice_prompt>"


OPERATION_CHOICE_PROMPT = "<operation_choice_prompt>Enter the Operation (Leave Empty to Exit):</operation_choice_prompt>"

PROMPT_DIRECTIVES = """
Here, we provide the features like
1. <wlc_list_item>Arithmetic Operations</wlc_list_item>
    a  <wlc_sub_list_item>Addition</wlc_sub_list_item>
    b. <wlc_sub_list_item>Subtraction</wlc_sub_list_item>
    c. <wlc_sub_list_item>Multiplication</wlc_sub_list_item>
    d. <wlc_sub_list_item>Division</wlc_sub_list_item>
    e. <wlc_sub_list_item>Exponentiation</wlc_sub_list_item>
    f. <wlc_sub_list_item>Factorial</wlc_sub_list_item>

2. <wlc_list_item>Geometric Operations</wlc_list_item>
    a. <wlc_sub_list_item>Area of Square</wlc_sub_list_item>
    b. <wlc_sub_list_item>Area of Rectangle</wlc_sub_list_item>
    c. <wlc_sub_list_item>Area of Circle</wlc_sub_list_item>
    d. <wlc_sub_list_item>Circumference of Circle</wlc_sub_list_item>
"""

GOODBYE_MSG = """<wlc_heading>Thank you for using the calculator!!</wlc_heading>"""


WELCOME_MSG = f"""
<wlc_heading>Hola! Welcome to our Mathemtical Calculator App</wlc_heading>
{PROMPT_DIRECTIVES}
"""


INTEGER_EXPECTED_ERROR = """<error_prompt>Only Integer Value expected..</error_prompt>
"""

ADD_SUBTRACT_MULTIPLY_PROMPT = [
    "<number_input_prompt>Enter the First Number:</number_input_prompt>",
    "<number_input_prompt>Enter the Second Number:</number_input_prompt>",
]
DIVISION_PROMPT = [
    "<number_input_prompt>Enter the Numerator:</number_input_prompt>",
    "<number_input_prompt>Enter the Denominator (Non 0):</number_input_prompt>",
]
FACTORIAL_PROMPT = [
    "<number_input_prompt>Enter a non-negative number:</number_input_prompt>"
]
EXPONENT_PROMPT = [
    "<number_input_prompt>Enter a number:</number_input_prompt>",
    "<number_input_prompt>Enter the exponent:</number_input_prompt>",
]


SQUARE_PROMPT = [
    "<number_input_prompt>Enter the length of the square:</number_input_prompt>"
]
RECTANGLE_PROMPT = [
    "<number_input_prompt>Enter the length of the rectangle:</number_input_prompt>",
    "<number_input_prompt>Enter the breadth of the rectangle:</number_input_prompt>",
]
CIRCLE_PROMPT = [
    "<number_input_prompt>Enter the length of radius:</number_input_prompt>"
]
