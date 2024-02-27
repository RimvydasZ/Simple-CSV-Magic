from pathlib import Path

#Deletes old my_data.db file and creates a new one.
Path('my_data.db').unlink()
Path('my_data.db').touch()