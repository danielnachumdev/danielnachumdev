from objects import *  # pylint: disable=wildcard-import,unused-wildcard-import

LANGUAGES_AND_TOOLS = sorted([
    "python", "c", "cplusplus", "csharp", "java",
    "javascript", "css3", "html5", "postgresql", "make",
    "cmake", "git", "linux", "docker", "vim",
    "jetbrains", "markdown", "mongodb", "sql", "npm",
    "numpy", "pandas", "pytest", "react", "visualstudio",
    "anaconda", "blender", "bootstrap", "canva", "express",
    "gcc", "github"
])

README: list[Markdownable] = [
    Comment("markdownlint-disable MD033 MD041"),
    Heading("Daniel Nachum"),
    Section(
        objects=[IconSvg(name) for name in LANGUAGES_AND_TOOLS],
        title=Heading("Languages & Tools", 2)
    )
]


def main() -> None:
    with open("./README.md", "w", encoding="utf8") as f:
        for obj in README:
            f.write(obj.to_markdown())


if __name__ == "__main__":
    main()
