WITH all_tags AS (
            SELECT DISTINCT name AS tag_name
            FROM pqr.pqr_tag
        ),
        all_sites AS (
            SELECT DISTINCT site_name
            FROM pqr.pqr_details_full_view
        ),
        tag_counts AS (
            SELECT 
                s.site_name AS sede,
                t.tag_name AS tipo,
                COUNT(pqr.pqr_request_id) AS cantidad
            FROM all_sites s
            CROSS JOIN all_tags t
            LEFT JOIN pqr.pqr_details_full_view pqr
                ON pqr.site_name = s.site_name
                AND pqr.tag_name = t.tag_name
                AND TO_TIMESTAMP(pqr.current_status->>'timestamp', 'DD-MM-YYYY HH12:MI am')
                    BETWEEN %(fecha_inicio)s AND %(fecha_fin)s
            GROUP BY s.site_name, t.tag_name
        )
        SELECT 
            sede,
            jsonb_object_agg(tipo, cantidad) AS tags
        FROM tag_counts
        GROUP BY sede
        ORDER BY sede;