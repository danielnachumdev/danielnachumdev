from typing import Optional, Self
from abc import ABC, abstractmethod


class Markdownable(ABC):
    @abstractmethod
    def to_markdown(self) -> str: ...


class Text(Markdownable):
    def __init__(self, text: str) -> None:
        self.text = text

    def to_markdown(self) -> str:
        return f"{self.text}\n"


class Tag(Markdownable):
    def __init__(self, name: str, contents: Optional[list["Tag"]] = None, **kwargs) -> None:
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
            del key, value  # pylint: disable=undefined-loop-variable

        if self.contents:
            res += ">\n"
            for content in self.contents:
                res += content.to_markdown()
            res += f"</{self.name}>\n"
        else:
            if self.name == "img":
                res += "/>\n"
            else:
                res += ">\n"
        return res
