import rethinkdb as r
import flask

# TODO: Fill in these details with the correct RethinkDB instance, and your
# personal database name (defaults to 'test' and a local RethinkDB instance)
RDB_HOST = 'localhost'
RDB_PORT = 28015
RDB_DB = 'test'

app = flask.Flask(__name__)

url = "earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"

def refresh_quakes():
    conn = r.connect(host=RDB_HOST, port=RDB_PORT, db=RDB_DB)
    r.table("quakes").insert(
        r.http(url)["features"].merge({
            "time": r.epoch_time(r.row["properties"]["time"] / 1000),
            "geometry": r.point(
                r.row["geometry"]["coordinates"][0],
                r.row["geometry"]["coordinates"][1])}),
        conflict="replace").run(conn)
    conn.close()

@app.route("/")
def get_index():
    conn = r.connect()
    # TODO: Fill in a ReQL query that:
    #  - Gets all documents in the `quakes` table (all earthquakes)
    #  - Orders them based on their magnitude (the `mag` property)
    #  - Limits them to the top ten earthquakes
    #  - Runs the query with the `conn` connection.
    #  This should return a cursor. Store it as `quakes_cursor`.
    #
    quakes = list(quakes_cursor)
    conn.close()

    return flask.render_template("quakes.html", quakes=quakes)

if __name__ == "__main__":
    refresh_quakes()
    app.run(host="localhost", port=8095, debug=True)
