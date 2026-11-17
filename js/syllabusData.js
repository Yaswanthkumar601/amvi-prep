/**
 * APPSC Assistant Motor Vehicle Inspector (AMVI) - Comprehensive Data Store
 * A.P. Transport Subordinate Service
 */

const APPSC_AMVI_DATA = {
  overview: {
    title: "Assistant Motor Vehicle Inspector (AMVI)",
    service: "A.P. Transport Subordinate Service",
    recruitmentAgency: "Andhra Pradesh Public Service Commission (APPSC)",
    payScale: "₹48,440 – ₹1,37,220 (RPS 2022 / Revised Pay Scale)",
    jobRole: "Executive cadre officer responsible for inspecting motor vehicles for mechanical fitness and roadworthiness, checking vehicle registration, granting fitness certificates (Form 38), enforcing Motor Vehicle Act (MVA) 1988 & AP Motor Vehicle Rules, conducting driving tests, anti-pollution checks, checking overloading, and road safety enforcement across transport check-posts and RTO/MVI unit offices.",
    educationalQualifications: [
      {
        stream: "Degree Standard",
        requirement: "Must hold a Degree in Mechanical Engineering or Automobile Engineering of a recognized University in India or an equivalent qualification."
      },
      {
        stream: "Diploma Standard",
        requirement: "Must hold a Diploma in Automobile Engineering (3-year or 4-year duration) awarded by the State Board of Technical Education and Training, Andhra Pradesh, or equivalent qualification."
      }
    ],
    drivingLicenceCriteria: [
      "Must possess a valid Motor Driving License authorized to drive a Heavy Transport Vehicle (HTV) / Heavy Goods/Passenger Vehicle (HGV/HPV).",
      "Must possess at least 3 years of continuous driving experience with Heavy Transport Vehicles as prescribed in the official service rules.",
      "Concession for Women: Female candidates possessing a Light Motor Vehicle (LMV) driving license are eligible to apply, subject to the condition that they acquire a Heavy Transport Vehicle (HTV) endorsement within 2 years of joining service."
    ],
    physicalStandards: {
      men: {
        height: "Minimum 165 cms (Relaxable to 160 cms for SC/ST and specified agency/tribal candidates)",
        chest: "Minimum 86.3 cms on full expansion with a minimum expansion of 5.0 cms",
        vision: "Standard vision required (Distant Vision: 6/6, Near Vision: 0.5 without glasses; No colour blindness, squint or morbid condition of eyes or lids)"
      },
      women: {
        height: "Minimum 157.5 cms (Relaxable to 152.5 cms for reserved categories)",
        chest: "Not applicable, general sound health and medical fitness",
        vision: "Distant Vision: 6/6, Near Vision: 0.5 without glasses; standard colour perception test mandatory"
      }
    },
    ageLimit: "21 to 36 years (as per latest AP State Govt norms with general age relaxations: 5 years for SC/ST/BC/EWS, up to 10 years for Ex-Servicemen/NCC instructors)",
    examScheme: {
      mode: "Computer Based Recruitment Test (CBRT) - Online Objective Multiple Choice",
      totalMarks: 300,
      totalQuestions: 300,
      totalDuration: "300 Minutes (5 Hours: 2.5 Hours per Paper)",
      negativeMarking: "1/3rd (0.33 mark penalty for every wrong answer)",
      papers: [
        {
          code: "Paper-I",
          subject: "General Studies & Mental Ability",
          standard: "Degree Standard",
          questions: 150,
          marks: 150,
          duration: "150 Minutes"
        },
        {
          code: "Paper-II",
          subject: "Automobile Engineering / Mechanical Engineering",
          standard: "Diploma Standard",
          questions: 150,
          marks: 150,
          duration: "150 Minutes"
        }
      ],
      qualifyingTest: "Computer Proficiency Test (CPT) - Practical test conducted for shortlisted candidates to verify basic office automation/computer skills (Qualifying nature)."
    }
  },

  syllabus: {
    paper1: {
      paperCode: "Paper-I",
      name: "General Studies and Mental Ability",
      standard: "Degree Standard",
      duration: "150 Minutes",
      marks: 150,
      questions: 150,
      units: [
        {
          id: "p1-u1",
          title: "Events of National and International Importance",
          weightage: "12-15 Marks",
          topics: [
            "Major global diplomatic summits (G20, COP Climate Summits, BRICS, SCO)",
            "National developments, bilateral treaties, key summits hosted in India",
            "Major awards, Nobel Prizes, Bharat Ratna, Gallantry and sports events",
            "Space exploration missions (ISRO Chandrayaan, Aditya-L1, Gaganyaan, Artemis accords)"
          ]
        },
        {
          id: "p1-u2",
          title: "Current Affairs - International, National and Regional (Andhra Pradesh)",
          weightage: "15-18 Marks",
          topics: [
            "State-specific socio-economic initiatives, infrastructure developments in AP",
            "Cabinet decisions, welfare schemes, transport policy reforms in Andhra Pradesh",
            "Major national bills, enactments, government flagships and statutory appointments",
            "Recent transport technology policies (Green Hydrogen, EV Policy of AP, PM E-Bus Sewa)"
          ]
        },
        {
          id: "p1-u3",
          title: "General Science & Its Applications in Day-to-Day Life and IT",
          weightage: "15-18 Marks",
          topics: [
            "Fundamental physics: Laws of motion, friction, work-energy, fluid pressure in braking",
            "Applied chemistry: Battery chemistry (Lead-acid, Li-ion), fuels, combustion chemistry, emissions",
            "Information Technology, AI/ML basics, Cyber Security, GPS, RFID FASTag, Telematics",
            "Renewable energy systems, solar, hydrogen fuel cells, biofuels (Ethanol blending)"
          ]
        },
        {
          id: "p1-u4",
          title: "Social, Economic and Political History of Modern India (with emphasis on AP)",
          weightage: "15-18 Marks",
          topics: [
            "Advent of Europeans, 1857 Revolt, Indian National Movement and moderate/extremist phases",
            "Role of Andhra in Freedom Struggle: Vandemataram Movement, Chirala-Perala, Rampa Rebellion (Alluri Sitarama Raju)",
            "Andhra Mahasabha, Visalandhra Movement, Martyrdom of Potti Sreeramulu",
            "Linguistic reorganization and formation of Andhra State (1953) and Andhra Pradesh (1956)"
          ]
        },
        {
          id: "p1-u5",
          title: "Indian Polity and Governance: Constitutional Issues, Public Policy & Reforms",
          weightage: "16-20 Marks",
          topics: [
            "Preamble, Fundamental Rights (Art 14-32), Directive Principles (DPSP), Fundamental Duties",
            "Structure of Union & State Executive, Parliament, Judiciary, Governor's powers",
            "73rd and 74th Constitutional Amendments (Panchayati Raj & Urban Local Bodies)",
            "Constitutional & Statutory bodies (UPSC, APPSC, Election Commission, CAG, CVC)",
            "Right to Information (RTI Act 2005), Citizen Charters, e-Governance services (Meeseva, Vahan, Sarathi)"
          ]
        },
        {
          id: "p1-u6",
          title: "Economic Development in India Since Independence & Andhra Pradesh Economy",
          weightage: "15-18 Marks",
          topics: [
            "Planning commission to NITI Aayog, Five-Year Plans trajectory, LPG Reforms (1991)",
            "Monetary policy (RBI, Repo rates, inflation control) and Fiscal policy (GST framework, Union Budget)",
            "Andhra Pradesh Economy: Agriculture, Industrial corridors (Vizag-Chennai, Bangalore-Hyderabad)",
            "Ports, maritime trade, logistics infrastructure in Andhra Pradesh, AP Socio-Economic Survey highlights"
          ]
        },
        {
          id: "p1-u7",
          title: "Physical, Social and Economic Geography of India and Andhra Pradesh",
          weightage: "14-16 Marks",
          topics: [
            "Physiography of India: Himalayas, Northern Plains, Peninsular Plateau, Coastal Plains",
            "Drainage systems: Godavari, Krishna, Penna river systems and irrigation canals in AP",
            "Climate, monsoons, agro-climatic zones, soils, forests and mineral wealth in Andhra Pradesh",
            "Demographics: Census data, population density, sex ratio, urbanization trends in AP"
          ]
        },
        {
          id: "p1-u8",
          title: "Disaster Management, Environmental Protection & Sustainable Development",
          weightage: "12-15 Marks",
          topics: [
            "Disasters: Cyclones (Bay of Bengal vulnerability in AP coastline), floods, droughts, heat waves",
            "NDMA framework, Early Warning Systems, disaster response protocols in coastal districts",
            "Ecology: Biodiversity hotspots, Protected Areas, wildlife sanctuaries in AP",
            "Sustainable Development Goals (SDGs), carbon footprint reduction, zero-emission mobility"
          ]
        },
        {
          id: "p1-u9",
          title: "Logical Reasoning, Analytical Ability and Data Interpretation",
          weightage: "18-20 Marks",
          topics: [
            "Verbal reasoning: Analogies, classification, series completion, coding-decoding, blood relations",
            "Analytical reasoning: Direction sense, seating arrangements, syllogisms, Venn diagrams",
            "Data interpretation: Bar charts, pie charts, line graphs, tabular data analysis",
            "Basic arithmetic: Speed-Time-Distance (trains, vehicles, average speeds), ratios, percentages"
          ]
        },
        {
          id: "p1-u10",
          title: "Bifurcation of Andhra Pradesh and Its Administrative & Economic Implications",
          weightage: "12-15 Marks",
          topics: [
            "AP Reorganisation Act, 2014: Provisions, sections, timelines, and implementation status",
            "Division of assets, liabilities, corporations, Schedule IX and X institutions",
            "Polavaram Irrigation Project (National Project status under Section 90)",
            "River water disputes: Krishna & Godavari River Management Boards (KRMB & GRMB)",
            "Special Category Status issue, industrial incentives under Section 94, Capital city development"
          ]
        }
      ]
    },

    paper2: {
      paperCode: "Paper-II",
      name: "Automobile Engineering / Mechanical Engineering",
      standard: "Diploma Standard",
      duration: "150 Minutes",
      marks: 150,
      questions: 150,
      units: [
        {
          id: "p2-u1",
          title: "Automotive Engines & Thermodynamics",
          weightage: "30-35 Marks",
          topics: [
            "Operating principles: 2-stroke vs 4-stroke Spark Ignition (SI) and Compression Ignition (CI) engines",
            "Thermodynamic air standard cycles: Otto, Diesel, and Dual cycles; thermal efficiencies and p-V / T-s diagrams",
            "Engine components: Cylinder block, cylinder head, liners, pistons, rings, connecting rod, crankshaft, camshaft, valves",
            "Fuel systems: Carburetors, Multi-Point Fuel Injection (MPFI), Gasoline Direct Injection (GDI)",
            "Diesel fuel injection: Fuel pump (inline & rotary), CRDI (Common Rail Direct Injection), electronic unit injectors, nozzles, cetane number",
            "Engine subsystems: Cooling systems (water cooling, thermostat, radiator), Lubrication systems (splash, pressure, dry sump, SAE viscosity)",
            "Supercharging & Turbocharging: Wastegate turbocharger, Variable Geometry Turbocharger (VGT), intercoolers",
            "Combustion & Emissions: Detonation, knocking, octane/cetane ratings, BS-VI emission standards, Catalytic Converter, SCR, DPF, EGR, DEF"
          ]
        },
        {
          id: "p2-u2",
          title: "Automotive Chassis, Transmission and Drivetrain Systems",
          weightage: "28-32 Marks",
          topics: [
            "Vehicle layouts: Front-engine rear-wheel drive (FR), Front-engine front-wheel drive (FF), All-wheel drive (4WD/AWD)",
            "Clutches: Single plate, multi-plate, centrifugal, diaphragm spring clutch, clutch linkages and hydraulic actuation",
            "Manual Transmissions: Sliding mesh, constant mesh, synchromesh gearbox, overdrive units",
            "Automatic Transmissions: Epicyclic/planetary gear trains, torque converters, Automatic Transmission (AT), AMT, Continuously Variable Transmission (CVT), Dual-Clutch (DCT)",
            "Propeller shaft: Universal joints (Hooke's joint), slip joint, critical whirling speed",
            "Final drive & Differential: Bevel, hypoid final drives, differential working, differential locks, limited-slip differentials (LSD)",
            "Rear axles: Semi-floating, full-floating, three-quarter floating axles"
          ]
        },
        {
          id: "p2-u3",
          title: "Steering, Suspension, Brakes, and Wheels & Tyres",
          weightage: "28-32 Marks",
          topics: [
            "Steering geometry: Camber, Caster, Kingpin Inclination (KPI/SAI), Included Angle, Scrub Radius, Toe-in, Toe-out",
            "Steering mechanisms: Ackermann and Davis steering principles, steering gear types (Rack and Pinion, Recirculating Ball, Worm & Roller)",
            "Power steering: Hydraulic power steering (HPS), Electric power steering (EPS) architecture",
            "Braking systems: Hydraulic brakes, tandem master cylinder, brake calipers, wheel cylinders",
            "Pneumatic / Air brakes: Compressor, unloader valve, air tanks, foot brake valve, diaphragm brake chambers",
            "Anti-lock Braking System (ABS): Wheel speed sensors, Electronic Control Unit (ECU), hydraulic modulator, EBD, ESP",
            "Suspension systems: Rigid axle vs Independent suspension, leaf springs, coil springs, torsion bar, MacPherson strut, double wishbone, dampers/shock absorbers",
            "Wheels & Tyres: Radial vs Cross-ply/bias ply tyres, tyre markings (e.g. 205/55 R16 91V), tyre rotation, tread wear indicators"
          ]
        },
        {
          id: "p2-u4",
          title: "Automotive Electrical and Electronics Systems",
          weightage: "20-25 Marks",
          topics: [
            "Storage Battery: Lead-acid battery chemistry, specific gravity of electrolyte (hydrometer testing), state of charge, capacity rating (Ah)",
            "Charging system: Alternator construction, rotor, stator, silicon diode rectification, solid-state voltage regulator",
            "Starting system: DC starter motor, starter solenoid, Bendix drive, overrunning clutch drive",
            "Ignition systems: Battery ignition system, electronic/transistorized ignition, distributorless ignition (DIS), spark plugs",
            "Automotive Sensors & Actuators: Throttle Position Sensor (TPS), Mass Air Flow (MAF), Manifold Absolute Pressure (MAP), Oxygen sensor (Lambda), Crankshaft position sensor",
            "Electronic Control Units (ECU): CAN (Controller Area Network) bus communication, On-Board Diagnostics (OBD-II port), fault codes (DTC)"
          ]
        },
        {
          id: "p2-u5",
          title: "Motor Vehicles Act (MVA) 1988, Amendments 2019 & Transport Management",
          weightage: "20-25 Marks",
          topics: [
            "Motor Vehicles Act 1988 & MVA Amendment Act 2019: Structure, key definitions, sections, and penalties",
            "Licensing of Drivers (Chapter II): Eligibility ages, learner's license, permanent license, commercial endorsement",
            "Registration of Motor Vehicles (Chapter IV): Temporary & permanent registration, transfer of ownership, HSRP (High Security Registration Plates)",
            "Fitness of Transport Vehicles: Section 56, inspection procedure, Form 38 (Certificate of Fitness), validity periods for new and old vehicles",
            "Control of Transport Vehicles (Chapter V): Stage carriage, contract carriage, goods carriage permits, national permits",
            "Pollution & Safety Regulations: CMVR Rule 115, PUC norms, Speed Governors, AIS safety standards, seatbelts, child restraints, helmet rules",
            "Penalties & Offences: Section 185 (Drunken driving limits: 30mg/100ml blood), Section 194 (Overloading), Section 194D (Helmet), Section 184 (Dangerous driving)",
            "Central Motor Vehicles Rules 1989 & Andhra Pradesh Motor Vehicles Rules 1989: Specific RTO protocols, tax structures"
          ]
        },
        {
          id: "p2-u6",
          title: "Applied Mechanical Sciences, Strength of Materials & Workshop Tech",
          weightage: "18-22 Marks",
          topics: [
            "Engineering Mechanics: Force systems, equilibrium, Lami's theorem, moments, friction, center of gravity",
            "Strength of Materials: Stress, strain, Young's modulus, shear modulus, Poisson's ratio, stress-strain curve for ductile materials",
            "Shear Force & Bending Moment (SFD & BMD) for simply supported and cantilever beams; simple bending equation M/I = σ/y = E/R",
            "Torsion of shafts: Torsional formula T/J = τ/r = Gθ/L, polar moment of inertia, power transmitted by shafts",
            "Fluid Mechanics: Fluid properties, viscosity, Pascal's law, continuity equation, Bernoulli's theorem and its application to venturi/carburetor",
            "Manufacturing & Metrology: Welding types (MIG, TIG, Spot welding), casting defects, heat treatments (quenching, tempering, case hardening), precision measuring instruments (vernier calipers, micrometer, dial gauge)"
          ]
        }
      ]
    }
  },

  previousPapers: [
    {
      year: "2023",
      title: "APPSC AMVI Exam 2023 (Official CBRT)",
      examDate: "August 2023",
      paper1MarksAvg: "92 / 150",
      paper2MarksAvg: "98 / 150",
      analysis: "Paper-1 was moderate with heavy emphasis on AP Reorganisation Act, Welfare Schemes, and Data Interpretation. Paper-2 featured in-depth questions on BS-VI emission technology (SCR, DEF, DPF), MVA 2019 penalty sections, and steering geometry calculations.",
      keyTopics: ["BS-VI Norms & SCR", "MVA 1988 Amended Penalties", "Steering Geometry", "AP Reorganisation Act", "CRDI Fuel Injection"]
    },
    {
      year: "2019",
      title: "APPSC AMVI Exam 2019 (Official CBRT)",
      examDate: "April 2019",
      paper1MarksAvg: "88 / 150",
      paper2MarksAvg: "94 / 150",
      analysis: "Paper-1 featured extensive modern AP history (Andhra movement, Potti Sreeramulu) and Indian Constitution. Paper-2 focused strongly on mechanical foundations: Otto vs Diesel cycle efficiencies, gear ratios in epicyclic gearboxes, and air brake schematics.",
      keyTopics: ["Thermodynamic Cycles", "Air Brakes & Dual Circuit", "Differential Operation", "Indian Constitution (Articles 14-32)", "Panchayati Raj"]
    },
    {
      year: "2012",
      title: "APPSC AMVI Exam 2012 (Offline OMR Archive)",
      examDate: "May 2012",
      paper1MarksAvg: "84 / 150",
      paper2MarksAvg: "90 / 150",
      analysis: "Legacy paper focusing on traditional automotive mechanics: carburettor circuits, sliding mesh gearbox, suspension leaf spring design calculations, and MVA 1988 foundational sections.",
      keyTopics: ["Carburettor Circuits", "Torsion & Bending", "Leaf Springs", "Lead-Acid Battery Maintenance", "MVA 1988 Chapter IV"]
    }
  ],

  formulaSheet: [
    {
      category: "IC Engines & Thermodynamics",
      title: "Air Standard Efficiency of Otto Cycle",
      formula: "η_otto = 1 - (1 / r^(γ - 1))",
      description: "Where r = Compression Ratio (V1/V2), γ = Ratio of specific heats (Cp/Cv = 1.4 for air). As compression ratio increases, thermal efficiency increases."
    },
    {
      category: "IC Engines & Thermodynamics",
      title: "Air Standard Efficiency of Diesel Cycle",
      formula: "η_diesel = 1 - (1 / (r^(γ - 1))) * [(rc^γ - 1) / (γ * (rc - 1))]",
      description: "Where r = Compression ratio, rc = Cut-off ratio (V3/V2). For the same compression ratio, η_otto > η_diesel."
    },
    {
      category: "IC Engines & Performance",
      title: "Brake Power (BP)",
      formula: "BP = (2 * π * N * T) / 60,000 [kW]",
      description: "Where N = Engine speed in RPM, T = Engine torque in N·m. Mechanical efficiency η_mech = BP / IP. Check units: this form gives kW when torque is in N·m and speed is in RPM."
    },
    {
      category: "IC Engines & Performance",
      title: "Engine Displacement (Swept Volume)",
      formula: "V_s = (π / 4) * D² * L; Total displacement = n * V_s",
      description: "D = cylinder bore, L = stroke, and n = number of cylinders. Use consistent length units; displacement is often converted from cm³ to litres by dividing by 1,000."
    },
    {
      category: "IC Engines & Performance",
      title: "Compression Ratio",
      formula: "r = (V_s + V_c) / V_c",
      description: "V_s = swept volume and V_c = clearance volume. Do not confuse compression ratio with pressure ratio. In an ideal Otto cycle, increasing r increases air-standard efficiency."
    },
    {
      category: "IC Engines & Performance",
      title: "Engine Efficiencies",
      formula: "η_mech = BP / IP;  η_brake,thermal = BP / (ṁ_f * CV)",
      description: "BP = brake power, IP = indicated power, ṁ_f = fuel mass-flow rate, and CV = fuel calorific value. Keep power and fuel-energy rate in matching units; efficiency is a ratio, not a percentage until multiplied by 100."
    },
    {
      category: "IC Engines & Performance",
      title: "Brake-Specific Fuel Consumption",
      formula: "BSFC = ṁ_f / BP",
      description: "Fuel consumed per unit brake power output; common units are kg/kWh. A lower BSFC indicates better fuel economy at the compared operating point."
    },
    {
      category: "IC Engines & Performance",
      title: "Power, Torque & Rotational Speed",
      formula: "P [kW] = 2πNT / 60,000;  T [N·m] = 9,550 * P [kW] / N [RPM]",
      description: "Use engine speed in RPM and torque in N·m. At constant power, torque decreases as RPM increases; remember that the factor 60,000 converts watts to kilowatts and minutes to seconds."
    },
    {
      category: "Strength of Materials",
      title: "Simple Bending Equation",
      formula: "(M / I) = (σ / y) = (E / R)",
      description: "M = Bending moment, I = Moment of inertia of section, σ = Bending stress at distance y from neutral axis, E = Young's modulus, R = Radius of curvature."
    },
    {
      category: "Strength of Materials",
      title: "Torsion Equation for Circular Shafts",
      formula: "(T / J) = (τ / r) = (G * θ / L)",
      description: "T = Twisting torque, J = Polar moment of inertia (π·d^4 / 32 for solid circular shaft), τ = Maximum shear stress at radius r, G = Shear modulus, θ = Angle of twist, L = Length of shaft."
    },
    {
      category: "Strength of Materials",
      title: "Axial Stress, Strain & Hooke's Law",
      formula: "σ = P / A;  ε = ΔL / L;  σ = Eε",
      description: "P = axial load, A = cross-sectional area, ΔL = extension, L = original length, and E = Young's modulus. Use the final relation only within the proportional/elastic limit."
    },
    {
      category: "Strength of Materials",
      title: "Solid Circular Shaft: Polar Moment & Torque Capacity",
      formula: "J = πd⁴ / 32;  τ_max = 16T / (πd³)",
      description: "For a solid circular shaft of diameter d under torque T. For a hollow shaft, J = π(D⁴ − d⁴) / 32; do not use the solid-shaft formula for a hollow section."
    },
    {
      category: "Thermodynamics & Fluids",
      title: "Heat, Work & Efficiency",
      formula: "η = Work output / Heat supplied",
      description: "For a heat engine, net work equals heat supplied minus heat rejected. Efficiency is always less than 1 (or 100%); check whether the question asks for thermal, mechanical, or overall efficiency."
    },
    {
      category: "Steering Geometry",
      title: "Included Angle",
      formula: "Included Angle = Camber Angle + Kingpin Inclination (KPI)",
      description: "The combined angle between the kingpin center line and the vertical wheel plane. For alignment diagnosis, a changed included angle can point to bent steering or suspension parts; caster is not part of this sum."
    },
    {
      category: "Vehicle Dynamics",
      title: "Gear Ratio & Ideal Torque Multiplication",
      formula: "Gear ratio = Input speed / Output speed",
      description: "For an ideal gear train, output torque is approximately input torque multiplied by the reduction ratio (before losses). A larger reduction ratio lowers output speed and raises output torque."
    },
    {
      category: "Quick Calculation Tip",
      title: "Speed Conversion",
      formula: "km/h → m/s: multiply by 5/18;  m/s → km/h: multiply by 18/5",
      description: "Useful for braking-distance, relative-speed, and vehicle-motion problems. Convert speed before combining it with distances in metres and times in seconds."
    },
    {
      category: "Paper-I Quantitative Aptitude",
      title: "Speed, Distance & Time",
      formula: "Speed = Distance / Time;  Distance = Speed × Time;  Time = Distance / Speed",
      description: "Use consistent units. For km/h with distance in km, time is in hours; for m/s with distance in metres, time is in seconds."
    },
    {
      category: "Paper-I Quantitative Aptitude",
      title: "Average Speed",
      formula: "Equal distances: 2uv / (u + v);  Equal time intervals: (u + v) / 2",
      description: "For unequal distances or time intervals, calculate total distance divided by total time. Do not take a simple mean unless the travel times are equal."
    },
    {
      category: "Paper-I Quantitative Aptitude",
      title: "Relative Speed & Train Problems",
      formula: "Opposite directions: u + v;  Same direction: |u − v|;  Crossing time = Total distance / Relative speed",
      description: "For crossing a pole, total distance is the train length. For crossing a platform, add platform length; for two trains, add their lengths. Convert speeds to the same units first."
    },
    {
      category: "Paper-I Quantitative Aptitude",
      title: "Ratios, Percentages & Percentage Change",
      formula: "Percentage = (Part / Whole) × 100;  % change = (New − Old) / Old × 100",
      description: "A ratio a:b has total parts a+b. Successive percentage changes are multiplicative: multiply the factors (1 ± rate/100), rather than adding the rates."
    },
    {
      category: "Paper-I Quantitative Aptitude",
      title: "Work Rate & Time",
      formula: "Combined rate = 1/t₁ + 1/t₂;  Time together = 1 / Combined rate",
      description: "Rates are fractions of the job completed per unit time. For a fixed amount of work, rate and time are inversely proportional."
    },
    {
      category: "Paper-I Quantitative Aptitude",
      title: "Pie-Chart Conversion",
      formula: "Sector angle = (Value / Total) × 360°;  1% = 3.6°",
      description: "To recover a value from a sector, use Value = (Sector angle / 360°) × Total."
    },
    {
      category: "Mechanics & General Science",
      title: "Newton's Second Law, Work & Power",
      formula: "F = ma;  Work = F s cosθ;  Power = Work / Time",
      description: "F is net force in newtons, m is mass in kg, a is acceleration in m/s², and s is displacement in metres. For constant speed, net force and net work are zero."
    },
    {
      category: "Mechanics & General Science",
      title: "Equations of Uniformly Accelerated Motion",
      formula: "v = u + at;  s = ut + ½at²;  v² = u² + 2as",
      description: "Use only for constant acceleration in a straight line. u and v are initial and final speeds, a acceleration, t time, and s displacement."
    },
    {
      category: "Mechanics & General Science",
      title: "Friction & Limiting Friction",
      formula: "F_f ≤ μN;  F_limiting = μN",
      description: "μ is the coefficient of friction and N is the normal reaction. Kinetic friction is commonly modelled as μ_kN; friction opposes relative motion or its tendency."
    },
    {
      category: "Mechanics & General Science",
      title: "Kinetic Energy & Momentum",
      formula: "K.E. = ½mv²;  Momentum = mv;  Impulse = FΔt = Δ(mv)",
      description: "For a moving vehicle, kinetic energy varies with the square of speed: doubling speed gives four times the kinetic energy."
    },
    {
      category: "Thermodynamics & Fluids",
      title: "Sensible Heat & Latent Heat",
      formula: "Q = mcΔT;  Phase change: Q = mL",
      description: "m is mass, c specific heat capacity, ΔT temperature change, and L specific latent heat. Use the appropriate relation for temperature change or phase change."
    },
    {
      category: "Thermodynamics & Fluids",
      title: "Hydrostatic Pressure & Hydraulic Power",
      formula: "Gauge pressure: p = ρgh;  Hydraulic power: P = pQ",
      description: "h is fluid depth, ρ density, g gravitational acceleration, and Q volumetric flow rate. The power equation gives watts when p is in pascals and Q in m³/s; ideal output ignores losses."
    },
    {
      category: "Thermodynamics & Fluids",
      title: "Pressure, Density & Hydraulic Force",
      formula: "p = F / A;  ρ = m / V;  F₁ / A₁ = F₂ / A₂",
      description: "Pressure p is in pascals when force is in newtons and area in m². The hydraulic-force relation follows Pascal's law for an ideal system; actual output is lower due to losses."
    },
    {
      category: "Thermodynamics & Fluids",
      title: "Continuity Equation",
      formula: "A₁v₁ = A₂v₂  (incompressible flow)",
      description: "For steady incompressible flow, flow rate is constant. A smaller flow area means higher fluid velocity."
    },
    {
      category: "Thermodynamics & Fluids",
      title: "Bernoulli Equation",
      formula: "p/(ρg) + v²/(2g) + z = constant",
      description: "Applies along a streamline to steady, incompressible, non-viscous flow with no pump or turbine work between points. Terms represent pressure, velocity, and elevation head."
    },
    {
      category: "Thermodynamics & Fluids",
      title: "Ideal-Gas Equation & First Law",
      formula: "pV = mRT;  Q − W = ΔU  (work done by the system)",
      description: "Use absolute pressure and absolute temperature in the ideal-gas equation. In the first-law form shown, Q is heat supplied and W is work done by the system."
    },
    {
      category: "Thermodynamics & Fluids",
      title: "Specific-Heat Relations & Carnot Efficiency",
      formula: "γ = Cₚ / Cᵥ;  Cₚ − Cᵥ = R;  η_Carnot = 1 − T_cold / T_hot",
      description: "The specific-heat relation shown is for an ideal gas on a mass basis. Carnot temperatures must be absolute (kelvin); no heat engine operating between the same reservoirs can exceed this ideal efficiency."
    },
    {
      category: "IC Engines & Thermodynamics",
      title: "Dual (Sabathe) Cycle Efficiency",
      formula: "η_dual = 1 − (α·ρ^γ − 1) / {r^(γ−1)[(α − 1) + γα(ρ − 1)]}",
      description: "Here r is compression ratio, γ = Cₚ/Cᵥ, α = p₃/p₂ is the pressure ratio during constant-volume heat addition, and ρ = V₄/V₃ is the cut-off ratio during constant-pressure heat addition."
    },
    {
      category: "IC Engines & Performance",
      title: "Mean Piston Speed",
      formula: "Cₘ = 2LN / 60",
      description: "L is the stroke in metres and N is engine speed in RPM. The piston travels one stroke in each direction per revolution, giving mean speed Cₘ in m/s."
    },
    {
      category: "IC Engines & Performance",
      title: "Volumetric Efficiency & Air-Fuel Ratio",
      formula: "ηᵥ = Actual air inducted / Theoretical swept-volume air;  A/F = m_air / m_fuel",
      description: "Compare air quantities at the same reference pressure and temperature when calculating volumetric efficiency. Air-fuel ratio is a mass ratio; petrol's stoichiometric value is approximately 14.7:1."
    },
    {
      category: "IC Engines & Performance",
      title: "Indicated Power for Reciprocating Engines",
      formula: "4-stroke: IP = pₘLANk / 120;  2-stroke: IP = pₘLANk / 60",
      description: "Use mean effective pressure pₘ in kPa, piston area A in m², stroke L in m, speed N in RPM, and k cylinders; result is kW. A four-stroke cylinder has one power stroke every two crankshaft revolutions."
    },
    {
      category: "IC Engines & Performance",
      title: "Mean Effective Pressure & Friction Power",
      formula: "pₘ = Work per cycle / Swept volume;  FP = IP − BP",
      description: "Mean effective pressure is a hypothetical constant pressure that would produce the same cycle work over the swept volume. Friction power is the difference between indicated and brake power."
    },
    {
      category: "Vehicle Dynamics",
      title: "Gear Trains & Speed Ratio",
      formula: "Simple gear pair: N₁/N₂ = T₂/T₁;  Overall ratio = product of stage ratios",
      description: "N is rotational speed and T is number of teeth. An ideal speed-reduction gear train increases output torque by the same ratio; account for losses in a real transmission."
    },
    {
      category: "Vehicle Dynamics",
      title: "Planetary Gear Train (Willis Relation)",
      formula: "(Z_s + Z_r)ω_c = Z_sω_s + Z_rω_r",
      description: "For a simple planetary set, Z_s and Z_r are sun and ring tooth counts; ω_s, ω_r, and ω_c are their speeds and carrier speed. The speed form is the reliable relation; set the held member's speed to zero for a specific gear ratio."
    },
    {
      category: "Vehicle Dynamics",
      title: "Open Differential Speed Relation",
      formula: "N_left + N_right = 2N_carrier",
      description: "For a symmetric open bevel differential, the carrier speed is the average of the two axle-shaft speeds. This is a speed relation, not a statement that torque is split unequally."
    },
    {
      category: "Vehicle Dynamics",
      title: "Vehicle Speed from Wheel RPM",
      formula: "Vehicle speed [km/h] = 0.06 × wheel RPM × tyre circumference [m]",
      description: "Assumes no tyre slip. Wheel RPM equals engine RPM divided by the product of gearbox and final-drive ratios; use the rolling circumference for best accuracy."
    },
    {
      category: "Vehicle Dynamics",
      title: "Road-Load Forces",
      formula: "Rolling: Fᵣ ≈ Cᵣmg;  Grade: Fg = mg sinθ;  Aero: Fd = ½ρCᴅAv²",
      description: "Cᵣ is rolling-resistance coefficient, θ is road angle, and ρ, Cᴅ, A, v are air density, drag coefficient, frontal area, and vehicle speed. These are idealized estimates; aerodynamic force grows with speed squared."
    },
    {
      category: "Vehicle Dynamics",
      title: "Braking & Stopping Distance (Ideal Level Road)",
      formula: "Braking distance = v² / (2μg);  Total stopping distance = v tᵣ + v² / (2μg)",
      description: "Assumes constant maximum deceleration μg on a level road. v must be in m/s; tᵣ is driver reaction time. Actual stopping distance changes with tyres, brakes, road, slope, and conditions."
    },
    {
      category: "Vehicle Dynamics",
      title: "Brake Torque & Hydraulic Brake Force",
      formula: "Brake torque = Tangential pad/shoe force × Effective radius;  F₂/F₁ = A₂/A₁",
      description: "The hydraulic-force ratio follows Pascal's law for an ideal circuit; piston areas determine force multiplication. Actual brake torque also depends on friction, geometry, and losses."
    },
    {
      category: "Vehicle Dynamics",
      title: "Single-Plate Clutch Torque Capacity",
      formula: "T = n μ W Rₘ;  Uniform wear: Rₘ = (rₒ + rᵢ) / 2",
      description: "n is the number of friction surfaces, μ coefficient of friction, W axial spring force, and rₒ/rᵢ the outer/inner friction radii. A single-plate clutch commonly has two friction surfaces; use the stated convention in the question."
    },
    {
      category: "Steering Geometry",
      title: "Ackermann Steering Geometry",
      formula: "cot(δ_outer) − cot(δ_inner) = Track / Wheelbase",
      description: "δ_inner and δ_outer are the inside and outside front-wheel steering angles. The inside wheel turns through the larger angle so the wheels roll about a common instantaneous centre."
    },
    {
      category: "Wheels & Tyres",
      title: "Tyre Size: Sidewall Height",
      formula: "Sidewall height = Section width × Aspect ratio / 100",
      description: "For a tyre marked 205/55 R16, the nominal sidewall height is 205 × 55/100 = 112.75 mm. R indicates radial construction; 16 is the rim diameter in inches."
    },
    {
      category: "Wheels & Tyres",
      title: "Tyre Overall Diameter & Circumference",
      formula: "Overall diameter ≈ Rim diameter + 2 × Sidewall height;  Circumference ≈ π × Diameter",
      description: "Convert rim diameter to the same units as sidewall height before adding. This is a nominal geometric estimate; loaded rolling radius and actual rolling circumference differ."
    },
    {
      category: "Automotive Electrical",
      title: "Ohm's Law & Electrical Power",
      formula: "V = IR;  P = VI = I²R = V²/R",
      description: "V is voltage in volts, I current in amperes, R resistance in ohms, and P power in watts. Use the power form matching the values given."
    },
    {
      category: "Automotive Electrical",
      title: "Series & Parallel Resistance",
      formula: "Series: R_total = ΣR;  Parallel: 1/R_total = Σ(1/R)",
      description: "In series, current is common and voltage divides. In parallel, voltage is common and current divides; equivalent resistance is less than the smallest parallel branch."
    },
    {
      category: "Automotive Electrical",
      title: "Electrical Energy & Battery Capacity",
      formula: "Energy [Wh] ≈ Voltage [V] × Capacity [Ah];  Q [Ah] = I [A] × Time [h]",
      description: "Ideal estimate only: actual usable battery energy depends on discharge rate, temperature, age, and system losses. Battery capacity in Ah is charge capacity, not power."
    },
    {
      category: "Strength of Materials",
      title: "Section Modulus & Rectangle Properties",
      formula: "Bending stress: σ_max = M/Z;  Rectangle: I = bd³/12;  Z = bd²/6",
      description: "b is breadth and d is depth in the bending direction. The rectangle's second moment of area changes with the cube of its depth, so orientation strongly affects bending strength."
    },
    {
      category: "Strength of Materials",
      title: "Axial Deformation of a Prismatic Bar",
      formula: "ΔL = PL / (AE)",
      description: "For a straight, uniform bar under axial load within the elastic range; P is load, L length, A area, and E Young's modulus. Use consistent units."
    },
    {
      category: "Strength of Materials",
      title: "Poisson's Ratio & Elastic Moduli",
      formula: "ν = − lateral strain / longitudinal strain;  E = 2G(1 + ν) = 3K(1 − 2ν)",
      description: "Relations apply to homogeneous, isotropic, linearly elastic materials. E is Young's modulus, G shear modulus, and K bulk modulus."
    },
    {
      category: "Strength of Materials",
      title: "Thermal Expansion & Fully Restrained Stress",
      formula: "Free expansion: ΔL = αLΔT;  Restrained stress magnitude: σ = EαΔT",
      description: "The stress expression assumes complete axial restraint and linear-elastic behavior with uniform temperature change. Its sign is tensile or compressive depending on heating/cooling and restraint."
    },
    {
      category: "Workshop Technology",
      title: "Vernier & Micrometer Reading",
      formula: "Vernier reading = Main-scale reading + (Coinciding division × Least count)",
      description: "Micrometer reading = sleeve (main-scale) reading + thimble reading. Apply zero correction when present; instrument least count depends on its scale design."
    },
    {
      category: "Suspension Systems",
      title: "Spring Rate & Natural Frequency",
      formula: "Spring force: F = kx;  Undamped natural frequency: fₙ = (1 / 2π)√(k/m)",
      description: "For a linear spring and a single-degree-of-freedom mass-spring model; k is stiffness in N/m and m is sprung mass in kg. Real suspension frequency also depends on damping and tyre compliance."
    },
    {
      category: "Motor Vehicles Act 1988",
      title: "Legal Blood Alcohol Limit",
      formula: "30 mg of alcohol per 100 ml of blood",
      description: "Section 185 MVA: driving or attempting to drive with alcohol exceeding 30 mg per 100 ml of blood is an offence. Watch the wording: the statutory trigger is 'exceeds' 30 mg per 100 ml."
    },
    {
      category: "Motor Vehicles Act 1988",
      title: "Registration, Fitness & Permit",
      formula: "Section 39: Registration  |  Section 56: Fitness  |  Section 66: Permit",
      description: "Fast recall: registration applies to motor vehicles generally; a transport vehicle's fitness certificate is addressed by Section 56; permit requirements for transport vehicles are under Section 66, subject to statutory exemptions."
    },
    {
      category: "Motor Vehicles Act 1988",
      title: "Third-Party Insurance",
      formula: "Section 146: Insurance against third-party risk",
      description: "A motor vehicle generally cannot be used in a public place without a policy complying with the Act's third-party insurance requirements. Do not confuse insurance (Section 146) with registration (Section 39)."
    },
    {
      category: "Motor Vehicles Act 1988",
      title: "Road-Safety Provisions: Match Section to Offence",
      formula: "184: Dangerous driving  |  185: Drunken driving  |  194B: Seat belt  |  194D: Helmet",
      description: "A common exam trap is mixing the offence section with the penalty section. Section 129 provides the protective-headgear requirement; Section 194D prescribes the penalty for its violation. Check the latest applicable Act/rules for penalty amounts."
    }
  ]
};
