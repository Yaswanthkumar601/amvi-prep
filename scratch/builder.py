# -*- coding: utf-8 -*-
import json
import os

# Helper to construct a question
def make_q(qid, test_tag, paper, cat, q_text, opts, ans_idx, exp_en, exp_te):
    return {
        "id": qid,
        "testTag": test_tag,
        "paper": paper,
        "category": cat,
        "question": q_text,
        "options": opts,
        "correctAnswer": ans_idx,
        "explanationEn": exp_en,
        "explanationTe": exp_te
    }

questions = []

print("Preparing generators...")

