
WITH date_range AS (
    SELECT generate_series(
        %(fecha_inicio)s::date, 
        %(fecha_fin)s::date, 
        '1 day'::interval
    )::date AS fecha
),
all_tags AS (
    SELECT DISTINCT name AS tag_name, color AS tag_color
    FROM pqr.pqr_tag
),
daily_counts AS (
    SELECT 
        d.fecha,
        t.tag_name AS tipo,
        COALESCE(COUNT(pqr.pqr_request_id), 0) AS cantidad,
        t.tag_color AS tag_color
    FROM date_range d
    CROSS JOIN all_tags t
    LEFT JOIN pqr.pqr_details_full_view pqr
        ON pqr.tag_name = t.tag_name
        AND pqr.site_id = ANY(%(site_ids)s)
        AND TO_DATE(pqr.current_status->>'timestamp', 'DD-MM-YYYY') = d.fecha
    GROUP BY d.fecha, t.tag_name, t.tag_color
)
SELECT 
    fecha,
    jsonb_object_agg(tipo, json_build_object('cantidad', cantidad, 'color', tag_color)) AS tags
FROM daily_counts
GROUP BY fecha
ORDER BY fecha;