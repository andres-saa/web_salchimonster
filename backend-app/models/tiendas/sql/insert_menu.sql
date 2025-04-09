UPDATE tiendas.menu
	SET data=%s
	WHERE local_id = %s returning id;

SELECT tiendas.sync_menu_products_categories()