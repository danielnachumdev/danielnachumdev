from typing import Optional, Self
from abc import ABC, abstractmethod


class Markdownable(ABC):
    @abstractmethod
    def to_markdown(self) -> str: ...


class Comment(Markdownable):
    def __init__(self, comment: str) -> None:
        self.comment = comment

    def to_markdown(self) -> str:
        return f"<!-- {self.comment}-->\n"


class Heading(Markdownable):
    def __init__(self, text: str, size: int = 1) -> None:
        self.size = size
        self.text = text

    def to_markdown(self) -> str:
        return f"\n{'#'*self.size} {self.text}\n"


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
    STRING = "<img alt={alt} width={width} height={height} style={style} src=\"{src}\"/>\n"

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
            style=self.style if self.style else '""',
            src=self.src
        )


class Break(Markdownable):
    def to_markdown(self) -> str:
        return "<br/>\n"


class IconSvg(Image):
    def __init__(self, name: str) -> None:
        src = f"https://raw.githubusercontent.com/devicons/devicon/master/icons/{name}/{name}-original.svg"
        super().__init__(src, 40, 40, name, None)


class Section(Markdownable):
    def __init__(self, *, title: Optional[Heading] = None, objects: Optional[list[Markdownable]] = None, style: Optional[dict] = None) -> None:
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


__all__ = [
    "Markdownable",
    "Comment",
    "Heading1",
    "Heading2",
    "Heading3",
    "Image",
    "Break",
    "IconSvg",
    "Section"
]
