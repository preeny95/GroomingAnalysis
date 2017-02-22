import sqlite3
import pandas as pd

conn = sqlite3.connect('viber_messages2')

cur = conn.cursor()
#Adapted from Stackoverflow.com by Parfait
cur.execute("""SELECT messages._id,messages.body AS Message, participants_info.number, participants_info.display_name, participants_info._id
        FROM messages, participants
        INNER JOIN participants_info
        ON participants.participant_info_id = participants._id;""")

query = "SELECT m._id, m.date, m.body, m.conversation_id," + \
         "     p.number, p.display_name, p._id" + \
         " FROM messages m" + \
         " INNER JOIN participants_info p" + \
         "         ON m.participant_id = p._id" + \
         " WHERE m.conversation_id = ?"

with open('messages.html', 'w') as h, open('test.txt', 'w') as t:
    for convo in cur.fetchall():
        df = pd.read_sql_query(query, conn, params=convo)

        # HTML WRITE
        h.write(df.to_html())
        h.write('<br/>')

        # TXT WRITE
        t.write(df.to_string())
        t.write('\n\n')

cur.close()
conn.close()
