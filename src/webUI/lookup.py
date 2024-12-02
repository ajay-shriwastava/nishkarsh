from flask_caching import Cache
cache = Cache()

static_content = {
    "title" : "Image Processing System",
    "application_name" : "Image Processing System"
}
locations_lookup = ["United States", "England", "France", "Brazil", "Germany", "Indonesia", "India"]
languages_lookup = ["English", "French", "Spanish", "hawaiian", "German", "Hindi"]
genres_lookup = ["Pop", "Rock", "Alternative", "Electronic", "Rap"]

tracks_lookup = [
    {
        "artist_id":  9192,
        "artist_name": "Adele",
        "tracks": [(141574, "Someone Like You"), (141567, "Set Fire to the Rain")]
    },
    {
        "artist_id":  122991,
        "artist_name": "Drake",
        "tracks": [(2106361, "Practice"), (2106383, "Shot for Me")]
    },
    {
        "artist_id":  228395,
        "artist_name": "Katy Perry",
        "tracks": [(4098232, "The One That Got Away")]
    }
]

cache_config = {
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 300
}

