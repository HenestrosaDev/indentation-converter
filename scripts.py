import subprocess


def test():
    """
    Run all unittests. Equivalent to:
    `poetry run python -m unittest discover tests`
    """
    subprocess.run(["python", "-m", "unittest", "discover", "."])
