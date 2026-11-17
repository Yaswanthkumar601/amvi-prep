# -*- coding: utf-8 -*-
"""
Generates Questions for Test 1 to Test 5 (250 questions total, 50 per test).
"""

def get_test_1_questions():
    q = []
    # Test 1: Paper-I Comprehensive General Studies (50 Qs)
    # Topics: Polity (1-10), History of AP (11-20), Geography (21-30), Economy & Env (31-40), Science & Mental Ability (41-50)
    items = [
        # 1-10 Polity
        ("t1_q01", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "Under which Article of the Indian Constitution can a High Court issue prerogative writs for the enforcement of Fundamental Rights and for any other legal purpose?",
         ["Article 32", "Article 226", "Article 131", "Article 143"], 1,
         "Article 226 empowers High Courts to issue writs for Fundamental Rights and ordinary legal rights, giving it broader scope than Article 32.",
         "ఆర్టికల్ 226 హైకోర్టులకు ప్రాథమిక హక్కులతో పాటు ఇతర చట్టపరమైన హక్కుల పరిరక్షణకు రిట్‌లను జారీ చేసే అధికారాన్ని కల్పిస్తుంది."),

        ("t1_q02", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "Which Article of the Constitution guarantees equality before the law and equal protection of the laws within the territory of India?",
         ["Article 14", "Article 19", "Article 21", "Article 25"], 0,
         "Article 14 guarantees equality before the law (British concept) and equal protection of the laws (American concept).",
         "ఆర్టికల్ 14 చట్టం ముందు అందరూ సమానులే మరియు చట్టం ద్వారా సమాన రక్షణను ప్రసాదిస్తుంది."),

        ("t1_q03", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "Under which Article is the right to life and personal liberty protected, which has been interpreted to include right to clean environment and privacy?",
         ["Article 14", "Article 19", "Article 21", "Article 32"], 2,
         "Article 21 guarantees that no person shall be deprived of his life or personal liberty except according to procedure established by law.",
         "ఆర్టికల్ 21 జీవించే హక్కు మరియు వ్యక్తిగత స్వేచ్ఛను పరిరక్షిస్తుంది."),

        ("t1_q04", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "Which writ is issued by a superior court to prevent an inferior court or tribunal from exceeding its statutory jurisdiction?",
         ["Mandamus", "Prohibition", "Certiorari", "Quo-Warranto"], 1,
         "The writ of Prohibition is an un-erring preventive order issued by a higher court to prevent lower courts from exceeding jurisdiction.",
         "ప్రోహిబిషన్ రిట్ ద్వారా దిగువ కోర్టులు తమ అధికార పరిధిని మించకుండా ఉన్నత న్యాయస్థానాలు నిరోధిస్తాయి."),

        ("t1_q05", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "Under Article 72, who holds the constitutional power to grant pardons, reprieves, respites or remissions of punishment for court martial sentences?",
         ["Prime Minister", "Chief Justice of India", "President of India", "Attorney General"], 2,
         "Article 72 vests the President of India with pardoning powers including death sentences and court-martial verdicts.",
         "ఆర్టికల్ 72 ప్రకారం భారత రాష్ట్రపతికి మాత్రమే క్షమాభిక్ష ప్రసాదించే పూర్తి రాజ్యాంగ అధికారం ఉంటుంది."),

        ("t1_q06", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "Which Directive Principle of State Policy (DPSP) under Article 50 directs the State to separate the judiciary from the executive?",
         ["Article 44", "Article 45", "Article 50", "Article 51"], 2,
         "Article 50 directs the state to separate the judiciary from the executive in public services.",
         "ఆర్టికల్ 50 న్యాయవ్యవస్థను కార్యనిర్వాహక వ్యవస్థ నుండి వేరు చేయాలని నిర్దేశిస్తుంది."),

        ("t1_q07", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "Under Article 324, the superintendence, direction, and control of elections to Parliament and State Legislatures is vested in:",
         ["Union Ministry of Law", "Supreme Court of India", "Election Commission of India", "NITI Aayog"], 2,
         "Article 324 provides for the independent constitutional authority of the Election Commission of India.",
         "ఆర్టికల్ 324 ప్రకారం ఎన్నికల నిర్వహణ మరియు నియంత్రణ అధికారాలు భారత ఎన్నికల సంఘానికి ఉన్నాయి."),

        ("t1_q08", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "Under which Article can the President proclaim President's Rule in a State on receipt of a report from the Governor regarding constitutional failure?",
         ["Article 352", "Article 356", "Article 360", "Article 365"], 1,
         "Article 356 empowers the President to impose President's Rule if governance cannot be carried on in accordance with the Constitution.",
         "రాష్ట్రాలలో రాజ్యాంగ యంత్రాంగం విఫలమైనప్పుడు ఆర్టికల్ 356 కింద రాష్ట్రపతి పాలన విధిస్తారు."),

        ("t1_q09", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "The 73rd Constitutional Amendment Act, 1992 added which Schedule containing 29 functional items for Panchayati Raj Institutions?",
         ["9th Schedule", "10th Schedule", "11th Schedule", "12th Schedule"], 2,
         "The 73rd Amendment inserted Part IX and the 11th Schedule containing 29 subjects for Panchayati Raj bodies.",
         "73వ రాజ్యాంగ సవరణ ద్వారా పంచాయతీల కోసం 29 అధికారాలతో కూడిన 11వ షెడ్యూల్‌ను చేర్చారు."),

        ("t1_q10", "mock_test_01", 1, "p1-u5", "Indian Polity & Governance",
         "The 74th Constitutional Amendment Act, 1992 added which Schedule containing 18 functional items for Urban Local Bodies (Municipalities)?",
         ["10th Schedule", "11th Schedule", "12th Schedule", "8th Schedule"], 2,
         "The 74th Amendment inserted Part IXA and the 12th Schedule containing 18 functional subjects for Municipalities.",
         "74వ రాజ్యాంగ సవరణ పట్టణ స్థానిక సంస్థల కోసం 18 అంశాలు గల 12వ షెడ్యూల్‌ను రాజ్యాంగంలో చేర్చింది."),

        # 11-20 History of AP
        ("t1_q11", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "Whose historic tour of coastal Andhra in April 1907 catalyzed the widespread Vandemataram student movement in Rajahmundry?",
         ["Lala Lajpat Rai", "Bal Gangadhar Tilak", "Bipin Chandra Pal", "Aurobindo Ghosh"], 2,
         "Bipin Chandra Pal toured Rajahmundry and Machilipatnam in 1907, sparking the famous Rajahmundry College student defiance led by Gadicherla.",
         "1907లో బిపిన్ చంద్రపాల్ ఆంధ్ర పర్యటన రాజమండ్రిలో వందేమాతరం విద్యార్థి ఉద్యమానికి నాంది పలికింది."),

        ("t1_q12", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "The Chirala-Perala non-violent municipal tax boycott in 1921, leading to the creation of Ramnagar, was led by which charismatic leader?",
         ["Tanguturi Prakasam Pantulu", "Duggirala Gopalakrishnayya ('Andhra Ratna')", "Konda Venkatappaiah", "Bhogaraju Pattabhi Sitaramayya"], 1,
         "Andhra Ratna Duggirala Gopalakrishnayya led the historic Chirala-Perala evacuation to Ramnagar protesting municipal taxation.",
         "చీరాల-పేరాల పన్నుల వ్యతిరేక పోరాటాన్ని 'ఆంధ్ర రత్న' దుగ్గిరాల గోపాలకృష్ణయ్య గారు నడిపించారు."),

        ("t1_q13", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "The armed Rampa Rebellion (1922-1924) in the Agency forests of Godavari and Visakhapatnam was led by which immortal hero?",
         ["Komaram Bheem", "Alluri Sitarama Raju ('Manyam Veerudu')", "Uyyalawada Narasimha Reddy", "Birsa Munda"], 1,
         "Manyam Veerudu Alluri Sitarama Raju waged a guerrilla uprising against British 1882 forest oppression until his martyrdom in May 1924.",
         "మన్యం వీరుడు అల్లూరి సీతారామరాజు బ్రిటీష్ అటవీ దోపిడీకి వ్యతిరేకంగా రంపా విప్లవాన్ని నడిపించారు."),

        ("t1_q14", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "The Pedanandipadu No-Tax Campaign during the Non-Cooperation movement in Guntur district was organized by:",
         ["Parvataneni Veeraiah Chowdary", "Tanguturi Prakasam", "Kalluri Subba Rao", "Potti Sreeramulu"], 0,
         "Parvataneni Veeraiah Chowdary led the legendary Pedanandipadu tax-refusal campaign in Guntur in 1921-22.",
         "గుంటూరు జిల్లా పెదనందిపాడు పన్నుల నిరాకరణ ఉద్యమాన్ని పర్వతనేని వీరయ్య చౌదరి నడిపించారు."),

        ("t1_q15", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "Where was the first Andhra Mahasabha session held in May 1913, demanding separate provincial status for Telugu speakers?",
         ["Vijayawada", "Bapatla", "Guntur", "Rajahmundry"], 1,
         "The first Andhra Mahasabha convened at Bapatla in May 1913 under the chairmanship of Bayya Narasimheswara Sarma.",
         "మొదటి ఆంధ్ర మహాసభ 1913 మేలో బాపట్లలో బి.ఎన్. శర్మ అధ్యక్షతన జరిగింది."),

        ("t1_q16", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "Amarajeevi Potti Sreeramulu undertook an epic hunger strike of how many days resulting in his martyrdom on December 15, 1952?",
         ["45 days", "50 days", "58 days", "64 days"], 2,
         "Potti Sreeramulu fasted for 58 consecutive days (19 Oct to 15 Dec 1952) for Andhra Statehood.",
         "అమరజీవి పొట్టి శ్రీరాములు గారు 58 రోజుల పాటు ఆమరణ నిరాహార దీక్ష చేసి అమరులయ్యారు."),

        ("t1_q17", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "On which historic date was the separate linguistic Andhra State officially inaugurated with Kurnool as its capital?",
         ["August 15, 1947", "January 26, 1950", "October 1, 1953", "November 1, 1956"], 2,
         "Andhra State was inaugurated on October 1, 1953 with Kurnool as capital by Prime Minister Jawaharlal Nehru.",
         "1953 అక్టోబర్ 1న కర్నూలు రాజధానిగా తొలి భాషా ప్రయుక్త ఆంధ్ర రాష్ట్రం అవతరించింది."),

        ("t1_q18", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "Who served as the first Chief Minister of the newly formed Andhra State in 1953?",
         ["Tanguturi Prakasam Pantulu ('Andhra Kesari')", "Neelam Sanjiva Reddy", "Burgula Ramakrishna Rao", "Bhavanam Venkataram"], 0,
         "Andhra Kesari Tanguturi Prakasam Pantulu took oath as the first Chief Minister of Andhra State at Kurnool in 1953.",
         "ఆంధ్ర కేసరి టంగుటూరి ప్రకాశం పంతులు గారు తొలి ఆంధ్ర రాష్ట్ర ముఖ్యమంత్రిగా ప్రమాణ స్వీకారం చేశారు."),

        ("t1_q19", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "The Gentlemen's Agreement that paved the way for the formation of Andhra Pradesh on November 1, 1956 was signed in which city?",
         ["Madras", "Hyderabad", "New Delhi", "Kurnool"], 2,
         "The Gentlemen's Agreement was signed at Hyderabad House in New Delhi on 20 February 1956.",
         "పెద్దమనుషుల ఒప్పందం 1956 ఫిబ్రవరి 20న న్యూఢిల్లీలో కుదిరింది."),

        ("t1_q20", "mock_test_01", 1, "p1-u4", "Modern Indian & AP History",
         "Who pioneered the Telugu social renaissance by performing the first widow remarriage in 1881 and establishing Rajahmundry Social Reform Association?",
         ["Gurajada Apparao", "Kandukuri Veeresalingam Pantulu", "Gidugu Ramamurthy", "Komarraju Lakshmana Rao"], 1,
         "Kandukuri Veeresalingam Pantulu is revered as the father of Telugu social renaissance for his crusade against social evils.",
         "కందుకూరి వీరేశలింగం పంతులు గారు 1881లో మొదటి వితంతు పునర్వివాహం జరిపించి సాంఘిక విప్లవానికి నాంది పలికారు."),

        # 21-30 Geography of AP
        ("t1_q21", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "The Dowleswaram Barrage across the river Godavari, which transformed the Godavari delta, was engineered by:",
         ["Sir Arthur Cotton", "Major General William Roxburgh", "Lord Curzon", "Colonel Colin Mackenzie"], 0,
         "Sir Arthur Cotton constructed the Dowleswaram Barrage (1847-1852), transforming the delta into the rice bowl of Andhra.",
         "సర్ ఆర్థర్ కాటన్ దవళేశ్వరం వద్ద గోదావరి నదిపై ఆనకట్ట నిర్మించి డెల్టాను సస్యశ్యామలం చేశారు."),

        ("t1_q22", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "The Krishna River discharges into the Bay of Bengal through multiple distributary streams at which geographic location in AP?",
         ["Antarvedi", "Hamsaladeevi", "Bapatla", "Kalingapatnam"], 1,
         "Krishna River meets the Bay of Bengal at Hamsaladeevi in Krishna district.",
         "కృష్ణా నది హంసలదీవి వద్ద బంగాళాఖాతంలో కలుస్తుంది (గోదావరి అంతర్వేది వద్ద కలుస్తుంది)."),

        ("t1_q23", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "Where does the Penna River, which drains the arid Rayalaseema districts, originate?",
         ["Mahabaleshwar", "Nandi Hills (Karnataka)", "Trimbakeshwar", "Brahmagiri Hills"], 1,
         "Penna River originates in Nandi Hills in Chikkaballapur, Karnataka and flows through Anantapur, Kadapa and Nellore.",
         "పెన్నా నది కర్ణాటకలోని నంది కొండలలో జన్మించి రాయలసీమ మీదుగా ప్రవహిస్తుంది."),

        ("t1_q24", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "Which premier port in Andhra Pradesh is a natural landlocked harbour shielded by the 'Dolphin's Nose' promontory?",
         ["Machilipatnam", "Visakhapatnam Port", "Krishnapatnam", "Kakinada"], 1,
         "Visakhapatnam Port is a natural deep-water harbour protected by the Dolphin's Nose hill projection.",
         "విశాఖపట్నం సహజ సిద్ధమైన లోతైన నౌకాశ్రయం, ఇది డాల్ఫిన్స్ నోస్ కొండ రక్షణలో ఉంది."),

        ("t1_q25", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "In which district of Andhra Pradesh is the privately operated Krishnapatnam deep-water port situated?",
         ["Prakasam", "SPSR Nellore", "Guntur", "West Godavari"], 1,
         "Krishnapatnam Port is an all-weather deep-water port in SPSR Nellore district.",
         "కృష్ణపట్నం పోర్టు ఎస్పీఎస్ఆర్ నెల్లూరు జిల్లాలో ఉంది."),

        ("t1_q26", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "Mangampet in YSR Kadapa district of Andhra Pradesh is globally famous for hosting single-deposit reserves of which mineral?",
         ["Bauxite", "Barytes (Barium Sulphate)", "Mica", "Graphite"], 1,
         "Mangampet contains one of the world's largest single deposits of bedded Barytes, essential for oil drilling muds.",
         "మంగంపేట ప్రపంచంలోనే అతిపెద్ద 'బెరైటీస్' (Barytes) ఖనిజ నిల్వలకు ప్రసిద్ధి చెందింది."),

        ("t1_q27", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "Which endemic valuable timber tree species with reddish-brown wood is strictly protected in the Seshachalam biosphere reserve?",
         ["Teak", "Red Sanders (Pterocarpus santalinus)", "Rosewood", "Sal"], 1,
         "Red Sanders is endemic to the Seshachalam hill tracts of Kadapa, Chittoor, and Nellore districts.",
         "ఎర్రచందనం (Red Sanders) శేషాచలం కొండలలో మాత్రమే పెరిగే అరుదైన వృక్షజాతి."),

        ("t1_q28", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "What is the total approximate length of the mainland coastline of Andhra Pradesh, ranking second longest in India?",
         ["750 km", "850 km", "974 km", "1050 km"], 2,
         "Andhra Pradesh has approximately 974 km of coastline, second only to Gujarat.",
         "ఆంధ్రప్రదేశ్ దాదాపు 974 కి.మీ పొడవైన సముద్ర తీరాన్ని కలిగి ఉండి దేశంలో రెండవ స్థానంలో ఉంది."),

        ("t1_q29", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "The scenic hill station of Araku Valley in Andhra Pradesh is situated in which mountain range?",
         ["Western Ghats", "Eastern Ghats", "Satpura Range", "Vindhya Range"], 1,
         "Araku Valley is situated in the Eastern Ghats in Alluri Sitarama Raju (formerly Visakhapatnam) district.",
         "అరకు లోయ తూర్పు కనుమలలో (Eastern Ghats) ఉన్న అందమైన పర్వత ప్రాంతం."),

        ("t1_q30", "mock_test_01", 1, "p1-u7", "Geography of India & AP",
         "Which major river system enters Andhra Pradesh near Bhairavunipadu and splits into Gautami and Vasishta distributaries?",
         ["Krishna", "Penna", "Godavari", "Tungabhadra"], 2,
         "Godavari River splits into the Gautami and Vasishta distributaries in the delta region before joining the sea.",
         "గోదావరి నది గౌతమి, వశిష్ఠ తదితర శాఖలుగా చీలి బంగాళాఖాతంలో కలుస్తుంది."),

        # 31-40 Economy & Environment
        ("t1_q31", "mock_test_01", 1, "p1-u6", "Indian & AP Economy",
         "On which date was NITI Aayog established by the Union Cabinet, replacing the erstwhile Planning Commission?",
         ["January 1, 2014", "January 1, 2015", "August 15, 2015", "April 1, 2016"], 1,
         "NITI Aayog (National Institution for Transforming India) was constituted on January 1, 2015.",
         "ప్రణాళికా సంఘం స్థానంలో నీతి ఆయోగ్ 2015 జనవరి 1న ఏర్పాటయింది."),

        ("t1_q32", "mock_test_01", 1, "p1-u6", "Indian & AP Economy",
         "Which Constitutional Amendment Act introduced the nationwide Goods and Services Tax (GST) effective from July 1, 2017?",
         ["99th Amendment", "100th Amendment", "101st Amendment", "103rd Amendment"], 2,
         "The 101st Constitutional Amendment Act, 2016 instituted the dual GST architecture.",
         "101వ రాజ్యాంగ సవరణ చట్టం ద్వారా దేశంలో జీఎస్టీ (GST) వ్యవస్థ అమల్లోకి వచ్చింది."),

        ("t1_q33", "mock_test_01", 1, "p1-u6", "Indian & AP Economy",
         "Under Article 279A, who chairs the constitutional Goods and Services Tax (GST) Council?",
         ["Prime Minister", "Union Finance Minister", "Governor of RBI", "Cabinet Secretary"], 1,
         "The GST Council is chaired by the Union Finance Minister with state finance ministers as members.",
         "ఆర్టికల్ 279A కింద ఏర్పాటైన జీఎస్టీ కౌన్సిల్‌కు కేంద్ర ఆర్థిక మంత్రి అధ్యక్షత వహిస్తారు."),

        ("t1_q34", "mock_test_01", 1, "p1-u6", "Indian & AP Economy",
         "The Monetary Policy Committee (MPC) of RBI targets Consumer Price Index (CPI) retail inflation at what percentage within a tolerance band?",
         ["3% (+/- 1%)", "4% (+/- 2%)", "5% (+/- 2%)", "6% (+/- 1%)"], 1,
         "The statutory inflation target set by the Government for the RBI MPC is 4% with a tolerance band of +/- 2%.",
         "ఆర్బీఐ ద్రవ్య విధాన కమిటీ రిటైల్ ద్రవ్యోల్బణాన్ని 4% (+/- 2%) వద్ద నియంత్రించాలని నిర్దేశించారు."),

        ("t1_q35", "mock_test_01", 1, "p1-u6", "Indian & AP Economy",
         "Which major industrial corridor passing through coastal Andhra Pradesh is co-financed by the Asian Development Bank (ADB)?",
         ["Delhi-Mumbai Industrial Corridor (DMIC)", "Vizag-Chennai Industrial Corridor (VCIC)", "Amritsar-Kolkata Corridor (AKIC)", "Hyderabad-Nagpur Corridor"], 1,
         "Vizag-Chennai Industrial Corridor (VCIC) is India's first coastal industrial corridor, funded partly by ADB.",
         "విశాఖ-చెన్నై పారిశ్రామిక కారిడార్ (VCIC) కు ఆసియా అభివృద్ధి బ్యాంక్ (ADB) ఆర్థిక సహాయం అందిస్తోంది."),

        ("t1_q36", "mock_test_01", 1, "p1-u8", "Disaster Management & Environment",
         "Under Section 14 of the Disaster Management Act, 2005, who is the ex-officio Chairperson of the State Disaster Management Authority (SDMA)?",
         ["State Governor", "Chief Minister of the State", "Chief Secretary", "Director General of Police"], 1,
         "The Chief Minister of the State is the ex-officio Chairperson of the State Disaster Management Authority (SDMA).",
         "రాష్ట్ర విపత్తు నిర్వహణ అథారిటీ (SDMA) కి రాష్ట్ర ముఖ్యమంత్రి గారే ఛైర్మన్‌గా ఉంటారు."),

        ("t1_q37", "mock_test_01", 1, "p1-u8", "Disaster Management & Environment",
         "Who is the designated Chairperson of the District Disaster Management Authority (DDMA)?",
         ["District Sessions Judge", "Superintendent of Police", "District Collector / Magistrate", "Zilla Parishad CEO"], 2,
         "Under Section 25, the District Collector/District Magistrate is the ex-officio Chairperson of the DDMA.",
         "జిల్లా విపత్తు నిర్వహణ అథారిటీ (DDMA) కి జిల్లా కలెక్టర్ ఛైర్మన్‌గా వ్యవహరిస్తారు."),

        ("t1_q38", "mock_test_01", 1, "p1-u8", "Disaster Management & Environment",
         "Why is the coastal region of Andhra Pradesh particularly vulnerable to severe Bay of Bengal cyclonic storms?",
         ["High altitude terrain", "Concave coastline curvature, shallow bathymetry and high tidal surges", "Proximity to the equator", "Cold oceanic currents"], 1,
         "The funnel-shaped curvature of Bay of Bengal and shallow sea bed amplify storm surges during cyclones.",
         "బంగాళాఖాతపు వంపు తిరిగిన తీర రేఖ మరియు నిస్సార సముద్రం తుఫాను తాకిడిని మరియు ఉప్పెనలను తీవ్రతరం చేస్తాయి."),

        ("t1_q39", "mock_test_01", 1, "p1-u6", "Indian & AP Economy",
         "Andhra Pradesh leads the nation in exports of which agricultural and allied commodity sector?",
         ["Basmati Rice", "Marine Products & Cultured Shrimp (Aquaculture)", "Wheat", "Tea"], 1,
         "Andhra Pradesh is the undisputed national leader in seafood and cultured Vannamei shrimp aquaculture exports.",
         "ఆక్వాకల్చర్ మరియు రొయ్యల ఎగుమతులలో ఆంధ్రప్రదేశ్ దేశంలోనే అగ్రస్థానంలో ఉంది."),

        ("t1_q40", "mock_test_01", 1, "p1-u8", "Disaster Management & Environment",
         "Under the National Vehicle Scrappage Policy, commercial transport vehicles must undergo automated mandatory fitness testing after how many years?",
         ["8 years", "10 years", "15 years", "20 years"], 2,
         "Commercial transport vehicles must undergo mandatory automated testing after 15 years (20 years for private passenger vehicles).",
         "జాతీయ వాహన స్క్రాపేజ్ విధానం ప్రకారం రవాణా వాహనాలకు 15 సంవత్సరాల తర్వాత ఆటోమేటెడ్ ఫిట్‌నెస్ పరీక్ష తప్పనిసరి."),

        # 41-50 Science & Mental Ability
        ("t1_q41", "mock_test_01", 1, "p1-u3", "General Science & Clean Tech",
         "In an Electric Vehicle (EV), which crucial component monitors cell temperatures, balances voltages and prevents dangerous thermal runaway?",
         ["Traction Inverter", "Battery Management System (BMS)", "Step-Down DC Converter", "Regenerative Resistor"], 1,
         "The BMS manages the state of charge, performs cell balancing, and prevents thermal runaway in lithium battery packs.",
         "బ్యాటరీ మేనేజ్‌మెంట్ సిస్టమ్ (BMS) కణాల ఉష్ణోగ్రత మరియు వోల్టేజ్‌లను సమతుల్యం చేసి బ్యాటరీ పేలకుండా కాపాడుతుంది."),

        ("t1_q42", "mock_test_01", 1, "p1-u3", "General Science & Clean Tech",
         "Which Lithium-ion cell cathode chemistry is renowned for superior thermal stability and long cycle life in commercial EVs?",
         ["Lithium Cobalt Oxide (LCO)", "Lithium Iron Phosphate (LiFePO4 / LFP)", "Lithium Manganese Oxide (LMO)", "Lead Peroxide"], 1,
         "LFP chemistry provides exceptional thermal and chemical stability, minimizing fire risks in commercial transport.",
         "లిథియం ఐరన్ ఫాస్ఫేట్ (LFP) కణాలు అద్భుతమైన ఉష్ణ స్థిరత్వాన్ని మరియు ఎక్కువ జీవిత కాలాన్ని కలిగి ఉంటాయి."),

        ("t1_q43", "mock_test_01", 1, "p1-u3", "General Science & Clean Tech",
         "Automotive Industry Standard 'AIS-140' makes which safety devices legally mandatory on public and commercial transport vehicles in India?",
         ["Rear defoggers", "Vehicle Location Tracking Devices (VLTD) and Emergency Panic Buttons", "Sunroofs", "Cruise control"], 1,
         "AIS-140 mandates real-time GPS tracking devices and emergency panic buttons on transport vehicles.",
         "AIS-140 ప్రకారం రవాణా వాహనాలలో జీపీఎస్ ట్రాకింగ్ పరికరం (VLTD) మరియు ఎమర్జెన్సీ పానిక్ బటన్లు తప్పనిసరి."),

        ("t1_q44", "mock_test_01", 1, "p1-u3", "General Science & Clean Tech",
         "What is the target percentage of ethanol blending in automotive petrol mandated by Government of India under National Biofuel Policy by 2025-26?",
         ["10% (E10)", "20% (E20)", "25% (E25)", "50% (E50)"], 1,
         "The target of achieving 20% ethanol blended petrol (E20) was advanced to the ethanol supply year 2025-26.",
         "2025-26 నాటికి పెట్రోల్‌లో 20% ఇథనాల్ బ్లెండింగ్ (E20) లక్ష్యాన్ని ప్రభుత్వం నిర్దేశించింది."),

        ("t1_q45", "mock_test_01", 1, "p1-u3", "General Science & Clean Tech",
         "In modern vehicles, which high-reliability serial bus protocol allows microcontrollers and sensors to communicate without bulky dedicated wiring?",
         ["USB 3.0", "Controller Area Network (CAN Bus)", "Ethernet Cat5", "RS-232"], 1,
         "CAN Bus protocol enables robust electronic communication among vehicle ECUs and sensors over a twisted pair.",
         "కంట్రోలర్ ఏరియా నెట్‌వర్క్ (CAN Bus) వాహనంలోని ఎలక్ట్రానిక్ సెన్సార్లు మరియు ECU లను వైర్ల రద్దీ లేకుండా అనుసంధానిస్తుంది."),

        ("t1_q46", "mock_test_01", 1, "p1-u9", "Mental Ability & Reasoning",
         "An AMVI inspection vehicle travels from Vijayawada to Eluru at 60 km/h and returns along the same route at 40 km/h. What is the average speed for the round trip?",
         ["50 km/h", "48 km/h", "52 km/h", "45 km/h"], 1,
         "Average Speed = 2xy / (x + y) = (2 * 60 * 40) / 100 = 4800 / 100 = 48 km/h.",
         "సమాన దూరాన్ని ప్రయాణించినప్పుడు సగటు వేగం = (2 * 60 * 40) / 100 = 48 కి.మీ/గం."),

        ("t1_q47", "mock_test_01", 1, "p1-u9", "Mental Ability & Reasoning",
         "A transport inspection bus 150 meters long is travelling at 54 km/h. How many seconds will it take to pass a stationary road milestone post?",
         ["8 seconds", "10 seconds", "12 seconds", "15 seconds"], 1,
         "Speed = 54 * (5/18) = 15 m/s. Time = Distance / Speed = 150 / 15 = 10 seconds.",
         "వేగం = 54 * (5/18) = 15 మీ/సె. పట్టే సమయం = 150 / 15 = 10 సెకన్లు."),

        ("t1_q48", "mock_test_01", 1, "p1-u9", "Mental Ability & Reasoning",
         "If in a code language, BRAKE is coded as 'ESDNH', what is the code for CLUTCH in that language?",
         ["FOXWFK", "EOXWEJ", "FNXVFJ", "FOXWFJ"], 0,
         "Each letter is shifted by +3 positions: C(+3)=F, L(+3)=O, U(+3)=X, T(+3)=W, C(+3)=F, H(+3)=K. Result: FOXWFK.",
         "ప్రతి అక్షరం +3 స్థానాలు పెంచబడింది: C→F, L→O, U→X, T→W, C→F, H→K. కోడ్ FOXWFK."),

        ("t1_q49", "mock_test_01", 1, "p1-u9", "Mental Ability & Reasoning",
         "Find the next number in the vehicle registration series: 3, 7, 15, 31, 63, ?",
         ["95", "112", "127", "131"], 2,
         "Pattern: Each number is (previous * 2) + 1. Hence, 63 * 2 + 1 = 127.",
         "వరుస క్రమం: (మునుపటి సంఖ్య * 2) + 1. కాబట్టి 63 * 2 + 1 = 127."),

        ("t1_q50", "mock_test_01", 1, "p1-u10", "AP Reorganisation Act, 2014",
         "Under Section 90 of the AP Reorganisation Act 2014, which project was declared a 'National Project' with funding execution by the Central Government?",
         ["Nagarjuna Sagar", "Polavaram Irrigation Project", "Srisailam Project", "Veligonda Project"], 1,
         "Section 90 declared the Polavaram Irrigation Project a National Project, executed and financed by the Centre.",
         "సెక్షన్ 90 ప్రకారం పోలవరం ప్రాజెక్టును కేంద్ర నిధులతో కూడిన జాతీయ ప్రాజెక్టుగా ప్రకటించారు.")
    ]
    return items

print("Test 1 builder ready with 50 questions.")

