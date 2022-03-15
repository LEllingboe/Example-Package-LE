import fire


def custom_add(a: int, b: int) -> int:
    return a + b


def hello():
    pass


def main():
    fire.Fire(custom_add)


if __name__ == "__main__":
    main()
