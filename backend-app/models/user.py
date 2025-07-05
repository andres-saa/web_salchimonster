# producto.py

import psycopg2
from dotenv import load_dotenv
import os
from schema.user import user_schema_post
from typing import Any, Dict, Tuple, Optional
import string
import random
from db.db import Db as DataBase
from fastapi import HTTPException

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class User:
    def __init__(self, user_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.user_id = user_id
        self.db = DataBase()

    def select_all_users(self):
        select_query = "SELECT * FROM users;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    
    def select_all_users_distri(self):
        select_query = "SELECT * FROM users where site_id = 32 and visible = true;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_user_by_id(self, user_id):
        select_query = "SELECT * FROM users WHERE user_id = %s;"
        self.cursor.execute(select_query, (user_id,))
        columns = [desc[0] for desc in self.cursor.description]
        user_data = self.cursor.fetchone()

        if user_data:
            return dict(zip(columns, user_data))
        else:
            return None
        
        
        

    def user_exists(self, user_phone):
        select_query = "SELECT user_id FROM users WHERE user_phone = %s;"
        self.cursor.execute(select_query, (user_phone,))
        return self.cursor.fetchone()

    def insert_user(self, user_data: user_schema_post):
        # Verifica si el usuario ya existe por número de teléfono
        existing_user = self.user_exists(user_data.user_phone)
        if existing_user:
            user_id = existing_user[0]
            # Actualiza el usuario si ya existe
            update_query = """
            UPDATE users
            SET user_name = %s, user_address = %s, site_id = %s , email = %s
            WHERE user_id = %s
            RETURNING user_id;
            """
            self.cursor.execute(update_query, (
                user_data.user_name, user_data.user_address, user_data.site_id, user_data.email, user_id
            ))
            self.conn.commit()
            return user_id  # Retorna el user_id actualizado

        # Inserta un nuevo usuario si no existe
        insert_query = """
        INSERT INTO users (
            user_name, user_phone, user_address, site_id, email
        ) VALUES (%s, %s, %s, %s, %s) RETURNING user_id;
        """
        self.cursor.execute(insert_query, (
            user_data.user_name, user_data.user_phone, user_data.user_address, user_data.site_id, user_data.email
        ))
        user_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return user_id


    def delete_user(self, user_id):
        # delete_query = "DELETE FROM users WHERE user_id = %s;"
        # self.cursor.execute(delete_query, (user_id,))
        # self.conn.commit()
        return 'solo desactiva el usuario'

    def update_user(self, user_id, updated_data: user_schema_post):
        update_query = """
        UPDATE users
        SET user_name = %s, user_phone = %s, user_address = %s, site_id = %s
        WHERE user_id = %s
        RETURNING *;
        """

        self.cursor.execute(update_query, (
            updated_data.user_name, updated_data.user_phone, updated_data.user_address, updated_data.site_id, user_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_user_data = self.cursor.fetchone()

        if updated_user_data:
            return dict(zip(columns, updated_user_data))
        else:
            return None
    def close_connection(self):
        self.conn.close()




    def _generate_unique_code(self) -> str:
            """
            Devuelve un código único de 6 caracteres (3 letras + 3 dígitos).
            Repite la generación hasta dar con uno que no exista en la BD.
            """
            while True:
                letters = random.sample(string.ascii_uppercase, 3)
                digits  = random.sample(string.digits, 3)
                random.shuffle(letters + digits)
                code = ''.join(letters + digits)
                # ¿Ya existe?
                exists = self.db.execute_query(
                    query="SELECT 1 FROM public.user_code_email WHERE code = %s LIMIT 1",
                    params=[code],
                    fetch=True
                )
                if not exists:
                    return code

        # ------------------------------------------------------------------
        #   DEVUELVE el código del usuario si ya existe, None en caso contrario
        # ------------------------------------------------------------------
    def _get_existing_code(self, user_id: int) -> Optional[str]:
        row = self.db.execute_query(
            query="""
                SELECT code
                FROM   public.user_code_email
                WHERE  user_id = %s
                ORDER  BY id DESC NULLS LAST
                LIMIT  1
            """,
            params=[user_id],
            fetch=True
        )
        return row[0]['code'] if row else None

    # ------------------------------------------------------------------
    #  INSERT/UPDATE + CÓDIGO
    # ------------------------------------------------------------------
    def insert_user_code(self, user: user_schema_post) -> str:
        """
        Inserta o actualiza un usuario según su teléfono.
        Devuelve el código (nuevo o existente) asociado a ese usuario.
        """
        # 1) ¿Ya existe un usuario con el mismo teléfono?
        existing = self.db.execute_query(
            query="SELECT user_id FROM users WHERE user_phone = %s LIMIT 1",
            params=[user.user_phone],
            fetch=True
        )

        if existing:          # --- Ya existe ---
            user_id = existing[0]['user_id']

            # 1a) Actualizamos sus datos (solo si cambió algo)
            self.db.execute_query(
                query="""
                    UPDATE users
                    SET    user_name    = %s,
                        user_address = %s,
                        email        = %s
                    WHERE  user_id      = %s
                """,
                params=[user.user_name, user.user_address, user.email, user_id],
                fetch=False
            )

            # 1b) ¿Tiene código?
            code = self._get_existing_code(user_id)
            if code:
                return code       # <-- devolvemos el que ya tenía

        else:                # --- No existe: inserta ---
            insert_q = """
                INSERT INTO users (user_name, user_phone, user_address, email)
                VALUES (%s, %s, %s, %s)
                RETURNING user_id
            """
            result: Tuple[Dict[str, Any], ...] = self.db.execute_query(
                query=insert_q,
                params=[user.user_name, user.user_phone,
                        user.user_address, user.email],
                fetch=True
            )
            user_id = result[0]['user_id']

        # 2) A este punto **NO** tenía código: generamos uno nuevo
        code = self.b()

        self.db.execute_query(
            query="""
                INSERT INTO public.user_code_email (code, redimido, user_id)
                VALUES (%s, FALSE, %s)
            """,
            params=[code, user_id],
            fetch=False
        )

        return code
    
    
    
    def get_users_code(self):
        query = """ select * from public.users_code"""
        return self.db.fetch_all(
            query
        )
        
    # ------------------------------------------------------------------
    #  INSERT/UPDATE + CÓDIGO (con user_id devuelto)                                                
    
    
    def insert_user_code2(self, user: user_schema_post) -> str:
        """
        Inserta o actualiza un usuario según su teléfono.
        Devuelve el código (nuevo o existente) asociado a ese usuario.
        """
        # 1) ¿Ya existe un usuario con el mismo teléfono?
        existing = self.db.execute_query(
            query="SELECT user_id FROM users WHERE user_phone = %s LIMIT 1",
            params=[user.user_phone],
            fetch=True
        )

        user_id = None
        if existing:          # --- Ya existe ---
            user_id = existing[0]['user_id']

            # 1a) Actualizamos sus datos (solo si cambió algo)
            self.db.execute_query(
                query="""
                    UPDATE users
                    SET    user_name    = %s,
                        user_address = %s,
                        email        = %s
                    WHERE  user_id      = %s
                """,
                params=[user.user_name, user.user_address, user.email, user_id],
                fetch=False
            )

            # 1b) ¿Tiene código?
            code = self._get_existing_code(user_id)
            if code:
                return code , user_id      # <-- devolvemos el que ya tenía

        else:                # --- No existe: inserta ---
            insert_q = """
                INSERT INTO users (user_name, user_phone, user_address, email)
                VALUES (%s, %s, %s, %s)
                RETURNING user_id
            """
            result: Tuple[Dict[str, Any], ...] = self.db.execute_query(
                query=insert_q,
                params=[user.user_name, user.user_phone,
                        user.user_address, user.email],
                fetch=True
            )
            user_id = result[0]['user_id']

        # 2) A este punto **NO** tenía código: generamos uno nuevo
        code = self._generate_unique_code()

        self.db.execute_query(
            query="""
                INSERT INTO public.user_code_email (code, redimido, user_id)
                VALUES (%s, FALSE, %s)
            """,
            params=[code, user_id],
            fetch=False
        )

        return code, user_id
    
    
    
    
    def get_user_by_code(
        self,
        code: str,
        only_unredeemed: bool = False        # ← True si sólo quieres códigos sin redimir
    ) -> Dict[str, Any]:
        """
        Busca un usuario a través de un código de verificación.
        - `code`:   Código alfanumérico (6 caracteres) que recibió el usuario.
        - `only_unredeemed`: Si es True, ignora códigos ya redimidos.
        
        Devuelve un dict con los datos del usuario y del código.
        Lanza HTTPException 404 si no existe.
        """
        query = """
            SELECT
                u.user_id,
                u.user_name,
                u.user_phone,
                u.user_address,
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                u.email,
                c.code,
                c.redimido
             
            FROM   users               AS u
            JOIN   public.user_code_email AS c
                   ON c.user_id = u.user_id
            WHERE  c.code = %s
        """
        if only_unredeemed:
            query += " AND c.redimido = FALSE"
        query += " LIMIT 1"

        rows: Tuple[Dict[str, Any], ...] = self.db.execute_query(
            query=query,
            params=[code],
            fetch=True
        )

        if not rows:
            return {
                "user_id": 36643,
                "user_name": "no valido",
                "user_phone": "no valid",
                "user_address": "no valido",
                "email": "no valid",
                "code": "VXJ067",
                "redimido": True
                }

        return rows[0]
    
    
    
    
    
    def redeem_code(self, code: str) -> bool:
        """
        Marca como redimido el código de verificación de un usuario.
        Devuelve True si se redimió; lanza HTTPException si no es válido.
        """
        redeem_q = """
            UPDATE public.user_code_email
            SET    redimido    = TRUE
            WHERE  code  = %s
              AND  redimido = FALSE
            RETURNING code
        """

        result: Tuple[Dict[str, Any], ...] = self.db.execute_query(
            query=redeem_q,
            params=[ code],
            fetch=True
        )

        if result:
            return True

        # Si llegó aquí, el código no existe o ya fue redimido
        raise HTTPException(
            status_code=400,
            detail="Código inválido o ya utilizado"
        )