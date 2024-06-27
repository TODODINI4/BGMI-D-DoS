import sqlite3

DEFAULT_ADMIN_ID = '1027596128'
token = '7345507165:AAErAcMHA6iT02v6QedQQC-fDcWEXkjKxYw'
bot_name = 'BGMI D-DoS BOT'
bot_username = '@BGMI_D_DoS_RoBot'
owner_username = '@PANEL_EXPERT'
channel_username = '@DARKESPYT'

def initialize_db():
    conn = sqlite3.connect('bot_data.db')
    cursor = conn.cursor()

    # Create table for bot configurations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bot_configs (
            id INTEGER PRIMARY KEY,
            token TEXT NOT NULL,
            bot_name TEXT NOT NULL,
            bot_username TEXT NOT NULL,
            owner_username TEXT NOT NULL,
            channel_username TEXT
        )
    ''')
    
    # Insert default bot config if not exists
    cursor.execute('''
        INSERT OR IGNORE INTO bot_configs (token,bot_name,bot_username,owner_username,channel_username)
        VALUES (?,?,?,?,?)
    ''', (token,bot_name,bot_username,owner_username,channel_username))
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            expiration_date DATETIME
        )
    ''')

    # Create admins table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            admin_id TEXT PRIMARY KEY
        )
    ''')
    
    # Insert default admin if not exists
    cursor.execute('''
        INSERT OR IGNORE INTO admins (admin_id)
        VALUES (?)
    ''', (DEFAULT_ADMIN_ID,))

    # Create logs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            username TEXT,
            target TEXT,
            port INTEGER,
            time INTEGER,
            command TEXT,
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()
