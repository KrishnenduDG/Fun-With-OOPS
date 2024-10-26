from typing import List, Tuple
from prompt_toolkit import print_formatted_text
from styles import GLOBAL_TERM_STYLES
from prompt_toolkit import HTML
from constants import *


class InputHandler:
    def __init__(self) -> None:
        pass

    def _print_handler(self, msg: str, end="") -> None:
        """
        An abstraction layer over the `print_formatted_text` method
        """
        print_formatted_text(HTML(msg), style=GLOBAL_TERM_STYLES, end=end)

    def print(self, msg: str, end=""):
        """
        Exposing the Print Handler
        """
        self._print_handler(msg=msg, end=end)

    def print_welcome_message(self) -> None:
        """
        Prints the welcome message
        """
        self._print_handler(WELCOME_MSG)

    def input_numbers(self, number_prompts: List[str]) -> List[int]:
        """
        Take `n` number of numerical inputs with custom prompts
        """
        input_array = []

        for num_input_prompt in number_prompts:
            correct_input_found = False

            while not correct_input_found:
                self._print_handler(num_input_prompt)
                raw_input = input()
                try:
                    input_parsed = int(raw_input)
                    correct_input_found = True
                    input_array.append(input_parsed)
                except:
                    self._print_handler(INTEGER_EXPECTED_ERROR, end="\n")

        return input_array

    def category_validator(self, category_input: str) -> Tuple[bool, str]:
        """
        Validate the Category
        """
        try:
            chosen_category = int(category_input.strip())
            if chosen_category in [1, 2]:
                return True, ""
            else:
                return False, "Invalid Category"
        except:
            return False, "Category must be an integer"

    def operation_validator(
        self, category_input: int, operator_input: str
    ) -> Tuple[bool, str]:
        """
        Validate the Operation
        """
        valid_ops = (
            ["a", "b", "c", "d", "e", "f"]
            if category_input == 1
            else ["a", "b", "c", "d"]
        )
        if operator_input.strip() not in valid_ops:
            return False, "Invalid Operation"
        else:
            return True, ""

    def category_choice_looper(self) -> Tuple[str, None]:
        """
        Getting the proper category
        """
        proper_category = False
        chosen_categoryegory = None

        while not proper_category:
            self._print_handler(CATEGORY_CHOICE_PROMPT)

            catgeory_choice = input()
            if not catgeory_choice:
                return None

            flag, msg = self.category_validator(catgeory_choice)
            if flag:
                chosen_categoryegory = catgeory_choice
                proper_category = True
            else:
                self._print_handler(f"<error_prompt>{msg}</error_prompt>", end="\n\n")

        return chosen_categoryegory

    def operation_choice_looper(self, catgeory_choice: str) -> str:
        """
        Function to get proper operation based on a given category
        """
        proper_operator = False
        chosen_operator = None
        while not proper_operator:
            self._print_handler(OPERATION_CHOICE_PROMPT)

            operator_choice = input()
            if not operator_choice:
                return None

            flag, msg = self.operation_validator(
                category_input=catgeory_choice, operator_input=operator_choice
            )
            if flag:
                chosen_operator = operator_choice
                proper_operator = True
            else:
                self._print_handler(f"<error_prompt>{msg}</error_prompt>", end="\n\n")

        return chosen_operator

    def start_ip_loop(self):
        """
        The infinitely running (stop as you need) loop for taking and validating the inputs
        """
        while 1:
            catgeory_choice = self.category_choice_looper()
            if not catgeory_choice:
                yield None

            operator_choice = self.operation_choice_looper(
                catgeory_choice=int(catgeory_choice)
            )
            if not operator_choice:
                yield None

            yield [int(catgeory_choice), operator_choice]
