import subprocess


def check_style(file_path):
    try:
        pylint_result = subprocess.run(
            ["pylint", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        ).stdout
    except Exception as ex:
        print(f"error with pylint analiz\n{ex}")
        pylint_result = "pylint error"

    try:
        flake8_result = subprocess.run(
            ["flake8", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        ).stdout
    except Exception as ex:
        print(f"error with flake8 analiz\n{ex}")
        flake8_result = "flake8 error"

    return (pylint_result, flake8_result)
