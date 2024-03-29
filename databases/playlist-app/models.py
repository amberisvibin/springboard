"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Columm = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    songs = db.relationship(
        'Song',
        secondary="playlists_songs",
        # cascade="all,delete",
    )

class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Columm = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.String(50), nullable=False)
    playlists = db.relationship(
        'Playlist',
        secondary="playlists_songs",
        # cascade="all,delete",
    )
class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlists_songs"

    playlist_id = db.Columm = db.Column(
        db.Integer, db.ForeignKey('playlists.id'), primary_key=True)
    song_id = db.Columm = db.Column(
        db.Integer, db.ForeignKey('songs.id'), primary_key=True)

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
