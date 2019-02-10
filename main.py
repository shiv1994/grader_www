from src.webvalidator import *


if __name__ == "__main__":
    print("Executing main function ...")
    report = validateProject()
    f = open ("out.html", "a")
    f.write(report["./public/index.html"].content)