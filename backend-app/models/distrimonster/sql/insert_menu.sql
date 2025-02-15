UPDATE distrimonster.menu
	SET data=%s
	WHERE id = %s returning id;