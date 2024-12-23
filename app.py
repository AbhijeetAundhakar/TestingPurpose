from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'example_db'
}

sdfsdfsdfsdf

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    text_field = data.get('text_field')

    if not text_field:
        return jsonify({'error': 'Text field is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO submissions (text_field) VALUES (%s)', (text_field,))
        conn.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({'message': 'Data submitted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
