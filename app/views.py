from flask import Blueprint, request, jsonify, render_template
from .models import Mariposa
from . import db

bp = Blueprint('main', __name__)

@bp.route('/api/mariposas/crear/', methods=['POST'])
def add_mariposa():
    data = request.json
    new_mariposa = Mariposa(
        nombre=data['nombre'],
        especie=data['especie'],
        familia=data['familia'],
        nombreCientifico=data['nombreCientifico'],
        pais=data['pais'],
        peligroExtincion=data['peligroExtincion'],
        migratoria=data['migratoria']
    )
    db.session.add(new_mariposa)
    db.session.commit()
    return jsonify(new_mariposa.id), 201

@bp.route('/cargabutterflies')
def cargabutterflies():
    return render_template('cargabutterflies.html')

@bp.route('/gestionbutterflies')
def gestionbutterflies():
    return render_template('gestionbutterflies.html')
