# Inheriting the Base Exception
class ArithmeticException(Exception):
    def __init__(
        self,
        msg: str,
        fn_name: str,
        *args: object,
    ) -> None:
        super().__init__(*args)
        self.msg = msg
        self.fn = fn_name
