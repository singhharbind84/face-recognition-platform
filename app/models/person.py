from dataclasses import dataclass
import numpy as np


@dataclass
class Person:

    id: int

    name: str

    embedding: np.ndarray

    image_path: str
