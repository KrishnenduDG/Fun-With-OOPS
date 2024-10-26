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
        ip_array = []

        for num_ip_prompt in number_prompts:
            correct_ip_found = False

            while not correct_ip_found:
                self._print_handler(num_ip_prompt)
                raw_ip = input()
                try:
                    ip_parsed = int(raw_ip)
                    correct_ip_found = True
                    ip_array.append(ip_parsed)
                except:
                    self._print_handler(INTEGER_EXPECTED_ERROR, end="\n")

        return ip_array

    def category_validator(self, cat_ip: str) -> Tuple[bool, str]:
        """
        Validate the Category
        """
        try:
            chosen_cat = int(cat_ip.strip())
            if chosen_cat in [1, 2]:
                return True, ""
            else:
                return False, "Invalid Category"
        except:
            return False, "Category must be an integer"

    def operation_validator(self, cat_ip: int, op_ip: str) -> Tuple[bool, str]:
        """
        Validate the Operation
        """
        valid_ops = (
            ["a", "b", "c", "d", "e", "f"] if cat_ip == 1 else ["a", "b", "c", "d"]
        )
        if op_ip.strip() not in valid_ops:
            return False, "Invalid Operation"
        else:
            return True, ""

    def category_choice_looper(self) -> Tuple[str, None]:
        """
        Getting the proper category
        """
        proper_category = False
        chosen_category = None

        while not proper_category:
            self._print_handler(CATEGORY_CHOICE_PROMPT)

            cat_choice = input()
            if not cat_choice:
                return None

            flag, msg = self.category_validator(cat_choice)
            if flag:
                chosen_category = cat_choice
                proper_category = True
            else:
                self._print_handler(f"<error_prompt>{msg}</error_prompt>", end="\n\n")

        return chosen_category

    def operation_choice_looper(self, cat_choice: str) -> str:
        """
        Function to get proper operation based on a given category
        """
        proper_ops = False
        chosen_ops = None
        while not proper_ops:
            self._print_handler(OPERATION_CHOICE_PROMPT)

            op_choice = input()
            if not op_choice:
                return None

            flag, msg = self.operation_validator(cat_ip=cat_choice, op_ip=op_choice)
            if flag:
                chosen_ops = op_choice
                proper_ops = True
            else:
                self._print_handler(f"<error_prompt>{msg}</error_prompt>", end="\n\n")

        return chosen_ops

    def start_ip_loop(self):
        """
        The infinitely running (stop as you need) loop for taking and validating the inputs
        """
        while 1:
            cat_choice = self.category_choice_looper()
            if not cat_choice:
                yield None

            op_choice = self.operation_choice_looper(cat_choice=int(cat_choice))
            if not op_choice:
                yield None

            yield [int(cat_choice), op_choice]
