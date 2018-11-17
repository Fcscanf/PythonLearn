@api.route('/get', methods=['GET'])
def test_javascript_http():
    p = request.args.get(name)
    return p, 200


@api.route('/psw', methods=['GET'])
@auth.login_required
def get_psw():
    p = request.args.get('psw')
    r = genertae_password_hash(p)
    return 'fc', 200
