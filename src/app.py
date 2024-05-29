import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri='https://localhost'))

ID_ARTISTA ='2ziB7fzrXBoh1HUPS6sVFn'
response = sp.artist_top_tracks(ID_ARTISTA)

TRACKS = response['tracks']
df_tracks = pd.DataFrame.from_records(TRACKS)
df_tracks.sort_values(['popularity'], inplace=True)  
print(df_tracks.head(3))

#Analisis entre popularidad y duracion de cada cancion.
plt.scatter(x=df_tracks['popularity'],y=df_tracks['duration_ms'])
plt.show

#Analisis entre popularidad y numero de track dentro del album de cada cancion.
plt.scatter(x=df_tracks['popularity'],y=df_tracks['track_number'])
plt.show

#No hay relacion entre duracion y popularidad, debido a que el grafico no presenta un patron lineal entre ambas caracteristicas,
#esto se debe a que toda la discografia de esta banda es excelente, independiente de su duracion ;)