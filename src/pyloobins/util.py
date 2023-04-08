"""Utility functions that support the CLI and library"""
from datetime import date
import yaml
from .models import *


def validate_loobin(yml_path: str) -> bool:
    """Validates LOOBin YAML file"""
    with open(yml_path, "r", encoding="utf-8") as stream:
        try:
            yml_content = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    try:
        LOOBin(**yml_content) # type: ignore
        return True
    except Exception as exc:
        # TODO add more specific Exception handling
        print(exc)
        return False


def make_template() -> LOOBin:
    """Creates a template LOOBin object"""
    loobin_template = LOOBin(
        name="Template",
        short_description="A short description of the binary goes here.",
        full_description="A full length description of the binary goes here.",
        author="Enter your name or alias here.",
        created=date.today(),
        example_use_cases=[ExampleUseCase(name="An Example Use Case", description="A description of the use case goes here.", code="A code snippet goes here.", tactics=["Discovery"],tags=["example_tag"])],
        paths=["/enter/binary/path/here"],
        detections=[
            Detection(
                name="A detection source (e.g. Sigma)",
                url="https://urltodetection.here",
            )
        ],
        external_references=[ExternalReference(
                name="Name of external reference.",
                url="https://urlofexternalreference.here",
            )
        ],
    )
    return loobin_template

def normalize_file_name(title: str)->str:
    """Accepts a binary title and normalizes it for the file name"""
    return title.lower().replace(" ","_")
