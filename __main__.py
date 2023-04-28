import sys

from module.Window import MWindow


def main():
    try:
        MWindow("Teilautomatisierte Kategorisierung")
    except ValueError as ve:
        return str(ve)


if __name__ == "__main__":
    sys.exit(main())
