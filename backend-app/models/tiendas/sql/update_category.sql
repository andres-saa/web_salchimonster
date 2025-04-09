UPDATE tiendas.categorie
	SET  english_name=%s
	WHERE categoria_id = %s returning categoria_id;