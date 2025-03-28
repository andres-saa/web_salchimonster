SELECT json_agg(
        json_build_object(
            'hoja', site_name,
            'title', site_name,
            'column_widths', json_build_object(
                'id',10,
                'nombre del barrio', 50,
                'valor del domicilio', 30
            ),
            'data', barrios
        )
    ) AS hojas
FROM (
    SELECT 
        s.site_name,
        json_agg(
            json_build_object(
                'id', n.neighborhood_id,
                'nombre del barrio', n.name,
                'valor del domicilio', n.delivery_price
            )
        ) AS barrios
    FROM sites s
    JOIN neighborhoods n 
      ON s.site_id = n.site_id
    WHERE s.show_on_web = true
      AND s.site_id IN (%s)
    GROUP BY s.site_id, s.site_name
) subquery;
