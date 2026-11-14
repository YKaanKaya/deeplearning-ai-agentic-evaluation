"""Small shared contracts passed from one evaluation stage to the next."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Case:
    case_id: str
    split: str
    requirement: str
    order_id: str
    expected_tools: tuple[str, ...]
    amount: int = 42
    eligible: bool = True
    prompt: str = "Please help with this demo order."


@dataclass(frozen=True)
class Span:
    span_id: str
    parent_id: str | None
    name: str
    sequence: int
    inputs: dict[str, Any]
    outputs: dict[str, Any]
    synthetic_ms: int


@dataclass(frozen=True)
class Run:
    case_id: str
    version: str
    response: str
    claims: dict[str, Any]
    spans: tuple[Span, ...]
    state: dict[str, Any]

    @property
    def tools(self) -> tuple[Span, ...]:
        return tuple(span for span in self.spans if span.parent_id is not None)


@dataclass(frozen=True)
class BenchmarkEntry:
    case: Case
    observed_run: Run

    @property
    def source_span_id(self) -> str:
        return self.observed_run.spans[0].span_id

    @property
    def observed_response(self) -> str:
        return self.observed_run.response
