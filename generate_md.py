from objects import *  # pylint: disable=wildcard-import,unused-wildcard-import
USERNAME: str = "danielnachumdev"
LANGUAGES_AND_TOOLS: list[str] = sorted([
    "python", "c", "cplusplus", "csharp", "java",
    "javascript", "css3", "html5", "postgresql",
    "cmake", "git", "linux", "docker", "vim",
    "jetbrains", "markdown", "mongodb",
    "numpy", "pandas", "pytest", "react",
    "anaconda", "blender", "bootstrap", "canva", "express",
    "gcc", "github"
])
STATISTICS_SRC: list[str] = [
    f"https://github-readme-stats.vercel.app/api/top-langs?username={USERNAME}&show_icons=true&locale=en&layout=compact&theme=grovbox",
    f"https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&locale=en&theme=grovbox",
    f"https://github-readme-streak-stats.herokuapp.com/?user={USERNAME}&theme=grovbox"
]
REPOS_TO_HIGHLIGHT: list[str] = [
    "danielutils",
    "gp_warpper",
    "SSH2HUJI",
    "scraper_ex",
    "python-la"
]

README: list[Markdownable] = [
    Comment("markdownlint-disable MD033 MD041"),
    Heading1("Daniel Nachum"),
    Section(
        title=Heading2("About me"),
        objects=[
            Text("My name is Daniel Nachum and I am a Software Developer")
        ]
    ),
    Section(
        title=Heading2("Languages & Tools"),
        objects=[IconSvg(name) for name in LANGUAGES_AND_TOOLS]
    ),

    Section(
        title=Heading2("Highlighted Projects"),
        objects=[
            UnorderedList([Repository(name, user=USERNAME)
                           for name in REPOS_TO_HIGHLIGHT])
        ]
    ),
    Section(
        title=Heading2("Statistics"),
        objects=[Image(src=src, alt=USERNAME)
                 for src in STATISTICS_SRC]
    ),
]


def main() -> None:
    with open("./README.md", "w", encoding="utf8") as f:
        for obj in README:
            f.write(obj.to_markdown())


if __name__ == "__main__":
    main()
