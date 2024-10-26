from prompt_toolkit.styles import Style


GLOBAL_TERM_STYLES = Style.from_dict(
    {
        "wlc_heading": "bold #00cc66",
        "wlc_list_item": "bold #ffcc00",
        "wlc_sub_list_item": "bold #5f5faf",
        "category_choice_prompt": "#66ff66",
        "operation_choice_prompt": "#ff6699",
        "error_prompt": "bold #ff3333",
        "number_input_prompt": "bold #ffa500",
        "result_output_prompt": "bold #00ced1",
        "result_error_prompt": "bold #ff4500",
    }
)
