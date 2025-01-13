
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
        filtrando por las sedes y un rango de fechas (por ejemplo: filtramos por last_purchase).

        :param site_ids: Lista de IDs de sedes a filtrar.
        :param start_date: Fecha de inicio en formato 'YYYY-MM-DD'.
        :param end_date: Fecha de fin en formato 'YYYY-MM-DD'.
        :return: Diccionario con la lista de usuarios (clave "data").
        """

        query = """
        WITH user_data AS (
            SELECT
                co.user_id,
                co.user_name,
                -- Agrupamos teléfonos únicos
                STRING_AGG(DISTINCT co.user_phone, ', ' ORDER BY co.user_phone) AS phone_numbers,
                co.user_address,
                
                -- Cantidad total gastada por el usuario en todas sus órdenes
                SUM(co.total_order_price) AS total_spent,

                -- Último registro de compra o cambio de estado
                MAX(co.latest_status_timestamp) AS last_purchase,

                -- Listado de órdenes como objetos JSON con id_order y valor_orden
                JSON_AGG(
                    JSONB_BUILD_OBJECT(
                         'id_order', co.order_id,
                        'valor_orden', co.total_order_price,
                        'fecha_order', TO_CHAR(co.latest_status_timestamp::date, 'DD-MM-YYYY')
                    ) ORDER BY co.order_id DESC
                ) AS orders,

                -- Veces que ha comprado (conteo de órdenes únicas)
                COUNT(DISTINCT co.order_id) AS times_purchased,

                -- Fecha de unión del usuario (usando el primer registro de latest_status_timestamp)
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
                co.user_address
        )
        SELECT
            user_id,
            user_name,
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
            # Ejecutar la consulta
            result = self.db.execute_query(query=query, params=params, fetch=True)
        except Exception as e:
            # Manejar errores de la consulta
            return {
                "error": str(e)
            }

        if result is None:
            return {
                "error": "La consulta no devolvió ningún resultado."
            }

        # Construir la respuesta
        user_data = []
        for row in result:
            # Las fechas ya están formateadas en la consulta SQL
            user_data.append({
                "user_id": row.get("user_id"),
                "user_name": row.get("user_name"),
                "phone_numbers": row.get("phone_numbers"),
                "user_address": row.get("user_address"),
                "total_spent": float(row["total_spent"]) if row.get("total_spent") else 0.0,
                "last_purchase": row.get("last_purchase"),    # Fecha ya formateada
                "orders": row.get("orders") or [],            # Lista de órdenes como objetos ya formateados
                "times_purchased": row.get("times_purchased") or 0,
                "joined_date": row.get("joined_date"),        # Fecha ya formateada
                # "site_id": row.get("site_id")              # Descomentar si se necesita site_id
            })

        return user_data
