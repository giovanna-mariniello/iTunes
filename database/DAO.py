from database.DB_connect import DBConnect
from model.album import Album


class DAO():
    @staticmethod
    def get_albums(durata):
        durata_millisec = durata*60*1000

        cnx = DBConnect.get_connection()

        cursor = cnx.cursor(dictionary=True)
        query = """ select a.*, sum(t.Milliseconds) as durata
                    from itunes.track t, itunes.album a 
                    where t.AlbumId = a.AlbumId 
                    group by AlbumId 
                    having durata > %s"""

        cursor.execute(query, (durata_millisec,))

        result = []
        for row in cursor:
            result.append(Album(row["AlbumId"], row["Title"], row["ArtistId"], row["durata"]))

        cursor.close()
        cnx.close()

        return result

    @staticmethod
    def get_archi(id_map):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT DISTINCTROW t1.AlbumId as a1, t2.AlbumId as a2
                    FROM playlisttrack p1, track t1, playlisttrack p2, track t2
                    WHERE p1.TrackId = t1.TrackId AND p2.TrackId = t2.TrackId
                    AND p1.PlaylistId = p2.PlaylistId
                    AND t1.AlbumId < t2.AlbumId  """

        cursor.execute(query)

        result = []
        for row in cursor:
            if row["a1"] in id_map and row["a2"] in id_map:
                result.append((id_map[row["a1"]], id_map[row["a2"]]))

        cursor.close()
        cnx.close()
        return result





