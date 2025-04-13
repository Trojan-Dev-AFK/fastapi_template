"""
Copyright (C) 2025 Aloysius. All rights reserved.

This software is proprietary and developed by Aloysius.
Unauthorized copying, modification, or distribution is prohibited.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from threading import Lock


class ChatbotLogger:
    """Logger for Chatbot."""

    _instance = None
    _lock = Lock()

    def __new__(cls) -> "ChatbotLogger":
        """
        Dunder method to initialize ChatbotLogger instance.

        Returns:
            ChatbotLogger: Instance of ChatbotLogger.
        """
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ChatbotLogger, cls).__new__(cls)
                cls._instance._init_logger()
            return cls._instance

    def _init_logger(self) -> None:
        """Method to initalize logger."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / "app.log"

        self.logger = logging.getLogger("ChatbotLogger")
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        # File handler
        file_handler = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=5)
        file_handler.setFormatter(formatter)

        # Console handler
        # console_handler = logging.StreamHandler()
        # console_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            # self.logger.addHandler(console_handler)

    def get_logger(self) -> logging.Logger:
        """
        Method to get ChatbotLogger.

        Returns:
            logger: ChatbotLogger instance.
        """
        return self.logger
