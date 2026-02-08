# scoring.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple

from questions import FUNCTIONS, TRAITS, LEVEL_DIMS

LIKERT_TO_VALUE = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5,
}

@dataclass
class ScoreResult:
    function_scores: Dict[str, float]
    trait_scores: Dict[str, float]
    level_scores: Dict[str, float]
    top_functions: List[Tuple[str, float]]
    level: str
    narrative: str

def _normalize(raw: Dict[str, float], max_possible: Dict[str, float]) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for k, v in raw.items():
        denom = max_possible.get(k, 0.0)
        score = 0.0 if denom <= 0 else (v / denom) * 100.0
        out[k] = max(0.0, min(100.0, score))
    return out

def compute_scores(questions: List[dict], answers: Dict[str, str]) -> ScoreResult:
    func_raw = {f: 0.0 for f in FUNCTIONS}
    trait_raw = {t: 0.0 for t in TRAITS}
    level_raw = {d: 0.0 for d in LEVEL_DIMS}

    func_max = {f: 0.0 for f in FUNCTIONS}
    trait_max = {t: 0.0 for t in TRAITS}
    level_max = {d: 0.0 for d in LEVEL_DIMS}

    for q in questions:
        qid = q.get("id")

        for f, w in q.get("func_w", {}).items():
            if f in func_max:
                func_max[f] += 5 * float(w)
        for t, w in q.get("trait_w", {}).items():
            if t in trait_max:
                trait_max[t] += 5 * float(w)
        for d, w in q.get("level_w", {}).items():
            if d in level_max:
                level_max[d] += 5 * float(w)

        if not qid or qid not in answers:
            continue

        val = LIKERT_TO_VALUE.get(answers[qid], 3)

        for f, w in q.get("func_w", {}).items():
            if f in func_raw:
                func_raw[f] += val * float(w)
        for t, w in q.get("trait_w", {}).items():
            if t in trait_raw:
                trait_raw[t] += val * float(w)
        for d, w in q.get("level_w", {}).items():
            if d in level_raw:
                level_raw[d] += val * float(w)

    function_scores = _normalize(func_raw, func_max)
    trait_scores = _normalize(trait_raw, trait_max)
    level_scores = _normalize(level_raw, level_max)

    top_functions = sorted(function_scores.items(), key=lambda x: x[1], reverse=True)[:3]

    exec_s = level_scores.get("Execution", 0.0)
    own_s = level_scores.get("Ownership", 0.0)
    strat_s = level_scores.get("Strategy", 0.0)
    lead_s = level_scores.get("Leadership", 0.0)

    seniority = (0.25 * exec_s + 0.30 * own_s + 0.25 * strat_s + 0.20 * lead_s)

    if seniority < 45:
        level = "Junior / Entry"
    elif seniority < 60:
        level = "Mid-level / Specialist"
    elif seniority < 75:
        level = "Senior / Lead Specialist"
    else:
        level = "Lead / Manager"

    top_traits = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)[:2]
    primary_func, primary_score = top_functions[0] if top_functions else ("General HR", 0.0)

    narrative = f"Your answers show strongest alignment with **{primary_func}** (fit score: {primary_score:.0f}%). "
    if len(top_traits) == 2:
        narrative += f"Your strongest working styles are **{top_traits[0][0]}** and **{top_traits[1][0]}**. "
    narrative += f"Overall, your recommended career level is **{level}**."

    return ScoreResult(
        function_scores=function_scores,
        trait_scores=trait_scores,
        level_scores=level_scores,
        top_functions=top_functions,
        level=level,
        narrative=narrative,
    )
