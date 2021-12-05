class TestPrinter:
    tests: list[str]

    @classmethod
    def reset(cls) -> None:
        cls.tests = []

    @classmethod
    def add(cls, func_name: str) -> None:
        cls.tests.append(f"----- Passed {func_name}() -----")

    @classmethod
    def print_passed_tests(cls) -> None:
        for test in cls.tests:
            print(test)
