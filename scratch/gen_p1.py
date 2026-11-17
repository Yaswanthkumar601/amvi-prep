# -*- coding: utf-8 -*-
"""
Generates Questions for Test 2 & Test 3 (100 questions total, 50 per test).
"""

def get_test_2_questions():
    # Test 2: Paper-I Polity, AP History & Reorganisation (50 Qs)
    # 1-20: Advanced Polity, 21-35: AP Freedom Movement & Personalities, 36-50: AP Reorganisation Act 2014
    items = []
    
    polity_data = [
        ("t2_q01", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "The Preamble to the Indian Constitution declares India to be which type of Democratic Republic?",
         ["Sovereign, Capitalist, Secular, Democratic Republic", "Sovereign, Socialist, Secular, Democratic Republic", "Federal, Socialist, Republican Democracy", "Unitary, Secular, Democratic Republic"], 1,
         "The 42nd Constitutional Amendment Act, 1976 added 'Socialist' and 'Secular' to 'Sovereign, Democratic Republic'.",
         "42వ రాజ్యాంగ సవరణ ద్వారా పీఠికలో 'సామ్యవాద', 'లౌకిక' అనే పదాలను చేర్చారు."),

        ("t2_q02", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Which Article of the Constitution guarantees the six fundamental democratic freedoms including freedom of speech and expression?",
         ["Article 14", "Article 19", "Article 21", "Article 22"], 1,
         "Article 19(1) guarantees 6 democratic freedoms: speech, assembly, association, movement, residence, and profession.",
         "ఆర్టికల్ 19 వాక్ స్వాతంత్ర్యం, సభలు సమావేశాలు ఏర్పాటు చేసుకునే స్వేచ్ఛ తదితర 6 ప్రాథమిక స్వేచ్ఛలను కల్పిస్తుంది."),

        ("t2_q03", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Under Article 21A, the State must provide free and compulsory education to all children of which age group?",
         ["3 to 10 years", "5 to 12 years", "6 to 14 years", "6 to 18 years"], 2,
         "The 86th Constitutional Amendment Act, 2002 inserted Article 21A making free education a fundamental right for ages 6 to 14.",
         "86వ రాజ్యాంగ సవరణ ద్వారా ఆర్టికల్ 21A కింద 6 నుండి 14 సంవత్సరాల పిల్లలకు ఉచిత ప్రాథమిక విద్యను ప్రాథమిక హక్కుగా చేశారు."),

        ("t2_q04", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Which Article of the Constitution strictly prohibits the employment of children below the age of 14 years in hazardous factories or mines?",
         ["Article 17", "Article 23", "Article 24", "Article 28"], 2,
         "Article 24 prohibits employment of children below the age of 14 in factories, mines, or any hazardous work.",
         "ఆర్టికల్ 24 ప్రకారం 14 సంవత్సరాల లోపు పిల్లలను ప్రమాదకర కర్మాగారాలు లేదా గనులలో పనిలో పెట్టుకోవడం నిషేధం."),

        ("t2_q05", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Article 44 of the Directive Principles of State Policy urges the State to secure for all citizens:",
         ["Panchayati Raj", "Separation of Judiciary", "Uniform Civil Code", "Right to Work"], 2,
         "Article 44 states that the State shall endeavor to secure for the citizens a Uniform Civil Code throughout the territory of India.",
         "ఆర్టికల్ 44 దేశవ్యాప్తంగా పౌరులందరికీ 'ఉమ్మడి పౌర స్మృతి' (Uniform Civil Code) అమలు చేయాలని సూచిస్తుంది."),

        ("t2_q06", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Fundamental Duties were incorporated into Part IVA under Article 51A by which Constitutional Amendment Act upon recommendation of Swaran Singh Committee?",
         ["24th Amendment", "42nd Amendment Act (1976)", "44th Amendment", "52nd Amendment"], 1,
         "The 42nd Amendment Act, 1976 added 10 Fundamental Duties under Article 51A on recommendation of Swaran Singh Committee.",
         "స్వరన్ సింగ్ కమిటీ సిఫారసుల మేరకు 42వ రాజ్యాంగ సవరణ (1976) ద్వారా ఆర్టికల్ 51A కింద ప్రాథమిక విధులను చేర్చారు."),

        ("t2_q07", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Under Article 148, who is appointed by the President as the guardian of the public purse to audit all receipts and expenditures of Union and States?",
         ["Attorney General of India", "Comptroller and Auditor General of India (CAG)", "Finance Commission Chairman", "Union Finance Secretary"], 1,
         "Article 148 establishes the independent constitutional office of the Comptroller and Auditor General of India (CAG).",
         "ఆర్టికల్ 148 కింద కంప్ట్రోలర్ అండ్ ఆడిటర్ జనరల్ (CAG) ప్రభుత్వ ఆదాయ వ్యయాలను ఆడిట్ చేసే అత్యున్నత రాజ్యాంగ అధికారి."),

        ("t2_q08", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Under Article 280, the Finance Commission is constituted by the President of India at expiration of every:",
         ["3 years", "5 years", "6 years", "10 years"], 1,
         "Article 280 provides that the President shall constitute a Finance Commission every 5th year for tax devolution.",
         "ఆర్టికల్ 280 ప్రకారం రాష్ట్రపతి ప్రతి 5 సంవత్సరాలకు ఒకసారి ఆర్థిక సంఘాన్ని (Finance Commission) ఏర్పాటు చేస్తారు."),

        ("t2_q09", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Which Constitutional Amendment Act deleted the Right to Property from the list of Fundamental Rights and made it an ordinary legal right under Article 300A?",
         ["42nd Amendment", "44th Constitutional Amendment Act (1978)", "52nd Amendment", "73rd Amendment"], 1,
         "The 44th Constitutional Amendment Act, 1978 removed Right to Property from Part III and made it a legal right under Article 300A.",
         "44వ రాజ్యాంగ సవరణ చట్టం (1978) ద్వారా ఆస్తి హక్కును ప్రాథమిక హక్కుల నుండి తొలగించి ఆర్టికల్ 300A కింద సాధారణ చట్టబద్ధ హక్కుగా మార్చారు."),

        ("t2_q10", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Under Article 213, who is empowered to promulgate ordinances during the recess of the State Legislature?",
         ["Chief Minister", "State Governor", "Chief Justice of High Court", "Speaker of Assembly"], 1,
         "Article 213 empowers the Governor to promulgate ordinances when the state legislative assembly is not in session.",
         "శాసనసభ సమావేశాలు లేనప్పుడు ఆర్టికల్ 213 కింద ఆర్డినెన్స్‌లను జారీ చేసే అధికారం రాష్ట్ర గవర్నర్‌కు ఉంటుంది."),

        ("t2_q11", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "The 91st Constitutional Amendment Act, 2003 limited the total number of ministers including the Chief Minister in a State Council to what maximum percentage of Legislative Assembly strength?",
         ["10%", "15%", "20%", "25%"], 1,
         "Article 164(1A) restricts the size of the council of ministers to a maximum of 15% of the total assembly strength (min 12 ministers).",
         "91వ రాజ్యాంగ సవరణ ద్వారా మంత్రిమండలి పరిమాణాన్ని శాసనసభ మొత్తం సభ్యుల సంఖ్యలో గరిష్టంగా 15% కు పరిమితం చేశారు."),

        ("t2_q12", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Which Constitutional Amendment Act provided 10% reservation in educational institutions and public employment for Economically Weaker Sections (EWS)?",
         ["101st Amendment", "102nd Amendment", "103rd Constitutional Amendment Act (2019)", "104th Amendment"], 2,
         "The 103rd Amendment Act, 2019 inserted Articles 15(6) and 16(6) granting 10% EWS reservation.",
         "103వ రాజ్యాంగ సవరణ చట్టం (2019) ద్వారా ఆర్థికంగా వెనుకబడిన వర్గాలకు (EWS) 10% రిజర్వేషన్ కల్పించారు."),

        ("t2_q13", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Under Article 368, an amendment to the Constitution requiring federal ratification must be passed by what proportion of State Legislatures?",
         ["One-third of States", "Not less than half of States", "Two-thirds of States", "Three-fourths of States"], 1,
         "Constitutional amendments affecting federal structures require ratification by simple resolution of not less than half of state legislatures.",
         "సమాఖ్య వ్యవస్థకు సంబంధించిన రాజ్యాంగ సవరణలకు కనీసం సగం (1/2) రాష్ట్రాల శాసనసభల ఆమోదం తప్పనిసరి."),

        ("t2_q14", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Under Article 163, who aids and advises the Governor in the exercise of his executive functions, except in matters where the Governor acts in discretion?",
         ["High Court Chief Justice", "Council of Ministers with Chief Minister as the head", "Advocate General", "State Chief Secretary"], 1,
         "Article 163 provides for a Council of Ministers with Chief Minister as head to aid and advise the Governor.",
         "ఆర్టికల్ 163 ప్రకారం గవర్నర్‌కు సలహాలు ఇవ్వడానికి ముఖ్యమంత్రి నేతృత్వంలోని మంత్రిమండలి ఉంటుంది."),

        ("t2_q15", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Under the RTI Act 2005, an applicant aggrieved by a decision of the Public Information Officer (PIO) may prefer a First Appeal within how many days?",
         ["15 days", "30 days", "45 days", "60 days"], 1,
         "Under Section 19(1), a first appeal must be filed within 30 days from the date of expiry of response or receipt of decision.",
         "సమాచార హక్కు చట్టం ప్రకారం మొదటి అప్పీలును 30 రోజుల్లోగా దాఖలు చేయాల్సి ఉంటుంది."),

        ("t2_q16", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Which Article establishes the State Public Service Commission (APPSC) for conducting examinations for appointments to public services of the State?",
         ["Article 312", "Article 315", "Article 320", "Article 323"], 1,
         "Article 315 provides for the establishment of a Public Service Commission for the Union and a Public Service Commission for each State.",
         "ఆర్టికల్ 315 రాష్ట్ర పబ్లిక్ సర్వీస్ కమిషన్ (APPSC) రాజ్యాంగబద్ధ ఏర్పాటును నిర్దేశిస్తుంది."),

        ("t2_q17", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Under Article 243I of the Constitution, who constitutes the State Finance Commission every 5 years to review the financial position of Panchayats?",
         ["State Chief Minister", "Governor of the State", "Speaker of Assembly", "Comptroller & Auditor General"], 1,
         "The Governor of the State constitutes the State Finance Commission every 5 years under Article 243I.",
         "ఆర్టికల్ 243I ప్రకారం రాష్ట్ర గవర్నర్ ప్రతి 5 సంవత్సరాలకు ఒకసారి రాష్ట్ర ఆర్థిక సంఘాన్ని ఏర్పాటు చేస్తారు."),

        ("t2_q18", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "The State Election Commission for conducting local panchayat and municipal elections is constituted under which Constitutional Article?",
         ["Article 243K", "Article 243Z", "Article 324", "Article 326"], 0,
         "Article 243K vests the superintendence of panchayat elections in an independent State Election Commissioner appointed by Governor.",
         "ఆర్టికల్ 243K కింద రాష్ట్ర ఎన్నికల సంఘం స్థానిక సంస్థల ఎన్నికలను పర్యవేక్షిస్తుంది."),

        ("t2_q19", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Under the Indian Constitution, the executive authority of the State is formally vested in whom?",
         ["Chief Minister", "State Governor", "Cabinet Secretary", "High Court Chief Justice"], 1,
         "Under Article 154, the executive power of the State is vested in the Governor and shall be exercised directly or through subordinate officers.",
         "ఆర్టికల్ 154 ప్రకారం రాష్ట్ర కార్యనిర్వాహక అధికారాలన్నీ లాంఛనప్రాయంగా రాష్ట్ర గవర్నర్ వద్దే ఉంటాయి."),

        ("t2_q20", "mock_test_02", 1, "p1-u5", "Indian Polity & Governance",
         "Which Article grants the President power to consult the Supreme Court on questions of law or fact of public importance (Advisory Jurisdiction)?",
         ["Article 131", "Article 136", "Article 143", "Article 226"], 2,
         "Article 143 empowers the President to seek advisory opinion from the Supreme Court on public matters of law or fact.",
         "ఆర్టికల్ 143 ప్రకారం రాష్ట్రపతి సుప్రీంకోర్టు నుండి సలహా లేదా న్యాయ అభిప్రాయాన్ని (Advisory Jurisdiction) కోరవచ్చు."),

        # 21-35 AP Freedom Movement
        ("t2_q21", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "Who designed the original Swaraj tricolour flag adopted by Mahatma Gandhi at the historic Vijayawada AICC session in 1921?",
         ["Alluri Sitarama Raju", "Pingali Venkayya", "Konda Venkatappaiah", "Tanguturi Prakasam"], 1,
         "Pingali Venkayya designed the National Flag, presented to Mahatma Gandhi at the Vijayawada AICC meeting in March 1921.",
         "1921 విజయవాడ కాంగ్రెస్ సమావేశాలలో పింగళి వెంకయ్య గారు జాతీయ పతాక నమూనాను గాంధీజీకి సమర్పించారు."),

        ("t2_q22", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "Who was the eminent nationalist leader and historian of the Indian National Congress who founded Andhra Bank in Machilipatnam in 1923?",
         ["Kasinadhuni Nageswara Rao", "Bhogaraju Pattabhi Sitaramayya", "Tanguturi Prakasam", "Duggirala Gopalakrishnayya"], 1,
         "Dr. Bhogaraju Pattabhi Sitaramayya founded Andhra Bank in 1923 and wrote 'The History of the Indian National Congress'.",
         "డాక్టర్ భోగరాజు పట్టాభి సీతారామయ్య గారు 1923లో మచిలీపట్నంలో ఆంధ్రా బ్యాంక్‌ను స్థాపించారు."),

        ("t2_q23", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "The famous social satirical play 'Kanyasulkam', ridiculing bride-price and social hypocrisies, was authored in modern spoken Telugu by:",
         ["Kandukuri Veeresalingam", "Gurajada Venkata Apparao", "Gidugu Ramamurthy", "Chilakamarti Lakshmi Narasimham"], 1,
         "Mahakavi Gurajada Apparao authored the landmark social drama 'Kanyasulkam' in 1892 promoting progressive spoken Telugu.",
         "మహాకవి గురజాడ అప్పారావు గారు 1892లో సాంఘిక దురాచారాలకు వ్యతిరేకంగా 'కన్యాశుల్కం' నాటకాన్ని రచించారు."),

        ("t2_q24", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "Who was hailed as 'Desoddharaka' for establishing the influential nationalist daily newspaper 'Andhra Patrika' in Bombay in 1908?",
         ["Tanguturi Prakasam", "Kasinadhuni Nageswara Rao Pantulu", "Nyapati Subba Rao", "Mutnuri Krishna Rao"], 1,
         "Desoddharaka Kasinadhuni Nageswara Rao founded 'Andhra Patrika' (1908) and Amrutanjan pain balm.",
         "దేశోద్ధారక కాశీనాథుని నాగేశ్వరరావు పంతులు గారు 1908లో 'ఆంధ్ర పత్రిక' దినపత్రికను స్థాపించారు."),

        ("t2_q25", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "Which fiery freedom fighter earned the title 'Andhra Kesari' (Lion of Andhra) for baring his chest to British police guns during the 1928 anti-Simon Commission protests in Madras?",
         ["Duggirala Gopalakrishnayya", "Tanguturi Prakasam Pantulu", "Kalluri Subba Rao", "Potti Sreeramulu"], 1,
         "Tanguturi Prakasam earned the title 'Andhra Kesari' in Madras by daring armed British troops to shoot him during the Simon Commission boycott.",
         "మద్రాసులో సైమన్ కమిషన్ వ్యతిరేక ప్రదర్శనలో తుపాకులకు ఎదురొడ్డి గుండెను చూపినందుకు టంగుటూరి ప్రకాశం గారికి 'ఆంధ్ర కేసరి' బిరుదు లభించింది."),

        ("t2_q26", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "The famous 'Sri Bagh Pact' between leaders of Coastal Andhra and Rayalaseema safeguarding capital and irrigation rights was signed in which year?",
         ["1928", "1937", "1947", "1953"], 1,
         "The Sri Bagh Pact was signed on 16 November 1937 at K. Nageswara Rao's residence (Sri Bagh) in Madras, balancing Rayalaseema interests.",
         "రాయలసీమ, కోస్తాంధ్ర నాయకుల మధ్య చారిత్రాత్మక 'శ్రీబాగ్ ఒప్పందం' 1937 నవంబర్ 16న మద్రాసులో కుదిరింది."),

        ("t2_q27", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "The Dhar Commission appointed by President Rajendra Prasad in June 1948 examined the feasibility of creating states primarily on which basis?",
         ["Linguistic basis", "Religious basis", "Administrative convenience", "Military strategy"], 0,
         "The S.K. Dhar Commission examined linguistic state demands and warned against dividing states purely on linguistic grounds.",
         "ఎస్.కె. ధార్ కమిషన్ (1948) భాషా ప్రయుక్త రాష్ట్రాల డిమాండ్లను పరిశీలించి పరిపాలనా సౌలభ్యానికే ప్రాధాన్యతనిచ్చింది."),

        ("t2_q28", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "The JVP Committee (1948) comprised which three prominent national leaders?",
         ["Jawaharlal Nehru, Vallabhbhai Patel, Pattabhi Sitaramayya", "Jawaharlal Nehru, V.V. Giri, Potti Sreeramulu", "Jayaprakash Narayan, Vallabhbhai Patel, Purushottam Das Tandon", "Jawaharlal Nehru, Vallabhbhai Patel, C. Rajagopalachari"], 0,
         "The JVP Committee comprised Jawaharlal Nehru, Vallabhbhai Patel, and Bhogaraju Pattabhi Sitaramayya.",
         "జేవీపీ (JVP) కమిటీలో జవహర్‌లాల్ నెహ్రూ, వల్లభాయ్ పటేల్ మరియు పట్టాభి సీతారామయ్య సభ్యులుగా ఉన్నారు."),

        ("t2_q29", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "In which house did Amarajeevi Potti Sreeramulu observe his final 58-day fast unto death in Madras from October 19, 1952?",
         ["Tanguturi Prakasam's residence", "Bulu Sambamurthy's house in Mylapore", "Madras High Court building", "Victoria Memorial Hall"], 1,
         "Potti Sreeramulu fasted at Bulu Sambamurthy's residence in Royapettah/Mylapore, Madras.",
         "పొట్టి శ్రీరాములు గారు మద్రాసులోని బులుసు సాంబమూర్తి గారి నివాసంలో ఆమరణ నిరాహార దీక్ష చేపట్టారు."),

        ("t2_q30", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "Who was the Chief Justice when the High Court of Andhra State was established at Guntur in July 1954?",
         ["Justice Koka Subba Rao", "Justice P. Satyanarayana Rao", "Justice Chandra Reddy", "Justice K. Umamaheswaram"], 0,
         "Justice Koka Subba Rao (later Chief Justice of India) was the first Chief Justice of the Andhra High Court at Guntur.",
         "గుంటూరులో ఆంధ్ర రాష్ట్ర హైకోర్టు ఏర్పడినప్పుడు జస్టిస్ కోకా సుబ్బారావు గారు తొలి ప్రధాన న్యాయమూర్తిగా ఉన్నారు."),

        ("t2_q31", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "Who was the tribal martyr of Palnadu Forest Satyagraha who was shot dead by British police at Minchalapadu in 1922?",
         ["Alluri Sitarama Raju", "Kanneganti Hanumanthu", "Parvataneni Veeraiah", "Komaram Bheem"], 1,
         "Kanneganti Hanumanthu organized the Palnadu Pullari (cattle grazing tax) satyagraha and was martyred at Minchalapadu.",
         "పల్నాడు పుల్లరి సత్యాగ్రహంలో కన్నెగంటి హనుమంతు బ్రిటీష్ తుపాకీ గుళ్లకు బలైన వీరుడు."),

        ("t2_q32", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "The historic 'Visalandhra' slogan demanding unification of all Telugu speaking regions of Madras and Hyderabad was first popularized by:",
         ["Communist Party of India (CPI)", "Justice Party", "Swatantra Party", "Congress Socialist Party"], 0,
         "Puchalapalli Sundarayya and the Communist Party of India pioneered the 'Visalandhralo Prajarajyam' movement.",
         "పుచ్చలపల్లి సుందరయ్య గారి నేతృత్వంలో కమ్యూనిస్టు పార్టీ విశాలాంధ్ర నినాదాన్ని ప్రజల్లోకి తీసుకెళ్లింది."),

        ("t2_q33", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "Who was the legendary leader of the Telangana armed struggle who popularized the slogan 'Jal, Jangal, Zameen' against Nizam feudal exploitation?",
         ["Alluri Sitarama Raju", "Komaram Bheem", "Chakali Ilamma", "Doddi Komaraiah"], 1,
         "Gond martyr Komaram Bheem fought the Nizam's police at Jodeghat asserting tribal sovereignty over land, forest, and water.",
         "గోండు వీరుడు కొమరం భీమ్ 'జల్, జంగల్, జమీన్' నినాదంతో నిజాం నిరంకుశత్వానికి వ్యతిరేకంగా పోరాడారు."),

        ("t2_q34", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "In which year was the historic Salt Satyagraha conducted in Andhra at George Town, Madras by Tanguturi Prakasam defying British prohibitory orders?",
         ["1920", "1930", "1942", "1946"], 1,
         "Prakasam led the Salt Satyagraha in Madras on 13 April 1930 in tandem with Mahatma Gandhi's Dandi March.",
         "1930లో గాంధీజీ దండి సత్యాగ్రహంతో పాటు మద్రాసులో టంగుటూరి ప్రకాశం ఉప్పు సత్యాగ్రహాన్ని నిర్వహించారు."),

        ("t2_q35", "mock_test_02", 1, "p1-u4", "Modern Indian & AP History",
         "Which prominent Andhra literary giant pioneered the Spoken Telugu (Vyavaharika Bhasha) movement challenging orthodox classical granthika dominance?",
         ["Kandukuri Veeresalingam", "Gidugu Venkata Ramamurthy", "Gurazada Apparao", "Tirupati Venkata Kavulu"], 1,
         "Gidugu Venkata Ramamurthy championed Vyavaharika Bhasha, enabling spoken Telugu to become the medium of literature and instruction.",
         "గిడుగు వెంకట రామమూర్తి గారు వాడుక భాషా ఉద్యమాన్ని నడిపించి సామాన్యుడి తెలుగును సాహితీ భాషగా మార్చారు."),

        # 36-50 AP Reorganisation Act 2014
        ("t2_q36", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "The Andhra Pradesh Reorganisation Act, 2014 was passed by Parliament under which Articles of the Constitution?",
         ["Articles 1 and 2", "Articles 3 and 4", "Article 356", "Article 368"], 1,
         "State reorganization acts are enacted under Articles 3 and 4 of the Constitution by simple majority.",
         "రాష్ట్రాల పునర్వ్యవస్థీకరణ రాజ్యాంగంలోని ఆర్టికల్ 3 మరియు 4 కింద సాధారణ మెజారిటీతో పార్లమెంటు ఆమోదిస్తుంది."),

        ("t2_q37", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "What was the official 'Appointed Day' on which the state of Andhra Pradesh was bifurcated into Telangana and successor AP?",
         ["March 1, 2014", "June 2, 2014", "August 15, 2014", "January 1, 2015"], 1,
         "June 2, 2014 was notified as the Appointed Day under Section 2(a) of the AP Reorganisation Act.",
         "2014 జూన్ 2 ను అధికారికంగా రెండు రాష్ట్రాల ఆవిర్భావ దినంగా (Appointed Day) నిర్ణయించారు."),

        ("t2_q38", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "Under Section 5 of the Act, for what maximum period was Hyderabad designated as a common capital before expiring in June 2024?",
         ["5 years", "10 years", "15 years", "20 years"], 1,
         "Section 5 provided that Hyderabad shall be the common capital for both States for a period not exceeding 10 years.",
         "సెక్షన్ 5 ప్రకారం హైదరాబాద్ గరిష్టంగా 10 సంవత్సరాల పాటు ఉమ్మడి రాజధానిగా నిర్ణయించబడింది."),

        ("t2_q39", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "Under Section 47 of the AP Reorganisation Act 2014, the apportionment of assets and liabilities between AP and Telangana was based on which ratio?",
         ["Equal 50 : 50 ratio", "2011 Census Population ratio (58.32% for AP, 41.68% for Telangana)", "Geographical area ratio", "Revenue contribution ratio"], 1,
         "Section 47 apportioned assets and public debt based on the 2011 Census population ratio of 58.32 : 41.68.",
         "సెక్షన్ 47 ప్రకారం ఆస్తులు మరియు అప్పుల పంపకం 2011 జనాభా నిష్పత్తి (58.32% : 41.68%) ఆధారంగా జరిగింది."),

        ("t2_q40", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "Under Section 90 of the Act, which multipurpose irrigation project was declared a 'National Project' to be executed by the Central Government?",
         ["Nagarjuna Sagar Project", "Polavaram Irrigation Project", "Pulichintala Project", "Srisailam Dam"], 1,
         "Section 90 declared the Polavaram Irrigation Project a National Project, consenting to Central execution and funding.",
         "సెక్షన్ 90 ప్రకారం పోలవరం ప్రాజెక్టును జాతీయ ప్రాజెక్టుగా ప్రకటించి కేంద్ర ప్రభుత్వమే పూర్తి చేస్తుందని హామీ ఇచ్చారు."),

        ("t2_q41", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "Under Section 85 of the Act, which two river management boards were constituted under the Union Ministry of Water Resources / Jal Shakti?",
         ["Penna and Vamsadhara Boards", "Krishna River Management Board (KRMB) & Godavari River Management Board (GRMB)", "Cauvery and Tungabhadra Boards", "Polavaram and Srisailam Boards"], 1,
         "Sections 85 and 87 established KRMB and GRMB to regulate water distribution and reservoir operations.",
         "సెక్షన్ 85 ప్రకారం కృష్ణా (KRMB) మరియు గోదావరి (GRMB) నదీ యాజమాన్య బోర్డులను ఏర్పాటు చేశారు."),

        ("t2_q42", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "How many Government Companies and Public Sector Corporations are listed for division under Schedule IX of the Act?",
         ["64", "91", "108", "142"], 1,
         "Schedule IX lists 91 Government companies and corporations for division between the two successor states.",
         "9వ షెడ్యూల్‌లో విభజన కోసం 91 ప్రభుత్వ కంపెనీలు మరియు కార్పొరేషన్లను చేర్చారు."),

        ("t2_q43", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "How many State training and cultural institutions/societies are listed for asset division under Schedule X of the Act?",
         ["75", "108", "142", "180"], 2,
         "Schedule X lists 142 institutions, apex training institutes, and societies.",
         "10వ షెడ్యూల్‌లో 142 శిక్షణా సంస్థలు మరియు సొసైటీలు విభజన జాబితాలో ఉన్నాయి."),

        ("t2_q44", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "Section 94 of the AP Reorganisation Act, 2014 mandates the Central Government to provide which crucial benefits to successor AP?",
         ["Military recruitment quotas", "Special fiscal incentives and tax concessions for industrialization and backward areas", "Nuclear power plants", "Exclusive port subsidies"], 1,
         "Section 94 mandates appropriate fiscal measures, tax incentives, and support for backward districts of Rayalaseema and North Coastal AP.",
         "సెక్షన్ 94 ప్రకారం వెనుకబడిన ప్రాంతాల పారిశ్రామికాభివృద్ధికి కేంద్ర ప్రభుత్వం పన్ను రాయితీలు మరియు ఆర్థిక ప్రోత్సాహకాలు ఇవ్వాలి."),

        ("t2_q45", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "On which date did the separate High Court of Andhra Pradesh commence independent judicial functioning at Amaravati?",
         ["June 2, 2014", "January 1, 2019", "March 15, 2020", "October 2, 2021"], 1,
         "The High Court of Andhra Pradesh at Amaravati was inaugurated and commenced functioning on January 1, 2019.",
         "ఆంధ్రప్రదేశ్ ప్రత్యేక హైకోర్టు 2019 జనవరి 1 నుండి అమరావతిలో స్వతంత్రంగా పనిచేయడం ప్రారంభించింది."),

        ("t2_q46", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "Under Section 8 of the Act, who was entrusted with special responsibility for the security of life, liberty and property of residents in the common capital?",
         ["Chief Minister of Telangana", "Chief Minister of AP", "Governor of Telangana / Common Governor", "Union Home Minister"], 2,
         "Section 8 vested the Governor with special responsibility for law and order in the common capital during the transition.",
         "సెక్షన్ 8 ప్రకారం ఉమ్మడి రాజధానిలో శాంతిభద్రతల రక్షణ బాధ్యతను గవర్నర్‌కు ప్రత్యేక అధికారంగా అప్పగించారు."),

        ("t2_q47", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "According to Schedule XIII of the Act, which apex national educational institutions were mandated to be established in Andhra Pradesh?",
         ["IIT, IIM, IISER, NIT, Central University and IIIT", "Only IIT and IIM", "AIIMS only", "DRDO and ISRO headquarters"], 0,
         "Schedule XIII mandated national institutes including IIT (Tirupati), IIM (Visakhapatnam), IISER (Tirupati), NIT (Tadepalligudem), and AIIMS (Mangalagiri).",
         "13వ షెడ్యూల్ ప్రకారం ఐఐటీ, ఐఐఎం, ఐఐఎస్‌ఈఆర్, ఎన్‌ఐటీ మరియు ఎయిమ్స్ వంటి జాతీయ విద్యాసంస్థలను ఏపీలో ఏర్పాటు చేశారు."),

        ("t2_q48", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "In order to avoid submergence of villages under Polavaram Project, which mandals of Khammam district were transferred to Andhra Pradesh in 2014?",
         ["7 mandals (including Bhadrachalam rural, Kunavaram, Chintoor, Vararamachandrapuram)", "3 mandals only", "12 mandals", "15 mandals"], 0,
         "An ordinance in May 2014 (later an amendment act) transferred 7 submerged mandals of Khammam to East and West Godavari districts.",
         "పోలవరం ప్రాజెక్టు ముంపునకు గురయ్యే ఖమ్మం జిల్లాలోని 7 మండలాలను ఆంధ్రప్రదేశ్‌లో విలీనం చేశారు."),

        ("t2_q49", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "What is the total number of Sections and Schedules in the Andhra Pradesh Reorganisation Act, 2014?",
         ["100 Sections and 10 Schedules", "108 Sections and 13 Schedules", "120 Sections and 15 Schedules", "95 Sections and 8 Schedules"], 1,
         "The Act comprises 12 Parts, 108 Sections, and 13 Schedules.",
         "ఏపీ పునర్వ్యవస్థీకరణ చట్టంలో 12 భాగాలు, 108 సెక్షన్లు మరియు 13 షెడ్యూళ్లు ఉన్నాయి."),

        ("t2_q50", "mock_test_02", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "Under Section 46 of the Act, the allocation of revenues and expenditures between the two states is finalized under the advice of which constitutional authority?",
         ["Planning Commission", "Comptroller and Auditor General of India (CAG)", "NITI Aayog", "Finance Minister"], 1,
         "CAG audits, certifies, and determines the apportioned balances and public accounts under Section 46.",
         "సెక్షన్ 46 ప్రకారం కాగ్ (CAG) సలహా మరియు ధృవీకరణతో ఆదాయాలు మరియు వ్యయాల విభజన జరుగుతుంది.")
    ]
    return polity_data

print("Test 2 builder ready.")
# -*- coding: utf-8 -*-
"""
Questions for Test 3, 4, 5, 6 (200 questions total, 50 each).
"""

def get_test_3_questions():
    # Test 3: Science, Clean Mobility, Economy & Mental Ability (50 Qs)
    items = []
    # 1-15 Science & EV Tech
    science_data = [
        ("t3_q01", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "In electric vehicles, what does 'Regenerative Braking' do during vehicle deceleration?",
         ["Heats up mechanical friction pads", "Converts vehicle kinetic energy into electrical energy to recharge the traction battery", "Disconnects the motor to reduce current", "Uses engine exhaust backpressure to slow the wheels"], 1,
         "Regenerative braking operates the electric traction motor in generator mode, converting kinetic energy into electricity.",
         "రీజెనరేటివ్ బ్రేకింగ్ ద్వారా వాహనం వేగం తగ్గేటప్పుడు గతిజ శక్తిని విద్యుత్ శక్తిగా మార్చి బ్యాటరీని రీఛార్జ్ చేస్తారు."),

        ("t3_q02", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "Which device in an EV powertrain converts the high-voltage direct current (DC) from the traction battery into 3-phase alternating current (AC) for the electric motor?",
         ["Step-down Transformer", "Traction Inverter", "DC-DC Converter", "Braking Resistor"], 1,
         "The traction inverter converts DC battery power into variable-frequency 3-phase AC to drive the traction motor.",
         "ట్రాక్షన్ ఇన్వర్టర్ బ్యాటరీలోని డీసీ (DC) కరెంట్‌ను మోటారుకు అవసరమైన 3-ఫేజ్ ఏసీ (AC) విద్యుత్‌గా మారుస్తుంది."),

        ("t3_q03", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "What is the function of the Auxiliary DC-DC Converter in an Electric Vehicle?",
         ["Steps up 400V battery to 1000V for motor", "Steps down 400V/800V high voltage battery to 12V to power dashboard lights, wipers, and ECUs", "Charges the main battery from regenerative brakes", "Controls motor speed directly"], 1,
         "The auxiliary DC-DC converter steps down high battery voltage (e.g. 400V) to standard 12V DC for vehicle low-voltage accessories.",
         "డీసీ-డీసీ కన్వర్టర్ మెయిన్ బ్యాటరీలోని 400V అధిక వోల్టేజ్‌ను లైట్లు, వైపర్లు, హారన్ మొదలైన వాటి కోసం 12V గా తగ్గిస్తుంది."),

        ("t3_q04", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "What dangerous phenomenon occurs when a Lithium-ion cell overheats uncontrollably, releasing flammable gases and causing self-sustaining fires?",
         ["Electrolytic cavitation", "Thermal Runaway", "Galvanic corrosion", "Sulfation"], 1,
         "Thermal runaway is an exothermic cascade where internal cell heat exceeds dissipation rate, causing combustion.",
         "థర్మల్ రన్‌అవే (Thermal Runaway) అనేది బ్యాటరీ కణాలలో అధిక వేడి వల్ల మంటలు చెలరేగే ప్రమాదకర ప్రక్రియ."),

        ("t3_q05", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "What is the primary technical reason Lithium Iron Phosphate (LiFePO4) batteries are preferred for Indian hot climate commercial transport?",
         ["Highest volumetric energy density", "Superior thermal stability, non-combustible olivine crystal structure, and longer cycle life", "Fastest charging in 5 minutes", "Lowest weight"], 1,
         "LFP cells have stable P-O covalent bonds that do not release oxygen at high temperatures, preventing fires.",
         "LFP బ్యాటరీలు అధిక ఉష్ణోగ్రతలను తట్టుకునే స్థిరత్వాన్ని మరియు ఎక్కువ జీవిత కాలాన్ని కలిగి ఉంటాయి."),

        ("t3_q06", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "In a hydrogen fuel cell vehicle (FCEV), what is the sole emission released from the vehicle tailpipe?",
         ["Carbon Monoxide (CO)", "Pure Water Vapor (H2O)", "Nitrogen Dioxide", "Sulfur Dioxide"], 1,
         "Proton Exchange Membrane (PEM) fuel cells combine Hydrogen and atmospheric Oxygen to generate electricity, emitting only pure water.",
         "హైడ్రోజన్ ఫ్యూయల్ సెల్ వాహనాల నుండి పొగకు బదులుగా కేవలం స్వచ్ఛమైన నీటి ఆవిరి (H2O) మాత్రమే వెలువడుతుంది."),

        ("t3_q07", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "What is the targeted green hydrogen production capacity per annum under India's National Green Hydrogen Mission by 2030?",
         ["1 Million Metric Tonnes (MMT)", "5 Million Metric Tonnes (MMT)", "10 Million Metric Tonnes (MMT)", "20 Million Metric Tonnes (MMT)"], 1,
         "The mission aims for at least 5 MMT of green hydrogen production per year by 2030, with coastal AP as a key green hydrogen hub.",
         "జాతీయ గ్రీన్ హైడ్రోజన్ మిషన్ కింద 2030 నాటికి ఏడాదికి 5 మిలియన్ మెట్రిక్ టన్నుల ఉత్పత్తిని లక్ష్యంగా పెట్టుకున్నారు."),

        ("t3_q08", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "What type of fast charging standard connector is commonly mandated for public four-wheeler DC fast charging stations in India?",
         ["Combined Charging System Type 2 (CCS-2)", "Type 1 J1772", "Tesla NACS only", "GB/T AC only"], 0,
         "CCS-2 (Combined Charging System Type 2) is the standard combined AC/DC charging connector adopted across India.",
         "భారతదేశంలో ఫోర్-వీలర్ ఫాస్ట్ ఛార్జింగ్ కోసం సీసీఎస్-2 (CCS-2) ప్రమాణాన్ని అధికారికంగా ఉపయోగిస్తున్నారు."),

        ("t3_q09", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "What is the state of charge (SoC) definition in automotive battery terminology?",
         ["Total weight of electrolyte", "Percentage of remaining battery capacity relative to its maximum rated capacity", "Voltage under zero load", "Internal cell resistance in ohms"], 1,
         "State of Charge (SoC) is the percentage of available capacity in a battery relative to its total capacity (similar to a fuel gauge).",
         "స్టేట్ ఆఫ్ ఛార్జ్ (SoC) అంటే బ్యాటరీలో ప్రస్తుతం అందుబాటులో ఉన్న ఛార్జింగ్ శాతం (ఫ్యూయల్ గేజ్ లాంటిది)."),

        ("t3_q10", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "In automotive lead-acid batteries, what harmful crystal layer forms on plates when a battery is left in a discharged state for prolonged periods?",
         ["Lead Peroxide", "Coarse Lead Sulphate (Sulfation)", "Sponge Lead", "Lead Carbonate"], 1,
         "Prolonged discharge causes lead sulphate crystals to harden (sulfation), irreversibly reducing battery capacity.",
         "డిశ్చార్జ్ అయిన బ్యాటరీని ఎక్కువ కాలం అలాగే ఉంచితే లెడ్ ప్లేట్లపై లెడ్ సల్ఫేట్ స్పటికాలు పేరుకుపోతాయి (సల్ఫేషన్)."),

        ("t3_q11", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "What liquid is added to top up an automotive lead-acid battery during periodic maintenance when electrolyte level falls below indicator?",
         ["Dilute Sulphuric Acid", "Concentrated Hydrochloric Acid", "Pure Distilled Water / Deionized Water", "Tap Water"], 2,
         "During operation only water evaporates via electrolysis (gassing). Hence, only pure distilled water must be added.",
         "బ్యాటరీలో నీటి శాతం తగ్గినప్పుడు ఎలక్ట్రోలైట్ స్థాయిని పెంచడానికి కేవలం స్వచ్ఛమైన డిస్టిల్డ్ వాటర్ మాత్రమే కలపాలి."),

        ("t3_q12", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "Which navigation satellite constellation developed by ISRO provides indigenous regional positioning across India and 1500 km around its borders?",
         ["GLONASS", "Galileo", "NavIC (Navigation with Indian Constellation)", "BeiDou"], 2,
         "NavIC (IRNSS) is India's independent satellite constellation providing standard positioning services (SPS) for transport tracking.",
         "ఇస్రో రూపొందించిన నావిక్ (NavIC) భారతదేశం మరియు పరిసర ప్రాంతాలలో స్వదేశీ ఉపగ్రహ నావిగేషన్ సేవలను అందిస్తుంది."),

        ("t3_q13", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "What radio frequency band does RFID FASTag use for automated toll payment on Indian national highways?",
         ["13.56 MHz (HF)", "865 - 868 MHz (UHF)", "2.4 GHz (Microwave)", "5.8 GHz (DSRC)"], 1,
         "Indian FASTag operates in the 865-868 MHz UHF band under the GS1 EPC Gen 2 standard.",
         "భారతదేశంలో ఫాస్టాగ్ (FASTag) 865-868 MHz UHF రేడియో ఫ్రీక్వెన్సీ పరిధిలో పనిచేస్తుంది."),

        ("t3_q14", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "What is the full form of the standard diagnostic connector OBD-II mandated in all BS-VI compliant automobiles?",
         ["On-Board Diagnostics Version II", "Operational Braking Dynamics II", "Over-Boost Drive Intercooler II", "Open Bus Detection II"], 0,
         "OBD-II stands for On-Board Diagnostics II, providing standard 16-pin access to emission and engine fault codes.",
         "OBD-II అంటే ఆన్-బోర్డ్ డయాగ్నోస్టిక్స్-II, ఇది వాహనం లోపాల డేటాను తెలుసుకోవడానికి ఉపయోగించే 16-పిన్ పోర్ట్."),

        ("t3_q15", "mock_test_03", 1, "p1-u3", "Science & Clean Mobility",
         "In vehicle dynamics, if vehicle velocity doubles from 40 km/h to 80 km/h, by what factor does kinetic energy (and stopping distance) increase?",
         ["Doubles (2 times)", "Triples (3 times)", "Quadruples (4 times)", "Remains unchanged"], 2,
         "Kinetic energy KE = 0.5 * m * v^2. When velocity doubles, KE increases by 2^2 = 4 times, quadrupling stopping distance.",
         "గతిజ శక్తి సూత్రం KE = 1/2 * m * v^2 ప్రకారం వేగం రెట్టింపు అయితే గతిజ శక్తి మరియు బ్రేకింగ్ దూరం 4 రెట్లు పెరుగుతాయి."),

        # 16-30 Economy & AP Socio-Economic Survey
        ("t3_q16", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "According to the AP Socio-Economic Survey, which sector registers the highest employment and major export revenue in Andhra Pradesh?",
         ["Heavy Metallurgy", "Agriculture and Allied Sectors (Horticulture, Aquaculture, Livestock)", "Automobile Assembly", "Software Development"], 1,
         "Agriculture, aquaculture, and livestock dominate Andhra Pradesh's rural economy and employment base.",
         "ఆంధ్రప్రదేశ్ ఆర్థిక వ్యవస్థలో వ్యవసాయం, ఉద్యానవనాలు మరియు ఆక్వా రంగం అత్యధిక ఉపాధిని కల్పిస్తున్నాయి."),

        ("t3_q17", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "Where in Andhra Pradesh is a major new greenfield commercial deep-water seaport recently developed in Prakasam district?",
         ["Bhavanapadu", "Ramayapatnam", "Kalingapatnam", "Bheemunipatnam"], 1,
         "Ramayapatnam Port in Prakasam district is developed as an all-weather non-major deep-water commercial port.",
         "ప్రకాశం జిల్లాలో రామాయపట్నం వద్ద సరికొత్త గ్రీన్‌ఫీల్డ్ లోతైన ఓడరేవును అభివృద్ధి చేశారు."),

        ("t3_q18", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "The proposed greenfield commercial seaport 'Mulapeta' is situated in which northern coastal district of Andhra Pradesh?",
         ["Srikakulam", "Vizianagaram", "Anakapalli", "Kakinada"], 0,
         "Mulapeta (formerly Bhavanapadu) seaport is located in Srikakulam district near the Odisha border.",
         "శ్రీకాకుళం జిల్లాలో మూలపేట (గతంలో భావనపాడు) వాణిజ్య ఓడరేవును నిర్మిస్తున్నారు."),

        ("t3_q19", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "Under the PM-eBus Sewa scheme, what major reform is underway in public transport across cities in Andhra Pradesh?",
         ["Phasing out buses completely", "Induction of electric city buses on Public-Private Partnership (PPP) model with charging depots", "Replacing buses with light rail", "Subsidizing diesel fuel for transport fleets"], 1,
         "PM-eBus Sewa deploys zero-emission electric city buses across tier-2 and tier-3 cities with dedicated charging infrastructure.",
         "పీఎం-ఈబస్ సేవా పథకం కింద నగరాల్లో పర్యావరణహిత విద్యుత్ బస్సులను (Electric Buses) ప్రవేశపెడుతున్నారు."),

        ("t3_q20", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "Which National Highway stretch connecting Chennai and Kolkata spans the entire length of the Andhra Pradesh coastal corridor?",
         ["National Highway 44 (NH-44)", "National Highway 16 (NH-16 / Old NH-5)", "National Highway 65 (NH-65)", "National Highway 40 (NH-40)"], 1,
         "NH-16 (part of the Golden Quadrilateral) runs across coastal AP from Srikakulam to Tada in Nellore.",
         "శ్రీకాకుళం నుండి నెల్లూరు తడ వరకు తీరప్రాంతం వెంబడి వెళ్లే ప్రధాన జాతీయ రహదారి ఎన్‌హెచ్-16 (పాత NH-5)."),

        ("t3_q21", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "Which district in Rayalaseema region has emerged as a premier hub for automotive manufacturing and renewable energy parks?",
         ["YSR Kadapa", "Anantapur (Sri Sathya Sai)", "Kurnool", "Nandyal"], 1,
         "Anantapur / Sri Sathya Sai district hosts major automobile manufacturing plants (e.g. Kia Motors) and solar/wind parks.",
         "అనంతపురం / శ్రీ సత్యసాయి జిల్లా ఆటోమొబైల్ తయారీ (కియా మోటార్స్) మరియు సౌరశక్తి కేంద్రాలకు హబ్‌గా మారింది."),

        ("t3_q22", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "What is the statutory basis of the GST Council established under the 101st Constitutional Amendment?",
         ["Statutory non-constitutional body", "Article 279A of the Constitution of India", "Executive order of NITI Aayog", "Section 12 of Finance Act"], 1,
         "Article 279A establishes the GST Council as a constitutional body governing GST rates and exemptions.",
         "ఆర్టికల్ 279A కింద జీఎస్టీ కౌన్సిల్ రాజ్యాంగబద్ధమైన అత్యున్నత సమాఖ్య సంస్థగా పనిచేస్తుంది."),

        ("t3_q23", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "In GST terminology, which tax is levied on inter-state supply of goods and services, collected by the Centre and shared with destination states?",
         ["CGST", "SGST", "Integrated Goods and Services Tax (IGST)", "UTGST"], 2,
         "IGST is levied on all inter-state supplies and imports under Article 269A.",
         "రెండు రాష్ట్రాల మధ్య జరిగే వ్యాపార లావాదేవీలపై ఐజీఎస్టీ (IGST) విధించబడుతుంది."),

        ("t3_q24", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "What is the direct benefit transfer flagship agricultural input support scheme implemented in Andhra Pradesh?",
         ["PM KISAN & YSR Rythu Bharosa", "Rythu Bandhu", "Krushak Assistance (KALIA)", "Bhavantar Bhugtan"], 0,
         "Rythu Bharosa provides direct financial assistance to landowning and tenant farmers for cultivation inputs.",
         "రైతులకు పెట్టుబడి సహాయం అందించే ప్రధాన పథకం వైఎస్సార్ రైతు భరోసా."),

        ("t3_q25", "mock_test_03", 1, "p1-u6", "AP Economy & Planning",
         "Which seaport in Andhra Pradesh has a dedicated outer harbour designed specifically for iron ore export to Japan and East Asia?",
         ["Machilipatnam", "Visakhapatnam Port Outer Harbour", "Kakinada Anchorage", "Bhavanapadu"], 1,
         "Visakhapatnam outer harbour features one of Asia's fastest automated iron ore handling conveyor berths.",
         "విశాఖపట్నం ఔటర్ హార్బర్ నుండి ఇనుప ఖనిజాన్ని జపాన్ మరియు తూర్పు ఆసియా దేశాలకు భారీగా ఎగుమతి చేస్తారు."),

        ("t3_q26", "mock_test_03", 1, "p1-u8", "Disaster Management & Environment",
         "What color-coded cyclone alert issued by India Meteorological Department (IMD) signifies 'Cyclone Warning' issued 24 hours in advance?",
         ["Yellow Alert", "Orange Alert", "Red Alert (Post-Landfall)", "Green Alert"], 1,
         "IMD 4-stage cyclone alerts: Yellow (Watch - 48h), Orange (Warning - 24h), Red (Landfall Outlook - 12h).",
         "ఐఎండీ రంగుల హెచ్చరికలలో 'ఆరెంజ్ అలర్ట్' 24 గంటల ముందు జారీ చేసే తుఫాను హెచ్చరికను సూచిస్తుంది."),

        ("t3_q27", "mock_test_03", 1, "p1-u8", "Disaster Management & Environment",
         "Under the Environment Protection Act, 1986, which statutory zone restricts commercial constructions within 500 meters of the high tide line?",
         ["Coastal Regulation Zone (CRZ)", "Special Economic Zone", "Eco-Sensitive Buffer", "Biosphere Reserve Core"], 0,
         "Coastal Regulation Zone (CRZ) notifications regulate developmental activities along the coastline to preserve ecology.",
         "తీర ప్రాంత నియంత్రణ మండలి (CRZ) నిబంధనల ప్రకారం సముద్ర తీరానికి 500 మీటర్ల పరిధిలో నిర్మాణాలు నియంత్రించబడతాయి."),

        ("t3_q28", "mock_test_03", 1, "p1-u8", "Disaster Management & Environment",
         "Which Doppler Weather Radar (DWR) station in coastal Andhra Pradesh provides early tracking of approaching cyclones in the central Bay of Bengal?",
         ["Kurnool Doppler Radar", "Visakhapatnam & Machilipatnam Doppler Weather Radars", "Tirupati Radar", "Kadapa Radar"], 1,
         "Doppler radars at Visakhapatnam and Machilipatnam monitor cyclone cyclonic vortex structure and precipitation intensity.",
         "విశాఖపట్నం మరియు మచిలీపట్నం డాప్లర్ రాడార్లు బంగాళాఖాతపు తుఫానులను ముందస్తుగా ట్రాక్ చేస్తాయి."),

        ("t3_q29", "mock_test_03", 1, "p1-u8", "Disaster Management & Environment",
         "Which UN Sustainable Development Goal (SDG) specifically deals with 'Climate Action'?",
         ["SDG 5", "SDG 7", "SDG 13", "SDG 15"], 2,
         "SDG 13 is dedicated to taking urgent action to combat climate change and its impacts.",
         "ఐక్యరాజ్యసమితి నిర్దేశించిన 13వ సుస్థిరాభివృద్ధి లక్ష్యం (SDG 13) 'వాతావరణ చర్య' (Climate Action) కు సంబంధించినది."),

        ("t3_q30", "mock_test_03", 1, "p1-u8", "Disaster Management & Environment",
         "What is the term for the biological and chemical breakdown of accumulated organic waste without oxygen, generating biogas?",
         ["Aerobic composting", "Anaerobic Digestion", "Pyrolysis", "Incineration"], 1,
         "Anaerobic digestion decomposes organic biomass in oxygen-free digesters to produce biogas (60% methane).",
         "ఆక్సిజన్ లేని పరిస్థితులలో వ్యర్థాలు కుళ్లిపోయి బయోగ్యాస్ ఉత్పత్తి అయ్యే ప్రక్రియను 'అనారోబిక్ డైజెషన్' అంటారు."),

        # 31-50 Mental Ability & Quantitative Aptitude
        ("t3_q31", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "A transport goods truck travels 360 km in 6 hours. If its speed is increased by 15 km/h, how much time will it take to cover the same distance?",
         ["4.0 hours", "4.8 hours", "5.0 hours", "5.2 hours"], 1,
         "Original speed = 360 / 6 = 60 km/h. New speed = 60 + 15 = 75 km/h. Time = 360 / 75 = 4.8 hours (4 hours 48 minutes).",
         "మొదటి వేగం = 360/6 = 60 కి.మీ/గం. పెరిగిన వేగం = 75 కి.మీ/గం. పట్టే సమయం = 360/75 = 4.8 గంటలు."),

        ("t3_q32", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "Two inspection patrol cars leave Guntur simultaneously in opposite directions at 65 km/h and 55 km/h. How far apart will they be after 2.5 hours?",
         ["250 km", "280 km", "300 km", "320 km"], 2,
         "Relative speed in opposite directions = 65 + 55 = 120 km/h. Distance = 120 * 2.5 = 300 km.",
         "వ్యతిరేక దిశల్లో ప్రయాణించినప్పుడు సాపేక్ష వేగం = 65 + 55 = 120 కి.మీ/గం. 2.5 గంటల్లో దూరం = 120 * 2.5 = 300 కి.మీ."),

        ("t3_q33", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "A train 240 meters long crosses a bridge 360 meters long in 30 seconds. What is the speed of the train in km/h?",
         ["60 km/h", "72 km/h", "80 km/h", "90 km/h"], 1,
         "Total distance = 240 + 360 = 600 m. Speed in m/s = 600 / 30 = 20 m/s. Speed in km/h = 20 * (18/5) = 72 km/h.",
         "మొత్తం దూరం = 240 + 360 = 600 మీ. వేగం = 600/30 = 20 మీ/సె. కి.మీ/గం లో వేగం = 20 * (18/5) = 72 కి.మీ/గం."),

        ("t3_q34", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "The price of diesel increases by 25%. By what percentage must a transport operator reduce consumption so that total expenditure remains unchanged?",
         ["15%", "20%", "25%", "30%"], 1,
         "Reduction % = [r / (100 + r)] * 100 = [25 / 125] * 100 = 20%.",
         "ఖర్చు మారకుండా ఉండాలంటే వినియోగం తగ్గించాల్సిన శాతం = [25 / (100 + 25)] * 100 = 20%."),

        ("t3_q35", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "A vehicle purchased for ₹8,00,000 depreciates in value by 10% per annum. What will be its book value after 2 years?",
         ["₹6,40,000", "₹6,48,000", "₹6,80,000", "₹7,20,000"], 1,
         "Value = 8,00,000 * (0.90)^2 = 8,00,000 * 0.81 = ₹6,48,000.",
         "రెండేళ్ల తర్వాత వాహనం విలువ = 8,00,000 * 0.9 * 0.9 = ₹6,48,000."),

        ("t3_q36", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "A boat travels 36 km downstream with water current in 3 hours and returns 36 km upstream against current in 6 hours. What is the speed of the water stream?",
         ["2 km/h", "3 km/h", "4 km/h", "6 km/h"], 1,
         "Downstream speed u = 36/3 = 12 km/h. Upstream speed v = 36/6 = 6 km/h. Stream speed = (u - v)/2 = (12 - 6)/2 = 3 km/h.",
         "ప్రవాహ వేగం = (డౌన్‌స్ట్రీమ్ వేగం - అప్‌స్ట్రీమ్ వేగం)/2 = (12 - 6)/2 = 3 కి.మీ/గం."),

        ("t3_q37", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "In a transport yard, the ratio of trucks to buses is 7 : 5. If there are 24 more trucks than buses, what is the total number of vehicles?",
         ["120", "144", "160", "180"], 1,
         "Difference = 7x - 5x = 2x = 24 -> x = 12. Total vehicles = 7x + 5x = 12x = 12 * 12 = 144.",
         "నిష్పత్తి 7x : 5x. తేడా 2x = 24 => x = 12. మొత్తం వాహనాలు = 12 * 12 = 144."),

        ("t3_q38", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "If 12 vehicle inspection officers can inspect 72 commercial vehicles in 6 hours, how many vehicles can 8 officers inspect in 9 hours?",
         ["54 vehicles", "64 vehicles", "72 vehicles", "80 vehicles"], 2,
         "(M1 * T1) / W1 = (M2 * T2) / W2 -> (12 * 6) / 72 = (8 * 9) / W2 -> 72 / 72 = 72 / W2 -> W2 = 72 vehicles.",
         "(12 * 6) / 72 = (8 * 9) / W2 => 1 = 72 / W2 => W2 = 72 వాహనాలు."),

        ("t3_q39", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "What is the angle between the hour hand and the minute hand of a clock at 3:40?",
         ["120 degrees", "130 degrees", "140 degrees", "150 degrees"], 1,
         "Angle = |30*H - 5.5*M| = |30(3) - 5.5(40)| = |90 - 220| = 130 degrees.",
         "కోణం సూత్రం = |30*H - 5.5*M| = |30(3) - 5.5(40)| = |90 - 220| = 130 డిగ్రీలు."),

        ("t3_q40", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "If January 1 of a non-leap year is a Monday, what day of the week will December 31 of the same year be?",
         ["Sunday", "Monday", "Tuesday", "Wednesday"], 1,
         "A non-leap year has 365 days (52 weeks + 1 day). Hence, the year ends on the same day it begins (Monday).",
         "సాధారణ సంవత్సరంలో 365 రోజులు ఉంటాయి కాబట్టి సంవత్సరం ఏ వారంతో మొదలవుతుందో అదే వారంతో ముగుస్తుంది (సోమవారం)."),

        ("t3_q41", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "Pointing to a photograph, a transport officer says: 'Her mother is the only daughter of my mother.' How is the officer related to the girl in the photo (assuming officer is male)?",
         ["Brother", "Father", "Maternal Uncle", "Grandfather"], 2,
         "'Only daughter of my mother' is the officer's sister. Her mother is the officer's sister, making the officer her Maternal Uncle.",
         "'నా తల్లి యొక్క ఏకైక కుమార్తె' అంటే అధికారి సోదరి. ఆమె కుమార్తెకు అధికారి మేనమామ (Maternal Uncle) అవుతారు."),

        ("t3_q42", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "Complete the series: 4, 9, 25, 49, 121, ?",
         ["144", "169", "196", "225"], 1,
         "Series of squares of prime numbers: 2^2, 3^2, 5^2, 7^2, 11^2, 13^2 = 169.",
         "ప్రధాన సంఖ్యల వర్గాలు: 2^2, 3^2, 5^2, 7^2, 11^2, 13^2 = 169."),

        ("t3_q43", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "In a code language, DIESEL is written as 'FLGUGN'. How is PETROL written in that code?",
         ["RGTTRN", "RGVTQN", "QFUCPM", "RGVTRP"], 1,
         "Each letter is shifted by +2 positions: P(+2)=R, E(+2)=G, T(+2)=V, R(+2)=T, O(+2)=Q, L(+2)=N -> RGVTQN.",
         "ప్రతి అక్షరం +2 స్థానాలు ముందుకు మార్చబడింది: P→R, E→G, T→V, R→T, O→Q, L→N => RGVTQN."),

        ("t3_q44", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "Statements: All trucks are vehicles. All vehicles have wheels. Conclusion I: All trucks have wheels. Conclusion II: Some wheels are vehicles.",
         ["Only Conclusion I follows", "Only Conclusion II follows", "Both Conclusions I and II follow", "Neither follows"], 2,
         "Standard syllogism: All A are B, all B are C -> All A are C (valid) and Some C are B (valid). Both follow.",
         "రెండు తీర్మానాలు సరైనవే (ట్రక్కులన్నీ చక్రాలు కలిగి ఉంటాయి మరియు కొన్ని చక్రాలు వాహనాలు)."),

        ("t3_q45", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "A vehicle travels 20 km North, turns right and travels 15 km, then turns right again and travels 20 km. How far and in which direction is the vehicle from its starting point?",
         ["15 km East", "15 km West", "25 km North-East", "35 km South"], 0,
         "North 20 km, East 15 km, South 20 km -> The North and South cancel out, leaving the vehicle 15 km East of starting point.",
         "ఉత్తరానికి 20 కి.మీ, కుడివైపునకు 15 కి.మీ, మళ్లీ కుడివైపునకు 20 కి.మీ ప్రయాణిస్తే ప్రారంభ స్థానం నుండి 15 కి.మీ తూర్పున ఉంటుంది."),

        ("t3_q46", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "In a pie chart representing transport fleet composition, buses occupy 72 degrees. What percentage of the total fleet do buses represent?",
         ["15%", "20%", "25%", "30%"], 1,
         "In a circle of 360 degrees, Percentage = (72 / 360) * 100 = 20%.",
         "వృత్తంలో మొత్తం 360 డిగ్రీలు. శాతం = (72 / 360) * 100 = 20%."),

        ("t3_q47", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "Find the odd one out among the following transport units:",
         ["Bicycle", "Electric Scooter", "Auto-Rickshaw", "Heavy Truck"], 0,
         "Bicycle is non-motorized (human-powered), whereas the other three are motorized transport vehicles.",
         "సైకిల్ మానవ చోదిత వాహనం (మోటారు లేనిది), మిగిలిన మూడు మోటారు వాహనాలు."),

        ("t3_q48", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "A transport inspector scores 70% in Test 1 (out of 100) and 80% in Test 2 (out of 150). What is his aggregate combined percentage across both tests?",
         ["74%", "76%", "75%", "78%"], 1,
         "Marks in Test 1 = 70. Marks in Test 2 = 80% of 150 = 120. Total = 190 / 250 = 76%.",
         "మొదటి పరీక్షలో 70, రెండో పరీక్షలో 120. మొత్తం = 190 / 250 = 76%."),

        ("t3_q49", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "If A is the father of B, but B is not the son of A, what is the relationship of B to A?",
         ["Daughter", "Grandson", "Nephew", "Brother"], 0,
         "If A is the father and B is not the son, B must be the daughter.",
         "A తండ్రి అయినప్పుడు, B కుమారుడు కాకపోతే B తప్పనిసరిగా కుమార్తె (Daughter) అవుతుంది."),

        ("t3_q50", "mock_test_03", 1, "p1-u9", "Mental Ability & Quantitative Aptitude",
         "What is the missing term in the alphabet sequence: Z, X, V, T, R, ?",
         ["P", "O", "Q", "N"], 0,
         "Pattern: Decreasing by -2 alphabetical positions (26, 24, 22, 20, 18, 16 -> P).",
         "అక్షరాలు 2 స్థానాలు వెనుకకు తగ్గుతున్నాయి: Z, X, V, T, R, P.")
    ]
    return science_data

print("Test 3 builder ready.")
