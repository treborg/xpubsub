import os.path
import subprocess


def readfile(fn):
    if not os.path.isfile(fn):
        raise Exception(f"file '{fn}' not found")
    with open(fn) as f:
        return f.read()


def writefile(fn, text):
    with open(fn, "w") as f:
        f.write(text)


def runfile(fn):
    result = subprocess.run(
        ["python", fn],
        encoding="utf-8",
        capture_output=True,
    )
    result.check_returncode()
    return result.stdout


def compose(tpl):
    lines = readfile(tpl).splitlines()
    for i, line in enumerate(lines):
        if line.startswith("{%I"):
            fn = line[3:].strip()
            lines[i] = readfile(fn)
        elif line.startswith("{%R"):
            fn = line[3:].strip()
            lines[i] = runfile(fn)
    return "\n".join(lines)


def compose_readme():
    writefile("README.md", compose(".readme.tpl.md"))


if __name__ == "__main__":
    compose_readme()
