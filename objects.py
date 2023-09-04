from typing import Optional, Self
from abc import ABC, abstractmethod
import urllib.parse
import json


class Markdownable(ABC):
    @abstractmethod
    def to_markdown(self) -> str: ...


class Tag(Markdownable):
    def __init__(self, name: str, contents: Optional["Tag"] = None, /, **kwargs) -> None:
        self.name = name
        self.kwargs = kwargs
        self.contents = contents

    def to_markdown(self) -> str:
        res = ""
        if self.contents:
            res += f"<{self.name}"
        else:
            res += f"</{self.name}"

        for key, value in self.kwargs.items():
            pass

        if self.contents:
            res += ">\n"+self.contents.to_markdown()+f"</{self.name}>\n"
        else:
            res += ">\n"
        return res


class Text(Markdownable):
    def __init__(self, text: str) -> None:
        self.text = text

    def to_markdown(self) -> str:
        return f"{self.text}\n"


class Comment(Text):
    def __init__(self, comment: str) -> None:
        super().__init__(f"<!-- {comment}-->\n")


class Section(Markdownable):
    def __init__(self, *, title: Optional["Heading"] = None, objects: Optional[list[Markdownable]] = None, style: Optional[dict] = None) -> None:
        self.title = title
        self.objects: list[Markdownable] = objects if objects else []
        self.style = style

    def append(self, markdownable: Markdownable) -> Self:
        self.objects.append(markdownable)
        return self

    def to_markdown(self) -> str:
        res = ""
        if self.title:
            res += self.title.to_markdown()
        style = self.style if self.style else ""
        res += f"<div class=\"section\" {style=}>\n"
        for obj in self.objects:
            res += "\t"+obj.to_markdown()
        res += "</div>\n"
        return res


class Heading(Tag):
    def __init__(self, text: str, size: int = 1, **kwargs) -> None:
        super().__init__(f"h{size}", Text(text), **kwargs)


class Heading1(Heading):
    def __init__(self, text: str) -> None:
        super().__init__(text, 1)


class Heading2(Heading):
    def __init__(self, text: str) -> None:
        super().__init__(text, 2)


class Heading3(Heading):
    def __init__(self, text: str) -> None:
        super().__init__(text, 3)


class Image(Markdownable):
    STRING = "<img alt=\"{alt}\" width=\"{width}\" height=\"{height}\" style=\"{style}\" src=\"{src}\"/>\n"

    def __init__(self, src: str, width: Optional[int] = None, height: Optional[int] = None, alt: str = "", style: Optional[dict] = None) -> None:
        self.src = src
        self.width = width
        self.height = height
        self.alt = alt
        self.style = style

    def to_markdown(self) -> str:
        return Image.STRING.format(
            alt=self.alt,
            width=self.width,
            height=self.height,
            style=self.style if self.style else None,
            src=self.src
        )


class Break(Markdownable):
    def to_markdown(self) -> str:
        return "<br/>\n"


class IconSvg(Image):
    def __init__(self, name: str) -> None:
        src = f"https://raw.githubusercontent.com/devicons/devicon/master/icons/{name}/{name}-original.svg"
        super().__init__(src, 40, 40, name, None)


class List(Markdownable):
    def __init__(self, objects: list[Markdownable], list_name: str) -> None:
        self.objects = objects
        self.list_name = list_name

    def to_markdown(self) -> str:
        res = f"<{self.list_name}>\n"
        for obj in self.objects:
            res += f"<li>\n\t{obj.to_markdown()}\n</li>\n"
        res += f"</{self.list_name}>\n"
        return res


class OrderedList(List):
    def __init__(self, objects: list[Markdownable]) -> None:
        super().__init__(objects, "ol")


class UnorderedList(List):
    def __init__(self, objects: list[Markdownable]) -> None:
        super().__init__(objects, "ul")


class Repository(Markdownable):
    def __init__(self, name: str, user: str) -> None:
        self.name = name
        self.user = user

    def to_markdown(self) -> str:
        link = f"\"https://www.github.com/{self.user}/{self.name}\""
        return Link(link, Text(self.name)).to_markdown()


RGBA_HEX_STR = str


def parser(obj):
    return obj


class Style(Text):
    def __init__(self, dct: dict) -> None:
        data = json.dumps(dct, default=parser, indent=4)
        text = f"<style>\n{data}\n</style>\n"
        super().__init__(text)


class Link(Markdownable):
    def __init__(self, href: str, contents: Optional[Markdownable] = None) -> None:
        self.href = href
        self.contents = contents

    def to_markdown(self) -> str:
        res = f"<a href=\"{self.href}\">"
        if self.contents:
            res += f"\n{self.contents.to_markdown()}"
        res += "</a>\n"
        return res


class TypingText(Link):
    def __init__(
        self,
        strings: list[str],
        *,
        font_name: str = "Fira+Code",
        font_size: int = 20,
        font_color: RGBA_HEX_STR = "36BCF7FF",
        pause: int = 1000,
        width: int = 435,
        height: int = 50
    ) -> None:
        lines = ";".join(urllib.parse.quote(s) for s in strings)
        text = f"https://readme-typing-svg.herokuapp.com?font={font_name}&size={font_size}&color={font_color}&pause={pause}&width={width}&height={height}&lines={lines}"
        img = Image(src=text, alt="Typing SVG")
        super().__init__(href="https://git.io/typing-svg", contents=img)


__all__ = [
    "Markdownable",
    "Comment",
    "Heading1",
    "Heading2",
    "Heading3",
    "Link",
    "Image",
    "Break",
    "IconSvg",
    "Section",
    "Repository",
    "OrderedList",
    "UnorderedList",
    "Text",
    "TypingText",
    "Style"
]
