# scoring.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple
import math

from questions import FUNCTIONS, TRAITS, LEVEL_DIMS

LIKERT_TO_VALUE = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5
}

@dataclass
class ScoreResult:
    function_scores: Dict[str, float]      # 0..100
    trait_scores: Dict[str, float]         # 0..100
    level_scores: Dict[str, float]         # 0..100
    top_functions: List[Tuple[str, float]] # sorted desc
    level: str
    narrative: str

def _normalize(raw: Dict[str, float], max_possible: Dict[str, float]) -> Dict[str, float]:
    out = {}
    for k, v in raw.items():
        denom = max_possible.get(k, 1.0)
        out[k] = 0.0 if denom <= 0 else (v / denom) * 100.0
        out[k] = max(0.0, min(100.0, out[k]))
    return out

def compute_scores(questions: List[dict], answers: Dict[str, str]) -> ScoreResult:
    # raw sums
    func_raw = {f: 0.0 for f in FUNCTIONS}
    trait_raw = {t: 0.0 for t in TRAITS}
    level_raw = {d: 0.0 for d in LEVEL_DIMS}

    # maximum possible (to normalize to 0..100)
    func_max = {f: 0.0 for f in FUNCTIONS}
    trait_max = {t: 0.0 for t in TRAITS}
    level_max = {d: 0.0 for d in LEVEL_DIMS}

    for q in questions:
        qid = q["id"]
        # max based on Strongly Agree = 5
        for f, w in q.get("func_w", {}).items():
            func_max[f] += 5 * w
        for t, w in q.get("trait_w", {}).items():
            trait_max[t] += 5 * w
        for d, w in q.get("level_w", {}).items():
            level_max[d] += 5 * w

        if qid not in answers:
            continue
        val = LIKERT_TO_VALUE.get(answers[qid], 3)

        for f, w in q.get("func_w", {}).items():
            func_raw[f] += val * w
        for t, w in q.get("trait_w", {}).items():
            trait_raw[t] += val * w
        for d, w in q.get("level_w", {}).items():
            level_raw[d] += val * w

    function_scores = _normalize(func_raw, func_max)
    trait_scores = _normalize(trait_raw, trait_max)
    level_scores = _normalize(level_raw, level_max)

    top_functions = sorted(function_scores.items(), key=lambda x: x[1], reverse=True)[:3]

    # Level decision (simple but robust):
    exec_s = level_scores["Execution"]
    own_s = level_scores["Ownership"]
    strat_s = level_scores["Strategy"]
    lead_s = level_scores["Leadership"]

    # Weighted "seniority index"
    seniority = (0.25*exec_s + 0.30*own_s + 0.25*strat_s + 0.20*lead_s)

    if seniority < 45:
        level = "Junior / Entry"
    elif seniority < 60:
        level = "Mid-level / Specialist"
    elif seniority < 75:
        level = "Senior / Lead Specialist"
    else:
        level = "Lead / Manager"

    # Narrative: highlight top 2 traits + top function
    top_trait = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)[:2]
    primary_func, primary_score = top_functions[0]

    narrative = (
        f"Your answers show strongest alignment with **{primary_func}** "
        f"(fit score: {primary_score:.0f}%). "
        f"Your strongest working styles are **{top_trait[0][0]}** and **{top_trait[1][0]}**. "
        f"Overall, your recommended career level is **{level}**."
    )

    return ScoreResult(
        function_scores=function_scores,
        trait_scores=trait_scores,
        level_scores=level_scores,
        top_functions=top_functions,
        level=level,
        narrative=narrative
    )