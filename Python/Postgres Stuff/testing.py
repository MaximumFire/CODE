import postgresplus

editor = postgresplus.editor("postgres", "root", "root", "192.168.1.5", "5432")

editor.create_table("test_table")