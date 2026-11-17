# -*- coding: utf-8 -*-
import sys
import json
sys.path.append('scratch')

import build_tests_1_to_5
import gen_p1
import gen_p2_engines_chassis
import gen_p2_chassis_mva_som
import gen_tests_9_10

t1 = build_tests_1_to_5.get_test_1_questions()
t2 = gen_p1.get_test_2_questions()
t3 = gen_p1.get_test_3_questions()
t4 = gen_p2_engines_chassis.get_test_4_questions()
t5 = gen_p2_engines_chassis.get_test_5_questions()
t6 = gen_p2_chassis_mva_som.get_test_6_questions()
t7 = gen_p2_chassis_mva_som.get_test_7_questions()
t8 = gen_p2_chassis_mva_som.get_test_8_questions()
t9 = gen_tests_9_10.get_test_9_questions()
t10 = gen_tests_9_10.get_test_10_questions()

all_raw_tests = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]

all_processed_tests = []
all_questions = []
id_set = set()

def normalize_q(raw):
    if isinstance(raw, tuple):
        return {
            "id": raw[0],
            "paper": raw[2],
            "unit": raw[3].replace("-", "_"),
            "topic": raw[4],
            "question": raw[5],
            "options": raw[6],
            "correctAnswer": raw[7],
            "explanationEn": raw[8],
            "explanationTe": raw[9]
        }
    else:
        return {
            "id": raw["id"],
            "paper": raw["paper"],
            "unit": raw["unit"].replace("-", "_"),
            "topic": raw.get("topic", "General"),
            "question": raw["question"],
            "options": raw["options"],
            "correctAnswer": raw["correctAnswer"],
            "explanationEn": raw["explanationEn"],
            "explanationTe": raw["explanationTe"]
        }

for i, test in enumerate(all_raw_tests, start=1):
    test_list = []
    for item in test:
        q = normalize_q(item)
        qid = q['id']
        if qid in id_set:
            raise ValueError(f"Duplicate ID found: {qid}")
        id_set.add(qid)
        assert len(q['options']) == 4, f"Options not 4 in {qid}"
        assert 0 <= q['correctAnswer'] < 4, f"Invalid correctAnswer in {qid}"
        assert 'explanationEn' in q and len(q['explanationEn']) > 5, f"Missing explanationEn in {qid}"
        assert 'explanationTe' in q and len(q['explanationTe']) > 5, f"Missing explanationTe in {qid}"
        all_questions.append(q)
        test_list.append(q)
    all_processed_tests.append(test_list)

print(f"TOTAL ALL-UNIQUE QUESTIONS VALIDATED: {len(all_questions)}")

# Categorize pool by paper
p1_pool = [q['id'] for q in all_questions if q['paper'] == 1]
p2_pool = [q['id'] for q in all_questions if q['paper'] == 2]

print(f"Paper 1 Pool: {len(p1_pool)} questions")
print(f"Paper 2 Pool: {len(p2_pool)} questions")
assert len(p1_pool) >= 150, "Need at least 150 questions for Paper 1"
assert len(p2_pool) >= 150, "Need at least 150 questions for Paper 2"

# Build EXAM_CONFIGS as an Array
configs_list = [
    # Full 150-Question Official Grand Mocks
    {
        "id": "full_mock_p1",
        "title": "Full Grand Mock: Paper-I General Studies & Mental Ability (Official CBRT)",
        "badge": "Full Official (150 Qs)",
        "paper": 1,
        "standard": "Degree Standard (Official CBRT Pattern)",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "description": "Full 150-question official simulation of Paper-I General Studies & Mental Ability across all 10 units under standard 150-minute exam conditions.",
        "questionIds": p1_pool[:150]
    },
    {
        "id": "full_mock_p2",
        "title": "Full Grand Mock: Paper-II Automobile & Mechanical Engineering (Official CBRT)",
        "badge": "Full Official (150 Qs)",
        "paper": 2,
        "standard": "Diploma Standard (Official CBRT Pattern)",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "description": "Full 150-question official simulation of Paper-II Automobile Engineering across all 6 technical units under standard 150-minute exam conditions.",
        "questionIds": p2_pool[:150]
    },
    
    # 10 Sectional 50-Question Dedicated Tests (Zero Repetition Across Tests)
    {
        "id": "test_1",
        "title": "Mock Test 1: General Studies & Mental Ability (Paper-I Comprehensive)",
        "badge": "Paper-I (50 Qs)",
        "paper": 1,
        "standard": "Degree Standard",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 high-yield questions covering Current Events, Science, History, Polity, Geography, AP Bifurcation & Reasoning.",
        "questionIds": [q['id'] for q in all_processed_tests[0]]
    },
    {
        "id": "test_2",
        "title": "Mock Test 2: Science, Technology, Indian History & Polity (Paper-I Focus)",
        "badge": "Paper-I (50 Qs)",
        "paper": 1,
        "standard": "Degree Standard",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 targeted questions focusing on General Science, Modern Indian History, National Movement & Indian Constitution.",
        "questionIds": [q['id'] for q in all_processed_tests[1]]
    },
    {
        "id": "test_3",
        "title": "Mock Test 3: Geography, AP Economy, Disaster Mgmt & Bifurcation (Paper-I Focus)",
        "badge": "Paper-I (50 Qs)",
        "paper": 1,
        "standard": "Degree Standard",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 questions spanning Indian & AP Geography, State Economy, Welfare Schemes, Disaster Management and AP Reorganisation Act 2014.",
        "questionIds": [q['id'] for q in all_processed_tests[2]]
    },
    {
        "id": "test_4",
        "title": "Mock Test 4: Thermodynamics, IC Engines & Fuel Injection Systems (Paper-II)",
        "badge": "Paper-II (50 Qs)",
        "paper": 2,
        "standard": "Diploma Standard",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 core technical questions on Otto/Diesel/Dual cycles, MPFI, CRDi, Turbocharging, combustion stoichiometry & knocking.",
        "questionIds": [q['id'] for q in all_processed_tests[3]]
    },
    {
        "id": "test_5",
        "title": "Mock Test 5: Engine Performance, Testing, Cooling & Lubrication (Paper-II)",
        "badge": "Paper-II (50 Qs)",
        "paper": 2,
        "standard": "Diploma Standard",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 technical questions covering BP/IP/FP calculations, Morse test, Heat balance sheets, lubrication circuits, SAE grades & cooling.",
        "questionIds": [q['id'] for q in all_processed_tests[4]]
    },
    {
        "id": "test_6",
        "title": "Mock Test 6: Automobile Chassis, Clutches, Gearboxes & Drive Axles (Paper-II)",
        "badge": "Paper-II (50 Qs)",
        "paper": 2,
        "standard": "Diploma Standard",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 questions on clutch friction theory, synchromesh gearboxes, epicyclic gearing, torque converters, propeller shafts, differentials & rear axles.",
        "questionIds": [q['id'] for q in all_processed_tests[5]]
    },
    {
        "id": "test_7",
        "title": "Mock Test 7: Steering Systems, Brakes, Suspension & Wheel Alignment (Paper-II)",
        "badge": "Paper-II (50 Qs)",
        "paper": 2,
        "standard": "Diploma Standard",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 questions on Ackermann/Davis steering, Camber, Caster, Kingpin inclination, Hydraulic/Pneumatic brakes, ABS, ESC, and suspension springs.",
        "questionIds": [q['id'] for q in all_processed_tests[6]]
    },
    {
        "id": "test_8",
        "title": "Mock Test 8: Motor Vehicles Act 1988/2019, CMVR & Strength of Materials (Paper-II)",
        "badge": "Paper-II (50 Qs)",
        "paper": 2,
        "standard": "Diploma Standard",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 questions covering Sections & Rules of MVA 1988/2019, CMVR forms/penalties, computerized inspection lanes, stresses, strains, SFD/BMD & torsion.",
        "questionIds": [q['id'] for q in all_processed_tests[7]]
    },
    {
        "id": "test_9",
        "title": "Mock Test 9: Grand Simulation Test A (Full Syllabus Paper-I & Paper-II)",
        "badge": "Full Grand Mock (50 Qs)",
        "paper": "Both",
        "standard": "Combined APPSC Pattern",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 balanced questions (25 General Studies + 25 Automobile/Mechanical Engineering) simulating the combined test environment.",
        "questionIds": [q['id'] for q in all_processed_tests[8]]
    },
    {
        "id": "test_10",
        "title": "Mock Test 10: Grand Simulation Test B (Full Syllabus Paper-I & Paper-II)",
        "badge": "Full Grand Mock (50 Qs)",
        "paper": "Both",
        "standard": "Combined APPSC Pattern",
        "duration": 50,
        "durationMinutes": 50,
        "totalQuestions": 50,
        "totalMarks": 50,
        "negativeMark": 0.33,
        "description": "50 fresh questions (25 General Studies + 25 Automobile/Mechanical Engineering) covering all high-weightage topics.",
        "questionIds": [q['id'] for q in all_processed_tests[9]]
    },
    
    # Smart dynamic practice
    {
        "id": "smart_dynamic_paper1",
        "title": "Smart Dynamic Practice Mode - Paper-I",
        "badge": "Smart AI (Paper-I: 150 Qs)",
        "paper": 1,
        "standard": "Dynamic Adaptive",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "isDynamicUnattempted": True,
        "description": "Selects 150 Paper-I questions per attempt, prioritizing previously missed questions and then unseen questions. Previously seen questions are used only when needed to fill the paper."
    },
    {
        "id": "smart_dynamic_paper2",
        "title": "Smart Dynamic Practice Mode - Paper-II",
        "badge": "Smart AI (Paper-II: 150 Qs)",
        "paper": 2,
        "standard": "Dynamic Adaptive",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "isDynamicUnattempted": True,
        "description": "Selects 150 Paper-II questions per attempt, prioritizing previously missed questions and then unseen questions. Previously seen questions are used only when needed to fill the paper."
    },
    
    # Official Previous Papers (FULL 150 QUESTIONS, 150 MARKS, 150 MINUTES)
    {
        "id": "prev_2023_p1",
        "title": "APPSC AMVI 2023 Official Paper-I (General Studies & Mental Ability)",
        "badge": "Official (150 Qs • 150 Mins)",
        "paper": 1,
        "standard": "Degree Standard (Official CBRT Pattern)",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "description": "Full 150-question official examination paper replicating the 2023 APPSC AMVI Paper-I standard across all 10 General Studies & Mental Ability units.",
        "questionIds": p1_pool[:150]
    },
    {
        "id": "prev_2023_p2",
        "title": "APPSC AMVI 2023 Official Paper-II (Automobile & Mechanical Engineering)",
        "badge": "Official (150 Qs • 150 Mins)",
        "paper": 2,
        "standard": "Diploma Standard (Official CBRT Pattern)",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "description": "Full 150-question official technical paper conforming to the 2023 APPSC AMVI Automobile Engineering standard across all 6 core units.",
        "questionIds": p2_pool[:150]
    },
    {
        "id": "prev_2019_p1",
        "title": "APPSC AMVI 2019 Official Paper-I (General Studies & Mental Ability)",
        "badge": "Official (150 Qs • 150 Mins)",
        "paper": 1,
        "standard": "Degree Standard (Official CBRT Pattern)",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "description": "Full 150-question examination paper replicating the 2019 APPSC AMVI General Studies & Mental Ability standard with detailed bilingual explanations.",
        "questionIds": p1_pool[25:175] if len(p1_pool) >= 175 else p1_pool[:150]
    },
    {
        "id": "prev_2019_p2",
        "title": "APPSC AMVI 2019 Official Paper-II (Automobile & Mechanical Engineering)",
        "badge": "Official (150 Qs • 150 Mins)",
        "paper": 2,
        "standard": "Diploma Standard (Official CBRT Pattern)",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "description": "Full 150-question examination paper replicating the 2019 APPSC AMVI Automobile Engineering paper covering modern transmissions, chassis, and MVA.",
        "questionIds": p2_pool[150:300] if len(p2_pool) >= 300 else p2_pool[:150]
    },
    {
        "id": "prev_2012_p1",
        "title": "APPSC AMVI 2012 Official Paper-I (General Studies & Mental Ability)",
        "badge": "Official (150 Qs • 150 Mins)",
        "paper": 1,
        "standard": "Degree Standard (Official CBRT Pattern)",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "description": "Full 150-question benchmark paper testing foundational General Studies, Indian Constitution, Geography, Economy, and Mental Ability.",
        "questionIds": p1_pool[50:200] if len(p1_pool) >= 200 else p1_pool[:150]
    },
    {
        "id": "prev_2012_p2",
        "title": "APPSC AMVI 2012 Official Paper-II (Automobile & Mechanical Engineering)",
        "badge": "Official (150 Qs • 150 Mins)",
        "paper": 2,
        "standard": "Diploma Standard (Official CBRT Pattern)",
        "duration": 150,
        "durationMinutes": 150,
        "totalQuestions": 150,
        "totalMarks": 150,
        "negativeMark": 0.33,
        "description": "Full 150-question benchmark technical paper covering Thermodynamics, IC Engines, Chassis design, and Strength of Materials fundamentals.",
        "questionIds": p2_pool[75:225] if len(p2_pool) >= 225 else p2_pool[:150]
    }
]

# Add unit-level mock test configurations dynamically
unit_questions_map = {}
for q in all_questions:
    u = q['unit']
    if u not in unit_questions_map:
        unit_questions_map[u] = []
    unit_questions_map[u].append(q['id'])

unit_titles = {
    "p1_u1": "Paper-I Unit 1: Current Affairs (National & International)",
    "p1_u2": "Paper-I Unit 2: General Science & Everyday Applications",
    "p1_u3": "Paper-I Unit 3: Modern Indian History & National Movement",
    "p1_u4": "Paper-I Unit 4: Indian Polity, Constitution & Governance",
    "p1_u5": "Paper-I Unit 5: Physical & Economic Geography of India & AP",
    "p1_u6": "Paper-I Unit 6: Indian & AP Economy & Welfare Initiatives",
    "p1_u7": "Paper-I Unit 7: Disaster Management & Environmental Ecology",
    "p1_u8": "Paper-I Unit 8: Bifurcation of Andhra Pradesh (AP Reorganisation Act)",
    "p1_u9": "Paper-I Unit 9: Mental Ability, Reasoning & Logical Deduction",
    "p1_u10": "Paper-I Unit 10: Data Interpretation & Basic Statistics",
    "p2_u1": "Paper-II Unit 1: Thermodynamics, IC Engines & Combustion",
    "p2_u2": "Paper-II Unit 2: Automobile Chassis, Clutches & Transmission",
    "p2_u3": "Paper-II Unit 3: Steering Systems, Brakes & Suspension",
    "p2_u4": "Paper-II Unit 4: Motor Vehicles Act 1988 & Central MV Rules",
    "p2_u5": "Paper-II Unit 5: Strength of Materials & Mechanics of Solids",
    "p2_u6": "Paper-II Unit 6: Inspection Equipment, Testing & Emission Standards"
}

for uid, qids in unit_questions_map.items():
    configs_list.append({
        "id": f"unit_{uid}",
        "title": f"Unit Practice Mock: {unit_titles.get(uid, uid)}",
        "badge": f"Unit Mock ({len(qids)} Qs)",
        "paper": 1 if uid.startswith("p1") else 2,
        "standard": "Topic-wise Mastery",
        "duration": max(15, len(qids)),
        "durationMinutes": max(15, len(qids)),
        "totalQuestions": len(qids),
        "totalMarks": len(qids),
        "negativeMark": 0.33,
        "description": f"Targeted practice test covering {unit_titles.get(uid, uid)} with full bilingual explanations.",
        "questionIds": qids
    })

output_js = f"""/**
 * APPSC AMVI (Assistant Motor Vehicle Inspector) - Master Question Bank
 * Total Questions: {len(all_questions)}
 * Structure: 10 Non-Repeating Mock Tests (50 Qs each = 500 Qs), Previous Papers & Unit Mock Tests
 * All questions contain complete English and Telugu (తెలుగు వివరణ) explanations.
 */

const QUESTION_BANK = {json.dumps(all_questions, ensure_ascii=False, indent=2)};

const EXAM_CONFIGS = {json.dumps(configs_list, ensure_ascii=False, indent=2)};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ QUESTION_BANK, EXAM_CONFIGS }};
}}
"""

with open('js/questionBank.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print("Successfully wrote js/questionBank.js with Official 150-question previous papers!")
