import sqlite3, json, os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='.')
CORS(app)
DB = os.path.join(os.path.dirname(__file__), 'data.db')

def get_db():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    db.executescript('''
        CREATE TABLE IF NOT EXISTS kv (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
    ''')
    db.commit()
    db.close()

init_db()

# ── Serve the app ──────────────────────────────────
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# ── Key-Value API (mirrors localStorage) ───────────
@app.route('/api/kv/<key>', methods=['GET'])
def kv_get(key):
    db = get_db()
    row = db.execute('SELECT value FROM kv WHERE key=?', (key,)).fetchone()
    db.close()
    if row:
        return jsonify({'value': json.loads(row['value'])})
    return jsonify({'value': None})

@app.route('/api/kv/<key>', methods=['POST'])
def kv_set(key):
    data = request.get_json()
    db = get_db()
    db.execute('INSERT OR REPLACE INTO kv(key,value) VALUES(?,?)',
               (key, json.dumps(data['value'])))
    db.commit()
    db.close()
    return jsonify({'ok': True})

@app.route('/api/kv/<key>', methods=['DELETE'])
def kv_delete(key):
    db = get_db()
    db.execute('DELETE FROM kv WHERE key=?', (key,))
    db.commit()
    db.close()
    return jsonify({'ok': True})

@app.route('/api/kv', methods=['GET'])
def kv_all():
    db = get_db()
    rows = db.execute('SELECT key, value FROM kv').fetchall()
    db.close()
    return jsonify({r['key']: json.loads(r['value']) for r in rows})

if __name__ == '__main__':
    print('\n✅  مhmd-world running at http://localhost:7788\n')
    app.run(port=7788, debug=False)
