# app.py
from __future__ import annotations

import json
from datetime import datetime

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from questions import QUESTIONS, LIKERT
from scoring import compute_scores

APP_TITLE = "HR Career Fit Analyzer"
APP_TAGLINE = "60-question assessment to discover your best-fit HR function(s) and recommended level."

def _brand_css() -> None:
    st.markdown(
        """
        <style>
          :root{
            --bg:#f6f7fb;
            --card:#ffffff;
            --text:#0f172a;
            --muted:#64748b;
            --border:#e2e8f0;
            --accent:#0ea5e9;
          }
          .stApp{ background: var(--bg); }
          .pv-wrap{ max-width: 980px; margin: 0 auto; }
          .pv-hero{
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 18px;
            box-shadow: 0 10px 30px rgba(2,6,23,0.06);
          }
          .pv-title{ font-size: 28px; font-weight: 800; margin: 0; color: var(--text); }
          .pv-sub{ margin-top: 6px; color: var(--muted); font-size: 14px; }
          .pv-card{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 16px;
            box-shadow: 0 10px 30px rgba(2,6,23,0.05);
          }
          .pv-kpi{
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 12px;
            background: #ffffff;
          }
          .pv-muted{ color: var(--muted); font-size: 13px; }
          .pv-badge{
            display:inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            border: 1px solid var(--border);
            font-size: 12px;
            color: var(--text);
            background: #fff;
            margin-right: 6px;
          }
          .pv-divider{ height: 1px; background: var(--border); margin: 12px 0; }
          .pv-small{ font-size: 12px; color: var(--muted); }
        </style>
        """,
        unsafe_allow_html=True,
    )

def _init_state() -> None:
    st.session_state.setdefault("started", False)
    st.session_state.setdefault("idx", 0)
    st.session_state.setdefault("answers", {})

def _reset() -> None:
    st.session_state.started = False
    st.session_state.idx = 0
    st.session_state.answers = {}

def _header() -> None:
    st.markdown('<div class="pv-wrap">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="pv-hero">
          <div class="pv-title">{APP_TITLE}</div>
          <div class="pv-sub">{APP_TAGLINE}</div>
          <div class="pv-divider"></div>
          <span class="pv-badge">General HR • Global-friendly</span>
          <span class="pv-badge">10 HR Tracks</span>
          <span class="pv-badge">Traits + Level Scoring</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

def _footer() -> None:
    st.markdown(
        """
        <div class="pv-wrap">
          <div class="pv-small">
            Tip: Answer honestly — there are no “right” answers. The goal is role-fit, not perfection.
          </div>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def _intro() -> None:
    st.markdown(
        """
        <div class="pv-card pv-wrap">
          <h3 style="margin:0 0 8px 0;">How it works</h3>
          <div class="pv-muted">
            • You will answer 60 statements using a 5-point scale.<br/>
            • The tool matches your answers to 10 HR functions + 6 work-style traits.<br/>
            • At the end, you will receive your top 3 HR tracks and a recommended level.
          </div>
          <div class="pv-divider"></div>
          <div class="pv-muted"><b>Estimated time:</b> 6–10 minutes</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Start Assessment", use_container_width=True, type="primary"):
            st.session_state.started = True
            st.session_state.idx = 0
    with c2:
        st.button("Reset", use_container_width=True, on_click=_reset)

def _go_back() -> None:
    st.session_state.idx = max(0, st.session_state.idx - 1)

def _go_next() -> None:
    st.session_state.idx = min(len(QUESTIONS) - 1, st.session_state.idx + 1)

def _go_results() -> None:
    st.session_state.idx = len(QUESTIONS)

def _question_view() -> None:
    idx = st.session_state.idx
    q = QUESTIONS[idx]
    total = len(QUESTIONS)

    st.markdown('<div class="pv-wrap">', unsafe_allow_html=True)
    st.progress(idx / total)
    st.markdown(f"<div class='pv-muted'>Question <b>{idx+1}</b> of <b>{total}</b></div>", unsafe_allow_html=True)
    st.write("")

    st.markdown(
        f"""
        <div class="pv-card">
          <div style="font-size:18px;font-weight:700;color:#0f172a;margin-bottom:10px;">
            {q['text']}
          </div>
          <div class="pv-muted">Select the option that best describes you.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    current = st.session_state.answers.get(q["id"], "Neutral")
    choice = st.radio("", options=LIKERT, index=LIKERT.index(current) if current in LIKERT else 2)
    st.session_state.answers[q["id"]] = choice

    st.write("")
    b1, b2, b3 = st.columns(3)
    with b1:
        st.button("Back", use_container_width=True, disabled=(idx == 0), on_click=_go_back)
    with b2:
        st.button("Reset", use_container_width=True, on_click=_reset)
    with b3:
        if idx < total - 1:
            st.button("Next", use_container_width=True, on_click=_go_next)
        else:
            st.button("Finish & See Results", use_container_width=True, type="primary", on_click=_go_results)

    st.markdown("</div>", unsafe_allow_html=True)

def _results_view() -> None:
    st.markdown('<div class="pv-wrap">', unsafe_allow_html=True)

    result = compute_scores(QUESTIONS, st.session_state.answers)

    st.markdown(
        """
        <div class="pv-card">
          <h3 style="margin:0 0 6px 0;">Your Results</h3>
          <div class="pv-muted">Top matches (ranked) + recommended level.</div>
          <div class="pv-divider"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    cols = st.columns(3)
    for i, (name, score) in enumerate(result.top_functions):
        with cols[i]:
            st.markdown(
                f"""
                <div class="pv-kpi">
                  <div class="pv-muted">#{i+1} Best Fit</div>
                  <div style="font-size:16px;font-weight:800;margin-top:4px;">{name}</div>
                  <div style="font-size:28px;font-weight:900;margin-top:6px;">{score:.0f}%</div>
                  <div class="pv-muted">Fit score</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    st.markdown(
        f"""
        <div class="pv-card">
          <div style="font-size:15px;font-weight:700;">Recommended Career Level</div>
          <div style="font-size:22px;font-weight:900;margin-top:6px;">{result.level}</div>
          <div class="pv-divider"></div>
          <div class="pv-muted">{result.narrative}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown('<div class="pv-card"><div style="font-size:15px;font-weight:700;margin-bottom:10px;">Function Scores</div>', unsafe_allow_html=True)
    func_df = pd.DataFrame({"Function": list(result.function_scores.keys()), "Score": list(result.function_scores.values())}).sort_values("Score", ascending=True)
    fig1 = plt.figure()
    plt.barh(func_df["Function"], func_df["Score"])
    plt.xlabel("Fit Score (0–100)")
    plt.tight_layout()
    st.pyplot(fig1, clear_figure=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="pv-card"><div style="font-size:15px;font-weight:700;margin-bottom:10px;">Work-Style Traits</div>', unsafe_allow_html=True)
    trait_df = pd.DataFrame({"Trait": list(result.trait_scores.keys()), "Score": list(result.trait_scores.values())}).sort_values("Score", ascending=True)
    fig2 = plt.figure()
    plt.barh(trait_df["Trait"], trait_df["Score"])
    plt.xlabel("Strength (0–100)")
    plt.tight_layout()
    st.pyplot(fig2, clear_figure=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown(
        """
        <div class="pv-card">
          <div style="font-size:15px;font-weight:700;margin-bottom:8px;">Download</div>
          <div class="pv-muted">Export your results (answers + scores) as JSON or CSV.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    export_payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "top_functions": result.top_functions,
        "recommended_level": result.level,
        "function_scores": result.function_scores,
        "trait_scores": result.trait_scores,
        "answers": st.session_state.answers,
    }

    st.download_button(
        "Download Results (JSON)",
        data=json.dumps(export_payload, indent=2),
        file_name="hr_career_fit_results.json",
        mime="application/json",
        use_container_width=True,
    )

    ans_df = pd.DataFrame([{"QuestionID": q["id"], "Answer": st.session_state.answers.get(q["id"], "")} for q in QUESTIONS])
    st.download_button(
        "Download Answers (CSV)",
        data=ans_df.to_csv(index=False),
        file_name="hr_career_fit_answers.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        st.button("Retake Assessment", use_container_width=True, on_click=_reset)
    with c2:
        st.button("Back to Review", use_container_width=True, on_click=lambda: st.session_state.update({"idx": max(0, len(QUESTIONS)-1)}))

def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon="🧭", layout="wide")
    _brand_css()
    _init_state()
    _header()

    if not st.session_state.started:
        _intro()
    else:
        if st.session_state.idx < len(QUESTIONS):
            _question_view()
        else:
            _results_view()

    _footer()

if __name__ == "__main__":
    main()
