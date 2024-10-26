from prompt_toolkit.styles import Style


GLOBAL_TERM_STYLES = Style.from_dict(
    {
        "wlc_heading": "bold #00cc66",  # Bright green, bold for main headings
        "wlc_list_item": "bold #ffcc00",  # Yellow, bold for main list items
        "wlc_sub_list_item": "bold #5f5faf",  # Dark blue, bold for sub-list items
        "category_choice_prompt": "#66ff66",  # Light green for category prompt
        "operation_choice_prompt": "#ff6699",  # Pinkish-red for operation prompt
        "error_prompt": "bold #ff3333",  # Bright red, bold for errors
        "number_input_prompt": "bold #ffa500",  # Orange, bold for numeric input prompt
        "result_output_prompt": "bold #00ced1",  # Bright cyan, bold for results
        "result_error_prompt": "bold #ff4500",  # Orange-red, bold for result errors
    }
)
