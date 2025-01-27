SELECT json_agg(
        json_build_object(
            'hoja', site_name,
            'title', site_name,
            'column_widths', json_build_object(
                'id',10,
                'name', 40,
                'delivery_price', 15
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
                'name', n.name,
                'delivery_price', n.delivery_price
            )
        ) AS barrios
    FROM 
        sites s
    JOIN 
        neighborhoods n ON s.site_id = n.site_id and s.show_on_web = true
    GROUP BY 
        s.site_id, s.site_name
) subquery;
