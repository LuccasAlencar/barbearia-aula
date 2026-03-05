from flask import Flask

from .models.database import criar_tabelas, popular_dados_exemplo

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'barbearia-escola-2024'

    from .controllers.main_controller import main_bp
    from .controllers.barbeiro_controller import barbeiro_bp
    from .controller.cliente_controller import cliente_bp
    from .controller.agendamento_controller import agendamento_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(barbeiro_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(agendamento_bp)

    criar_tabelas()
    popular_dados_exemplo()

    return app

