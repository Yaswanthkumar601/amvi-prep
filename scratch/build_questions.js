/**
 * Node script to generate 500 authentic, non-repeating APPSC AMVI questions across 10 distinct Mock Tests (50 Qs each)
 * with complete English & Telugu explanations.
 */

const fs = require('fs');
const path = require('path');

// We will construct 10 tests x 50 questions = 500 questions total.
// Each question has: id, testId, paper, category, question, options, correctAnswer, explanationEn, explanationTe

const testsMeta = [
  {
    id: "test_01",
    title: "Mock Test 1: Paper-I Comprehensive General Studies (50 Qs)",
    badge: "Paper-I Standard",
    paper: 1,
    durationMinutes: 50,
    description: "50 non-repeating questions covering Indian Polity, AP History, Geography, Economy, Science, and Mental Ability."
  },
  {
    id: "test_02",
    title: "Mock Test 2: Paper-I Indian Polity, AP History & Reorganisation (50 Qs)",
    badge: "Paper-I Special",
    paper: 1,
    durationMinutes: 50,
    description: "50 non-repeating questions dedicated to Constitutional Articles, Writs, AP Freedom Struggle, and AP Reorganisation Act 2014."
  },
  {
    id: "test_03",
    title: "Mock Test 3: Paper-I Science, Environment, Economy & Mental Ability (50 Qs)",
    badge: "Paper-I Applied",
    paper: 1,
    durationMinutes: 50,
    description: "50 non-repeating questions covering EV Battery Tech, BMS, Disaster Management, AP Socio-Economic Survey, and Speed-Time Aptitude."
  },
  {
    id: "test_04",
    title: "Mock Test 4: Paper-II IC Engines, Combustion & BS-VI Emissions (50 Qs)",
    badge: "Paper-II Engines",
    paper: 2,
    durationMinutes: 50,
    description: "50 non-repeating questions on Otto/Diesel/Dual cycles, CRDI, MPFI, Turbochargers, and BS-VI SCR/DEF/DPF."
  },
  {
    id: "test_05",
    title: "Mock Test 5: Paper-II Chassis, Transmission & Drivetrain (50 Qs)",
    badge: "Paper-II Drivetrain",
    paper: 2,
    durationMinutes: 50,
    description: "50 non-repeating questions on Clutches, Synchromesh gearboxes, Torque converters, Propeller shafts, Differentials, and Drive axles."
  },
  {
    id: "test_06",
    title: "Mock Test 6: Paper-II Steering Geometry, Suspension & Brakes (50 Qs)",
    badge: "Paper-II Chassis",
    paper: 2,
    durationMinutes: 50,
    description: "50 non-repeating questions on Camber, Caster, KPI, Scrub Radius, Pneumatic Air Brakes, Tandem Master Cylinder, and ABS."
  },
  {
    id: "test_07",
    title: "Mock Test 7: Paper-II Motor Vehicles Act 1988, Amendments 2019 & CMVR (50 Qs)",
    badge: "Paper-II MVA Rules",
    paper: 2,
    durationMinutes: 50,
    description: "50 non-repeating questions on Fitness Form 38, Section 185 drunk driving, Section 194 overloading, HSRP, and CMVR rules."
  },
  {
    id: "test_08",
    title: "Mock Test 8: Paper-II SOM, Applied Mechanics & Workshop Metrology (50 Qs)",
    badge: "Paper-II Mechanics",
    paper: 2,
    durationMinutes: 50,
    description: "50 non-repeating questions on Hooke's Law, Bending, Torsion equations, Fluid mechanics, Bernoulli, and Precision Metrology."
  },
  {
    id: "test_09",
    title: "Mock Test 9: Grand Simulation Test A (Paper-I + Paper-II Combined - 50 Qs)",
    badge: "Grand Mock A",
    paper: "both",
    durationMinutes: 50,
    description: "50 non-repeating questions combining balanced Paper-I General Studies and Paper-II Core Automobile Engineering."
  },
  {
    id: "test_10",
    title: "Mock Test 10: Grand Simulation Test B (Final APPSC AMVI Strike Test - 50 Qs)",
    badge: "Grand Mock B",
    paper: "both",
    durationMinutes: 50,
    description: "50 non-repeating high-yield questions covering the entire APPSC AMVI examination syllabus."
  }
];

console.log("Generating 500 questions across 10 tests...");

