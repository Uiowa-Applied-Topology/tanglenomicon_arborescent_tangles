from pathlib import Path


def read_datafile(filepath:Path):
    with open(filepath,"r") as file:
        data = file.read()
        return ["i"+entry for entry in data.split("i")][1:]


if __name__ == "__main__":
    tangles = []
    data_dir = Path("./data")
    for file in data_dir.glob("*.txt"):
        tangles.extend(read_datafile(file))
        ...
    ...
