UPDATE distrimonster.prices
	SET  mayor= %s, distribuidor= %s, presentacion= %s, unit_measure_id= %s, presentation_unit_measure_id= %s
	WHERE product_id = %s returning product_id;