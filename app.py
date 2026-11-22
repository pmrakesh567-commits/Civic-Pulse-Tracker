import json
import sqlite3
from typing import Literal
import streamlit as st
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

DB_PATH = "civicpulse.db"


class IssueClassification(BaseModel):
    category: Literal[
        "Roads & Potholes",
        "Garbage & Sanitation",
        "Water & Drainage",
        "Streetlights & Power",
        "Public Safety",
        "Other",
    ]
    severity: int = Field(ge=1, le=5)
    department: str
    summary: str
    def init_db():
     with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS issues (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT NOT NULL,
                note TEXT,
                media_name TEXT,
                category TEXT NOT NULL,
                severity INTEGER NOT NULL,
                department TEXT NOT NULL,
                def init_db()
                status TEXT NOT NULL DEFAULT 'Pending'
            )
            """
        )
        st.set_page_config(page_title="CivicPulse Tracker")
#init_db()

st.title("CivicPulse Tracker")

with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Gemini API Key", type="password")

tab1, tab2 = st.tabs(["Submit Issue", "Public Dashboard"])
with tab1:
   st.subheader("Submit a Civic Issue")
issue_tittle =st.text_input("Issue Tittle")
issue_desc=st.text_area("Issue Description")
if st.button("Submit Issue"):
   if issue_tittle.strip() and issue_desc.strip():
      st.success("Issue form captured! Ready for database/Gemini integration.")
   else:
      st.warning("Please fill in both an Issue Tittle and an Issue Description.")









from google import genai
from google.genai import types
from pydantic import BaseModel, Field

DB_PATH = "civicpulse.db" 

class IssueClassification(BaseModel):
    category: Literal[
        "Roads & Potholes",
        "Garbage & Sanitation",
        "Water & Drainage",
        "Streetlights & Power",
        "Public Safety",
        "Other",
    ]
    severity: int = Field(ge=1, le=5)
    department: str
    summary: str 
    
        
        
        
        
        
        
    
    
    
    
