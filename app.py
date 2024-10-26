from input import InputHandler
from constants import *
from operations import *
from exceptions import *

if __name__ == "__main__":
    ip_handler = InputHandler()
    ip_handler.print_welcome_message()
    ip_loop = ip_handler.start_ip_loop()

    while True:
        user_input = next(ip_loop)
        if not user_input:
            ip_handler.print()
            exit(0)
        else:
            cat, op = user_input

            # Arithmetic Case
            if cat == 1:
                # Addition
                if op == "a":
                    num1, num2 = ip_handler.input_numbers(ADD_SUBTRACT_MULTIPLY_PROMPT)
                    ip_handler.print(
                        f"<result_output_prompt>Addition Result is {ArithmeticOps.add(num1,num2)}</result_output_prompt>",
                        end="\n\n",
                    )

                # Subtraction
                elif op == "b":
                    num1, num2 = ip_handler.input_numbers(ADD_SUBTRACT_MULTIPLY_PROMPT)
                    ip_handler.print(
                        f"<result_output_prompt>Subtraction Result is {ArithmeticOps.subtract(num1,num2)}</result_output_prompt>",
                        end="\n\n",
                    )

                # Multiplication
                elif op == "c":
                    num1, num2 = ip_handler.input_numbers(ADD_SUBTRACT_MULTIPLY_PROMPT)
                    ip_handler.print(
                        f"<result_output_prompt>Multiplication Result is {ArithmeticOps.multiply(num1,num2)}</result_output_prompt>",
                        end="\n\n",
                    )

                # Division
                elif op == "d":
                    num1, num2 = ip_handler.input_numbers(DIVISION_PROMPT)

                    try:
                        ip_handler.print(
                            f"<result_output_prompt>Division Result is {ArithmeticOps.divide(num1,num2)}</result_output_prompt>",
                            end="\n\n",
                        )
                    except ArithmeticException as e:
                        ip_handler.print(
                            f"<result_error_prompt>{e.msg}</result_error_prompt>",
                            end="\n\n",
                        )

                # Exponentiation
                elif op == "e":
                    num1, num2 = ip_handler.input_numbers(EXPONENT_PROMPT)
                    try:
                        ip_handler.print(
                            f"<result_output_prompt>Exponentiation Result is {ArithmeticOps.exponent(num1,num2)}</result_output_prompt>",
                            end="\n\n",
                        )
                    except ArithmeticException as e:
                        ip_handler.print(
                            f"<result_error_prompt>{e.msg}</result_error_prompt>",
                            end="\n\n",
                        )

                # Factorial
                else:
                    num_ips = ip_handler.input_numbers(FACTORIAL_PROMPT)
                    try:
                        ip_handler.print(
                            f"<result_output_prompt>Factorial is {ArithmeticOps.factorial(num_ips[0])}</result_output_prompt>",
                            end="\n\n",
                        )
                    except ArithmeticException as e:
                        ip_handler.print(
                            f"<result_error_prompt>{e.msg}</result_error_prompt>",
                            end="\n\n",
                        )
            else:
                # Area of Square
                if op == "a":
                    num_ips = ip_handler.input_numbers(SQUARE_PROMPT)
                    try:
                        ip_handler.print(
                            f"<result_output_prompt>Area of Square is {GeometricOps.area_square(num_ips[0])}</result_output_prompt>",
                            end="\n\n",
                        )
                    except GeometricException as e:
                        ip_handler.print(
                            f"<result_error_prompt>{e.msg}</result_error_prompt>",
                            end="\n\n",
                        )

                # Area of Rectangle
                elif op == "b":
                    num1, num2 = ip_handler.input_numbers(RECTANGLE_PROMPT)
                    try:
                        ip_handler.print(
                            f"<result_output_prompt>Area of Rectangle is {GeometricOps.area_rect(num1,num2)}</result_output_prompt>",
                            end="\n\n",
                        )
                    except GeometricException as e:
                        ip_handler.print(
                            f"<result_error_prompt>{e.msg}</result_error_prompt>",
                            end="\n\n",
                        )

                # Area of Circle
                elif op == "c":
                    num_ips = ip_handler.input_numbers(CIRCLE_PROMPT)
                    try:
                        ip_handler.print(
                            f"<result_output_prompt>Area of Cicrle is {GeometricOps.area_circle(num_ips[0])}</result_output_prompt>",
                            end="\n\n",
                        )
                    except GeometricException as e:
                        ip_handler.print(
                            f"<result_error_prompt>{e.msg}</result_error_prompt>",
                            end="\n\n",
                        )

                # Circumference of Circle
                elif op == "d":
                    num_ips = ip_handler.input_numbers(CIRCLE_PROMPT)
                    try:
                        ip_handler.print(
                            f"<result_output_prompt>Circumference of Cicrle is {GeometricOps.circumference_circle(num_ips[0])}</result_output_prompt>",
                            end="\n\n",
                        )
                    except GeometricException as e:
                        ip_handler.print(
                            f"<result_error_prompt>{e.msg}</result_error_prompt>",
                            end="\n\n",
                        )

            ip_handler.print(msg=PROMPT_DIRECTIVES)