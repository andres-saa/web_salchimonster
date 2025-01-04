WITH all_states AS (
            /* 
            1) Tomamos todos los estados existentes en pqr.pqr_status;
                ya existe 'generada', por lo que no necesitamos UNION.
            */
            SELECT DISTINCT name AS state_name
            FROM pqr.pqr_status
        ),
        all_responsibles AS (
            /*
            2) Tomamos todos los responsables, 
                pero forzamos incluir 'pendiente' si es nulo o vacío.
            */
            SELECT DISTINCT 
                COALESCE(NULLIF(current_status->>'responsible_name', ''), 'pendiente') AS responsible_name
            FROM pqr.pqr_details_full_view
        ),
        state_counts AS (
            SELECT 
                r.responsible_name,
                st.state_name AS estado,
                COUNT(pqr.pqr_request_id) AS cantidad
            FROM all_responsibles r
            CROSS JOIN all_states st
            LEFT JOIN pqr.pqr_details_full_view pqr
                ON COALESCE(NULLIF(pqr.current_status->>'responsible_name', ''), 'pendiente') = r.responsible_name
                /* Si el estado está vacío o nulo, usar 'generada' (que ya existe en pqr.pqr_status). */
                AND COALESCE(NULLIF(pqr.current_status->>'status', ''), 'generada') = st.state_name
                AND TO_TIMESTAMP(pqr.current_status->>'timestamp', 'DD-MM-YYYY HH12:MI am')
                    BETWEEN %(fecha_inicio)s AND %(fecha_fin)s
            GROUP BY r.responsible_name, st.state_name
        )
        SELECT 
            jsonb_object_agg(estado, cantidad) 
            || jsonb_build_object('responsible_name', responsible_name) AS result
        FROM state_counts
        GROUP BY responsible_name
        ORDER BY responsible_name;