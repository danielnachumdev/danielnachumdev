from typing import Optional, Self
from abc import ABC, abstractmethod


class Markdownable(ABC):
    @abstractmethod
    def to_markdown(self) -> str: ...


class Tag(Markdownable):
    def __init__(self, name: str, contents: Optional["Tag"] = None, **kwargs) -> None:
        self.name = name
        self.kwargs = kwargs
        self.contents = contents

    def to_markdown(self) -> str:
        res = ""
        if self.contents:
            res += f"<{self.name}"
        else:
            if self.name == "img":
                res += f"<{self.name}"
            else:
                res += f"</{self.name}"
        if self.kwargs:
            res += " "
            for key, value in self.kwargs.items():
                if value is not None:
                    res += f'{key}="{value}" '

        if self.contents:
            res += ">\n"+self.contents.to_markdown()+f"</{self.name}>\n"
        else:
            if self.name == "img":
                res += "/>\n"
            else:
                res += ">\n"
        return res


class Text(Markdownable):
    def __init__(self, text: str) -> None:
        self.text = text

    def to_markdown(self) -> str:
        return f"{self.text}\n"


class Section(Markdownable):
    def __init__(self, *, title: Optional[Markdownable] = None, objects: Optional[list[Markdownable]] = None, style: Optional[dict] = None) -> None:
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
