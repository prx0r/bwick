"""Jev routing — post-generation typed decisions (cheap/fast)."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass
class JevVerdict:
    best_template: str
    best_candidate: str
    tone_fit: float      # 0-1
    personal_fit: float  # 0-1
    instant_clarity: float
    genericness: float   # lower = better
    topical_fit: float
    confidence: float
    needs_more_context: bool
    rationale: str

def jev_rank(
    candidates: list[dict[str, Any]],
    template_id: str,
    recipient_name: str,
    facts: list[str],
    roast_level: str,
    humour_context: dict[str, Any] | None = None,
    topical_context: str | None = None,
) -> JevVerdict:
    """Score and rank candidates using deterministic heuristics.
    
    Replace with real Jev/OpenRouter calls when API key available.
    """
    best = None
    best_score = -1

    for c in candidates:
        score = 0.0

        # tone_fit: does the candidate tone match the roast level?
        tone = c.get("tone", [])
        if roast_level == "savage" and "roast" in tone:
            score += 0.3
        elif roast_level == "roast" and ("roast" in tone or "dry" in tone):
            score += 0.25
        elif roast_level == "mild" and ("warm" in tone or "relatable" in tone):
            score += 0.25
        elif roast_level == "dry" and "dry" in tone:
            score += 0.3
        else:
            score += 0.1

        # personal_fit: how many personal facts are referenced?
        personalisation = c.get("personalisation_used", facts)
        fact_hits = sum(1 for f in facts if any(w in c.get("setup","") + c.get("punchline","") for w in f.lower().split()))
        score += min(0.3, fact_hits * 0.1)

        # instant_clarity: setup + punchline should be short and clear
        total_len = len(c.get("setup","")) + len(c.get("punchline",""))
        if total_len < 100:
            score += 0.2
        elif total_len < 150:
            score += 0.1
        else:
            score += 0.05

        # genericness: penalise if no personalisation
        if fact_hits == 0:
            score -= 0.1

        # topical fit
        if topical_context:
            topical_words = topical_context.lower().split()
            joke_text = (c.get("setup","") + " " + c.get("punchline","")).lower()
            topical_hits = sum(1 for w in topical_words if w in joke_text)
            score += min(0.2, topical_hits * 0.05)

        # humour_context preferences
        if humour_context:
            preferred = humour_context.get("preferred_tones", [])
            if any(t in tone for t in preferred):
                score += 0.1

        if score > best_score:
            best_score = score
            best = c

    if not best:
        best = candidates[0] if candidates else {}
        best_score = 0

    confidence = min(1.0, best_score / 0.8)
    genericness = 1.0 - min(1.0, len(facts) / 3)
    needs_more = confidence < 0.4 or genericness > 0.7

    return JevVerdict(
        best_template=template_id,
        best_candidate=best.get("id", ""),
        tone_fit=min(1.0, best_score),
        personal_fit=min(1.0, fact_hits * 0.1) if facts else 0,
        instant_clarity=min(1.0, (150 - total_len) / 150) if total_len < 200 else 0.2,
        genericness=genericness,
        topical_fit=min(1.0, topical_hits * 0.05) if topical_context else 0.5,
        confidence=confidence,
        needs_more_context=needs_more,
        rationale=f"score={best_score:.2f} conf={confidence:.2f} generic={genericness:.2f}",
    )
