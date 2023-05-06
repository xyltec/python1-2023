from dataclasses import dataclass
from enum import Enum


@dataclass
class ShipState:
    height: float
    speed: float
    max_thrust: float  # can't exceed this value in ThrustVectors


@dataclass
class ThrustVectors:
    a_vertical: float


class FinalState(Enum):
    OK = 0
    DISASSEMBLY = 1
    ILLEGAL_THRUST_VALUE = 2
    NO_LANDING = 3


@dataclass
class SimulationResult:
    fuel_used: float
    status: FinalState


class Ship:

    def __init__(self, fuel: float = 100):
        # konstruktor
        self.fuel = fuel

    def initialize(self, state: ShipState):
        # todo:  you might save the initial state
        pass

    def get_thrust_vectors(self, time: float, state: ShipState) -> ThrustVectors:
        h = state.height
        v = state.speed
        thr = 0

        # rocket is too close to the ground and moving too fast
        if h < 1 and v > 1:
            thr = -1.5
        return ThrustVectors(a_vertical=0)
