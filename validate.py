import json
from sys import stdin
from typing import Generic, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


class Interval(BaseModel):
    start: str
    end: str


class Location(BaseModel):
    city: str
    country: str
    address: str | None
    zip_: str | None = Field(alias="zip")


class Personalia(BaseModel):
    name: str
    date_of_birth: str
    job: str
    email: str
    phone: str
    url: str
    location: Location
    summary: str


class Experience(BaseModel):
    name: str
    title: str
    url: str
    location: Location
    date: Interval
    description: str | None
    tags: list[str] | None


class ListItem(BaseModel):
    name: str
    description: str
    url: str | None


class Keyword(BaseModel):
    name: str
    description: str | None


T = TypeVar("T")


class Category(GenericModel, Generic[T]):
    name: str
    items: list[T]


class CV(BaseModel):
    personalia: Personalia
    experience: list[Category[Experience]]
    lists: list[Category[ListItem]]
    keywords: list[Category[Keyword]]


def main():
    CV.parse_raw(stdin.read())


if __name__ == "__main__":
    main()
