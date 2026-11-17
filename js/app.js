/**
 * APPSC AMVI Application Controller
 * Handles UI interactions, tab routing, study material documentation rendering,
 * syllabus tracking, CBT simulation, previous papers launcher, and bilingual solution rendering.
 */

document.addEventListener("DOMContentLoaded", () => {
  initTabs();
  renderStudyDocumentation();
  renderSyllabusAccordions();
  renderPreviousPapers();
  renderFormulaCards();
  initExamLauncher();
  initCbtControls();
  initResultsFilter();
});

// =========================================================================
// 1. TAB ROUTING & NAVIGATION
// =========================================================================
function initTabs() {
  const tabButtons = document.querySelectorAll(".nav-tab-btn");
  const tabPanes = document.querySelectorAll(".tab-pane");

  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetTabId = btn.getAttribute("data-tab");
      switchTab(targetTabId);
    });
  });
}

function switchTab(targetTabId) {
  const tabButtons = document.querySelectorAll(".nav-tab-btn");
  const tabPanes = document.querySelectorAll(".tab-pane");

  tabButtons.forEach(b => {
    if (b.getAttribute("data-tab") === targetTabId) {
      b.classList.add("active");
    } else {
      b.classList.remove("active");
    }
  });

  tabPanes.forEach(pane => {
    if (pane.id === targetTabId) {
      pane.classList.add("active");
    } else {
      pane.classList.remove("active");
    }
  });

  window.scrollTo({ top: 0, behavior: "smooth" });
}

// =========================================================================
// 2. IN-DEPTH STUDY DOCUMENTATION RENDERING (PHASE 1 & PHASE 2)
// =========================================================================
function renderStudyDocumentation() {
  const p1DocsContainer = document.getElementById("p1-docs-view");
  const p2DocsContainer = document.getElementById("p2-docs-view");

  if (p1DocsContainer && AMVI_STUDY_MATERIAL.paper1) {
    p1DocsContainer.innerHTML = AMVI_STUDY_MATERIAL.paper1.map(doc => createDocCardHtml(doc, "p1")).join("");
  }

  if (p2DocsContainer && AMVI_STUDY_MATERIAL.paper2) {
    p2DocsContainer.innerHTML = AMVI_STUDY_MATERIAL.paper2.map(doc => createDocCardHtml(doc, "p2")).join("");
  }
}

function createDocCardHtml(doc, prefix) {
  const conceptsHtml = doc.keyConcepts.map(c => `
    <div style="margin-bottom:16px;">
      <h5 style="color:var(--primary-dark); font-size:1.02rem; margin-bottom:6px; font-weight:700;">${c.heading}</h5>
      <p style="font-size:0.92rem; color:#334155; line-height:1.7; white-space:pre-line;">${c.content}</p>
    </div>
  `).join("");

  const pointersHtml = doc.examPointers.map(p => `
    <li style="margin-bottom:6px; position:relative; padding-left:22px; font-size:0.9rem; color:#0f172a;">
      <span style="position:absolute; left:0; color:#d97706; font-weight:bold;">★</span>
      ${p}
    </li>
  `).join("");

  const borderColor = prefix === "p1" ? "var(--primary)" : "var(--secondary)";

  return `
    <div class="card" style="border-left:5px solid ${borderColor}; margin-bottom:24px;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
        <h3 style="font-size:1.22rem; color:var(--primary-dark); margin:0;">${doc.title}</h3>
        <span class="badge-tag" style="background:#e0f2fe; color:#0369a1; font-weight:700;">📖 Study Notes & Concepts</span>
      </div>
      <p style="font-size:0.92rem; color:var(--text-secondary); margin-bottom:18px; font-style:italic;">
        ${doc.overview}
      </p>

      <div style="background:#fafafa; border:1px solid #e2e8f0; border-radius:var(--radius-sm); padding:18px; margin-bottom:18px;">
        ${conceptsHtml}
      </div>

      <div style="background:#fffbeb; border:1.5px solid #fde68a; border-radius:var(--radius-sm); padding:14px 18px;">
        <strong style="display:block; color:#b45309; font-size:0.9rem; text-transform:uppercase; letter-spacing:0.04em; margin-bottom:8px;">
          🎯 High-Yield APPSC Exam Pointers
        </strong>
        <ul style="list-style:none; padding-left:0; margin:0;">
          ${pointersHtml}
        </ul>
      </div>
    </div>
  `;
}

// Toggle between In-Depth Docs and Checklist
window.togglePaperView = function(paperPrefix, viewType) {
  const docsView = document.getElementById(`${paperPrefix}-docs-view`);
  const checklistView = document.getElementById(`${paperPrefix}-checklist-view`);
  const btnDocs = document.getElementById(`btn-${paperPrefix}-view-docs`);
  const btnChecklist = document.getElementById(`btn-${paperPrefix}-view-checklist`);

  if (viewType === 'docs') {
    docsView.style.display = 'block';
    checklistView.style.display = 'none';
    btnDocs.classList.add('active');
    btnChecklist.classList.remove('active');
  } else {
    docsView.style.display = 'none';
    checklistView.style.display = 'block';
    btnDocs.classList.remove('active');
    btnChecklist.classList.add('active');
  }
};

// =========================================================================
// 3. SYLLABUS CHECKLIST RENDERING & LOCALSTORAGE
// =========================================================================
function renderSyllabusAccordions() {
  const p1Container = document.getElementById("p1-syllabus-accordion-container");
  const p2Container = document.getElementById("p2-syllabus-accordion-container");

  if (p1Container) {
    p1Container.innerHTML = APPSC_AMVI_DATA.syllabus.paper1.units.map(unit => createUnitHtml(unit, "p1")).join("");
  }
  if (p2Container) {
    p2Container.innerHTML = APPSC_AMVI_DATA.syllabus.paper2.units.map(unit => createUnitHtml(unit, "p2")).join("");
  }

  // Bind accordion toggles
  document.querySelectorAll(".unit-header").forEach(header => {
    header.addEventListener("click", () => {
      const content = header.nextElementSibling;
      const isAlreadyActive = header.classList.contains("active");
      header.classList.toggle("active", !isAlreadyActive);
      content.classList.toggle("active", !isAlreadyActive);
    });
  });

  // Bind topic checkbox progress
  document.querySelectorAll(".topic-checkbox").forEach(chk => {
    chk.addEventListener("change", (e) => {
      saveTopicState(e.target.dataset.topicId, e.target.checked);
      updateSyllabusProgress();
    });
  });

  loadSavedTopics();
  updateSyllabusProgress();
}

function createUnitHtml(unit, paperPrefix) {
  const topicsHtml = unit.topics.map((t, idx) => {
    const topicId = `${unit.id}-t${idx}`;
    return `
      <li style="display:flex; align-items:flex-start; gap:10px; margin-bottom:8px;">
        <input type="checkbox" class="topic-checkbox" data-topic-id="${topicId}" data-paper="${paperPrefix}" id="${topicId}" style="margin-top:4px; cursor:pointer; width:16px; height:16px;">
        <label for="${topicId}" style="cursor:pointer; flex:1; font-size:0.92rem; color:#334155;">${t}</label>
      </li>
    `;
  }).join("");

  // Retrieve matching In-Depth Study Material for this unit
  const docList = paperPrefix === "p1" ? AMVI_STUDY_MATERIAL.paper1 : AMVI_STUDY_MATERIAL.paper2;
  const doc = docList ? docList.find(d => d.unitId === unit.id) : null;

  let inDepthDropdownHtml = "";
  if (doc) {
    const conceptsHtml = doc.keyConcepts.map(c => `
      <div style="margin-bottom:14px;">
        <h6 style="color:var(--primary-dark); font-size:0.95rem; font-weight:700; margin-bottom:4px;">${c.heading}</h6>
        <p style="font-size:0.88rem; color:#334155; line-height:1.65; white-space:pre-line; margin:0;">${c.content}</p>
      </div>
    `).join("");

    const pointersHtml = doc.examPointers.map(p => `
      <li style="margin-bottom:6px; position:relative; padding-left:20px; font-size:0.88rem; color:#0f172a;">
        <span style="position:absolute; left:0; color:#d97706; font-weight:bold;">★</span>
        ${p}
      </li>
    `).join("");

    inDepthDropdownHtml = `
      <details class="unit-indepth-details" style="margin-top:14px; border:1px solid #cbd5e1; border-radius:var(--radius-sm); background:#f8fafc; padding:12px 16px;">
        <summary style="cursor:pointer; font-weight:700; color:var(--primary-dark); font-size:0.95rem; display:flex; align-items:center; gap:8px;">
          <span>📖 View In-Depth Concepts & High-Yield Exam Points (Click to Expand)</span>
        </summary>
        <div style="margin-top:14px; padding-top:12px; border-top:1px solid #e2e8f0;">
          <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:12px; font-style:italic;">${doc.overview}</p>
          <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin-bottom:14px;">
            ${conceptsHtml}
          </div>
          <div style="background:#fffbeb; border:1.5px solid #fde68a; border-radius:6px; padding:12px 16px;">
            <strong style="display:block; color:#b45309; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.04em; margin-bottom:6px;">
              🎯 High-Yield APPSC Exam Pointers
            </strong>
            <ul style="list-style:none; padding-left:0; margin:0;">
              ${pointersHtml}
            </ul>
          </div>
        </div>
      </details>
    `;
  }

  const unitExamId = `unit_${unit.id.replace(/-/g, '_')}`;

  return `
    <div class="unit-accordion">
      <div class="unit-header">
        <div class="unit-title-group">
          <span class="unit-index-badge">${unit.id.toUpperCase()}</span>
          <span style="font-weight:600; color:#1e293b; font-size:1.02rem;">${unit.title}</span>
        </div>
        <div style="display:flex; align-items:center; gap:10px;">
          <span class="unit-weightage-pill">⚖️ ${unit.weightage}</span>
          <span style="font-size:0.85rem; color:var(--text-secondary);">▼</span>
        </div>
      </div>
      <div class="unit-content">
        <div style="margin-bottom:12px;">
          <strong style="display:block; font-size:0.85rem; text-transform:uppercase; color:var(--text-secondary); margin-bottom:8px;">Syllabus Checklist:</strong>
          <ul style="list-style:none; padding-left:0; margin:0;">
            ${topicsHtml}
          </ul>
        </div>

        ${inDepthDropdownHtml}

        <div style="margin-top:16px; padding-top:14px; border-top:1px dashed #cbd5e1; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
          <span style="font-size:0.84rem; color:var(--text-secondary);">
            Mastered this unit? Test your knowledge with a focused mock test:
          </span>
          <button class="btn-primary" onclick="launchExamDirect('${unitExamId}')" style="padding:8px 18px; font-size:0.88rem; display:inline-flex; align-items:center; gap:6px;">
            🎯 Practice ${unit.id.toUpperCase()} Mock Test Now ➡️
          </button>
        </div>
      </div>
    </div>
  `;
}

function saveTopicState(topicId, isChecked) {
  const saved = JSON.parse(localStorage.getItem("appsc_amvi_syllabus_checked") || "{}");
  saved[topicId] = isChecked;
  localStorage.setItem("appsc_amvi_syllabus_checked", JSON.stringify(saved));
}

function loadSavedTopics() {
  const saved = JSON.parse(localStorage.getItem("appsc_amvi_syllabus_checked") || "{}");
  document.querySelectorAll(".topic-checkbox").forEach(chk => {
    if (saved[chk.dataset.topicId]) {
      chk.checked = true;
    }
  });
}

function updateSyllabusProgress() {
  ["p1", "p2"].forEach(prefix => {
    const all = document.querySelectorAll(`.topic-checkbox[data-paper="${prefix}"]`);
    const checked = document.querySelectorAll(`.topic-checkbox[data-paper="${prefix}"]:checked`);
    const pct = all.length > 0 ? Math.round((checked.length / all.length) * 100) : 0;
    const elem = document.getElementById(`${prefix}-progress-pct`);
    if (elem) elem.textContent = `${pct}%`;
  });
}

// =========================================================================
// 4. PREVIOUS PAPERS & DIRECT LAUNCHER
// =========================================================================
function renderPreviousPapers() {
  const container = document.getElementById("previous-papers-container");
  if (!container) return;

  container.innerHTML = APPSC_AMVI_DATA.previousPapers.map(paper => {
    const p1Id = `prev_${paper.year}_p1`;
    const p2Id = `prev_${paper.year}_p2`;
    return `
      <div class="card" style="border-top:4px solid var(--primary); display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <span style="background:var(--primary); color:#fff; font-size:0.8rem; font-weight:700; padding:3px 10px; border-radius:12px;">${paper.year} Official Paper</span>
            <small style="color:var(--text-secondary);">${paper.examDate}</small>
          </div>
          <h3 style="font-size:1.1rem; color:var(--primary-dark); margin-bottom:8px;">${paper.title}</h3>
          <div style="background:#f8fafc; padding:10px; border-radius:var(--radius-sm); font-size:0.85rem; margin-bottom:12px;">
            <div>Paper-1 Degree Std Avg: <strong>${paper.paper1MarksAvg}</strong></div>
            <div>Paper-2 Diploma Std Avg: <strong>${paper.paper2MarksAvg}</strong></div>
          </div>
          <p style="font-size:0.88rem; color:#475569; margin-bottom:12px;">${paper.analysis}</p>
          <div style="margin-bottom:16px;">
            <strong style="font-size:0.8rem; text-transform:uppercase; color:var(--text-secondary);">High-Frequency Focus Areas:</strong>
            <div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:6px;">
              ${paper.keyTopics.map(t => `<span style="background:#e0e7ff; color:#3730a3; font-size:0.75rem; font-weight:600; padding:2px 8px; border-radius:10px;">${t}</span>`).join("")}
            </div>
          </div>
        </div>

        <div style="display:flex; flex-direction:column; gap:8px; margin-top:10px;">
          <button class="btn-primary" onclick="launchExamDirect('${p1Id}')" style="width:100%; justify-content:center; padding:10px; font-size:0.88rem;">
            🚀 Practice ${paper.year} Paper-I (GS & Mental Ability — 150 Qs • 150 Marks • 150 Mins)
          </button>
          <button class="btn-primary" onclick="launchExamDirect('${p2Id}')" style="width:100%; justify-content:center; padding:10px; font-size:0.88rem; background:var(--secondary); border-color:var(--secondary);">
            ⚙️ Practice ${paper.year} Paper-II (Auto & Mech Engg — 150 Qs • 150 Marks • 150 Mins)
          </button>
        </div>
      </div>
    `;
  }).join("");
}

window.launchExamDirect = function(examConfigId) {
  selectedExamConfigId = examConfigId;
  switchTab("tab-mock-exams");
  startExamSession(examConfigId);
};

function renderFormulaCards() {
  const container = document.getElementById("formulas-container");
  if (!container) return;

  container.innerHTML = APPSC_AMVI_DATA.formulaSheet.map(item => `
    <div class="card" style="border-left:5px solid var(--secondary);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
        <span style="font-size:0.78rem; text-transform:uppercase; color:var(--text-secondary); font-weight:700;">${item.category}</span>
      </div>
      <h4 style="color:var(--primary-dark); font-size:1.05rem; margin-bottom:8px;">${item.title}</h4>
      <div style="background:#f1f5f9; padding:12px; border-radius:var(--radius-sm); font-family:monospace; font-size:1.05rem; font-weight:700; color:#0f172a; margin-bottom:10px; overflow-x:auto;">
        ${item.formula}
      </div>
      <p style="font-size:0.86rem; color:#475569; line-height:1.6;">${item.description}</p>
    </div>
  `).join("");
}

// =========================================================================
// 5. MOCK EXAM LAUNCHER & CBT CONTROLS
// =========================================================================
let selectedExamConfigId = EXAM_CONFIGS[0].id;
let currentExamFilter = "mocks";

window.filterExamCards = function(category) {
  currentExamFilter = category;
  ["mocks", "smart", "prev", "units", "all"].forEach(cat => {
    const btn = document.getElementById(`btn-filter-${cat}`);
    if (btn) btn.classList.toggle("active", cat === category);
  });
  renderExamCards();
};

function renderExamCards() {
  const listElem = document.getElementById("exam-selection-list");
  if (!listElem) return;

  let filteredExams = [];
  if (currentExamFilter === "mocks") {
    filteredExams = EXAM_CONFIGS.filter(e => e.id.startsWith("test_"));
  } else if (currentExamFilter === "smart") {
    filteredExams = EXAM_CONFIGS.filter(e => e.isDynamicUnattempted);
  } else if (currentExamFilter === "prev") {
    filteredExams = EXAM_CONFIGS.filter(e => e.id.startsWith("prev_"));
  } else if (currentExamFilter === "units") {
    filteredExams = EXAM_CONFIGS.filter(e => e.id.startsWith("unit_"));
  } else {
    filteredExams = EXAM_CONFIGS;
  }

  listElem.innerHTML = filteredExams.map((exam, idx) => {
    const isSelected = exam.id === selectedExamConfigId || (idx === 0 && !filteredExams.some(e => e.id === selectedExamConfigId));
    return `
      <div class="exam-choice-btn ${isSelected ? 'selected' : ''}" data-exam-id="${exam.id}">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
          <div class="exam-choice-title" style="margin:0; font-size:1.02rem;">${exam.title}</div>
          <span style="background:${exam.isDynamicUnattempted ? '#dcfce7' : (exam.id.startsWith('test_') ? '#e0f2fe' : '#e0e7ff')}; color:${exam.isDynamicUnattempted ? '#15803d' : (exam.id.startsWith('test_') ? '#0369a1' : '#3730a3')}; font-size:0.75rem; font-weight:700; padding:3px 10px; border-radius:12px;">
            ${exam.badge || 'Mock'}
          </span>
        </div>
        <div class="exam-choice-meta" style="color:#475569; font-weight:600;">
          ⏱️ ${exam.durationMinutes || exam.duration} Mins • 📝 ${exam.totalQuestions} Questions • ⚖️ Negative: -0.33
        </div>
        <p style="font-size:0.84rem; color:#64748b; margin-top:8px; line-height:1.5;">${exam.description}</p>
      </div>
    `;
  }).join("");

  if (!filteredExams.some(e => e.id === selectedExamConfigId) && filteredExams.length > 0) {
    selectedExamConfigId = filteredExams[0].id;
  }

  document.querySelectorAll(".exam-choice-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".exam-choice-btn").forEach(b => b.classList.remove("selected"));
      btn.classList.add("selected");
      selectedExamConfigId = btn.getAttribute("data-exam-id");
    });
  });
}

function initExamLauncher() {
  renderExamCards();

  const startBtn = document.getElementById("btn-start-exam");
  if (startBtn) {
    startBtn.addEventListener("click", () => {
      startExamSession(selectedExamConfigId);
    });
  }
}

function startExamSession(examId) {
  examEngine.startExam(examId);

  // Switch UI views
  document.getElementById("cbt-launcher").style.display = "none";
  document.getElementById("cbt-active-screen").style.display = "block";

  renderCurrentQuestion();
  renderQuestionPalette();
}

function initCbtControls() {
  // Timer tick listener
  window.addEventListener("exam-timer-tick", (e) => {
    const timerElem = document.getElementById("cbt-timer");
    if (timerElem) {
      timerElem.textContent = e.detail.formatted;
      timerElem.classList.toggle("low-time", e.detail.isLowTime);
    }
  });

  // Action buttons
  document.getElementById("btn-save-next").addEventListener("click", () => {
    examEngine.saveAndNext();
    renderCurrentQuestion();
    renderQuestionPalette();
  });

  document.getElementById("btn-clear-response").addEventListener("click", () => {
    examEngine.clearResponse();
    renderCurrentQuestion();
    renderQuestionPalette();
  });

  document.getElementById("btn-mark-review").addEventListener("click", () => {
    examEngine.markForReviewAndNext();
    renderCurrentQuestion();
    renderQuestionPalette();
  });

  document.getElementById("btn-prev-q").addEventListener("click", () => {
    examEngine.goToPrevious();
    renderCurrentQuestion();
    renderQuestionPalette();
  });

  // Submit Modal Controls
  const modal = document.getElementById("submit-confirm-modal");
  document.getElementById("btn-trigger-submit").addEventListener("click", () => {
    const summary = examEngine.getSummaryCounts();
    document.getElementById("modal-summary-answered").textContent = summary.answered + summary.answeredAndMarked;
    document.getElementById("modal-summary-not-answered").textContent = summary.notAnswered;
    document.getElementById("modal-summary-marked").textContent = summary.marked;
    document.getElementById("modal-summary-not-visited").textContent = summary.notVisited;
    modal.style.display = "flex";
  });

  document.getElementById("btn-modal-cancel").addEventListener("click", () => {
    modal.style.display = "none";
  });

  document.getElementById("btn-modal-confirm").addEventListener("click", () => {
    modal.style.display = "none";
    examEngine.submitExam(false);
  });

  // Exam submitted event handler
  window.addEventListener("exam-submitted", (e) => {
    displayResults(e.detail);
  });

  // Retake exam button in results pane
  document.getElementById("btn-retake-exam").addEventListener("click", () => {
    document.getElementById("cbt-launcher").style.display = "block";
    document.getElementById("cbt-active-screen").style.display = "none";
    switchTab("tab-mock-exams");
  });
}

function renderCurrentQuestion() {
  const q = examEngine.getCurrentQuestion();
  if (!q) return;

  const state = examEngine.getCurrentState();
  const currentIdx = examEngine.currentIndex;

  document.getElementById("cbt-current-q-num").textContent = `Question ${currentIdx + 1} of ${examEngine.questions.length}`;
  document.getElementById("cbt-q-category").textContent = `[${q.category}]`;
  document.getElementById("cbt-question-text").textContent = q.question;

  // Render options
  const optionsWrapper = document.getElementById("cbt-options-wrapper");
  optionsWrapper.innerHTML = q.options.map((opt, optIdx) => {
    const isSelected = state && state.selectedOption === optIdx;
    return `
      <div class="option-item ${isSelected ? 'selected' : ''}" onclick="selectExamOption(${optIdx})">
        <input type="radio" name="cbt_option" class="option-radio" value="${optIdx}" ${isSelected ? 'checked' : ''}>
        <label class="option-label">
          <strong>${String.fromCharCode(65 + optIdx)}.</strong> ${opt}
        </label>
      </div>
    `;
  }).join("");

  // Disable Prev on first question
  document.getElementById("btn-prev-q").disabled = currentIdx === 0;
}

window.selectExamOption = function(optionIndex) {
  examEngine.selectOption(optionIndex);
  renderCurrentQuestion();
  renderQuestionPalette();
};

function renderQuestionPalette() {
  const grid = document.getElementById("cbt-palette-grid");
  if (!grid) return;

  grid.innerHTML = examEngine.questions.map((q, idx) => {
    const resp = examEngine.userResponses[q.id];
    const isCurrent = idx === examEngine.currentIndex;
    let statusClass = "palette-not-visited";

    if (resp) {
      if (resp.status === "answered") statusClass = "palette-answered";
      else if (resp.status === "not-answered") statusClass = "palette-not-answered";
      else if (resp.status === "marked-for-review") statusClass = "palette-marked";
      else if (resp.status === "answered-and-marked") statusClass = "palette-answered-marked";
    }

    return `
      <button class="palette-cell ${statusClass} ${isCurrent ? 'current-q' : ''}" onclick="jumpToExamQuestion(${idx})">
        ${idx + 1}
      </button>
    `;
  }).join("");
}

window.jumpToExamQuestion = function(idx) {
  examEngine.goToQuestion(idx);
  renderCurrentQuestion();
  renderQuestionPalette();
};

// =========================================================================
// 6. RESULTS & BILINGUAL EXPLANATIONS RENDERING
// =========================================================================
let currentResultsData = null;
let activeSolutionFilter = "all";
let activeLanguageFilter = "both";

function displayResults(results) {
  currentResultsData = results;

  // Unhide the Results tab in header
  const resultsNavBtn = document.getElementById("nav-btn-results");
  if (resultsNavBtn) resultsNavBtn.style.display = "inline-flex";

  // Switch to Results tab
  switchTab("tab-results");

  // Populate Scorecard
  document.getElementById("results-exam-title").textContent = `Scorecard: ${results.examTitle}`;
  document.getElementById("res-net-score").textContent = results.netMarks;
  document.getElementById("res-max-marks").textContent = `out of ${results.maxMarks} Marks`;
  document.getElementById("res-correct-count").textContent = results.correctCount;
  document.getElementById("res-incorrect-count").textContent = results.incorrectCount;
  document.getElementById("res-unattempted-count").textContent = results.unattemptedCount;
  document.getElementById("res-accuracy-pct").textContent = `${results.accuracy}%`;
  document.getElementById("res-time-taken").textContent = results.timeTaken;
  document.getElementById("res-penalty-text").textContent = 
    `Gross Marks: +${results.grossPositiveScore.toFixed(2)} | Negative Penalty (-0.33): -${results.penaltyDeduction} marks`;

  renderFilteredSolutions();
}

function initResultsFilter() {
  document.querySelectorAll(".filter-btn[data-filter]").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".filter-btn[data-filter]").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeSolutionFilter = btn.getAttribute("data-filter");
      renderFilteredSolutions();
    });
  });

  document.querySelectorAll(".filter-btn[data-lang]").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".filter-btn[data-lang]").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeLanguageFilter = btn.getAttribute("data-lang");
      renderFilteredSolutions();
    });
  });
}

function renderFilteredSolutions() {
  if (!currentResultsData) return;

  const container = document.getElementById("results-questions-list");
  if (!container) return;

  const filtered = currentResultsData.detailedEvaluation.filter(item => {
    if (activeSolutionFilter === "correct") return item.isCorrect;
    if (activeSolutionFilter === "incorrect") return item.isIncorrect;
    if (activeSolutionFilter === "unattempted") return !item.isAttempted;
    return true; // 'all'
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding:40px; color:var(--text-secondary); background:#fff; border-radius:var(--radius-md);">
        No questions match the selected filter.
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map((item, idx) => {
    const q = item.question;
    let cardStatusClass = "unattempted";
    let statusBadgeText = "⚪ Not Attempted";

    if (item.isCorrect) {
      cardStatusClass = "correct";
      statusBadgeText = "✅ Correct (+1.00)";
    } else if (item.isIncorrect) {
      cardStatusClass = "incorrect";
      statusBadgeText = "❌ Incorrect (-0.33)";
    }

    const showEnglish = activeLanguageFilter === "both" || activeLanguageFilter === "en";
    const showTelugu = activeLanguageFilter === "both" || activeLanguageFilter === "te";

    return `
      <div class="review-card ${cardStatusClass}">
        <div class="review-card-header">
          <div>
            <strong style="color:var(--primary-dark); font-size:1.05rem;">Q${idx + 1} [${q.category}]</strong>
          </div>
          <span class="q-status-badge ${cardStatusClass}">${statusBadgeText}</span>
        </div>

        <div style="font-size:1.02rem; font-weight:500; color:#1e293b; margin-bottom:14px; line-height:1.6;">
          ${q.question}
        </div>

        <!-- Options with Answer highlights -->
        <div style="display:flex; flex-direction:column; gap:8px; margin-bottom:14px;">
          ${q.options.map((opt, oIdx) => {
            const isCorrectAnswer = oIdx === q.correctAnswer;
            const isUserSelection = oIdx === item.selectedOption;
            let optStyle = "background:#f8fafc; border:1px solid #e2e8f0; color:#334155;";

            if (isCorrectAnswer) {
              optStyle = "background:#dcfce7; border:1.5px solid #16a34a; font-weight:600; color:#14532d;";
            } else if (isUserSelection && !isCorrectAnswer) {
              optStyle = "background:#fee2e2; border:1.5px solid #dc2626; color:#7f1d1d;";
            }

            return `
              <div style="padding:10px 14px; border-radius:var(--radius-sm); font-size:0.92rem; display:flex; justify-content:space-between; align-items:center; ${optStyle}">
                <span><strong>${String.fromCharCode(65 + oIdx)}.</strong> ${opt}</span>
                <span>
                  ${isCorrectAnswer ? '✔️ <span style="font-size:0.75rem; text-transform:uppercase;">(Correct Answer)</span>' : ''}
                  ${isUserSelection && !isCorrectAnswer ? '❌ <span style="font-size:0.75rem; text-transform:uppercase;">(Your Answer)</span>' : ''}
                  ${isUserSelection && isCorrectAnswer ? ' ⭐ <span style="font-size:0.75rem; text-transform:uppercase;">(Your Choice)</span>' : ''}
                </span>
              </div>
            `;
          }).join("")}
        </div>

        <!-- Bilingual Explanations -->
        <div class="explanation-box">
          ${showEnglish ? `
            <div>
              <div class="explanation-title">
                📘 English Explanation:
              </div>
              <div class="explanation-text-en">
                ${q.explanationEn}
              </div>
            </div>
          ` : ''}

          ${showTelugu ? `
            <div class="${showEnglish ? 'explanation-box-te' : ''}">
              <div class="explanation-title-te">
                📙 తెలుగు వివరణ (Telugu Explanation):
              </div>
              <div class="explanation-text-te">
                ${q.explanationTe}
              </div>
            </div>
          ` : ''}
        </div>
      </div>
    `;
  }).join("");
}
