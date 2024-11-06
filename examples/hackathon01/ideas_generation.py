from ai_engineer.generate_ideas import ChatManager
from pathlib import Path
import autogen
import os
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
import sys

# Create logs directory if it doesn't exist
def setup_logging():
    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Create file handler
    file_handler = logging.FileHandler('examples/hackathon01/logging/debug.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    
    # Optional: Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # Configure the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels
    root_logger.setLevel(logging.INFO) 
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # Set logging levels for specific loggers
    logging.getLogger('autogen').setLevel(logging.INFO)
    logging.getLogger('autogen.agentchat').setLevel(logging.INFO)
    logging.getLogger('autogen.agentchat.contrib').setLevel(logging.INFO)
    logging.getLogger('autogen.agentchat.contrib.retrieve_user_proxy_agent').setLevel(logging.INFO)
    logging.getLogger('chromadb').setLevel(logging.INFO)
    logging.getLogger('sentence_transformers').setLevel(logging.INFO)
    
    # Set DEBUG level for more detailed logging
    logging.getLogger('autogen').setLevel(logging.DEBUG)
    logging.getLogger('autogen.agentchat').setLevel(logging.DEBUG)
    logging.getLogger('autogen.agentchat.contrib').setLevel(logging.DEBUG)
    logging.getLogger('autogen.agentchat.contrib.retrieve_user_proxy_agent').setLevel(logging.DEBUG)
    logging.getLogger('chromadb').setLevel(logging.DEBUG)
    logging.getLogger('sentence_transformers').setLevel(logging.DEBUG)
    
    # Prevent duplicate logs
    root_logger.propagate = False

# Call this function at the start of your program

def main():
    setup_logging()
    
    # logging_session_id = autogen.runtime_logging.start(
    #     logger_type="file",
    #     config={"filename": f"runtime.log"},
    # )
    # logger.info(f"Logging session ID: {logging_session_id}")

    chat_manager = ChatManager(
        problem="What is the best project to build for the hackathon?",
        model="gpt-4o-mini",
        api_key=os.environ["OPENAI_API_KEY"],
    )
    # logger.info("Chat manager initialized")
    
    chat_manager.rag_chat()
    # logger.info("RAG chat completed")
    
    # # autogen.runtime_logging.stop()
    # logger.info("Application finished")


if __name__ == "__main__":
    main()
