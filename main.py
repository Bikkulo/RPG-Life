mmr = 12550

quests = {
    "урок питон": 50,
    "мем": 100,
    "оплата кредита": 300,
    "фитнес": 30
}

def add_mmr():
    print("Выбери квест:")
    for quest in quests:
        print(f'- {quest}')
    choice = input(">>> ")
    if choice in quests:
        return mmr + quests[choice]
    else:
        print("Такого квеста нет")
        return mmr
    
new_mmr = add_mmr()
print(f"Твой мMR: {new_mmr}")