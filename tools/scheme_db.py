def get_scheme(category):
    db = {
        "student": "தமிழ்நாடு கல்வி உதவித் தொகை",
        "woman": "மகளிர் உரிமைத் தொகை",
        "farmer": "பிரதான் மந்திரி கிசான்"
    }
    return db.get(category, "பொதுத் திட்டம்")


