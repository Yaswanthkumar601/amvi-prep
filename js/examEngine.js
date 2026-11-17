/**
 * APPSC AMVI Exam Engine
 * Handles online Computer Based Recruitment Test (CBRT) simulation, timer, state, scoring, and review.
 * Features smart non-repeating question tracking across test attempts.
 */

class AMVIExamEngine {
  constructor() {
    this.currentExamConfig = null;
    this.questions = [];
    this.currentIndex = 0;
    this.userResponses = {}; // { questionId: { selectedOption: number|null, status: string, timeSpent: number } }
    this.timerInterval = null;
    this.remainingSeconds = 0;
    this.totalSeconds = 0;
    this.isExamActive = false;
    this.examResults = null;
    this.solutionLanguageFilter = "both"; // "both", "en", "te"
  }

  startExam(examConfigId) {
    const config = EXAM_CONFIGS.find(c => c.id === examConfigId);
    if (!config) {
      console.error("Exam config not found:", examConfigId);
      return;
    }

    this.currentExamConfig = config;

    // Handle paper-specific Smart Dynamic Practice Mode.
    if (config.isDynamicUnattempted) {
      this.questions = this.buildSmartDynamicPaper(config);
    } else if (config.questionIds && config.questionIds.length > 0) {
      // Map configured IDs to questions from master bank
      const qMap = new Map(QUESTION_BANK.map(q => [q.id, q]));
      this.questions = config.questionIds.map(id => qMap.get(id)).filter(Boolean);
    } else if (typeof config.filterFn === "function") {
      this.questions = QUESTION_BANK.filter(config.filterFn);
    } else {
      this.questions = QUESTION_BANK.slice(0, config.totalQuestions || 50);
    }

    this.currentIndex = 0;
    this.userResponses = {};
    this.examResults = null;

    // Initialize state for each question
    this.questions.forEach((q, idx) => {
      this.userResponses[q.id] = {
        index: idx,
        selectedOption: null,
        status: idx === 0 ? "not-answered" : "not-visited",
        isMarked: false
      };
    });

    this.totalSeconds = (config.durationMinutes || config.duration || 50) * 60;
    this.remainingSeconds = this.totalSeconds;
    this.isExamActive = true;

    this.startTimer();
  }

  shuffleArray(arr) {
    const copy = [...arr];
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }

  getAttemptedQuestionIds() {
    try {
      return JSON.parse(localStorage.getItem("appsc_amvi_attempted_qids") || "[]");
    } catch (e) {
      return [];
    }
  }

  recordAttemptedQuestions(qids) {
    try {
      const existing = this.getAttemptedQuestionIds();
      const updated = Array.from(new Set([...existing, ...qids]));
      localStorage.setItem("appsc_amvi_attempted_qids", JSON.stringify(updated));
    } catch (e) {
      console.warn("Could not save attempted question IDs:", e);
    }
  }

  // Record which questions the user got WRONG for priority re-testing
  recordWrongAnswers(wrongQids) {
    try {
      const existing = JSON.parse(localStorage.getItem("appsc_amvi_wrong_qids") || "{}");
      wrongQids.forEach(qid => {
        existing[qid] = (existing[qid] || 0) + 1; // count how many times wrong
      });
      localStorage.setItem("appsc_amvi_wrong_qids", JSON.stringify(existing));
    } catch (e) {
      console.warn("Could not save wrong answer tracking:", e);
    }
  }

  getWrongAnswerMap() {
    try {
      return JSON.parse(localStorage.getItem("appsc_amvi_wrong_qids") || "{}");
    } catch (e) {
      return {};
    }
  }

  /**
   * Smart Dynamic Paper Builder
   * Builds a paper-specific exam (150 questions by default) with intelligent
   * question selection that prioritizes:
   *   1. Questions the user previously answered WRONG (highest priority)
   *   2. Unattempted questions (fresh questions they haven't seen)
   *   3. Previously answered questions when needed to fill the paper
   * On every retry the mix shifts — missed answers are prioritized for review.
   */
  buildSmartDynamicPaper(config) {
    const wrongMap = this.getWrongAnswerMap();
    const attemptedSet = new Set(this.getAttemptedQuestionIds());

    // Separate the full bank by paper
    const p1All = QUESTION_BANK.filter(q => q.paper === 1);
    const p2All = QUESTION_BANK.filter(q => q.paper === 2);

    const p1Need = config.paper === 2
      ? 0
      : Math.min(config.paper === 1 ? config.totalQuestions || config.p1Count || 150 : config.p1Count || 150, p1All.length);
    const p2Need = config.paper === 1
      ? 0
      : Math.min(config.paper === 2 ? config.totalQuestions || config.p2Count || 150 : config.p2Count || 150, p2All.length);

    const pickSmart = (pool, needed) => {
      // Bucket 1: Previously wrong answers (sorted by times-wrong descending)
      const wrong = pool.filter(q => wrongMap[q.id])
                        .sort((a, b) => (wrongMap[b.id] || 0) - (wrongMap[a.id] || 0));

      // Bucket 2: Unattempted (never seen before)
      const fresh = pool.filter(q => !attemptedSet.has(q.id) && !wrongMap[q.id]);

      // Bucket 3: Previously correct (lowest priority, for padding)
      const correct = pool.filter(q => attemptedSet.has(q.id) && !wrongMap[q.id]);

      // Assemble in priority order
      const prioritized = [];

      // Take all wrong answers first (capped at 40% of paper to leave room)
      const maxWrong = Math.ceil(needed * 0.4);
      prioritized.push(...wrong.slice(0, maxWrong));

      // Fill with fresh unattempted questions (shuffled for variety)
      const freshShuffled = this.shuffleArray(fresh);
      const freshNeeded = needed - prioritized.length;
      prioritized.push(...freshShuffled.slice(0, freshNeeded));

      // If still short, pad with previously correct questions (reshuffled)
      if (prioritized.length < needed) {
        const correctShuffled = this.shuffleArray(correct);
        const remaining = needed - prioritized.length;
        prioritized.push(...correctShuffled.slice(0, remaining));
      }

      // If STILL short (tiny pool), take whatever is left
      if (prioritized.length < needed) {
        const usedIds = new Set(prioritized.map(q => q.id));
        const leftover = this.shuffleArray(pool.filter(q => !usedIds.has(q.id)));
        prioritized.push(...leftover.slice(0, needed - prioritized.length));
      }

      // Final shuffle within the selected set so wrong answers aren't all at the start
      return this.shuffleArray(prioritized.slice(0, needed));
    };

    const p1Selected = pickSmart(p1All, p1Need);
    const p2Selected = pickSmart(p2All, p2Need);

    // Paper-I first, then Paper-II (like the real exam order)
    return [...p1Selected, ...p2Selected];
  }

  startTimer() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    this.timerInterval = setInterval(() => {
      if (this.remainingSeconds > 0) {
        this.remainingSeconds--;
        this.onTimerTick(this.remainingSeconds);
      } else {
        clearInterval(this.timerInterval);
        this.submitExam(true); // auto-submit on timeout
      }
    }, 1000);
  }

  pauseTimer() {
    if (this.timerInterval) clearInterval(this.timerInterval);
  }

  resumeTimer() {
    if (this.isExamActive && this.remainingSeconds > 0) {
      this.startTimer();
    }
  }

  onTimerTick(secondsLeft) {
    const event = new CustomEvent("exam-timer-tick", {
      detail: {
        secondsLeft,
        formatted: this.formatTime(secondsLeft),
        isLowTime: secondsLeft < 180
      }
    });
    window.dispatchEvent(event);
  }

  formatTime(totalSec) {
    const minutes = Math.floor(totalSec / 60);
    const seconds = totalSec % 60;
    return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
  }

  getCurrentQuestion() {
    return this.questions[this.currentIndex];
  }

  getCurrentState() {
    const q = this.getCurrentQuestion();
    return q ? this.userResponses[q.id] : null;
  }

  selectOption(optionIndex) {
    const q = this.getCurrentQuestion();
    if (!q) return;
    const resp = this.userResponses[q.id];
    resp.selectedOption = optionIndex;
    resp.status = resp.isMarked ? "answered-and-marked" : "answered";
  }

  clearResponse() {
    const q = this.getCurrentQuestion();
    if (!q) return;
    const resp = this.userResponses[q.id];
    resp.selectedOption = null;
    resp.status = resp.isMarked ? "marked-for-review" : "not-answered";
  }

  markForReviewAndNext() {
    const q = this.getCurrentQuestion();
    if (!q) return;
    const resp = this.userResponses[q.id];
    resp.isMarked = true;
    if (resp.selectedOption !== null) {
      resp.status = "answered-and-marked";
    } else {
      resp.status = "marked-for-review";
    }
    this.goToNext();
  }

  saveAndNext() {
    const q = this.getCurrentQuestion();
    if (!q) return;
    const resp = this.userResponses[q.id];
    if (resp.selectedOption !== null) {
      resp.status = resp.isMarked ? "answered-and-marked" : "answered";
    } else {
      if (resp.status === "not-visited") resp.status = "not-answered";
    }
    this.goToNext();
  }

  goToQuestion(index) {
    if (index >= 0 && index < this.questions.length) {
      this.currentIndex = index;
      const q = this.getCurrentQuestion();
      const resp = this.userResponses[q.id];
      if (resp.status === "not-visited") {
        resp.status = "not-answered";
      }
    }
  }

  goToNext() {
    if (this.currentIndex < this.questions.length - 1) {
      this.goToQuestion(this.currentIndex + 1);
    }
  }

  goToPrevious() {
    if (this.currentIndex > 0) {
      this.goToQuestion(this.currentIndex - 1);
    }
  }

  getSummaryCounts() {
    let answered = 0;
    let notAnswered = 0;
    let marked = 0;
    let answeredAndMarked = 0;
    let notVisited = 0;

    this.questions.forEach(q => {
      const resp = this.userResponses[q.id];
      if (resp.status === "answered") answered++;
      else if (resp.status === "not-answered") notAnswered++;
      else if (resp.status === "marked-for-review") marked++;
      else if (resp.status === "answered-and-marked") answeredAndMarked++;
      else if (resp.status === "not-visited") notVisited++;
    });

    return {
      total: this.questions.length,
      answered,
      notAnswered,
      marked,
      answeredAndMarked,
      notVisited
    };
  }

  submitExam(autoSubmit = false) {
    if (this.timerInterval) clearInterval(this.timerInterval);
    this.isExamActive = false;

    const timeTakenSeconds = this.totalSeconds - this.remainingSeconds;
    let correctCount = 0;
    let incorrectCount = 0;
    let unattemptedCount = 0;
    const attemptedQids = [];

    const detailedEvaluation = this.questions.map((q, idx) => {
      const resp = this.userResponses[q.id];
      const selected = resp ? resp.selectedOption : null;
      const isAttempted = selected !== null;
      const isCorrect = isAttempted && selected === q.correctAnswer;
      const isIncorrect = isAttempted && selected !== q.correctAnswer;

      if (!isAttempted) {
        unattemptedCount++;
      } else {
        attemptedQids.push(q.id);
        if (isCorrect) {
          correctCount++;
        } else if (isIncorrect) {
          incorrectCount++;
        }
      }

      return {
        question: q,
        selectedOption: selected,
        isAttempted,
        isCorrect,
        isIncorrect,
        correctOption: q.correctAnswer,
        marksAwarded: isCorrect ? 1.0 : (isIncorrect ? -0.33 : 0.0)
      };
    });

    // Record attempted questions to ensure non-repetition in dynamic practice
    this.recordAttemptedQuestions(attemptedQids);

    // Record wrong answers for smart retry prioritization
    const wrongQids = detailedEvaluation
      .filter(e => e.isIncorrect)
      .map(e => e.question.id);
    if (wrongQids.length > 0) {
      this.recordWrongAnswers(wrongQids);
    }

    // Score Calculation with APPSC 1/3rd penalty
    const grossPositiveScore = correctCount * 1.0;
    const penaltyDeduction = incorrectCount * 0.33;
    const netMarks = Math.max(0, parseFloat((grossPositiveScore - penaltyDeduction).toFixed(2)));
    const maxMarks = this.questions.length * 1.0;
    const percentage = parseFloat(((netMarks / maxMarks) * 100).toFixed(1));
    const accuracy = (correctCount + incorrectCount) > 0
      ? parseFloat(((correctCount / (correctCount + incorrectCount)) * 100).toFixed(1))
      : 0;

    this.examResults = {
      examTitle: this.currentExamConfig.title,
      paper: this.currentExamConfig.paper,
      autoSubmitted: autoSubmit,
      totalQuestions: this.questions.length,
      attemptedCount: correctCount + incorrectCount,
      correctCount,
      incorrectCount,
      unattemptedCount,
      grossPositiveScore,
      penaltyDeduction: parseFloat(penaltyDeduction.toFixed(2)),
      netMarks,
      maxMarks,
      percentage,
      accuracy,
      timeTaken: this.formatTime(timeTakenSeconds),
      timeTakenSeconds,
      detailedEvaluation
    };

    // Save exam attempt to local storage
    this.saveResultToHistory(this.examResults);

    const event = new CustomEvent("exam-submitted", { detail: this.examResults });
    window.dispatchEvent(event);
  }

  saveResultToHistory(results) {
    try {
      const history = JSON.parse(localStorage.getItem("appsc_amvi_exam_history") || "[]");
      const record = {
        date: new Date().toISOString(),
        examTitle: results.examTitle,
        netMarks: results.netMarks,
        maxMarks: results.maxMarks,
        percentage: results.percentage,
        accuracy: results.accuracy,
        correctCount: results.correctCount,
        incorrectCount: results.incorrectCount,
        unattemptedCount: results.unattemptedCount,
        timeTaken: results.timeTaken
      };
      history.unshift(record);
      localStorage.setItem("appsc_amvi_exam_history", JSON.stringify(history.slice(0, 25)));
    } catch (e) {
      console.warn("Could not save to localStorage:", e);
    }
  }

  getHistory() {
    try {
      return JSON.parse(localStorage.getItem("appsc_amvi_exam_history") || "[]");
    } catch (e) {
      return [];
    }
  }
}

// Global instance
const examEngine = new AMVIExamEngine();
