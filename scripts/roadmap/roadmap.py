#!/usr/bin/env python3
"""Validates the Qhatu roadmap and keeps docs/fases/ESTADO.md in sync with it.

Usage:
    python3 scripts/roadmap/roadmap.py validar   # check ordering and dependency coherence
    python3 scripts/roadmap/roadmap.py estado    # create or update ESTADO.md, preserving states

The canonical order lives in ROADMAP.md as "#### Ola N" headings followed by backticked
sub-phase IDs. Sub-phases are defined in docs/roadmap/*/*.md as "### <ID> · <title>"
headings, each followed by "**Ola:** N" and "**Depende de:** ..." lines.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROADMAP = ROOT / "ROADMAP.md"
PHASES_DIR = ROOT / "docs" / "roadmap"
STATUS_FILE = ROOT / "docs" / "fases" / "ESTADO.md"

ID = r"[A-Z]{2,4}-\d{2}\.\d+[a-z]?"
HEADING_RE = re.compile(rf"^### ({ID}) · (.+?)\s*$")
WAVE_RE = re.compile(r"\*\*Ola:\*\*\s*(\d+)")
DEPS_RE = re.compile(r"\*\*Depende de:\*\*\s*(.+)$")
ID_RE = re.compile(ID)
ORDER_HEADING_RE = re.compile(r"^#### Ola (\d+)\b")
ORDER_ID_RE = re.compile(rf"`({ID})`")
STATUS_ROW_RE = re.compile(rf"^\|\s*\d+\s*\|\s*\d+\s*\|\s*({ID})\s*\|")


@dataclass
class SubPhase:
    id: str
    title: str
    file: Path
    wave: int | None = None
    deps: list[str] = field(default_factory=list)


def parse_subphases() -> dict[str, SubPhase]:
    subphases: dict[str, SubPhase] = {}
    for path in sorted(PHASES_DIR.glob("*/*.md")):
        current: SubPhase | None = None
        for line in path.read_text(encoding="utf-8").splitlines():
            heading = HEADING_RE.match(line)
            if heading:
                current = SubPhase(heading.group(1), heading.group(2), path)
                if current.id in subphases:
                    raise SystemExit(f"Sub-fase duplicada: {current.id} en {path} y {subphases[current.id].file}")
                subphases[current.id] = current
                continue
            if current is None:
                continue
            if current.wave is None and (wave := WAVE_RE.search(line)):
                current.wave = int(wave.group(1))
            if deps := DEPS_RE.search(line):
                current.deps = ID_RE.findall(deps.group(1))
    return subphases


def parse_order() -> list[tuple[str, int]]:
    order: list[tuple[str, int]] = []
    wave: int | None = None
    for line in ROADMAP.read_text(encoding="utf-8").splitlines():
        heading = ORDER_HEADING_RE.match(line)
        if heading:
            wave = int(heading.group(1))
            continue
        if line.startswith("#"):
            wave = None
            continue
        if wave is not None:
            order.extend((sub_id, wave) for sub_id in ORDER_ID_RE.findall(line))
    return order


def validate(subphases: dict[str, SubPhase], order: list[tuple[str, int]]) -> list[str]:
    errors: list[str] = []
    position: dict[str, int] = {}
    for index, (sub_id, wave) in enumerate(order):
        if sub_id in position:
            errors.append(f"{sub_id} aparece más de una vez en el orden de ROADMAP.md")
            continue
        position[sub_id] = index
        sub = subphases.get(sub_id)
        if sub is None:
            errors.append(f"{sub_id} está en el orden de ROADMAP.md pero no está definida en docs/roadmap/")
        elif sub.wave != wave:
            errors.append(f"{sub_id} declara ola {sub.wave} pero ROADMAP.md la ubica en la ola {wave}")

    for sub in subphases.values():
        rel = sub.file.relative_to(ROOT).as_posix()
        if sub.id not in position:
            errors.append(f"{sub.id} ({rel}) no aparece en el orden de ROADMAP.md")
            continue
        if sub.wave is None:
            errors.append(f"{sub.id} ({rel}) no declara su ola")
        for dep in sub.deps:
            if dep == sub.id:
                errors.append(f"{sub.id} depende de sí misma")
            elif dep not in subphases:
                errors.append(f"{sub.id} depende de {dep}, que no existe")
            elif dep not in position:
                continue  # already reported as missing from the order
            elif position[dep] > position[sub.id]:
                errors.append(f"{sub.id} depende de {dep}, que está después en el orden")
    return errors


def read_existing_status() -> dict[str, str]:
    if not STATUS_FILE.exists():
        return {}
    rows: dict[str, str] = {}
    for line in STATUS_FILE.read_text(encoding="utf-8").splitlines():
        if STATUS_ROW_RE.match(line):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            rows[cells[2]] = "| " + " | ".join(cells[4:]) + " |"
    return rows


def write_status(subphases: dict[str, SubPhase], order: list[tuple[str, int]]) -> None:
    existing = read_existing_status()
    lines = [
        "# Estado de las sub-fases",
        "",
        "Fuente de verdad del avance. La actualiza `/fase` en cada paso. Las filas se generan con",
        "`python3 scripts/roadmap/roadmap.py estado`, que conserva los estados ya registrados.",
        "",
        "Estados: `PENDIENTE` → `EN ANÁLISIS` → `PLANIFICADA` → `EN IMPLEMENTACIÓN` → `CERRADA` (o `BLOQUEADA`, con motivo en Notas).",
        "",
        "| # | Ola | Sub-fase | Título | Estado | Cerrada el | Notas |",
        "|---|---|---|---|---|---|---|",
    ]
    for index, (sub_id, wave) in enumerate(order, start=1):
        tail = existing.get(sub_id, "| PENDIENTE | | |")
        lines.append(f"| {index} | {wave} | {sub_id} | {subphases[sub_id].title} {tail}")
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATUS_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in {"validar", "estado"}:
        print(__doc__)
        return 2
    subphases = parse_subphases()
    order = parse_order()
    errors = validate(subphases, order)
    if errors:
        print(f"Roadmap incoherente ({len(errors)} problemas):")
        for error in errors:
            print(f"  - {error}")
        return 1
    waves = sorted({wave for _, wave in order})
    print(f"Roadmap coherente: {len(order)} sub-fases en {len(waves)} olas; todas las dependencias están antes en el orden.")
    if sys.argv[1] == "estado":
        write_status(subphases, order)
        print(f"Actualizado {STATUS_FILE.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
