


UPDATE public.users
	SET  user_name=%s, user_phone=%s , cedula_nit=%s, email=%s, first_last_name=%s, second_last_name=%s, second_name=%s,  visible=%s
	WHERE user_id = %s;
