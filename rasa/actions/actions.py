from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import sqlite3

DB_PATH = '/chatbot/db/demo-co.db'

class ActionFindEmployee(Action):
    """ Class that handles a find employee request from rasa server"""

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def name(self) -> Text:
        return "action_find_employee"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        """ Function to return employees based on query"""

        # Extract message entities
        role = next(tracker.get_latest_entity_values("role"), None)
        comparison = next(tracker.get_latest_entity_values("comparison"), None)
        experience = next(tracker.get_latest_entity_values("experience"), None)
        contracts = next(tracker.get_latest_entity_values("contracts"), None)
        neg_contracts = next(tracker.get_latest_entity_values("neg_contract"), None)

        conditions = [] # SQL conditions
        
        # If experience found, append condition
        if comparison and experience:
            # Text to sql comparator
            sql_comparison = {
                "more than": ">",
                "less than": "<"
            }.get(comparison, "")
            conditions.append(f"experience {sql_comparison} {experience}")
        
        # If contract status found, append condition
        if contracts:
            if neg_contracts:
                sql_contracts = 0
            else: 
                sql_contracts = 1
            conditions.append(f"contracts = {sql_contracts}")
        
        # If role found, append condition
        if role:
            conditions.append(f"role = '{role}'")
        
        # Build staff query
        query = "SELECT * FROM staff"
        
        # Add conditions to query, if present
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        # Execute query and fetch result
        results = self.cursor.execute(query).fetchall()
        
        # Check if query returns names and format accordingly
        if results:
            # Names found, return as list
            response = ', '.join([result[0] for result in results])
        else:
            # No results found
            response = "Sorry, could not find any employees with those details!"
        
        dispatcher.utter_message(text=response)
        return[]

