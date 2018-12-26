from flask import Flask, request, url_for, render_template, redirect, session, flash

app = Flask(__name__)
app.secret_key = "secret"

class Jogo:
	def __init__(self, nome, categoria, console):
		self.nome = nome
		self.categoria = categoria
		self.console = console

jogo1 = Jogo("Mario", "Ação", "SNES")
jogo2 = Jogo("Pokemon", "RPG", "GBA")
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [jogo1, jogo2, jogo3]



@app.route("/")
def index():
	return "Home"

@app.route("/login2", methods=["GET", "POST"])
def login2():
	if request.method == "POST":
		return do_the_login()
	else:
		return show_the_login_form()

@app.route("/jogos")
def jogos():
	return render_template("lista.html", titulo = "Jogos", jogos = lista)

@app.route("/user/")
@app.route("/user/<username>")
def profile(username=None):
	if username != None:
		return "Hello " + username
	else:
		return "Hello you"


@app.route("/novo")
def novo():
	if "usuario_logado" not in session or session["usuario_logado"] == None:
		return redirect("/login")
	else:
		return render_template("novo.html", titulo="Novo Jogo")


@app.route("/criar", methods=["POST",])
def criar():
	nome = request.form["nome"]
	categoria = request.form["categoria"]
	console = request.form["console"]

	jogo = Jogo(nome, categoria, console)
	lista.append(jogo)

	return redirect("/jogos")


@app.route("/login")
def login():
	return render_template("login.html")


@app.route("/autenticar", methods=["POST",])
def autenticar():
	if "mestra" == request.form["senha"]:
		session["usuario_logado"] = request.form["usuario"]
		flash(request.form["usuario"] + " logou com sucesso")
		return redirect("/")
	else:
		flash("Não logado")
		return redirect("/login")


@app.route("/logout")
def logout():
	session["usuario_logado"] = None
	flash("Nenhum usuário logado")
	return redirect("/")