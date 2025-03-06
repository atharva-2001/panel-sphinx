import logging
import time
from source.logger import logging_state

def demonstrate_logging():
    # Initialize the logging widget
    logging_state(log_level="DEBUG", display_logging_widget=True)
    
    # Get the tardis logger
    logger = logging.getLogger("tardis")
    
    # Demonstrate different log levels
    logger.debug("🔍 This is a debug message - useful for detailed debugging information")
    time.sleep(1)  # Small delay to better see the messages appear
    
    logger.info("ℹ️ This is an info message - general information about program execution")
    time.sleep(1)
    
    logger.warning("⚠️ This is a warning message - something might be wrong!")
    time.sleep(1)
    
    logger.error("❌ This is an error message - something has definitely gone wrong!")
    time.sleep(1)
    
    # Demonstrate structured logging
    logger.info("📊 Processing data batch: %d", 1)
    logger.debug("🔢 Variables: x=%d, y=%d", 10, 20)
    
    # Demonstrate exception logging
    try:
        result = 1 / 0
    except Exception as e:
        logger.error("💥 Division by zero error occurred", exc_info=True)
    
    logger.info("✅ Logging demonstration completed!")

if __name__ == "__main__":
    demonstrate_logging() 