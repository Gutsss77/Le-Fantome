import subprocess


def open_application(app_name: str) -> str:
    try:
        subprocess.run(
            ["open", "-a", app_name],
            check=True
        )
        return f"Successfully opened {app_name}."

    except subprocess.CalledProcessError:
        return f"Could not open application: {app_name}"