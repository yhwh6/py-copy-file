def copy_file(command: str) -> None:
    if len(command) == 3:
        cp, current_file_name, copied_file_name = command.split()

        if cp == "cp" and current_file_name != copied_file_name:
            with (
                open(f"{current_file_name}.txt", "r") as file_to_copy,
                open(f"{copied_file_name}.txt", "w") as file_result
            ):
                file_result.write(file_to_copy.read())
