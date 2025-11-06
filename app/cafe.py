import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        data1 = datetime.date.today()
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{visitor["name"]} is not vaccinated")
        elif visitor["vaccine"].get("expiration_date") < data1:
            raise OutdatedVaccineError(
                f"{visitor["name"]}'s"
                f" vaccine expired on "
                f"{visitor["vaccine"].get("expiration_date")}")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor["name"]} "
                                      f"is not wearing a mask")
        return f"Welcome to {self.name}"
