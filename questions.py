# questions.py
# 60 questions designed for a general global HR audience.
# Each question contributes (with weights) to: HR functions, traits, and level indicators.

FUNCTIONS = [
    "Talent Acquisition",
    "Compensation & Benefits",
    "HR Operations",
    "HRIS / HR Technology",
    "Learning & Development",
    "Employee Relations",
    "Organizational Development",
    "Performance Management",
    "HR Analytics",
    "Talent Management"
]

TRAITS = [
    "People-centric",
    "Analytical",
    "Process-oriented",
    "Tech-savvy",
    "Strategic",
    "Learning agility"
]

LEVEL_DIMS = [
    "Execution",
    "Ownership",
    "Strategy",
    "Leadership"
]

LIKERT = [
    "Strongly Disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Strongly Agree"
]

# Helper: smaller weights are fine; scoring normalizes at the end.
QUESTIONS = [
    # --- General HR mindset / operations ---
    {
        "id": "Q01",
        "text": "I enjoy solving day-to-day employee requests quickly and accurately.",
        "func_w": {"HR Operations": 2, "Employee Relations": 1},
        "trait_w": {"People-centric": 1, "Process-oriented": 2},
        "level_w": {"Execution": 2}
    },
    {
        "id": "Q02",
        "text": "I like working with policies and ensuring consistent application across employees.",
        "func_w": {"Employee Relations": 2, "HR Operations": 2},
        "trait_w": {"Process-oriented": 2, "People-centric": 1},
        "level_w": {"Execution": 1, "Ownership": 1}
    },
    {
        "id": "Q03",
        "text": "I feel confident explaining HR policies in a calm and fair way during sensitive conversations.",
        "func_w": {"Employee Relations": 3},
        "trait_w": {"People-centric": 3},
        "level_w": {"Execution": 1, "Leadership": 1}
    },
    {
        "id": "Q04",
        "text": "I enjoy creating checklists, templates, and standard workflows to reduce errors.",
        "func_w": {"HR Operations": 3, "HRIS / HR Technology": 1},
        "trait_w": {"Process-oriented": 3, "Tech-savvy": 1},
        "level_w": {"Ownership": 1, "Execution": 1}
    },
    {
        "id": "Q05",
        "text": "I prefer structured work with clear deadlines and measurable accuracy.",
        "func_w": {"HR Operations": 2, "Compensation & Benefits": 1},
        "trait_w": {"Process-oriented": 2},
        "level_w": {"Execution": 2}
    },

    # --- Talent Acquisition ---
    {
        "id": "Q06",
        "text": "I enjoy sourcing candidates and reaching out proactively to build pipelines.",
        "func_w": {"Talent Acquisition": 3},
        "trait_w": {"People-centric": 2, "Learning agility": 1},
        "level_w": {"Execution": 1, "Ownership": 1}
    },
    {
        "id": "Q07",
        "text": "I can assess a candidate's fit using structured interviews and competency questions.",
        "func_w": {"Talent Acquisition": 3, "Talent Management": 1},
        "trait_w": {"People-centric": 2, "Analytical": 1},
        "level_w": {"Ownership": 1}
    },
    {
        "id": "Q08",
        "text": "I enjoy negotiating offers and aligning expectations between candidates and hiring managers.",
        "func_w": {"Talent Acquisition": 2, "HR Operations": 1},
        "trait_w": {"People-centric": 2},
        "level_w": {"Leadership": 1, "Ownership": 1}
    },
    {
        "id": "Q09",
        "text": "I like tracking recruitment metrics (time-to-fill, quality of hire) and improving the process.",
        "func_w": {"Talent Acquisition": 2, "HR Analytics": 2},
        "trait_w": {"Analytical": 2, "Process-oriented": 1},
        "level_w": {"Ownership": 1, "Strategy": 1}
    },
    {
        "id": "Q10",
        "text": "I’m comfortable handling high-volume hiring without compromising candidate experience.",
        "func_w": {"Talent Acquisition": 2},
        "trait_w": {"People-centric": 1, "Process-oriented": 1},
        "level_w": {"Execution": 2}
    },

    # --- Compensation & Benefits / Total Rewards ---
    {
        "id": "Q11",
        "text": "I enjoy working with numbers like salary structures, allowances, and benefits costs.",
        "func_w": {"Compensation & Benefits": 3, "HR Analytics": 1},
        "trait_w": {"Analytical": 2},
        "level_w": {"Execution": 1, "Ownership": 1}
    },
    {
        "id": "Q12",
        "text": "I prefer roles where accuracy and compliance are critical.",
        "func_w": {"Compensation & Benefits": 2, "HR Operations": 2},
        "trait_w": {"Process-oriented": 2},
        "level_w": {"Execution": 2}
    },
    {
        "id": "Q13",
        "text": "I like explaining pay or benefits decisions in a clear and respectful way.",
        "func_w": {"Compensation & Benefits": 2, "Employee Relations": 1},
        "trait_w": {"People-centric": 2},
        "level_w": {"Leadership": 1}
    },
    {
        "id": "Q14",
        "text": "I enjoy analyzing internal equity and proposing compensation improvements.",
        "func_w": {"Compensation & Benefits": 2, "HR Analytics": 2, "Organizational Development": 1},
        "trait_w": {"Analytical": 2, "Strategic": 1},
        "level_w": {"Strategy": 1, "Ownership": 1}
    },
    {
        "id": "Q15",
        "text": "I like benchmarking jobs and pay against external market data.",
        "func_w": {"Compensation & Benefits": 3},
        "trait_w": {"Analytical": 2, "Strategic": 1},
        "level_w": {"Strategy": 1}
    },

    # --- HRIS / HR Tech ---
    {
        "id": "Q16",
        "text": "I enjoy configuring systems, fields, workflows, or forms to make HR processes smoother.",
        "func_w": {"HRIS / HR Technology": 3, "HR Operations": 1},
        "trait_w": {"Tech-savvy": 3, "Process-oriented": 1},
        "level_w": {"Ownership": 1}
    },
    {
        "id": "Q17",
        "text": "I feel energized when troubleshooting system issues and finding the root cause.",
        "func_w": {"HRIS / HR Technology": 3},
        "trait_w": {"Tech-savvy": 2, "Analytical": 1},
        "level_w": {"Execution": 1, "Ownership": 1}
    },
    {
        "id": "Q18",
        "text": "I like translating HR requirements into clear technical requirements for IT or vendors.",
        "func_w": {"HRIS / HR Technology": 2, "HR Operations": 1},
        "trait_w": {"Tech-savvy": 2, "Strategic": 1},
        "level_w": {"Ownership": 1, "Leadership": 1}
    },
    {
        "id": "Q19",
        "text": "I enjoy improving data quality and ensuring HR records are consistent across systems.",
        "func_w": {"HRIS / HR Technology": 2, "HR Operations": 2, "HR Analytics": 1},
        "trait_w": {"Process-oriented": 2, "Analytical": 1},
        "level_w": {"Execution": 2}
    },
    {
        "id": "Q20",
        "text": "I prefer building dashboards or self-service reports rather than manual reporting.",
        "func_w": {"HR Analytics": 2, "HRIS / HR Technology": 2},
        "trait_w": {"Analytical": 2, "Tech-savvy": 1},
        "level_w": {"Ownership": 1}
    },

    # --- L&D ---
    {
        "id": "Q21",
        "text": "I enjoy designing training programs and learning journeys.",
        "func_w": {"Learning & Development": 3, "Talent Management": 1},
        "trait_w": {"People-centric": 1, "Strategic": 1, "Learning agility": 1},
        "level_w": {"Ownership": 1}
    },
    {
        "id": "Q22",
        "text": "I like facilitating workshops and keeping people engaged in learning sessions.",
        "func_w": {"Learning & Development": 3},
        "trait_w": {"People-centric": 2},
        "level_w": {"Leadership": 1, "Execution": 1}
    },
    {
        "id": "Q23",
        "text": "I enjoy building competency frameworks and linking them to development plans.",
        "func_w": {"Learning & Development": 2, "Organizational Development": 2, "Talent Management": 1},
        "trait_w": {"Strategic": 2, "Analytical": 1},
        "level_w": {"Strategy": 1}
    },
    {
        "id": "Q24",
        "text": "I like measuring training impact (behavior change, performance outcomes) not just attendance.",
        "func_w": {"Learning & Development": 2, "HR Analytics": 2, "Performance Management": 1},
        "trait_w": {"Analytical": 2, "Strategic": 1},
        "level_w": {"Strategy": 1, "Ownership": 1}
    },
    {
        "id": "Q25",
        "text": "I can coach others and give feedback that helps them improve.",
        "func_w": {"Learning & Development": 2, "Performance Management": 2},
        "trait_w": {"People-centric": 2},
        "level_w": {"Leadership": 2}
    },

    # --- Employee Relations ---
    {
        "id": "Q26",
        "text": "I’m comfortable investigating workplace issues and documenting cases carefully.",
        "func_w": {"Employee Relations": 3},
        "trait_w": {"Process-oriented": 1, "Analytical": 1, "People-centric": 1},
        "level_w": {"Ownership": 1}
    },
    {
        "id": "Q27",
        "text": "I prefer preventing conflict through early intervention and clear expectations.",
        "func_w": {"Employee Relations": 2, "Organizational Development": 1},
        "trait_w": {"People-centric": 2, "Strategic": 1},
        "level_w": {"Strategy": 1}
    },
    {
        "id": "Q28",
        "text": "I can stay neutral and fair even when people are emotional or upset.",
        "func_w": {"Employee Relations": 3},
        "trait_w": {"People-centric": 2},
        "level_w": {"Leadership": 1, "Execution": 1}
    },
    {
        "id": "Q29",
        "text": "I’m confident in handling disciplinary processes with empathy and compliance.",
        "func_w": {"Employee Relations": 3, "HR Operations": 1},
        "trait_w": {"People-centric": 1, "Process-oriented": 1},
        "level_w": {"Ownership": 1}
    },
    {
        "id": "Q30",
        "text": "I enjoy building trust with managers so they consult HR early, not only when problems escalate.",
        "func_w": {"Employee Relations": 2, "Organizational Development": 1, "Talent Management": 1},
        "trait_w": {"People-centric": 2, "Strategic": 1},
        "level_w": {"Leadership": 1}
    },

    # --- OD / Culture / Change ---
    {
        "id": "Q31",
        "text": "I enjoy shaping culture initiatives (values, engagement, communication) across the organization.",
        "func_w": {"Organizational Development": 3, "Talent Management": 1},
        "trait_w": {"Strategic": 2, "People-centric": 1},
        "level_w": {"Strategy": 2}
    },
    {
        "id": "Q32",
        "text": "I like leading change and supporting people through transitions (restructure, new policies, new systems).",
        "func_w": {"Organizational Development": 2, "HRIS / HR Technology": 1},
        "trait_w": {"Strategic": 2, "People-centric": 1},
        "level_w": {"Leadership": 2}
    },
    {
        "id": "Q33",
        "text": "I enjoy diagnosing organizational issues using surveys, interviews, and data.",
        "func_w": {"Organizational Development": 2, "HR Analytics": 2},
        "trait_w": {"Analytical": 2, "Strategic": 1},
        "level_w": {"Strategy": 1}
    },
    {
        "id": "Q34",
        "text": "I prefer roles where I influence leadership decisions and long-term workforce strategy.",
        "func_w": {"Organizational Development": 2, "Talent Management": 2},
        "trait_w": {"Strategic": 3},
        "level_w": {"Strategy": 2, "Leadership": 1}
    },
    {
        "id": "Q35",
        "text": "I enjoy building new HR programs from scratch and iterating them based on feedback.",
        "func_w": {"Organizational Development": 2, "Learning & Development": 1, "Performance Management": 1},
        "trait_w": {"Strategic": 1, "Learning agility": 2},
        "level_w": {"Ownership": 1, "Strategy": 1}
    },

    # --- Performance Management ---
    {
        "id": "Q36",
        "text": "I enjoy helping managers set clear goals and performance expectations.",
        "func_w": {"Performance Management": 3, "Talent Management": 1},
        "trait_w": {"People-centric": 1, "Strategic": 1},
        "level_w": {"Ownership": 1}
    },
    {
        "id": "Q37",
        "text": "I like building fair evaluation systems (ratings, calibration, feedback cycles).",
        "func_w": {"Performance Management": 2, "Organizational Development": 1},
        "trait_w": {"Process-oriented": 2, "Strategic": 1},
        "level_w": {"Strategy": 1}
    },
    {
        "id": "Q38",
        "text": "I’m comfortable challenging a manager respectfully when performance decisions are biased or inconsistent.",
        "func_w": {"Performance Management": 2, "Employee Relations": 1},
        "trait_w": {"People-centric": 1, "Leadership": 0},
        "level_w": {"Leadership": 2}
    },
    {
        "id": "Q39",
        "text": "I prefer performance improvement conversations that balance accountability and support.",
        "func_w": {"Performance Management": 2, "Employee Relations": 1},
        "trait_w": {"People-centric": 2},
        "level_w": {"Leadership": 1}
    },
    {
        "id": "Q40",
        "text": "I enjoy linking performance outcomes to development and rewards in a fair way.",
        "func_w": {"Performance Management": 2, "Compensation & Benefits": 1, "Talent Management": 1},
        "trait_w": {"Strategic": 1, "Analytical": 1},
        "level_w": {"Strategy": 1}
    },

    # --- HR Analytics ---
    {
        "id": "Q41",
        "text": "I enjoy turning HR data into insights that leadership can act on.",
        "func_w": {"HR Analytics": 3, "Organizational Development": 1},
        "trait_w": {"Analytical": 3, "Strategic": 1},
        "level_w": {"Strategy": 1}
    },
    {
        "id": "Q42",
        "text": "I like building dashboards and tracking trends (attrition, headcount, engagement).",
        "func_w": {"HR Analytics": 3, "HRIS / HR Technology": 1},
        "trait_w": {"Analytical": 2, "Tech-savvy": 1},
        "level_w": {"Ownership": 1}
    },
    {
        "id": "Q43",
        "text": "I enjoy running root-cause analysis and testing hypotheses using data.",
        "func_w": {"HR Analytics": 3},
        "trait_w": {"Analytical": 3},
        "level_w": {"Strategy": 1}
    },
    {
        "id": "Q44",
        "text": "I prefer decisions backed by evidence, even when it requires extra analysis.",
        "func_w": {"HR Analytics": 2, "Compensation & Benefits": 1},
        "trait_w": {"Analytical": 2},
        "level_w": {"Ownership": 1}
    },
    {
        "id": "Q45",
        "text": "I enjoy explaining complex numbers in a simple way for non-technical stakeholders.",
        "func_w": {"HR Analytics": 2, "Compensation & Benefits": 1},
        "trait_w": {"Analytical": 1, "People-centric": 1},
        "level_w": {"Leadership": 1}
    },

    # --- Talent Management (Succession, mobility, career paths) ---
    {
        "id": "Q46",
        "text": "I enjoy identifying high-potential employees and planning development paths.",
        "func_w": {"Talent Management": 3, "Learning & Development": 1},
        "trait_w": {"Strategic": 2, "People-centric": 1},
        "level_w": {"Strategy": 1}
    },
    {
        "id": "Q47",
        "text": "I like building succession plans and supporting internal mobility.",
        "func_w": {"Talent Management": 3, "Organizational Development": 1},
        "trait_w": {"Strategic": 2},
        "level_w": {"Strategy": 1}
    },
    {
        "id": "Q48",
        "text": "I enjoy designing competency models and career ladders.",
        "func_w": {"Talent Management": 2, "Organizational Development": 2},
        "trait_w": {"Strategic": 2, "Analytical": 1},
        "level_w": {"Strategy": 1}
    },
    {
        "id": "Q49",
        "text": "I like working with leaders to align talent decisions with business goals.",
        "func_w": {"Talent Management": 2, "Organizational Development": 1},
        "trait_w": {"Strategic": 2, "People-centric": 1},
        "level_w": {"Leadership": 1, "Strategy": 1}
    },
    {
        "id": "Q50",
        "text": "I prefer long-term talent planning over only reacting to urgent vacancies.",
        "func_w": {"Talent Management": 2, "Organizational Development": 1},
        "trait_w": {"Strategic": 2},
        "level_w": {"Strategy": 2}
    },

    # --- Cross-functional / hybrid questions (tie-breakers) ---
    {
        "id": "Q51",
        "text": "I enjoy creating HR playbooks and service catalogs that improve consistency across regions/teams.",
        "func_w": {"HR Operations": 2, "Organizational Development": 1, "HRIS / HR Technology": 1},
        "trait_w": {"Process-oriented": 2, "Strategic": 1},
        "level_w": {"Ownership": 1, "Strategy": 1}
    },
    {
        "id": "Q52",
        "text": "I like presenting HR recommendations to stakeholders and handling tough questions confidently.",
        "func_w": {"Organizational Development": 1, "HR Analytics": 1, "Talent Management": 1},
        "trait_w": {"Strategic": 2, "People-centric": 1},
        "level_w": {"Leadership": 2}
    },
    {
        "id": "Q53",
        "text": "I feel comfortable working with confidential information and maintaining trust.",
        "func_w": {"Employee Relations": 1, "Compensation & Benefits": 1, "HR Operations": 1},
        "trait_w": {"People-centric": 1, "Process-oriented": 1},
        "level_w": {"Execution": 1}
    },
    {
        "id": "Q54",
        "text": "I enjoy learning new HR concepts, tools, or frameworks quickly when needed.",
        "func_w": {"HRIS / HR Technology": 1, "Learning & Development": 1, "HR Analytics": 1},
        "trait_w": {"Learning agility": 3},
        "level_w": {"Ownership": 1}
    },
    {
        "id": "Q55",
        "text": "I prefer improving processes rather than repeating the same steps without change.",
        "func_w": {"Organizational Development": 1, "HRIS / HR Technology": 1, "HR Operations": 1},
        "trait_w": {"Learning agility": 1, "Strategic": 1, "Process-oriented": 1},
        "level_w": {"Ownership": 2}
    },

    # --- Level-focused (still mapped to functions) ---
    {
        "id": "Q56",
        "text": "I can independently run an HR process end-to-end and deliver results without close supervision.",
        "func_w": {"HR Operations": 1, "Talent Acquisition": 1, "Compensation & Benefits": 1},
        "trait_w": {"Process-oriented": 1},
        "level_w": {"Ownership": 3}
    },
    {
        "id": "Q57",
        "text": "I often spot risks early (compliance, people impact, data quality) and prevent issues before they happen.",
        "func_w": {"Employee Relations": 1, "HR Operations": 1, "HRIS / HR Technology": 1},
        "trait_w": {"Analytical": 1, "Strategic": 1},
        "level_w": {"Strategy": 2, "Ownership": 1}
    },
    {
        "id": "Q58",
        "text": "I enjoy mentoring others and helping them become more effective in their roles.",
        "func_w": {"Learning & Development": 1, "Talent Management": 1},
        "trait_w": {"People-centric": 1, "Learning agility": 1},
        "level_w": {"Leadership": 3}
    },
    {
        "id": "Q59",
        "text": "I can translate business goals into HR priorities and a clear roadmap.",
        "func_w": {"Organizational Development": 1, "Talent Management": 1, "HR Analytics": 1},
        "trait_w": {"Strategic": 2},
        "level_w": {"Strategy": 3}
    },
    {
        "id": "Q60",
        "text": "I’m comfortable influencing senior stakeholders even when there is resistance.",
        "func_w": {"Organizational Development": 1, "Employee Relations": 1, "Talent Management": 1},
        "trait_w": {"People-centric": 1, "Strategic": 1},
        "level_w": {"Leadership": 3}
    },
]
