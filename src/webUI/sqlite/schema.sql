CREATE TABLE USER(
    user_Id INTEGER PRIMARY KEY,
    preferences TEXT
);

INSERT INTO USER (user_Id)
VALUES
(17291429),
(23573258),
(26432623),
(52793396),
(53633605),
(55012109),
(57226048),
(58937384),
(67057254),
(67057735),
(74488735),
(76019825),
(83578673),
(93769355),
(96787900)

CREATE TABLE ARTIST(
    artist_id INTEGER PRIMARY KEY,
    artist_name TEXT
);

INSERT INTO ARTIST (artist_id, artist_name)
VALUES
    (9192, 'Adele'),
    (82745, 'Coldplay'),
    (52897, 'BoB feat. Bruno Mars'),
    (356772, 'Rihanna'),
    (122991, 'Drake'),
    (228395, 'Katy Perry'),
    (466569, 'Usher');

CREATE TABLE TRACK(
    track_Id INTEGER PRIMARY KEY,
    track_title TEXT,
    artist_id INTEGER,
    tweet_count INTEGER
);

INSERT INTO TRACK (track_Id, track_title, artist_id, tweet_count)
VALUES
    (141574, 'Someone Like You', 9192, 432),
    (1479214, 'Paradise', 82745, 383),
    (141567, 'Set Fire to the Rain', 9192, 263),
    (1072515, 'It Will Rain', 52897, 197),
    (6213223, 'You da One', 356772, 178),
    (2106361, 'Practice', 122991, 174),
    (6213179, 'We Found Love', 356772, 173),
    (2106383, 'Shot for Me', 122991, 170),
    (4098232, 'The One That Got Away', 228395, 162),
    (8010733, 'Climax', 466569, 160);