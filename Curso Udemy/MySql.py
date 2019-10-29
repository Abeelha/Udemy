import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)
#SELECT
def select(fields, tables, where=None):
	
	global c

	query = "SELECT " + fields + " FROM " + tables
	if(where):
		query = query + " WHERE " + where

	return c.fetchall()

result = (select("nome, cpf","alunos"))

#INSERT
def insert(values, table, fields=None):

	global c, con

	query = "INSERT INTO" + table
	if (fields):
		query = query + "DEFAULT, 'RONALDO' , '2002-06-12', 'Rua abacate , 666', 'Pato branco','PR', '12345876511'"" (" + fields + ") "
	query = " VALUES " + ",".join(["(" + v + ")" for v in values])

	print(query)

"""values = [
	"DEFAULT, 'RONALDO' , '2002-06-12', 'Rua abacate , 666', 'Pato branco','PR', '12345876511'"
	"DEFAULT, 'maria joana' , '1234-06-12', 'Rua abacate , 666', 'Pato branco','PR', '16543876511'"]
insert(values, "alunos")
"""

#UPDATE
def update(sets, table, where=None):
	global c, con

	query = "UPDATE " + table
	query = query + " SET " + "," .join([field + "= '" + value + "'" for field, value in sets.items()])
	if (where):
		query = query + " WHERE " + where
print(select("*", "alunos", "id_aluno = 5"))
#update({"nome":"Roberto Rivelino","cidade":"Porto Seguro"}, "alunos", "id_aluno = 5")

#DELET
def delete(table, where):

	global c, con

	query = "DELETE FROM" + table + " WHERE " +where