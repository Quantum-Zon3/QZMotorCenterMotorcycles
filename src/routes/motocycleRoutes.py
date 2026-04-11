from flask import Blueprint, request, jsonify
from src.services.motorcycleService import *

motorcycle_bp = Blueprint('motorcycles', __name__)

@motorcycle_bp.route('/', methods=['GET'])
def get_all():
    motos = get_all_motorcycles()
    return jsonify([m.to_dict() for m in motos])


@motorcycle_bp.route('/<string:placa>', methods=['GET'])
def get_one(placa):
    moto = get_motorcycle_by_id(placa)
    if not moto:
        return jsonify({"error": "No encontrada"}), 404
    return jsonify(moto.to_dict())


@motorcycle_bp.route('/', methods=['POST'])
def create():
    data = request.json
    moto = create_motorcycle(data)
    return jsonify(moto.to_dict()), 201


@motorcycle_bp.route('/<string:placa>', methods=['PUT'])
def update(placa):
    data = request.json
    moto = update_motorcycle(placa, data)

    if not moto:
        return jsonify({"error": "No encontrada"}), 404

    return jsonify(moto.to_dict())


@motorcycle_bp.route('/<string:placa>', methods=['DELETE'])
def delete(placa):
    success = delete_motorcycle(placa)

    if not success:
        return jsonify({"error": "No encontrada"}), 404

    return jsonify({"message": "Eliminada"})