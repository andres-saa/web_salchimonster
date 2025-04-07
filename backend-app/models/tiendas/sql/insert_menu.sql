UPDATE tiendas.menu
	SET data=%s
	WHERE local_id = %s returning id;