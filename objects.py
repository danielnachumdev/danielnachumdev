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


class Image(Markdownable):
    STRING = "<img alt={alt} width={width} height={height} style={style} src=\"{src}\" />\n"

    def __init__(self, src: str, width: Optional[int], height: Optional[int], alt: str, style: Optional[dict] = None) -> None:
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
    def __init__(self) -> None:
        pass

    def append(self, markdownable: Markdownable) -> Self:
        return self

    def to_markdown(self) -> str:
        return ""


__all__ = [
    "Markdownable",
    "Comment",
    "Heading",
    "Image",
    "Break",
    "IconSvg"
]
