"""Allergen panel renderer for Mistvale Ingredients"""

class AllergenPanel:
    """Internal service for allergen-panel."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(AllergenPanel().status())
