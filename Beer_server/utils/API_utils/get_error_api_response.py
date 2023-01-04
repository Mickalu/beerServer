def handle_serializer_error(error_serializer):
    str_errors:str = ""

    list_errors_not_field = error_serializer.get("non_field_errors")

    if list_errors_not_field:
        for error in list_errors_not_field:
            str_errors += error.title()

    return str_errors
