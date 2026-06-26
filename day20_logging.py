import logging

# ===== Basic Logging =====
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("This is a debug message")
logging.info("User logged in successfully")
logging.warning("Low disk space")
logging.error("Database connection failed")
logging.critical("System is down!")


# ===== File + Console Handler =====
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logging.info("Application started")
logging.warning("Low memory warning")
logging.error("Failed to connect to database")
