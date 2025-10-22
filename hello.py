"""Simple greeting script."""

def greet(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    return f"Hello, {name}!"


def main() -> None:
    """Print a greeting for a default name when run as a script."""
    print(greet("world"))


if __name__ == "__main__":
    main()
