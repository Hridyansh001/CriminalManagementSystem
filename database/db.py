import mysql.connector
from mysql.connector import pooling, Error
from config import Config
import logging

logger = logging.getLogger(__name__)

# Connection pool instance
_connection_pool = None

def init_db_pool():
    """Initialize the MySQL connection pool."""
    global _connection_pool
    try:
        _connection_pool = pooling.MySQLConnectionPool(
            pool_name=Config.DB_POOL_NAME,
            pool_size=Config.DB_POOL_SIZE,
            pool_reset_session=True,
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT
        )
        logger.info("Database connection pool initialized successfully.")
    except Error as e:
        logger.error(f"Error initializing connection pool: {e}")
        _connection_pool = None

def get_db_connection():
    """Get a connection from the pool or establish a direct connection as fallback."""
    global _connection_pool
    if _connection_pool is None:
        init_db_pool()
    
    if _connection_pool:
        try:
            return _connection_pool.get_connection()
        except Error as e:
            logger.warning(f"Failed to get pooled connection, trying direct connection: {e}")
    
    # Direct connection fallback
    return mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        port=Config.DB_PORT
    )

def test_connection():
    """Test if database is reachable."""
    try:
        conn = get_db_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            cursor.close()
            conn.close()
            return True, f"Connected to MySQL database: {db_name[0]}"
    except Exception as e:
        return False, f"Database connection failed: {str(e)}"
    return False, "Unable to establish connection."

def fetch_all(query, params=None):
    """Execute a SELECT query and return all rows as list of dictionaries."""
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        return results
    except Error as e:
        logger.error(f"Database error in fetch_all: {e}\nQuery: {query}\nParams: {params}")
        raise e
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def fetch_one(query, params=None):
    """Execute a SELECT query and return a single row as a dictionary."""
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())
        result = cursor.fetchone()
        return result
    except Error as e:
        logger.error(f"Database error in fetch_one: {e}\nQuery: {query}\nParams: {params}")
        raise e
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def execute_query(query, params=None):
    """Execute an INSERT, UPDATE, or DELETE query and commit transaction."""
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        affected_rows = cursor.rowcount
        return affected_rows
    except Error as e:
        if conn:
            conn.rollback()
        logger.error(f"Database error in execute_query: {e}\nQuery: {query}\nParams: {params}")
        raise e
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_and_get_id(query, params=None):
    """Execute an INSERT query, commit transaction, and return last inserted ID."""
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        last_id = cursor.lastrowid
        return last_id
    except Error as e:
        if conn:
            conn.rollback()
        logger.error(f"Database error in insert_and_get_id: {e}\nQuery: {query}\nParams: {params}")
        raise e
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
