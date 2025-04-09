UPDATE tiendas.categorie
	SET  index=%s, visible=%s
	WHERE categoria_id=%s returning categoria_id;