from pytest import fixture


@fixture
def get_data():
    def _get_data(file_path: str) -> str:
        with open(f"data/{file_path}", "r") as fp:
            data = fp.read()
        return data

    return _get_data
