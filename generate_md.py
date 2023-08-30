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
    Heading1("Daniel Nachum"),
    Section(
        title=Heading2("About me"),
    ),
    Section(
        title=Heading2("Languages & Tools"),
        objects=[IconSvg(name) for name in LANGUAGES_AND_TOOLS]
    ),
    Section(
        title=Heading2("Projects Highlight"),
    ),
    Section(
        title=Heading2("Statistics"),
        objects=[
            Image("https://github-readme-stats.vercel.app/api/top-langs?username=danielnachumdev&show_icons=true&locale=en&layout=compact&theme=grovbox", alt="danielnachumdev"),
            Image("https://github-readme-stats.vercel.app/api?username=danielnachumdev&show_icons=true&locale=en&theme=grovbox", alt="danielnachumdev"),
            Image(
                "https://github-readme-streak-stats.herokuapp.com/?user=danielnachumdev&theme=grovbox", alt="danielnachumdev"),
        ]
    ),
]
# <p><img align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username=danielnachumdev&show_icons=true&locale=en&layout=compact&theme=grovbox" alt="danielnachumdev" /></p>

# <p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=danielnachumdev&show_icons=true&locale=en&theme=grovbox" alt="danielnachumdev" /></p>

# <p><img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=danielnachumdev&theme=grovbox" alt="danielnachumdev" /></p>


def main() -> None:
    with open("./README.md", "w", encoding="utf8") as f:
        for obj in README:
            f.write(obj.to_markdown())


if __name__ == "__main__":
    main()
