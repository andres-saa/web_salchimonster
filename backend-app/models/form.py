import psycopg2
from schema.form import FormSchema, QuestionSchema, QuestionOptionSchema, ResponseSchema
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class FormManager:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_form(self, form_data: FormSchema):
        insert_query = """
        INSERT INTO forms (user_id, title, description) VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (form_data.user_id, form_data.title, form_data.description))
        form_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return form_id

    def insert_question(self, question_data: QuestionSchema):
        insert_query = """
        INSERT INTO questions (form_id, question_text, question_type) VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (question_data.form_id, question_data.question_text, question_data.question_type))
        question_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return question_id

    def insert_question_option(self, option_data: QuestionOptionSchema):
        insert_query = """
        INSERT INTO question_options (question_id, option_text) VALUES (%s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (option_data.question_id, option_data.option_text))
        option_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return option_id

    def insert_response(self, response_data: ResponseSchema):
        insert_query = """
        INSERT INTO responses (question_id, user_id, response) VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (response_data.question_id, response_data.user_id, response_data.response))
        response_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return response_id



    def get_all_forms(self):
        select_query = "SELECT * FROM forms;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_form_by_id(self, form_id):
        select_query = "SELECT * FROM forms WHERE id = %s;"
        self.cursor.execute(select_query, (form_id,))
        columns = [desc[0] for desc in self.cursor.description]
        form_data = self.cursor.fetchone()

        if form_data:
            return dict(zip(columns, form_data))
        else:
            return None

    def get_questions_by_form_id(self, form_id):
        select_query = "SELECT * FROM questions WHERE form_id = %s;"
        self.cursor.execute(select_query, (form_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_question_options_by_question_id(self, question_id):
        select_query = "SELECT * FROM question_options WHERE question_id = %s;"
        self.cursor.execute(select_query, (question_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_responses_by_question_id(self, question_id):
        select_query = "SELECT * FROM responses WHERE question_id = %s;"
        self.cursor.execute(select_query, (question_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def update_form(self, form_id, updated_data: FormSchema):
        update_query = """
        UPDATE forms
        SET title = %s, description = %s, user_id = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.title, updated_data.description, updated_data.user_id, form_id
        ))
        self.conn.commit()
        columns = [desc[0] for desc in self.cursor.description]
        updated_form_data = self.cursor.fetchone()
        return dict(zip(columns, updated_form_data)) if updated_form_data else None

    def update_question(self, question_id, updated_data: QuestionSchema):
        update_query = """
        UPDATE questions
        SET form_id = %s, question_text = %s, question_type = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.form_id, updated_data.question_text, updated_data.question_type, question_id
        ))
        self.conn.commit()
        columns = [desc[0] for desc in self.cursor.description]
        updated_question_data = self.cursor.fetchone()
        return dict(zip(columns, updated_question_data)) if updated_question_data else None

    def update_question_option(self, option_id, updated_data: QuestionOptionSchema):
        update_query = """
        UPDATE question_options
        SET question_id = %s, option_text = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.question_id, updated_data.option_text, option_id
        ))
        self.conn.commit()
        columns = [desc[0] for desc in self.cursor.description]
        updated_option_data = self.cursor.fetchone()
        return dict(zip(columns, updated_option_data)) if updated_option_data else None

    def update_response(self, response_id, updated_data: ResponseSchema):
        update_query = """
        UPDATE responses
        SET question_id = %s, user_id = %s, response = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.question_id, updated_data.user_id, updated_data.response, response_id
        ))
        self.conn.commit()
        columns = [desc[0] for desc in self.cursor.description]
        updated_response_data = self.cursor.fetchone()
        return dict(zip(columns, updated_response_data)) if updated_response_data else None

    def insert_form(self, form_data: FormSchema):
        insert_query = """
        INSERT INTO forms (user_id, title, description) VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (form_data.user_id, form_data.title, form_data.description))
        form_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return form_id

    def insert_question(self, question_data: QuestionSchema):
        insert_query = """
        INSERT INTO questions (form_id, question_text, question_type) VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (question_data.form_id, question_data.question_text, question_data.question_type))
        question_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return question_id

    def insert_question_option(self, option_data: QuestionOptionSchema):
        insert_query = """
        INSERT INTO question_options (question_id, option_text) VALUES (%s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (option_data.question_id, option_data.option_text))
        option_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return option_id

    def insert_response(self, response_data: ResponseSchema):
        insert_query = """
        INSERT INTO responses (question_id, user_id, response) VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (response_data.question_id, response_data.user_id, response_data.response))
        response_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return response_id

    def close_connection(self):
        self.conn.close()
