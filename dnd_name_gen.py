'''Allow user via CLI to select a race and gender to create a randomized
    Dungeons & Dragons character name.
    Currently, this is only for PHB Dungeons & Dragons 5th edition classes.'''
import sys
import random

# A replacement for these could be to use the public dnd5e API
# Although, I'm not sure if it has all of the names listed in the Player's Handbook...
first_names = {
    "dragonborn": {
        "male": [
            "Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadarr", "Pandjed", "Patrin", "Rhogar", "Shamash", "Shedinn", "Tarhun", "Torinn"],
        "female": [
            "Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Jheri", "Kava", "Korinn", "Mishann", "Nala", "Perra", "Raiann", "Sora", "Surina", "Thava", "Uadjit"]},
    "dwarf": {
        "male": [
            "Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"],
        "female": [
            "Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra"]},
    "elf": {
        "male": [
            "Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"],
        "female": [
            "Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"]},
    "gnome": {
        "male": [
            "Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug", "Gerbo", "Gimble", "Glim", "Jebeddo", "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo", "Sindri", "Warryn", "Wrenn", "Zook"],
        "female": [
            "Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli", "Loopmottin", "Lorilla", "Mardnab", "Nissa", "Nyx", "Oda", "Orla", "Roywyn", "Shamil", "Tana", "Waywocket", "Zanna"]},
    "halfling": {
        "male": [
            "Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"],
        "female": [
            "Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"]},
    "half-orc": {
        "male": [
            "Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Mhurren", "Ront", "Shump", "Thokk"],
        "female": [
            "Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Sutha", "Vola", "Volen", "Yevelda"]},
    "human": {
        "male": [
            "Bor", "Fodel", "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor", "Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth", "Aoth", "Bareris", "Ehput-Ki", "Kethoth", "Mumed", "Ramas", "So-Kehur", "Thazar-De", "Urhur", "Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar", "Vladislak", "An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui", "Wen; (female) Bai", "Chao", "Jia", "Lei", "Mei", "Qiao", "Shui", "Tai", "Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"],
        "female": [
            "Atala", "Ceidil", "Hama", "Jasmal", "Meilil", "Seipora", "Yasheira", "Zasheida", "Arveene", "Esvele", "Jhessail", "Kerri", "Lureene", "Miri", "Rowan", "Shandri", "Tessele", "Alethra", "Kara", "Katernin", "Mara", "Natali", "Olma", "Tana", "Zora", "Amafrey", "Betha", "Cefrey", "Kethra", "Mara", "Olga", "Silifrey", "Westra", "Arizima", "Chathi", "Nephis", "Nulara", "Murithi", "Sefris", "Thola", "Umara", "Zolis", "Fyevarra", "Hulmarra", "Immith", "Imzel", "Navarra", "Shevarra", "Tammith", "Yuldra", "Bai", "Chao", "Jia", "Lei", "Mei", "Qiao", "Shui", "Tai", "Balama", "Dona", "Faila", "Jalana", "Luisa", "Marta", "Quara", "Selise", "Vonda"]},
    "tiefling": {
        "male": [
            "Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech", "Mordai", "Morthos", "Pelaios", "Skamos", "Therai"],
        "female": [
            "Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia", "Orianna", "Phelaia", "Rieta"]}}
other_names = {
    "dragonborn": [
        "Climber", "Earbender", "Leaper", "Pious", "Shieldbiter", "Zealous"],
    "elf": [
        "Ara", "Bryn", "Del", "Eryn", "Faen", "Innil", "Lael", "Mella", "Naill", "Naeris", "Phann", "Rael", "Rinn", "Sai", "Syllin", "Thia", "Vall"],
    "gnome": [
        "Aleslosh", "Ashhearth", "Badger", "Cloak", "Doublelock", "Filchbatter", "Fnipper", "Ku", "Nim", "Oneshoe", "Pock", "Sparklegem", "Stumbleduck"],
    "tiefling": [
        "Art", "Carrion", "Chant", "Creed", "Despair", "Excellence", "Fear", "Glory", "Hope", "Ideal", "Music", "Nowhere", "Open", "Poetry", "Quest", "Random", "Reverence", "Sorrow", "Temerity", "Torment", "Weary"]}
last_names = {
    "dragonborn": [
        "Clethtinthiallor", "Daardendrian", "Delmirev", "Drachedandion", "Fenkenkabradon", "Kepeshkmolik", "Kerrhylon", "Kimbatuul", "Linxakasendalor", "Myastan", "Nemmonis", "Norixius", "Ophinshtalajiir", "Prexijandilin", "Shestendeliath", "Turnuroth", "Verthisathurgiesh", "Yarjerit"],
    "dwarf": [
        "Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"],
    "elf": [
        "Amakiir (Gemflower)", "Amastacia (Starflower)", "Galanodel (Moonwhisper)", "Holimion (Diamonddew)", "Ilphelkiir (Gemblossom)", "Liadon (Silverfrond)", "Meliamne (Oakenheel)", "Naïlo (Nightbreeze)", "Siannodel (Moonbrook)", "Xiloscient (Goldpetal)"],
    "gnome": [
        "Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Timbers", "Turen"],
    "halfling": [
        "Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"],
    "human": [
        "Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein", "Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag", "Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag", "Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind", "Windrivver", "Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt", "Chergoba", "Dyernina", "Iltazyara", "Murnyethara", "Stayanoga", "Ulmokina", "Chien", "Huang", "Kao", "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum", "Tan", "Wan", "Agosto", "Astorio", "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"]}
race_options = {
    1: "dragonborn",
    2: "dwarf",
    3: "elf",
    4: "gnome",
    5: "half-elf",
    8: "human",
    9: "tiefling",
    10: "no preference"
}
gender_options = {
    1: "male",
    2: "female",
    3: "no preference"
}


def get_race() -> int:
    '''Allows user to select a D&D character race from some available options.'''
    selection = int(input(
        f"Please select a race and enter its number {race_options}: "))
    if selection not in race_options:
        print("Invalid input.")
        get_race()
    return selection


def get_gender() -> int:
    '''Allows user to select a D&D character gender from some available options.'''
    selection = int(input(
        f"Please select a gender and enter its number {gender_options}: "))
    if selection not in gender_options:
        print("Invalid input.")
        get_gender()
    return selection


def get_child() -> bool:
    '''Allows user to choose if character will be a child.\n
    * Relevant for elf race only.'''
    user_response = input("Will it be a child's name? (y/n): ")

    match user_response.lower():
        case "y":
            return True
        case "n":
            return False
        case _:
            get_child()


def create_name():
    '''Using user inputs, generate a random name
    based on character race and gender selections.'''
    race = get_race()
    gender = get_gender()
    name = '\n'

    if race == 10:
        race = random.randrange(1, 10)

    if gender == 3:
        gender = random.randrange(1, 3)

    name += f'Race: {race_options[race]}\n'
    name += f'Gender: {gender_options[gender]}\n'

    match race:
        case 1:  # dragonborn
            match gender:
                case 1:
                    name += f'{random.choice(first_names["dragonborn"]["male"])} '
                case 2:
                    name += f'{random.choice(first_names["dragonborn"]["female"])} '
            name += f'"{random.choice(other_names["dragonborn"])}" {random.choice(last_names["dragonborn"])}'
        case 2:  # dwarf
            match gender:
                case 1:
                    name += f'{random.choice(first_names["dwarf"]["male"])} '
                case 2:
                    name += f'{random.choice(first_names["dwarf"]["female"])} '
            name += f'{random.choice(last_names["dwarf"])}'
        case 3:  # elf
            is_child = get_child()
            if is_child:
                name += f'{random.choice(other_names["elf"])} '
            else:
                match gender:
                    case 1:
                        name += f'{random.choice(first_names["elf"]["male"])} '
                    case 2:
                        name += f'{random.choice(first_names["elf"]["female"])} '
            name += f'{random.choice(last_names["elf"])}'
        case 4:  # gnome
            match gender:
                case 1:
                    name += f'{random.choice(first_names["gnome"]["male"])} '
                case 2:
                    name += f'{random.choice(first_names["gnome"]["female"])} '
            name += f'"{random.choice(other_names["gnome"])}" {random.choice(last_names["gnome"])}'
        case 5:  # half-elf
            match gender:
                case 1:
                    name += f'{random.choice(first_names["human"]["male"] + first_names["elf"]["male"])} '
                case 2:
                    name += f'{random.choice(first_names["human"]["female"] + first_names["elf"]["female"])} '
            name += f'{random.choice(last_names["human"] + last_names["elf"])}'
        case 6:  # halfling
            match gender:
                case 1:
                    name += f'{random.choice(first_names["halfling"]["male"])} '
                case 2:
                    name += f'{random.choice(first_names["halfling"]["female"])} '
            name += f'{random.choice(last_names["halfling"])}'
        case 7:  # half-orc
            match gender:
                case 1:
                    name += f'{random.choice(first_names["human"]["male"] + first_names["half-orc"]["male"])} '
                case 2:
                    name += f'{random.choice(first_names["human"]["female"] + first_names["half-orc"]["female"])} '
            name += f'{random.choice(last_names["human"])}'
        case 8:  # human
            match gender:
                case 1:
                    name += f'{random.choice(first_names["human"]["male"])} '
                case 2:
                    name += f'{random.choice(first_names["human"]["female"])} '
            name += f'{random.choice(last_names["human"])}'
        case 9:  # tiefling
            match gender:
                case 1:
                    name += f'{random.choice(first_names["tiefling"]["male"])} '
                case 2:
                    name += f'{random.choice(first_names["tiefling"]["female"])} '
            name += f'{random.choice(other_names["tiefling"])}'

    print(f'{name}', file=sys.stderr)
    try_again = input("\n\nTry again? (Press Enter, else 'n' to quit)\n")
    if try_again.lower() != "n":
        create_name()


if __name__ == "__main__":
    create_name()
