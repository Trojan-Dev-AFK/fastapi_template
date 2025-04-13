"""
Copyright (C) 2025 Aloysius. All rights reserved.

This software is proprietary and developed by Aloysius.
Unauthorized copying, modification, or distribution is prohibited.
"""
# Dependent microservice and databases
AUTH_SERVICE_URL = "http://13.235.31.250:8000/api/v1/auth/verify_access"
DATABASE_URL = "postgresql+psycopg2://avnadmin:AVNS_CUF1VBjOCh3Osau8xMJ@hr-ai-chatbot-db-e-commerce-001.k.aivencloud.com:27271/defaultdb"

# Qdrant
QDRANT_HOST = "http://54.254.14.47/dashboard"
QDRANT_PORT = 6333
QDRANT_COLLECTION_NAME = "handbook_chatbot_collection"

# Embedding
EMBEDDING_DIM = 0
SPACY_CPU_MODEL = "en_core_web_sm"
SPACY_GPU_MODEL = "en_core_web_trf"
TRANSFORMER_MODEL = "all-MiniLM-L6-v2"

# AWS
AWS_ACCESS_KEY_ID="AKIATOMARQLENPAMXZ7J"
AWS_SECRET_ACCESS_KEY="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"
AWS_REGION="ap-southeast-1"
AWS_BUCKET_NAME="bucket-salient"

# General
USE_GPU = False