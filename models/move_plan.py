from dataclasses import dataclass


@dataclass
class MovePlan:

    problem_id: int

    source: str

    destination: str

    status: str = "pending"

    def to_dict(self):

        return {
            "problem_id": self.problem_id,
            "source": self.source,
            "destination": self.destination,
            "status": self.status
        }