from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def store(request):
    games = [
        "The Witcher 3: Wild Hunt",
        "Dark Souls III",
        "Minecraft",
        "Counter-Strike: Global Offensive",
        "The Legend of Zelda: Breath of the Wild",
        "Cyberpunk 2077",
        "Stardew Valley",
        "Dota 2",
        "Among Us",
        "Hades",
        "Portal 2",
        "Assassin's Creed Valhalla",
        "Valorant",
        "Overwatch",
        "Hollow Knight",
        "Final Fantasy VII Remake",
        "Sekiro: Shadows Die Twice",
        "CyberConnect2's Naruto RPG Series",
        "The Sims 4",
        "Genshin Impact"
    ]

    context = {
        'games': games,
    }
    return render(request, 'store.html', context)

def cart(request):
    return render(request, 'cart.html')