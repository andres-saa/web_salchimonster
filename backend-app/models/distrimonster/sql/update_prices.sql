UPDATE distrimonster.prices
	SET  mayor=%s, distribuidor=%s
	WHERE product_id = %s returning product_id;