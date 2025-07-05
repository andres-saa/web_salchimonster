
from db.db import Db as DataBase
from pydantic import BaseModel
# from schema.pqr import pqrs
# from schema.user import user_schema_post
from models.orders.order2 import Order2




class StatusHistory(BaseModel):
    pqr_request_id: int
    status_id: int
    notes: str
    
    
    
class ChangeStatusRequest(BaseModel):
    pqr_request_id: int
    status_id: int
    responsible_id: int
    value: float = 0.0
    notes: str = ''
    order_id:str
    


class Users:
    
    def __init__(self):
        self.db = DataBase()
                
    def get_user_report(self, site_ids: list, start_date: str, end_date: str):
        """
        Obtiene un reporte de usuarios a partir de la vista orders.combined_order_view,
        filtrando por sedes y rango de fechas.
        Devuelve: lista de usuarios con métricas, clasificación y email.
        """

        query = """
        WITH user_data AS (
            SELECT
                co.user_id,
                co.user_name,
                co.email AS email,                                        -- ⬅️ email
                STRING_AGG(DISTINCT co.user_phone, ', ' ORDER BY co.user_phone) AS phone_numbers,
                co.user_address,

                SUM(co.total_order_price) AS total_spent,
                MAX(co.latest_status_timestamp) AS last_purchase,

                JSON_AGG(
                    JSONB_BUILD_OBJECT(
                        'id_order',  co.order_id,
                        'valor_orden', co.total_order_price,
                        'fecha_order', TO_CHAR(co.latest_status_timestamp::date, 'DD-MM-YYYY')
                    ) ORDER BY co.order_id DESC
                ) AS orders,

                COUNT(DISTINCT co.order_id) AS times_purchased,
                TO_CHAR(MIN(co.latest_status_timestamp)::date, 'DD-MM-YYYY') AS joined_date
            FROM orders.combined_order_view co
            JOIN public.sites s ON s.site_id = co.site_id
            WHERE s.show_on_web = TRUE
            AND s.site_id = ANY(%(site_ids)s)
            AND co.latest_status_timestamp::date BETWEEN %(start_date)s AND %(end_date)s
            AND co.user_name     NOT ILIKE '%%prueba%%'
            AND co.user_address  NOT ILIKE '%%prueba%%'
            AND co.order_notes   NOT ILIKE '%%prueba%%'
            GROUP BY
                co.user_id,
                co.user_name,
                co.email,                                                -- ⬅️ incluido en GROUP BY
                co.user_address
        )
        SELECT
            user_id,
            user_name,
            email,                                                       -- ⬅️ email en SELECT final
            phone_numbers,
            user_address,
            total_spent,
            TO_CHAR(last_purchase::date, 'DD-MM-YYYY') AS last_purchase,
            orders,
            times_purchased,
            joined_date
        FROM user_data
        ORDER BY total_spent DESC
        """

        params = {
            "site_ids": site_ids,
            "start_date": start_date,
            "end_date": end_date
        }

        try:
            result = self.db.execute_query(query=query, params=params, fetch=True)
        except Exception as e:
            return {"error": str(e)}

        if result is None:
            return {"error": "La consulta no devolvió ningún resultado."}

        user_data = []
        for row in result:
            times_purchased = row.get("times_purchased") or 0

            # Clasificación según compras
            if times_purchased == 1:
                classification = "PREOCUPANTE"
            elif times_purchased == 2:
                classification = "CASUAL"
            elif times_purchased in [3, 4]:
                classification = "FRECUENTE"
            elif 5 <= times_purchased <= 8:
                classification = "TOP"
            elif times_purchased > 8:
                classification = "ESTRELLA"
            else:
                classification = "SIN DATOS"

            user_data.append({
                "user_id": row.get("user_id"),
                "user_name": row.get("user_name"),
                "email": row.get("email"),                              # ⬅️ email en la salida
                "phone_numbers": row.get("phone_numbers"),
                "user_address": row.get("user_address"),
                "total_spent": float(row["total_spent"]) if row.get("total_spent") else 0.0,
                "last_purchase": row.get("last_purchase"),
                "orders": row.get("orders") or [],
                "times_purchased": times_purchased,
                "joined_date": row.get("joined_date"),
                "classification": classification
            })

        return user_data
