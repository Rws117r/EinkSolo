import random

# Noble Titles & Historical Terms
NOBLE_TITLES = {
    "Emperor": {
        "Address": "Your Imperial Majesty",
        "Terms": ["Imperator", "Imperatrice", "Maharaja", "Maharini", "Padishah", "Khagan", "Caliph"]
    },
    "King": {
        "Address": "Your Majesty",
        "Terms": ["Rex", "Regina", "Roi", "Reine", "König", "Königen", "Tsar", "Tsarina", "Shah", "Sultan", "Khan"]
    },
    "Archduke": {
        "Address": "Your Highness",
        "Terms": ["Erzherzog", "Archidux"]
    },
    "Grand Duke": {
        "Address": "Your Serene Grace",
        "Terms": ["Magnus Dux", "Grossherzog", "Groothertog"]
    },
    "Sovereign Prince": {
        "Address": "Your Highness",
        "Terms": ["Princeps", "Emir", "Emira", "Sheikh"]
    },
    "Sovereign Duke": {
        "Address": "Your Grace",
        "Terms": ["Dux", "Herzog", "Bey", "Begum"]
    },
    "Crown Prince": {
        "Address": "Your Royal Highness",
        "Terms": ["Atheling"]
    },
    "Prince": {
        "Address": "Your Highness",
        "Terms": ["Prince"]
    },
    "Duke": {
        "Address": "Your Grace",
        "Terms": ["Duke", "Duchess"]
    },
    "Marquess": {
        "Address": "My Lord",
        "Terms": ["Marquess", "Marchioness"]
    },
    "Count": {
        "Address": "My Lord",
        "Terms": ["Count", "Countess", "Earl"]
    },
    "Viscount": {
        "Address": "My Lord",
        "Terms": ["Viscount", "Viscountess"]
    },
    "Baron": {
        "Address": "My Lord",
        "Terms": ["Baron", "Baroness"]
    },
    "Baronet": {
        "Address": "Sir/Lady",
        "Terms": ["Baronet"]
    },
    "Knight": {
        "Address": "Sir/Lady/Dame",
        "Terms": ["Knight"]
    }
}

# Table 27-2: Title Adjective Categories
TITLE_ADJECTIVE_CATS = {
    20: "Admired",
    40: "Capacity and Metaphors",
    60: "Holy or Reverent",
    80: "Luminescent or Distinguished",
    100: "Powerful"
}

# Table 27-3: Admired
ADJECTIVES_ADMIRED = [
    "Admired", "Popular", "Adored", "Prized", "Beliked", "Princely", "Beloved", "Respected",
    "Bereverenced", "Revered", "Cared for", "Treasured", "Cherished", "Venerated", "Dignified",
    "Well-Admired", "Eminent", "Well-Beloved", "Esteemed", "Well-Cherished", "Exalted",
    "Well-Esteemed", "Glorific", "Well-liked", "Glorious", "Well-Loved", "Hallowed",
    "Well-Prized", "Highly regarded", "Well-Regarded", "Highly valued", "Well-Respected",
    "Honored", "Well-Revered", "Idolized", "Well-Treasured", "Loved", "Well-Valued",
    "Peerless", "Well-Venerated"
]

# Table 27-4: Capacity and Metaphors
ADJECTIVES_CAPACITY = [
    "Accordant", "Electric", "Sapphire", "Alert", "Elliptical", "Scholastic", "Attentive",
    "Euphonious", "Sensible", "Autonomous", "Forthright", "Sincere", "Candid", "Harmonic",
    "Solidified", "Careful", "Harmonious", "Sonorous", "Categorical", "Heedful", "Straightforward",
    "Cautious", "Knowing", "Studious", "Cognizant", "Knowledgeable", "Symphonic", "Concerted",
    "Lineal", "Symphonious", "Concordant", "Mellifluous", "Thoughtful", "Concrete", "Melodic",
    "Thunderous", "Conducive", "Melodious", "Unambiguous", "Conductive", "Mindful", "Unconcealed",
    "Conscientious", "Observant", "Undisguised", "Conscious", "Observative", "Unequivocal",
    "Consonant", "Outspoken", "Unreserved", "Conversant", "Plainspoken", "Vigilant",
    "Diamond", "Proximate", "Wary", "Dulcet", "Regardful", "Watchful"
]

# Table 27-5: Holy or Reverent
ADJECTIVES_HOLY = [
    "Angelic", "Goodly", "Sacred", "Beatific", "Hallowed", "Sacrosanct", "Believing", "Holy",
    "Sainted", "Blessed", "Humble", "Saintlike", "Canonical", "Immaculate", "Saintly", "Chaste",
    "Innocent", "Sanctified", "Clerical", "Just", "Sanctimonious", "Consecrated", "Moral",
    "Seraphic", "Dedicated", "Oracular", "Spiritual", "Devoted", "Orthodox", "Sublime",
    "Devotional", "Perfect", "Theological", "Devout", "Pietistic", "Uncorrupt", "Divine",
    "Pious", "Undefiled", "Ecclesiastical", "Prayerful", "Untainted", "Faithful", "Priestly",
    "Unworldly", "Faultless", "Pure", "Upright", "Glorified", "Religious", "Venerable",
    "God-fearing", "Revered", "Venerated", "Godlike", "Reverent", "Virtuous", "Godly",
    "Righteous"
]

# Table 27-6: Luminescent or Distinguished
ADJECTIVES_LUMINESCENT = [
    "Acclaimed", "Imposing", "Radiant", "Aristocratic", "Ineffable", "Remarkable",
    "Arresting", "Inimitable", "Renowned", "Bright", "Iridescent", "Reputable",
    "Brilliant", "Irradiant", "Resplendent", "Celebrated", "Irreplaceable", "Royal",
    "Conspicuous", "Luminant", "Salient", "Coruscant", "Luminous", "Shining",
    "Coruscating", "Lustrant", "Signal", "Dignified", "Lustrous", "Singular",
    "Distinguished", "Marked", "Splendent", "Eminent", "Memorable", "Splendid",
    "Extraordinary", "Noble", "Stately", "Famed", "Notable", "Striking",
    "Fluorescent", "Noted", "Superior", "Gloriant", "Noteworthy", "Unforgettable",
    "Glorious", "Opalescent", "Unique", "Glowing", "Peerless", "Venerable",
    "Honored", "Phosphorescent", "Wondrous", "Illuminated", "Prominent"
]

# Table 27-7: Powerful
ADJECTIVES_POWERFUL = [
    "Able", "Forceful", "Omnipotent", "Authoritative", "Forcible", "Paramount",
    "Capable", "Formidable", "Persuasive", "Cogent", "Great", "Ponderous",
    "Commanding", "Greater", "Potent", "Compelling", "Illustrious", "Powerful",
    "Competent", "Important", "Preeminent", "Convincing", "Imposing", "Prevailing",
    "Dangerous", "Impressive", "Prominent", "Daunting", "Influential", "Puissant",
    "Dire", "Inscrutable", "Robust", "Dominant", "Inspiring", "Ruthless",
    "Dominating", "Instrumental", "Significant", "Dread", "Intimidating", "Sovereign",
    "Effectual", "Leading", "Strong", "Efficacious", "Meaningful", "Substantial",
    "Energetic", "Menacing", "Supreme", "Famous", "Mighty", "Telling",
    "Ferocious", "Momentous", "Unprofaned", "Fierce", "Monumental", "Weighty"
]

# Table 27-8 & 27-9: Nouns of Majesty
NOUNS_MAJESTY = [
    "Aristocracy", "Conversance", "Fluorescence", "Infamy",
    "Attentiveness", "Coruscation", "Forcefulness", "Influence",
    "Authority", "Deadliness", "Formidability", "Inimitability",
    "Beatitude", "Dedication", "Forthrightness", "Innocence",
    "Belief", "Devotion", "Gloriance", "Inscrutability",
    "Blessing", "Dignity", "Gloriousness", "Inspiration",
    "Brightness", "Distinguishment", "Glory", "Instrumentality",
    "Brilliance", "Divinity", "Godliness", "Intimidation",
    "Capability", "Dominance", "Goodliness", "Iridescence",
    "Celebration", "Domination", "Greatness", "Irradiance",
    "Chasteness", "Dreadfulness", "Harmony", "Irreplaceability",
    "Chastity", "Effectuality", "Heedfulness", "Justice",
    "Cogence", "Efficaciousness", "Holiness", "Knowledge",
    "Cognizance", "Eminence", "Honor", "Leadership",
    "Commandment", "Euphoniousness", "Humility", "Luminance",
    "Competence", "Exaltation", "Illumination", "Luminousness",
    "Compulsion", "Faithfulness", "Illustriousness", "Lustrance",
    "Conduciveness", "Fame", "Importance", "Lustrousness",
    "Consecration", "Ferocity", "Imposition", "Magnificence",
    "Conspicuousness", "Fierceness", "Ineffability", "Magnitude",
    # Table 27-9
    "Meaningfulness", "Piety", "Sacredness", "Superiority",
    "Melodiousness", "Piousness", "Sacristy", "Supremacy",
    "Memory", "Ponderousness", "Saintliness", "Theology",
    "Menace", "Potency", "Salience", "Thunderousness",
    "Mightiness", "Prayerfulness", "Sanctimony", "Ultimacy",
    "Mindfulness", "Preeminence", "Sanctity", "Uncorruptability",
    "Momentousness", "Priestliness", "Sensibility", "Unforgettability",
    "Monumentality", "Prominence", "Significance", "Uniqueness",
    "Morality", "Proximacy", "Sincerity", "Unprofanity",
    "Nobility", "Puissance", "Singularity", "Untaintedness",
    "Noteworthiness", "Purity", "Solidarity", "Unworldliness",
    "Omnipotence", "Radiance", "Sonorousness", "Uprightness",
    "Opalescence", "Remarkability", "Sovereignty", "Venerability",
    "Orthodoxy", "Reputability", "Spirituality", "Veneration",
    "Paramountcy", "Resplendence", "Splendence", "Vigilance",
    "Peerlessness", "Perfectability", "Stateliness", "Virtue",
    "Perfection", "Reverence", "Strength", "Watchfulness", 
    "Persuasiveness", "Righteousness", "Robustness", "Sublimity",
    "Wondrousness", "Phosphorescence", "Ruthlessness", "Substantiality",
    "Worshipfulness", "Weightiness"
]

# Table 27-10: Tyrannical Title Adjective
ADJECTIVES_TYRANNICAL = [
    "Baleful", "Obdurate", "Barbarous", "Pitiless", "Bloody", "Relentless",
    "Callous", "Rigorous", "Cruel", "Ruthless", "Dangerous", "Sanguinary",
    "Daunting", "Savage", "Dire", "Shameless", "Ferocious", "Terrifying",
    "Fierce", "Tyrannical", "Forbidding", "Uncompassionate", "Grim", "Uncontrite",
    "Hard", "Unforgiving", "Hardened", "Unmerciful", "Harsh", "Unregenerate",
    "Impenitent", "Unrelenting", "Implacable", "Unremitting", "Inexorable", "Unrepenting",
    "Intolerant", "Unyielding", "Merciless", "Vindictive"
]

# Table 27-11: Noun of Wickedness
NOUNS_WICKEDNESS = [
    "Abomination", "Malignity", "Amorality", "Nefariousness", "Atrociousness", "Offensiveness",
    "Atrocity", "Perilousness", "Awfulness", "Profanity", "Baseness", "Scandalousness",
    "Degeneracy", "Severity", "Depravity", "Shame", "Dreadfulness", "Shamefulness",
    "Egregiousness", "Shamelessness", "Fiendishness", "Sinfulness", "Foulness", "Treacherousness",
    "Harmfulness", "Unpleasantness", "Heartlessness", "Unrighteousness", "Heinousness", "Viciousness",
    "Immorality", "Impiety", "Vileness", "Impiousness", "Villainousness", "Indecency",
    "Waywardness", "Iniquity", "Wickedness"
]

def _get_from_dict(d, roll):
    keys = sorted(d.keys())
    for k in keys:
        if roll <= k:
            return d[k]
    return d[keys[-1]]

def generate_mode_of_address(gender="His", m_type="Ordinary"):
    if m_type == "Ordinary":
        # Category
        cat_roll = random.randint(1, 100)
        cat = _get_from_dict(TITLE_ADJECTIVE_CATS, cat_roll)
        
        # Adjective
        if cat == "Admired": adj = random.choice(ADJECTIVES_ADMIRED)
        elif cat == "Capacity and Metaphors": adj = random.choice(ADJECTIVES_CAPACITY)
        elif cat == "Holy or Reverent": adj = random.choice(ADJECTIVES_HOLY)
        elif cat == "Luminescent or Distinguished": adj = random.choice(ADJECTIVES_LUMINESCENT)
        else: adj = random.choice(ADJECTIVES_POWERFUL)
        
        # Noun
        noun = random.choice(NOUNS_MAJESTY)
        
    elif m_type == "Tyrant":
        adj = random.choice(ADJECTIVES_TYRANNICAL)
        noun = random.choice(["Majesty", "Highness", "Grace"] + NOUNS_MAJESTY[:20]) # Limit to some nouns
        
    else: # Wicked
        # Adjective from Ordinary Cat or Tyrannical
        if random.randint(1, 2) == 1:
            adj = random.choice(ADJECTIVES_TYRANNICAL)
        else:
            adj = random.choice(ADJECTIVES_POWERFUL + ADJECTIVES_LUMINESCENT)
        noun = random.choice(NOUNS_WICKEDNESS)
        
    return f"{gender} {adj} {noun}"
