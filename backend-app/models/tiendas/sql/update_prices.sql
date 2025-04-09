UPDATE tiendas.producto
	SET  index=%s, english_name=%s, english_description=%s, last_price=%s
	WHERE producto_id = %s returning producto_id;